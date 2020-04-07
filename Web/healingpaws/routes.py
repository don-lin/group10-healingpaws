import os

from werkzeug.utils import secure_filename

from healingpaws import app, DatabaseSecretConfig
from healingpaws.dbConnector import *
from flask import render_template, send_from_directory, request, flash, redirect
from healingpaws.forms import NewBranchForm


@app.route("/")
@app.route("/about")
def about_page():
    hospital = getHospital()

    # deleteBranch("Beijing Healing Paws General Hospital")
    # deleteBranch("Shanghai branch of Healing Paws Hospital")
    # deleteBranch("Chengdu branch of Healing Paws Hospital")
    #
    # addBranch(name="Beijing Healing Paws General Hospital",
    #           address="Beijing ChaoYang 100",
    #           pic_address="img/beijing_h.jpg",
    #           intro="Beijing general hospital has the most powerful team of doctors and the most cutting-edge medical equipment and the best service attitude.It will make your pet sad when he comes and peaceful when he goes.<br>北京总院有着最强大的医生团队，最尖端的医疗设备和最优质的服务态度.会让您的宠物来的时候很伤心，走的时候很安详。")
    # addBranch(name="Shanghai branch of Healing Paws Hospital",
    #           address="Shanghai PuDong 100",
    #           pic_address="img/shanghai_h.jpg",
    #           intro="Shanghai Branch has unique geographical advantages. Because of its coastal area, our hospital can not only treat ordinary pets, but also treat pets like dolphins, hippos, seals, penguins and polar bears.<br>上海分院有着独特的地理优势。因为这个分院它靠近海边，所以我们不仅能收治普通的宠物，还能够治疗像海豚，河马，海豹，企鹅，北极熊这样的宠物。并且配备了很多医疗人员去照顾它们。")
    # addBranch(name="Chengdu branch of Healing Paws Hospital",
    #           address="Chengdu QingYang 100",
    #           pic_address="img/chengdu_h.jpg",
    #           intro="This hospital is in mountain city of Chengdu, so we can not only treat pets, but also provide free Panda babies for owners who come to treat their pets. And provide a free hotpot base for every pet who has undergone sterilization.<br>这所医院在山城成都，所以我们不仅能够治疗宠物，还有免费的熊猫宝宝可供前来治疗自己宠物的主人们观赏。并且为每一个做完绝育手术的宠物提供免费的火锅")

    return render_template("about.html", hospital=hospital)


@app.route('/login')
def login():
    return render_template('login.html')


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
    branches = getAllBranches()
    return render_template("locations.html", branches=branches)


@app.route("/information")
def information():
    return render_template("information.html")


@app.route("/manage")
def manager_page():
    return render_template("manager.html", users=getAllUser())


@app.route("/mydate")
def my_date():
    return render_template("my_date.html")


@app.route("/android/doctors", methods=["POST"])
def send_android_doctors():
    doc_list = getAllDoctors()
    result = ""
    for d in doc_list:
        result += d.formatCode("ccddll") + "dlcc"
    return result


@app.route("/admin", methods=["GET", "POST"])
def pet_page():
    print(request.form)
    if (request.form.get("submit") == '1'):
        addPet(request.form['pet_name'], int(request.form['pet_health']), request.form['pet_birthday'])

    if (request.form.get("submit") == '2'):
        addDoctor(request.form['doctor_name'], int(request.form['age']), request.form['doctor_telphone'],
                  request.form['doctor_introduction'])
    if (request.form.get("delete_pet")):
        deletePet(request.form.get("delete_pet"))
    if (request.form.get("delete_doctor")):
        deleteDoctor(request.form.get("delete_doctor"))
    if (request.form.get("update_doctor")):
        updateDoctor(request.form.get("update_doctor"), request.form['doctor_name'], int(request.form['age']),
                     request.form['doctor_telphone'], request.form['doctor_introduction'])
    if (request.form.get("update_pet")):
        updatePet(request.form.get("update_pet"), request.form['pet_name'], int(request.form['pet_health']),
                  request.form['pet_birthday'])
    return render_template("admin.html", pet_list=getAllPets(), doctor_list=getAllDoctors())


@app.route('/css/<filename>')
def get_css(filename):
    return send_from_directory(DatabaseSecretConfig.cssdir, filename)


@app.route('/img/<filename>')
def get_img(filename):
    return send_from_directory(DatabaseSecretConfig.imgdir, filename)


@app.route('/javascript/<filename>')
def get_js(filename):
    return send_from_directory(DatabaseSecretConfig.jsdir, filename)
