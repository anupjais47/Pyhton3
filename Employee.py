class Employee:
    emp = []
    def __init__(self, name, desig, gender, doj, sal):
        self.name = name
        self.desig = desig
        self.gender = gender
        self.doj = doj
        self.sal = sal
        Employee.emp.append(self)

    def numEmp():
        return len(Employee.emp)
    
    def countGender(gender):
        count = 0
        for e in Employee.emp:
            if e.gender == gender:
                count += 1
        return count
    
    def high_sal(sal):
        high_sal_emp = []
        for e in Employee.emp:

            if e.sal > sal:
                high_sal_emp.append(e)
        return high_sal_emp
    
    def asst_manager(desig="Asst Manager"):
        asst_manager_emp = []
        for e in Employee.emp:
            if e.desig == desig:
                asst_manager_emp.append(e)
        return asst_manager_emp

e1 = Employee("Para Agrawal", "CEO", "Male", "2020-01-01", 15000)
e2 = Employee("Pratima Ganguli", "Asst Manager", "Female", "2021-01-01", 10000)
e3 = Employee("Krim M. Karmale", "Clerk", "Male", "2022-01-01", 5000)

print("Total number of employees:", Employee.numEmp())
print("Male employees:", Employee.countGender("Male"))
print("Female employees:", Employee.countGender("Female"))

high_sal_emp = Employee.high_sal(10000)
print("Employees with salary more than 10,000.")
for e in high_sal_emp:
    print(e.name)
    print("Employees with designation 'Asst Manager'.")
asst_manager_emp=Employee.asst_manager()
for e in asst_manager_emp:
    print(e.name)
