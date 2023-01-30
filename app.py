from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Database.db"
db = SQLAlchemy(app)


class Student(db.Model):
    name=db.Column(db.String(100),nullable=False)
    rollNo=db.Column(db.String(100),nullable=False,primary_key=True)
    address=db.Column(db.String(200),nullable=False)
    contact=db.Column(db.String(12),nullable=False)

    def __repr__(self) -> str:
        return f"exi{self.name} {self.rollNo} {self.address} {self.contact}"

@app.route("/",methods=['GET','POST'])
def hello_world():
    allRecords=Student.query.all()
    return render_template('index.html',allRecords=allRecords)

@app.route("/addStudent",methods=['GET','POST'])
def handlePost():
    if request.method=='POST':
        student=Student(name=request.form['name'],rollNo=request.form['rollNo'],address=request.form['address'],contact=request.form['contact'])
        db.session.add(student)
        db.session.commit()
    
    return redirect("/")

@app.route("/deleteStudent/<string:rollNo>")
def handleDelete(rollNo):
    student=Student.query.filter_by(rollNo=rollNo).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")

@app.route("/updateStudent/<string:rollNo>",methods=['GET','POST'])
def handleUpdate(rollNo):
    if request.method=='POST':
        name=request.form['name']
        rollno=request.form['rollNo']
        address=request.form['address']
        contact=request.form['contact']
        student=Student.query.filter_by(rollNo=rollNo).first()
        student.name=name
        student.rollNo=rollno
        student.address=address
        student.contact=contact
        db.session.commit()
        return redirect("/")
    student=Student.query.filter_by(rollNo=rollNo).first()
    return render_template('update.html',student=student)




if __name__=="__main__":
    app.run(debug=True)

# student=Student(name="Parivesh",rollNo="0829CS191101",address="4,5-Maa Ambika Nagar",contact="9753485751")
#     db.session.add(student)
#     db.session.commit()