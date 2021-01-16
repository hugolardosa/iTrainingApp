from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from DataTypes import *
from databases.database import *

##### Clients and PT for demo ##############

## 
train_list = [Trains("Braços", "1-12-2020", "5", [Exercice("Elevações na cadeira", "10")])]


#############

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'm─AIQUDSddaosidfASIFOjeifowseiI*heO'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

user = None

@login_manager.user_loader
def load_user(id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return user


# Auth File
@app.route('/')
def login():
    create_db()
    return render_template('login.html')


@app.route('/', methods=['POST'])
def login_post():
    global user
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    sha, tbl = get_element('CHECK_PASSWORD', None, email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if sha is None:
        return redirect(url_for('login'))
    if not sha[0] == password:
        flash('O e-mail ou a password está errada. Tente novamente.')
        return redirect(url_for('login'))  # if the user doesn't exist or password is wrong, reload the page

    if tbl == 'client':
        test = get_row(tbl, email)
        e, name, passw, addr, city, phone, pcode, b, w , h, obj, prob= test[0]

        user = Client(email = e, name = name, password = passw, address= addr, city = city, cell_phone= phone, \
                      postal_code=pcode, bday=b,starting_weight=w, height=h, obj = obj, health_problems=prob)

    elif tbl == 'pt':
        test = get_row(tbl,email)
        e, name, passw, code, addr, city, phone, pcode = test[0]

        user = Pt(email=e, name=name, password= passw, pt_code = code, address=addr,\
                 city= city,cell_phone= phone, postal_code=pcode )

    print('ID do user logado: ')
    print(user.id)
    print(user)


    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    #TODO check the line above
    # if it's a client then go to the calendar page

    if user.pt_code != 0:
        return redirect(url_for('my_clients'))
    else:
        return redirect(url_for('calendar'))


@app.route('/signup')
def signup():
    return render_template('New_SignUp.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    # print("estou aqui!")
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    pt_code = request.form.get('pt_code')
    pt_code = 0 if pt_code == "" else pt_code
    # print(type(pt_code))
    address = request.form.get('address') + " Nº " + request.form.get('Nporta')
    city = request.form.get('city')
    cell_phone = request.form.get('cell_phone')
    postal_code = request.form.get('postal_code')
    # 2a página
    bday = request.form.get('bday')
    weight = request.form.get('weight')
    height = request.form.get('height')
    obj = request.form.get('obj')
    health_problems = request.form.get('health_problems')

    checkmail = get_element('CHECK_EMAIL',None, email)


    if checkmail[0] is not None:  # if a user is found, we want to redirect back to signup page so user can try again
        print("existe")
        flash('Email address already exists')
        return render_template('New_SignUp.html')


    # if it's a client append to list
    # # else is a PT, append to user lists
    if pt_code == 0:

        values = (email, name, password, address,
                  city, cell_phone, postal_code, bday, weight, height,
                  obj, health_problems)
        create_entry_db('CLIENT_DETAILS', values)

    else:
        values = (email, name, password, pt_code,
                  address, city, cell_phone, postal_code)
        create_entry_db('PT_DETAILS', values)

    return redirect(url_for('mensalidade'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/editProfile_Client')
def editProfile_Client():
    return render_template('editProfile_Client.html')


@app.route('/editProfile_Client', methods=['POST'])
def editProfile_Client_post():
    ## A FAZER: Ir buscar todos os campos
    email = request.form.get('email')
    name = request.form.get('name')

    #TODO
    password = request.form.get('password')
    passwordRepet = request.form.get('password')  # posso fazer assim?
    # print(type(pt_code))
    if(request.form.get('address')  is None or request.form.get('Nporta') is None):
        address = None
    else:
        address = request.form.get('address') + " Nº " + request.form.get('Nporta')
    city = request.form.get('city')
    cell_phone = request.form.get('cell_phone')
    postal_code = request.form.get('postal_code')
    # 2a página
    bday = request.form.get('bday')
    weight = request.form.get('weight')
    height = request.form.get('height')
    obj = request.form.get('obj')
    health_problems = request.form.get('health_problems')

    if passwordRepet != password:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Password não confirmada')
        return redirect(url_for('editProfile_Client'))



    return redirect(url_for('profile'))


@app.route('/editProfile_PT')
def editProfile_PT():
    return render_template('editProfile_PT.html')


@app.route('/editProfile_PT', methods=['POST'])
def editProfile_PT_post():
    ## A FAZER: Ir buscar todos os campos
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    passwordRepet = request.form.get('password')  # posso fazer assim?
    # print(type(pt_code))
    address = request.form.get('address') + " Nº " + request.form.get('Nporta')
    city = request.form.get('city')
    cell_phone = request.form.get('cell_phone')
    postal_code = request.form.get('postal_code')

    if passwordRepet != password:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Password não confirmada')
        return redirect(url_for('editProfile_PT'))



    return redirect(url_for('profile'))  # VER PAGINA DO PROFILE DO PT


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/getPt')
def getPt():
    return render_template('getPt.html')

@app.route('/train')  # /train?id=
def train():
    train_id = int(request.args.get("id"))
    current_user.train_list[train_id].done = True
    return render_template('train.html', exs=current_user.train_list[train_id].exerc_list,
                           time=current_user.train_list[train_id].duration)


'''@app.route('/myclients')
def my_clients():
    return "My clients page, coming soon"'''

@app.route('/addtrain')
def addtrain():
    return render_template('addtrain.html')

@app.route('/mensalidade')
def mensalidade():
    return render_template('mensalidade.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/local')
def local():
    return render_template('local.html')

@app.route('/bodyfatCalculator')
def bodyfatCalculator():
    return render_template('bodyfat_calculator.html')
        
