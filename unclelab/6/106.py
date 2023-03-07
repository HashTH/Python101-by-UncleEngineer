class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and work as a {self.occupation}.")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday! Now I am {self.age} years old.")
    
    def change_occupation(self, new_occupation):
        self.occupation = new_occupation
        print(f"I have changed my occupation to {self.occupation}.")

p1 = Person("John", 30, "programmer")
p1.introduce()
# Output: Hi, my name is John. I am 30 years old and work as a programmer.

p1.celebrate_birthday()
# Output: Happy Birthday! Now I am 31 years old.

p1.change_occupation("engineer")
# Output: I have changed my occupation to engineer.

print(p1.name)
# Output: John

class Student(Person):
    def __init__(self, name, age, grade, school):
        super().__init__(name, age, "student")
        self.grade = grade
        self.school = school
    
    def introduce(self):
        super().introduce()
        print(f"I am currently in grade {self.grade} at {self.school}.")
    
    def study(self):
        print("I am studying hard!")
    
    def take_exam(self):
        print("I am taking the exam now.")

