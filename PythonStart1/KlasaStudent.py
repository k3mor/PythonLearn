class StudentsClass:
    promoted: bool

    def __init__(self):
        self.first_name = "Roman"
        self.last_name = "Zbroiński"
        self.age = 52
        self.promoted = True
student1 = StudentsClass()
def view_student():
    print(f"Student first name:{student1.first_name}")
    print(f"Student last name:{student1.last_name}")
    print(f"Student age:{student1.age}")
    print(f"Student promoted:{student1.promoted}")
view_student()


class StudentcClass2:
    def __init__(self, first_name,last_name,age,promoted):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.promoted = promoted
    
student1 = StudentsClass()
student1.first_name = "Roman2"
student1.last_name = "Zbroiński2"
student1.age = 52
student1.promoted = False
def view_student2():
    print(f"Student first name:{student1.first_name}")
    print(f"Student last name:{student1.last_name}")
    print(f"Student age:{student1.age}")
    print(f"Student name:{student1.promoted}")
view_student2()


