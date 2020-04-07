from healingpaws import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64))
    passwordHash = db.Column(db.String(64))
    user_level = db.Column(db.Integer)
    email = db.Column(db.String, default="no email")
    dateOfBirth = db.Column(db.String, default="unknown birthday")
    isMale = db.Column(db.Boolean, default=True)

    pet = db.relationship('Pets', backref="pet_owner", lazy="dynamic")
    doctorInfo = db.relationship("Doctors", backref="doctor_user", lazy="dynamic")

    def __repr__(self):
        return "id : " + str(
            self.id) + " name : " + self.username + " email : " + self.email + " birthday : " + self.dateOfBirth + " male : " + str(
            self.isMale) + " level : " + str(self.user_level) + "\n"


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    petsname = db.Column(db.String(64))
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    health = db.Column(db.Integer, default=-1)
    birthDay = db.Column(db.String, default="unknown birthday")
    appoinment = db.relationship('Appoinments', backref="appoint_pet", lazy="dynamic")

    def __repr__(self):
        return "id : " + str(self.id) + " pet name : " + self.petsname + " owner : " + str(
            self.owner) + " health : " + str(self.health) + " birthday : " + self.birthDay + "\n"


class Doctors(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"))
    doctor_name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    telephone = db.Column(db.String)
    introduction = db.Column(db.String)
    appointment = db.relationship('Appoinments', backref="appoint_doctor", lazy="dynamic")

    def formatCode(self, format):
        return str(self.id) + format + self.doctor_name + format + str(
            self.age) + format + self.telephone + format + self.introduction

    def __repr__(self):
        return "id : " + str(self.id) + " doctor name : " + self.doctor_name + " age : " + str(
            self.age) + " telphone : " + self.telephone + " introduction : " + self.introduction + "\n"


class Appoinments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet = db.Column(db.Integer, db.ForeignKey('pets.id'))
    doctor = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    date = db.Column(db.String)


class Branches(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    introduction = db.Column(db.String)
    pic_address = db.Column(db.String)


class Hospital(object):
    name = 'Healing Paws'
    introduction = [
        "for test"
        ,
        "The new system will allow customers to make appointments for their pets online, and allow employees of Healing Paws to organize, prioritize, and keep track of appointments. Healing Paws has three locations: Beijing, Shanghai and Chengdu."
        ,
        "The solution must be cloud-based, and work on mobile as well as PCs. Healing Paws main concerns are the following:"
        ,
        "• Ability for customers to make appointments for their pets. There are two appointment types:emergency and standard. These will need to be handled by Healing Paws employees accordingly. It should be possible for one customer to make appointments for multiple pets if possible."
        ,
        "• Ability for customers to see the status of their pets for serious cases when required. For instance, surgery date confirmed, surgery complete, pet ready for release, etc."
        , "• Ability for employees to organize, prioritize and keep track of pets in the system"
        , "• Ability for customers to ask questions and for employees to answer them."
        , "• The system should have two portals – one for customers and one for employees."]
    pic_address = 'img/timg.jpg'
