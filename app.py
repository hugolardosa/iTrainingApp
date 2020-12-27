from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin, login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'm─AIQUDSddaosidfASIFOjeifowseiI*heO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

# Auth File
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('profile'))


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email') 
    name = request.form.get('name')
    password = request.form.get('password')
    pt_code = request.form.get('pt_code')
    address = request.form.get('address')
    city = request.form.get('city')
    cell_phone = request.form.get('cell_phone') 
    cell_phone = cell_phone if cell_phone != "" else 0

    postal_code = request.form.get('postal_code')
    #2a página
    bday = request.form.get('bday')

    weight = request.form.get('weight')
    weight = weight if weight != "" else 0

    height = request.form.get('height')
    height = height if height != "" else 0

    obj = request.form.get('obj')
    health_problems = request.form.get('health_problems')
    
    
    
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), pt_code=pt_code, address=address, city=city, cell_phone=cell_phone, postal_code=postal_code,bday=bday, weight=weight, height=height, obj=obj, health_problems=health_problems)
    #new_user = User(id=0, email='', name='', password='', pt_code=0, address='', city='', cell_phone=0, postal_code=0,bday='', weight=0.0, height=0.0, obj='', health_problems='') 
    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

"""
    new_user = User(id=0, email='', name='', password='', pt_code=0, address='', city='', cell_phone=0, postal_code=0,bday='', weight=0.0, height=0.0, obj='', health_problems='')
    db.session.add(new_user)
    db.session.commit()
"""

### Main Class
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, db.Sequence('user_id_seq') ,primary_key=True, autoincrement=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    pt_code = db.Column(db.String(1000))
    address = db.Column(db.String(1000))
    city = db.Column(db.String(100))
    cell_phone = db.Column(db.Integer)
    postal_code = db.Column(db.String(1000))
    #2a página
    bday = db.Column(db.String(10)) #dd-mm-aaaa
    weight = db.Column(db.Float) #kg
    height = db.Column(db.Float) #cm
    obj = db.Column(db.String(1000))
    health_problems = db.Column(db.String(1000))

