class parent :
    def __init__ (self, age, job, income):
        self.age = age
        self.job = job
        self.income = income

    def say_age (self):
        print (f"I am {self.age} years old")

    def say_income (self):
        print (f"I earn {self.income} shillings per month")


class child (parent):
    def __init__ (self, age, grade, job, income):
        super().__init__(age, job, income)
        self.grade = grade

    def say_child_age (self):
        super().say_age()

    def say_grade(self):
        print (f"I am in grade {self.grade}")

mtu = parent(42, "doctor", 50000)
mtoto = child (12, 7, None, None)
mtu.say_age()
mtoto.say_age()
    