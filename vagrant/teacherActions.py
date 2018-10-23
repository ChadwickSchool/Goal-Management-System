from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, StudentCreator, Student
app = Flask(__name__)

engine = create_engine('sqlite:///teacheractions.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


'''
def createStudent(student_id):
    newStudent = Student(name=request.form['name'], goal= request.form['goal'],student_id=student_id)
    session.add(newStudent)
    session.commit()
'''
def makeStudent(name, goal):
    if(name == None or goal == None):
        return "Must have a first name and goal, 404"
    else:
        student = Student(name = name, goal = goal)

    session.add(student)
    session.commit()
    return "TODO: Implement", 200

def getStudent(name):

    wantedStudent = session.query(Student).filter(Student.name == name)
    return wantedStudent
    '''
    note to self: current problem for testing is lack of connection, must add instance of object and stuff(dal stuff maybe?)
    student_list = []
        customer_info = { "name" : student.name
                        , "goal" : student.goal

                        }
        customer_list.append(customer_info)
        return customer_list
        '''
    return wantedStudent.name
def assignGoal(goal, student_id):''' TODO
    editedStudent = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedStudent.name = request.form['name']
        if request.form['description']:
            editedStudent.description = request.form['description']

        session.add(editedItem)
        session.commit()
'''
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
