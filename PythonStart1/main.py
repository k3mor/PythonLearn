#Add new push - number 3
'''
print("Helo World!")
text1="Helo World!"
print(f"{text1}")
'''
'''
class Student:
    pass
class Grade:
    pass
class School:
    pass

student_Roman = Student()
grade_a = Grade()
grade_b = Grade()
LOGora_school = School()
print(student_Roman)
print(f"{grade_a},{grade_b}")
print(LOGora_school)

print(type(student_Roman))
print(type(grade_a),type(grade_b))
print(type(LOGora_school))
grades = {
    1: Grade(),
    2: Grade(),
    3: Grade(),
    4: Grade(),
    5: Grade(),
    6: Grade()
}
students=[Student(),Student(),Student()]
print(students)
print(grades)
#Zad1
class Produkt:
    pass
class Zamowienia:
    pass
class Jablka:
    pass
class Ziemniaki:
    pass
jablko1 = Jablka()
jablko2 = Jablka()

ziemniak1 = Ziemniaki()
ziemniak2 = Ziemniaki()

print(type(jablko1),type(jablko2))
print(type(ziemniak1),type(ziemniak2))

zamowienie = [Zamowienia(),Zamowienia()]
zamowienia = []
# lub
for _ in range(2):
    zamowienia.append(Zamowienia())
print(zamowienia)
produkty = {
    "Jabłko1": Produkt(),
    "Jabłko2": Produkt(),
}
print(produkty)

'''
class Students:
    print("Nowy obiekt")
    name1 = "Roman1"
    surname1 = "Zbroiński1"
    age1 = 52

    # Konstruktor
    def __init__(self):
        self.name2 = "Roman2"
        self.surname2 = "Zbroiński2"
        self.age2 = 52

def view_fields_student():
    print(f"Imię: {student1.name1}, Nazwisko: {student1.surname1}, Wiek: {student1.age1}")

def view_fields_student_constr():
    print(f"Imię: {student1.name2}, Nazwisko: {student1.surname2}, Wiek: {student1.age2}")

student1 = Students()
#print(f"Imię: {student1.name}, Nazwisko: {student1.surname}, Wiek: {student1.age}")
view_fields_student()
view_fields_student_constr()