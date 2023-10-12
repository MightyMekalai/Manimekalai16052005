'''Implement a function called sort_student that takes a list of student objects as input and sorts the
list based  on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
'''

class Student:

  def __init__(self, name, roll_number, cpga):
    self.name = name
    self.roll_number = roll_number
    self.cpga = cpga


def sort_student(student_list):
  # Sort the list of students in descending order of CPGA
  sorted_students = sorted(student_list,
                           key=lambda student: student.cpga,
                           reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students


# Example usage:
students = [
    Student("Hema", "A123", 7.6),
    Student("Raji", "A124", 8.9),
    Student("Sanju", "A125", 9.1),
    Student("Kavi", "A126", 9.9),
]

sorted_students = sort_student(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name:{},Roll Number:{}, CPGA:{}".format(student.name,
                                           student.roll_number,
                          student.cpga)