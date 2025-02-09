#ուսանողների ցուցակ՝ ներառող տվյալներ յուրաքանչյուր ուսանողի վերաբյալ՝ անուն, տարիք, միջին բալ։
#Անհրաժեշտ է տեսակավորել այդ ցուցակը ըստ միջին բալի:
def add_student():
    st_name = input("Enter student name: ")
    st_age = int(input("Enter student age: "))
    st_grade = float(input("Enter student mean grade: "))
    return st_name, st_age, st_grade

students = []
n = int(input("Enter how many students you want to add: "))
for i in range(n):
    students.append(add_student())

sorted_students = sorted(students, key=lambda student: student[0])

for student in sorted_students:
    print(f"Student: {student[0]}, Average grade: {student[2]}")


