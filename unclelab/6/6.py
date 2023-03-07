class Company:
    #Constructor
    def __init__(self,company,branch):
        self.company = company
        self.branch = branch
    
    #Method
    def introduce(self):
        print(f'Company : {self.company} | Branch : {self.branch}')

    def changeBranch(self,new_branch):
        print(f'from : {self.branch}')
        self.branch = new_branch
        print(f'to : {self.branch}')
    
    def changeCompany(self, new_company):
        print(f'from : {self.company}') 
        self.company = new_company
        print(f'to : {self.company}')
    
    def delete(self):
        print(f'Delete {self.company} Successfully')
        del self
        

class Employee(Company):
    employeeList = []
    #Constructor
    def __init__(self,company,branch,name,role):
        super().__init__(company, branch)
        self.name = name
        self.role = role
        Employee.employeeList.append(self)
    
    #Method
    def introduce(self):
        super().introduce()
        print(f'Name : {self.name} | Role : {self.role}')

    def changeName(self, new_name):
        print(f'from : {self.name}')
        self.name = new_name
        print(f'to : {self.name}')
    
    def changeRole(self, new_role):
        print(f'from : {self.role}')
        self.role = new_role
        print(f'to : {self.role}')

    def quit(self):
        print(f'Delete {self.name} Successfully')
        del self        

#Instance
Toyo = Company('Toyota','JP')
OMG = Company('OMG','Africa')
print('........Show Company..........')
Toyo.introduce()
OMG.introduce()
print('.....Change Company Name.....')
Toyo.changeCompany('Facebook')
print('....Change Company Branch....')
Toyo.changeBranch('TH')
print('.......Delete OMG Company....')
OMG.delete()
print('........Update Company.......')
Toyo.introduce()
print('.............................')

Emp = Employee(Toyo.company, Toyo.branch, 'John', 'Saleman')
Zap = Employee(Toyo.company, Toyo.branch, 'Zap', 'Bandit')
print('_______Show Employee_________')
Emp.introduce()
Zap.introduce()
print('_________Change Name_________')
Emp.changeName('Rock Lee')
print('_________Change Role_________')
Emp.changeRole('Accountant')
print('__________Delete Zap_________')
Zap.quit()
print('_______Update Employee_______')
Emp.introduce()
print('_____________________________')