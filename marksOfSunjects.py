#WAP to enter marks of 3 subjects from the user and store them in a dictonary, start with an empty dictionary & add one by one. Use subjects name as key & marks as value.

subjects = {

}
physics = int(input("Enter the marks of Physics : "))
chemistory = int(input("Enter the marks of chemistory : "))
maths = int(input("Enter the marks of maths : "))

subjects.update({"physics " : physics})
subjects.update({"chemistory" : chemistory})
subjects.update({"maths" : maths})


print(subjects)