from flask import Flask, render_template, request, redirect
from datetime import datetime
from models.user import db, user
from models.attendance import db, Attendance
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
                return redirect(f'/user/{id}')

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

@app.route('/user/<id>', methods=['GET'])
def userlogin(id):

    id1 = student_data.query.filter_by(student_id = id ).first()

    if id1:
        roll = id1.roll_no # as id1 have all info about user that logged in i use id1(object which has data of Attendance class) to acess its roll no. and count the attendance

        total_count = Attendance.query.filter_by(roll_no = roll).count()
        present_count = Attendance.query.filter_by(roll_no = roll,status = True).count()
        absent_count = Attendance.query.filter_by(roll_no = roll,status = False).count()

        if not total_count == 0:
            percent_count = round((present_count/total_count)*100,2)
            return render_template('userlogin.html', total_count=total_count, present_count=present_count, absent_count=absent_count, percent_count=percent_count)
        else:
            return render_template('userlogin.html')
            
    else:
        return redirect('/?message=Look like you didnt use given ID during Sign up,retry')

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
        student_id = request.form['id']

        exist3 = student_data.query.filter_by(name=name, branch=branch).first()

        if exist3:
            return render_template('adminlogin.html', message='Data already exist')
        else:
            born_date = datetime.strptime(born, '%Y-%m-%d').date()  
            st1 = student_data(name=name, branch=branch, dob=born_date, roll_no=roll_no, student_id = student_id)
            db.session.add(st1)
            db.session.commit()
            return render_template('adminlogin.html', message='Data submitted')
        
    return render_template('adminlogin.html')

@app.route('/professor', methods = ['POST','GET'])
def professorlogin():

   
        if request.method == 'POST':
            action = request.form.get('action')
            
            if action == 'Load':
                date = request.form['date']
                branch = request.form['branch']
                date2 = datetime.strptime(date, '%Y-%m-%d').date()
                
                filter = Attendance.query.filter_by(date = date2, branch = branch).all()
                
                if filter:
                    return render_template('professorlogin.html', filter = filter)
                
                else:

                    student = student_data.query.filter_by(branch=branch).all()
                    for s in student:

                        new_row = Attendance( roll_no  = s.roll_no, student_name = s.name, branch = branch,date = date2,status = False,student_id =s.student_id  )
                        db.session.add(new_row)

                    db.session.commit()
                    filter = Attendance.query.filter_by(date = date2, branch = branch).all()
                    return render_template('professorlogin.html',filter=filter)
            
            if action == 'edit':
                attend = request.form['attend']
                roll = request.form.get('roll')
                date = request.form.get('date')
                branch = request.form.get('branch')
                date2 = datetime.strptime(date, '%Y-%m-%d').date()

                exist = Attendance.query.filter_by(roll_no=roll, date = date2).first()
                if exist:
                    if attend == 'Present':
                        exist.status = True
                    elif attend == 'Absent':
                        exist.status = False
                
                db.session.commit()
                filter = Attendance.query.filter_by(date = date2, branch = branch).all()

                if filter:

                    return render_template('Professorlogin.html',filter = filter)

                return render_template('professorlogin.html',message = 'Data not found')
                       
        return render_template('Professorlogin.html')


if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True,port='3000')