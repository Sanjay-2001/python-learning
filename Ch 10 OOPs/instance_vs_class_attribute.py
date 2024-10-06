class Employee:
    language = "Python"
    salary = 120000


sanjay = Employee()
sanjay.language = "Javascript"  # instance attribute gets priority
print(sanjay.language, sanjay.salary)
