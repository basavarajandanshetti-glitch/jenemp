import sys

# Expecting 4 arguments: name, rollno, salary, exp
if len(sys.argv) != 5:
    print("Usage: script.py <name> <rollno> <salary> <exp>")
    sys.exit(1)

script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]
salary = sys.argv[3]
exp = sys.argv[4]

print(f"Script Name: {script_name}")
print(f"Name: {name}")
print(f"Roll Number: {rollno}")
print(f"Salary: {salary}")
print(f"Experience: {exp}")

