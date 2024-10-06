class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod  # to avoid self
    def greet():
        print("Good Morning")


sanjay = Employee()
sanjay.language = "Javascript"

sanjay.getInfo()
# or
Employee.getInfo(sanjay)

sanjay.greet()
