class Person:
    '''A base class to defin Person Properties'''
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count +=1
    def speak(self):
        return self.name     
