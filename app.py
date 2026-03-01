import os
from flask import Flask, render_template, request, redirect
from datetime import datetime
from models.user import db, user
from models.studentdata import db, student_data
from models.teacherdata import db, teacher_data
from models.admindata import db, admin_data

center_style = 'style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: Arial, sans-serif;"'
button_style = 'style="padding: 10px 20px; font-size: 16px; cursor: pointer; background-color: #007BFF; color: white; border: none; border-radius: 5px;"'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db.init_app(app)

with app.app_context():
    db.create_all()
    
    if not admin_data.query.filter_by(name='admin').first():
        admin1 = admin_data(name='admin', password='Admin@1234')
        db.session.add(admin1)
        db.session.commit()


@app.route('/', methods = ['GET','POST'])
def Homepage():

    if request.method  == 'POST':
        role = request.form.get('role')
        id = request.form['ID']
        pasword = request.form['password']


        if role == 'user':
            match = user.query.filter_by(studentid=id, pass_hash=pasword).first()

            if match:
                return redirect('/user')

            else:
                return render_template('index.html', message ='No Student found')

        if role == 'professor':
            match = teacher_data.query.filter_by(teacherid = id, password=pasword).first()

            if match:
                return redirect('/professor')

            else:
                return render_template('index.html', message ='No Professor found')
        

        if role == 'admin':
            match = admin_data.query.filter_by(name=id, password=pasword).first()

            if match:
                return redirect('/admin')

            else:
                return render_template('index.html', message ='No admin found')


    return render_template('index.html')

@app.route('/user')
def userlogin():
    return render_template('userlogin.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():

    if request.method == 'POST':
        role = request.form.get('role')
        name = request.form['name']
        id = request.form['id']
        password = request.form['pass']


        if role == 'user':
            exist = user.query.filter_by(studentid=id).first() 
            exist2 = user.query.filter_by(pass_hash = password).first()

            if exist or exist2:
                return render_template('signup.html', message = "Already have account")

            else:

                user1 = user(name = name ,studentid = id,pass_hash = password)
                db.session.add(user1)
                
                if not student_data.query.filter_by(name=name).first():
                    st1 = student_data(name=name, branch='Unknown', attendance=0, roll_no=id)
                    db.session.add(st1)

                db.session.commit()
                return render_template('signup.html', message = "Account Created")



        if role == 'professor':

            exist = teacher_data.query.filter_by(teacherid = id).first() 
            exist2 = teacher_data.query.filter_by(password = password).first()

            if exist or exist2:
                return render_template('signup.html', message = "Already have account")

            else:

                teacher1 = teacher_data(name = name,password = password,teacherid = id)
                db.session.add(teacher1)
                db.session.commit()
                return render_template('signup.html', message = "Account Created")

    return render_template('signup.html')

@app.route('/admin', methods = ['GET','POST'])
def adminlogin():

    if request.method == 'POST':

        name = request.form['name']
        branch = request.form['branch']
        born = request.form['born']
        roll_no = request.form['roll_no']

        exist3 = student_data.query.filter_by(name=name, branch=branch).first()

        if exist3:
            return render_template('adminlogin.html', message='Data already exist')
        else:
            born_date = datetime.strptime(born, '%Y-%m-%d').date()  
            st1 = student_data(name=name, branch=branch, dob=born_date, attendance=0, roll_no=roll_no)
            db.session.add(st1)
            db.session.commit()
            return render_template('adminlogin.html', message='Data submitted')
        
    return render_template('adminlogin.html')

@app.route('/professor')
def professorlogin():

    return render_template('Professorlogin.html')


if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True,port='3000')