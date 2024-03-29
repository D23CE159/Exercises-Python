# Consider an example of declaring the examination result. Design three classes:
# Student, Exam, and Result. The Student class has data members such as those
# representing rollNumber, Name, etc. Create the class Exam by inheriting Student
# class. The Exam class adds fields representing the marks scored in six subjects. Derive
# Result from the Exam class, and it has its own fields such as total marks. Write an
# interactive program to model this relationship.

class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name

    def display_info(self):
        print("Roll Number:", self.roll_number)
        print("Name:", self.name)


class Exam(Student):
    def __init__(self, roll_number, name):
        super().__init__(roll_number, name)
        self.marks = []

    def enter_marks(self):
        print("Enter marks for 6 subjects:")
        for i in range(6):
            mark = float(input(f"Subject {i + 1}: "))
            self.marks.append(mark)

    def display_marks(self):
        print("Marks:")
        for i, mark in enumerate(self.marks):
            print(f"Subject {i + 1}: {mark}")


class Result(Exam):
    def __init__(self, roll_number, name):
        super().__init__(roll_number, name)
        self.total_marks = 0

    def calculate_total_marks(self):
        self.total_marks = sum(self.marks)

    def display_result(self):
        super().display_info()
        super().display_marks()
        print("Total Marks:", self.total_marks)


def main():
    roll_number = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    result = Result(roll_number, name)
    result.enter_marks()
    result.calculate_total_marks()
    result.display_result()


if __name__ == "__main__":
    main()
