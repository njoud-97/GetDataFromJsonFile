import json

class Employee:
    def __init__(self, id, name, sal, permission, dept_name):
        self.id = id
        self.name = name
        self.sal = sal
        self.permission = permission
        self.dept_name = dept_name
    def checkPer(self):
        per = d["employees"][idd]['permission']
        if per == "True":
            print("id sal department")
            for i in range(1, 11):
                print(str(d["employees"][i]['id'])+" "+str(d["employees"][i]['sal'])+" "+str(d["employees"][i]['dept_name']))
            search = int(input('To search for an employee, enter his id or 0 to exit : '))
            if search in range(1,11):
                print("id name sal department")
                print(str(d["employees"][search]['id']) + " " +str(d["employees"][search]['name']) + " " + str(d["employees"][search]['sal']) + " " + str(d["employees"][search]['dept_name']))
            elif search == 0:
                print('You are finish')
        else:
            print("id sal department")
            print(str(d["employees"][idd]['id'])+" "+str(d["employees"][idd]['sal'])+" "+str(d["employees"][idd]['dept_name']))






class Department:
    def __init__(self, did, dept_name):
        self.id = did
        self.dept_name = dept_name

class CEO(Employee, Department):
    def __init__(self, id, name, sal, did, dept_name, permission):
        super().__init__(self, id, name, sal)
        super().__init__(self, did, dept_name)
        self.permission = permission
    def per(self):
        permission = True

class PM(Employee, Department):
    def __init__(self, id, name, sal, did, dept_name, permission):
        super().__init__(self, id, name, sal)
        super().__init__(self, did, dept_name)
        self.permission = permission

class TL(Employee, Department):
    def __init__(self, id, name, sal, did, dept_name, permission):
        super().__init__(self, id, name, sal)
        super().__init__(self, did, dept_name)
        self.permission = permission
    def per(self):
        permission = True

class SandM(Employee, Department):
    def __init__(self, id, name, sal, did, dept_name):
        super().__init__(self, id, name, sal)
        super().__init__(self, did, dept_name)


with open("tt.json", "r") as file:
    data = file.read()
d = json.loads(data)

idd = int(input('pls enter your id to login: '))
employ = d["employees"][idd]
emp_obj = Employee(**employ)
emp_obj.checkPer()


