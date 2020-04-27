from healingpaws import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(64))
    passwordHash=db.Column(db.String(64))
    #customer 0,  doctor 1, employee 2
    user_level=db.Column(db.Integer)
    email=db.Column(db.String,default="no email")
    dateOfBirth=db.Column(db.String,default="unknown birthday")
    isMale=db.Column(db.Boolean,default=True)
    pet=db.relationship('Pets',backref="pet_owner",lazy="dynamic")
    questions = db.relationship('Question', backref="questions", lazy="dynamic")
    replies = db.relationship('Reply',backref="replies", lazy="dynamic")
    doctorInfo=db.relationship("Doctors",backref="doctor_user",lazy="dynamic")

    def __repr__(self):
        return "id : "+str(self.id)+" name : "+self.username+" email : "+self.email+" birthday : "+self.dateOfBirth+" male : "+str(self.isMale) +" level : "+str(self.user_level)+"\n"

class Pets(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    petsname=db.Column(db.String(64))
    owner=db.Column(db.Integer,db.ForeignKey('user.id'))
    #这个health属性改为描述目前宠物的处理！ 只能员工操作！
    #['Surgery date confirmed', 'Surgery Completed', 'Ready for Release', 'Wait for Surgery'] 0 1 2 3
    health=db.Column(db.Integer,default=-1)
    birthDay=db.Column(db.String,default="unknown birthday")
    appoinment=db.relationship('Appointments',backref="appoint_pet",lazy="dynamic")
    def __repr__(self):
        return "id : "+str(self.id)+" pet name : "+self.petsname+" owner : "+str(self.owner)+" health : "+str(self.health)+" birthday : "+self.birthDay +"\n"


class Doctors(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    userId=db.Column(db.Integer,db.ForeignKey("user.id"))
    doctorname=db.Column(db.String(64))
    age=db.Column(db.Integer)
    telphone=db.Column(db.String)
    introduction=db.Column(db.String)
    appoinment=db.relationship('Appointments',backref="appoint_doctor",lazy="dynamic")
    def formatCode(self,format):
        return str(self.id)+format+self.doctorname+format+str(self.age)+format+self.telphone+format+self.introduction

    def __repr__(self):
        return "id : "+str(self.id)+" doctor name : "+self.doctorname+" age : "+str(self.age)+" telphone : "+self.telphone+" introduction : "+self.introduction +"\n"

class Appointments(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pet=db.Column(db.Integer,db.ForeignKey('pets.id'))
    doctor=db.Column(db.Integer,db.ForeignKey('doctors.id'))
    date=db.Column(db.String)
    #分院的位置 1北京 2上海 3成都,目前默认是北京
    loc=db.Column(db.Integer,default=1)
    #Appointment的状态只有员工可以更改
    #status = 0 已处理(默认) "unchecked"
    #status = 1 未处理      "checked"
    status=db.Column(db.Integer,default=0)
    #Appointment具体安排的时间段 只有员工可以操作
    time_slot = db.Column(db.String)
    #紧急程度 1 urgent/ 0 normal
    emergency = db.Column(db.Integer)
    #对本次预约的描述
    description = db.Column(db.String)

    def __repr__(self):
        return 'id: '+str(self.id)+' pet: '+str(self.pet)+' doctor: '+str(self.doctor)+' date: '+str(self.date)



#一级提问主题
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String)
    replys = db.relationship('Reply', backref="reolys",lazy="dynamic")

    def __repr__(self):
        return "id : "+str(self.id)+" user_id: "+ str(self.user) +" title: "+ self.title


#二级评论,相当于两个用户在该问题下聊天
class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    def __repr__(self):
        return "id : "+str(self.id)+" user_id: "+ str(self.user) + " content: "+ self.content + "question_id" + str(self.question_id)