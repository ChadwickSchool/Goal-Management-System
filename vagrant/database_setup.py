import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import DateTime



Base = declarative_base()


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(250), nullable=False)
    login = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
#need to modify from login.py file to call the commands and create teachers and set login info and stuff

class Student(Base):
    __tablename__ = 'student'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True, autoincrement = True)
    #goal = Column(String(250))
    goals = relationship('Goal', secondary = 'student_goal_link')
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

class Goal(Base):

    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True, autoincrement = True)
    description = Column(String(250))
    name = Column(String(80), nullable=False)
#    student = relationship(Student)
#    assignedDate = Column(DateTime, default = func.now())
    dueDate = Column(DateTime(), nullable = True)
#deal with "createdBy" later, practically useless as of 11/8/18
    createdBy = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship(Teacher)
    students = relationship(Student, secondary = 'student_goal_link')
    #the createdBy stuff is login related
class StudentGoalLink(Base):
    __tablename__= 'student_goal_link'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key = True)
    goal_id = Column(Integer, ForeignKey('goal.id'), primary_key = True)




dal = Student()

engine = create_engine('sqlite:///teacheractions.db')


Base.metadata.create_all(engine)
