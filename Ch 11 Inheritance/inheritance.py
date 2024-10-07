class Employee:
    company = "TCS"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "TATA"

#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(
#             f"The name is {self.name} and is good with this {self.language} language")


"""Now using inheritance"""


class Programmer(Employee):
    company = "TATA"

    def showLanguage(self):
        print(
            f"The name is {self.name} and is good with {self.language} language")


a = Employee("Sanjay", 120000)
b = Programmer("Akash", 130000)

print(a.company, b.company)
a.show()
b.show()
b.language = "Python"
b.showLanguage()
