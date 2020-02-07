import sys
import cs50
if (len(sys.argv) != 2):
    print("Incorrect number of arguments!")
    exit()


housename = (sys.argv[1].lower()).capitalize()
db = cs50.SQL("sqlite:///students.db")

studentsinhouse = db.execute("SELECT first,middle,last,birth FROM students WHERE house = ? ORDER BY last, first", housename)
for i in studentsinhouse:
    first = i["first"]
    middle = i["middle"]
    last = i["last"]
    birth = i["birth"]
    if i["middle"] != None:
        print(f"{first} {middle} {last}, born {birth}")
    else:
        print(f"{first} {last}, born {birth}")