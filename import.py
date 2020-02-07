import sys
import cs50
import csv

if (len(sys.argv) != 2):
    print("Incorrect number of args!")
    exit()

db = cs50.SQL("sqlite:///students.db")
db.execute("DELETE FROM students")
file = sys.argv[1]
with open(f"{sys.argv[1]}", "r") as fileobject:
    filei = csv.DictReader(fileobject)

    for i in filei:
        fullname = i["name"].split(" ")
        first = fullname[0]
        if (len(fullname) == 3):
            middle = fullname[1]
            last = fullname[2]
        if (len(fullname) == 2):
            middle = None
            last = fullname[1]
        house = i["house"]
        birth = i["birth"]
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", first, middle, last, house, birth)