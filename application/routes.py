from application import app, db, db1
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import Patient,Admin
from application.forms import LoginForm,CreateCustomer
@app.route("/")
@app.route("/index")
def index():
  return render_template("index.html", index=True )
@app.route("/admin")
def admin():
  return render_template("admin.html")

@app.route("/test")
def test():
    db1.user_collection.insert_one({"name": "John"})
    return "Connected to the data base!"

@app.route("/createcustomer", methods=['POST','GET'])
def register():
    if session.get('name'):
        return redirect(url_for('index'))
    form = CreateCustomer()
    if form.validate_on_submit():
        
        ssnid  = form.ssnid.data
        name    = form.name.data
        age  = form.age.data
        dateofadmit=form.dateofadmit.data
        typeofbed =form.typeofbed.data
        address   = form.address.data
        city = form.city.data
        state=form.state.data

        patient = Patient(ssnid=ssnid, name=name, age=age, dateofadmit=dateofadmit,typeofbed=typeofbed,address=address,city=city,state=state)
        patient.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('admin'))
    return render_template("register.html", title="Register", form=form, register=True)

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username  = form.username.data
        password  = form.password.data

        admin = Admin.objects(username=username).first()
        if admin and admin.get_password(password):
            flash(f"{admin.username}, you are successfully logged in!", "success")
            session['username'] = admin.username
            return redirect("/admin")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

