#
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

student={"Alice":45,"Bob":32,"Carol":25,"Dave":50}
a=input("Enter The Student Name:")
b=student.get(a)
if b==None:
    print(a+" not found")
else:
    print(a+"'s mark is",student[a])
