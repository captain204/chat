from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template,session)
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user)

from werkzeug.security import (generate_password_hash, 
                               check_password_hash)
from chat.extensions import db,login_manager

from chat.blueprints.user.models import(
     User,Message,Friend) 

from chat.blueprints.user.forms import (
     SignupForm,
     LoginForm)

user = Blueprint('user', __name__, template_folder='templates')

############### User Authentication #########################
@user.route('/signup', methods=['GET','POST'])
def signup():
    """User sign-up page."""
    form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if form.validate():
            # Get Form Fields
            username = request.form.get('username')
            email = request.form.get('email')
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            password = request.form.get('password')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(username=username,email=email,firstname=firstname,lastname=lastname,password=generate_password_hash(password, method='sha256'))
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('user.dashboard'))
            flash('A user already exists with that email address.')
            return redirect(url_for('user.dashboard'))
    # GET: Serve Sign-up page
    return render_template('user/signup.html', form=form)


@user.route('/login', methods=['GET','POST'])
def login():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))
    form = LoginForm(request.form)
    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        if form.validate():
            # Get Form Fields
            email = request.form.get('email')
            password = request.form.get('password')
            # Validate Login Attempt
            user = User.query.filter_by(email=email).first()
            if user:
                if user.check_password(password=password):
                    login_user(user)
                    next = request.args.get('next')
                    session['user_id'] = user.id
                    return redirect(next or url_for('user.dashboard'))
        flash('Invalid username/password combination')
        return redirect(url_for('user.login'))
    # GET: Serve Log-in page
    return render_template('user/login.html', form=form)
    
@user.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('user.login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('user.login'))



########### Main Chat Application ###############

# List potential friends
@user.route('/find_friends',methods=['GET','POST'])
@login_required
def friends():
    #users= session.query().join(Order, Order.customer_id == Customer.id).all()
    #users = session.query().join(Friend, Friend.user_id == User.id).all()
    users = User.query.all()
    return render_template('user/add_list.html', list = users)

@user.route('/add_friend/<id>',methods=['GET','POST'])
@login_required
def add_friend(id):
    user_id = session['user_id']
    friend_id = id
    new_friend = (user_id,friend_id)
    db.session.add(new_friend)
    db.session.commit()
    return redirect('/find_friend')


@user.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('user/dashboard.html')

@user.route('/inbox', methods=['GET','POST'])
@login_required
def inbox():
    return render_template('user/inbox.html')