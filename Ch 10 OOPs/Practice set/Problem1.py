class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


emp1 = Programmer("Sanjay", 1200000, 412308)

print(
    f"The name of the employee is {emp1.name} and earns {emp1.salary} . The pincode is {emp1.pin}")
