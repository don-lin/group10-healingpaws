from healingpaws import  app,DatabaseSecretConfig
from healingpaws.dbConnector import  *
from flask import render_template,send_from_directory,request, redirect
from werkzeug.security import genera_password_hash, check_password_hash
from healingpaws.forms import LoginForm

@app.route("/")
@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_in_db = User.query.filter(User.username == form.username.data).first()
        if not user_in_db:
            flash('No user found with username: {}'.format(form.username.data))
            return redirect('login.html')
        if (check_password_hash(user_in_db.password_hash, form.password.data)):
            flash('Login success!')
            session['USERNAME'] = user_in_db.username
            return render_template('information.html', user=user_in_db)
        flash('Incorrect Password')
        return redirect('login.html')
    return render_template('login.html', form=form)

@app.route("/doctors")
def doctors_page():
    return render_template("doctors.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")
@app.route("/locations")
def location_page():
    return render_template("locations.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/manage")
def manager_page():
    return render_template("manager.html",users=getAllUser())

@app.route("/mydate")
def my_date():
    return render_template("my_date.html")

@app.route("/android/doctors",methods=["POST"])
def send_android_doctors():
    doc_list=getAllDoctors()
    result=""
    for d in doc_list:
        result+=d.formatCode("ccddll")+"dlcc"
    return result

@app.route("/admin",methods=["GET","POST"])
def pet_page():
    print(request.form)
    if(request.form.get("submit")=='1'):
        addPet(request.form['pet_name'],int(request.form['pet_health']),request.form['pet_birthday'])

    if(request.form.get("submit")=='2'):
        addDoctor(request.form['doctor_name'],int(request.form['age']),request.form['doctor_telphone'],request.form['doctor_introduction'])
    if(request.form.get("delete_pet")):
        deletePet(request.form.get("delete_pet"))
    if(request.form.get("delete_doctor")):
        deleteDoctor(request.form.get("delete_doctor"))
    if(request.form.get("update_doctor")):
        updateDoctor(request.form.get("update_doctor"),request.form['doctor_name'],int(request.form['age']),request.form['doctor_telphone'],request.form['doctor_introduction'])
    if(request.form.get("update_pet")):
        updatePet(request.form.get("update_pet"),request.form['pet_name'],int(request.form['pet_health']),request.form['pet_birthday'])
    return render_template("admin.html", pet_list=getAllPets(),doctor_list=getAllDoctors())


@app.route('/css/<filename>')
def get_css(filename):
    return send_from_directory(DatabaseSecretConfig.cssdir,filename)
@app.route('/img/<filename>')
def get_img(filename):
    return send_from_directory(DatabaseSecretConfig.imgdir,filename)
@app.route('/javascript/<filename>')
def get_js(filename):
    return send_from_directory(DatabaseSecretConfig.jsdir,filename)
@app.route("/pet",methods=["GET"])
def load_pet():
    pet_in_db = Pet.query.filter().first()
    
    