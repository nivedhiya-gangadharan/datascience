student = {
    1: "ritu",
    2: "akhil",
    3: "rema",
    4: "sarika"
}
print("")

print(student)

student[1] = "amal"
print("after updating:", student)

student.pop(2)
print(student)

print("all students with name and roll number", student)

roll = int(input("Enter the roll number of student to be searched: "))

if roll in student:
    print("The student is in the class")
else:
    print("The student is not in the class")
