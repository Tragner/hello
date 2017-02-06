from flask import Flask, render_template, redirect, url_for, request, flash, session
from forms import NewForm, EditForm, UserForm
from models import Experience, db, User
from functools import wraps
import hashlib

app = Flask(__name__)
app.secret_key = 'secret'

def login_required(f):
    # Decoration: check login in session
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            session.clear()
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/dashboard")
@login_required
def index():
        experience = Experience.query.order_by(Experience.end.desc())
        return render_template('items/curriculum.html', experience=experience)

@app.route("/delete/<int:id>")
@login_required
def delete_experience(id):
    experience = Experience.query.filter_by(id=id).first()
    db.session.delete(experience)
    try:
        db.session.commit()
        flash('Post eliminado', 'success')
    except:
        db.session.rollback()
        flash('Ha ocurrido un error', 'danger')

    return redirect(url_for('index'))

@app.route("/new", methods=['GET', 'POST'])
@login_required
def new_experience():
    form = NewForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Guardado correctamente', 'success')
            experience = Experience(request.form['company'], request.form['role'],
                                    request.form['start'], request.form['end'])
            db.session.add(experience)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            todos_errores = form.errors.items()
            for campo, errores in todos_errores:
                for error in errores:
                    flash(error, 'danger')
    return render_template('items/new.html', form=form)

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_experience(id):
    experience = Experience.query.filter_by(id=id).first()
    form = EditForm(company=experience.company, role=experience.role, start=experience.start, end=experience.end)
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Guardado correctamente', 'success')
            experience = Experience(request.form['company'], request.form['role'],
                                    request.form['start'], request.form['end'])
            db.session.add(experience)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('index'))
        else:
            todos_errores = form.errors.items()
            for campo, errores in todos_errores:
                for error in errores:
                    flash(error, 'danger')
    return render_template('items/edit.html', form=form, experience=experience)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = UserForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        my_user = User.query.filter_by(email=email, password=password).first()
        if my_user:
            session['email'] = email
            return redirect(url_for('index'))
        else:
            flash('Su email o contraseña no es correcto', 'danger')
    return render_template('items/login.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Usuario creado correctamente', 'success')
            print('afasdfsa')
            my_user = User(request.form['name'], request.form['email'],
                                    request.form['password'])
            db.session.add(my_user)
            try:
                db.session.commit()
            except:
                db.session.rollback()
            return redirect(url_for('login'))
        else:
            todos_errores = form.errors.items()
            for campo, errores in todos_errores:
                for error in errores:
                    flash(error, 'danger')
    return render_template('items/signup.html', form=form)

@app.route("/logout")
@login_required
def logout():
        session.clear()
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)