# 创建一个类，用于存储IBI1学生的信息
class Student:
    def __init__(self, name, major, portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.portfolio_score = portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    # 类方法，打印学生的所有信息
    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, "
              f"Portfolio Score: {self.portfolio_score}, "
              f"Group Project Score: {self.group_project_score}, "
              f"Exam Score: {self.exam_score}")
# example
student1 = Student("Alice Smith", "BMI", 85, 90, 78)
student1.print_details()