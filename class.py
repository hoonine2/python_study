class Student:

    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.is_graduated = False

    def study(self):
        print(f'{self.name} 학생은 공부 중입니다.')

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경되었습니다.')

student_1 = Student('김멋사', '컴퓨터공학과')
# student_1.major = '기계공학과'
student_1.edit_major('기계공학과')

print(student_1.major)

# print('========')
# student_1_name = student_1.name
# print(student_1_name)

# print('========')

# student_1_graduated = student_1.is_graduated
# print(student_1_graduated)

# print('========')

# student_1.study()