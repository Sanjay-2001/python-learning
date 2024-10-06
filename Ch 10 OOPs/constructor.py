class Employee:
    language = "Python"
    salary = 120000

    # __ dunder method which is automatically called
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The langugae is {self.language}. The salary is {self.salary}")


sanjay = Employee("Sanjay", 130000, "Javascript")
# sanjay.getInfo()
print(sanjay.name, sanjay.salary, sanjay.language)

# akash = Employee()
