import sys
if len(sys.argv) != 3:
    print("Usage: script.py <name> <rollno> <salary> <exp>")
    sys.exit(1)
    script_name = sys.argv[0]
    name = sys.argv[1]
    id = sys.argv[2]
    salary = sys.argv[3]
    exp = sys.argv[4]
print(f"Script Name: {script_name}")
print(f"Name: {name}")
print(f"Roll Number: {rollno}")
print(f"salary: {salary}")
