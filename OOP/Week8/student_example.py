class Student(object):
    """Simple student class"""
    def __init__ (self, first = "", last = "", id=0, grade=0): # initializer
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id
        self.grade = grade

    def __str__(self):
        return "{} {}, ID: {}".format(self.first_name_str, self.last_name_str, self.id_int)

    def print_grade(self):
        return "Grade is: {}".format(self.grade)

student1 = Student("Lucas", "Rizzo", 1, 100)
print(student1.print_grade())

student1.age = 31
print(student1.age)

print(type(student1))


# print("Grade student1: ", student1.print_grade())
#
# student2 = Student("New", "Student", 2)
# print(student2)
# print("Grade student2: ", student2.print_grade())
#
# students = []
#
# for i in range(100):
#     students.append(Student("Name" + str(i), "Last" + str(i), i))
#
# print(students[99])

