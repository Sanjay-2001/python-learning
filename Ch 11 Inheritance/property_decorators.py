class Employee:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
        # return

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        # self.language = "Python"

    @property
    def language(self):
        return f"{self.lang1}, {self.lang2}"

    @language.setter
    def language(self, value):
        self.lang1 = value.split(",")[0]
        self.lang2 = value.split(",")[1]


e = Employee()

e.name = "Sanjay Dutta"
e.language = "python,javascript"
print(e.name)
print(f"first name is : {e.fname}, last name is {e.lname}")
print(e.language)
print(f"lang1 is {e.lang1}, lang2 is {e.lang2}")
