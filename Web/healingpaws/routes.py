from healingpaws import  *
from healingpaws.dbConnector import  *
from flask import render_template,send_from_directory,request

@app.route("/")
@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/doctors")
def doctors_page():
    return render_template("doctors.html")

@app.route("/signup")
def signup_page():
    return render_template("signup.html")
@app.route("/locations")
def location_page():
    return render_template("locations.html")

@app.route("/manage")
def manager_page():
    return render_template("manager.html",users=getAllUser())

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
