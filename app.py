from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from DataTypes import *

demo_cl = Client(email="c@c", name="Demo Cliente", password=generate_password_hash("123", method='sha256'), address="Client Demo Address", city="Client Demo City", cell_phone="c1c1c1c1", postal_code="client postal_code", bday="Cl bday", weight="CL weight", height="height", obj="obj", health_problems="I'm helpless")
demo_pt = Pt(email="p@p", name="Demo Pt", password=generate_password_hash("123", method='sha256'), pt_code="!THE_PT_CODE_123!", address="PT Demo Address", city="pT Demo City", cell_phone="p9191919", postal_code="pt postal_code")

users = [demo_cl, demo_pt]
print(users)

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'm─AIQUDSddaosidfASIFOjeifowseiI*heO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return next((x for x in users if x.id == int(user_id)), None)

# Auth File
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = next((x for x in users if x.email == email), None)
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    
    # if it's a client then go to the calendar page
    if user.pt_code == 0:
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
    # print(pt_code)

    address = request.form.get('address')
    city = request.form.get('city')
    cell_phone = request.form.get('cell_phone') 
    postal_code = request.form.get('postal_code')
    #2a página
    bday = request.form.get('bday')
    weight = request.form.get('weight')
    height = request.form.get('height')
    obj = request.form.get('obj')
    health_problems = request.form.get('health_problems')


    user = next((x for x in users if x.email == email), None)  # if this returns a user, then the email already exists in database

    if user != None: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('login'))
    
    # if it's a client append to list
    # # else is a PT, append to user lists
    if pt_code == 0:
        users.append(Client(email, name, generate_password_hash(password, method='sha256'), address, city, cell_phone, postal_code, bday, weight, height, obj, health_problems))
    else:
        users.append(Pt(email, name, generate_password_hash(password, method='sha256'), pt_code, address, city, cell_phone, postal_code))
    
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

        
    