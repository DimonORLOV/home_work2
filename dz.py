class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if grade in range(1,11) and isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка')

    def average_score(self):
        res = []
        for it in self.grades.values():
            res.extend(it)
        s = sum(res) / len(res)
        return s

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_score()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self,name, surname)
        self.grades = {}

    def average_score(self):
        res = []
        for it in self.grades.values():
            res.extend(it)
        s = sum(res) / len(res)
        return s

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_score()}'



class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if grade in range(1,11) and isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'




student1 = Student('Dmitry', 'Orlov', 'man')
student1.finished_courses = 'Верстка сайта на HTML и CSS'
student1.courses_in_progress = 'Основы программирования Python', 'Английский для программистов'

student2 = Student('Alexey', 'Ivanov', 'man')
student2.finished_courses = 'Английский язык'
student2.courses_in_progress = 'Основы программирования Python'

lecturer1 = Lecturer('Mike', 'Shinoda')
lecturer1.courses_attached = 'Основы программирования Python', 'Английский для программистов'
lecturer2 = Lecturer('John', 'Wick')
lecturer2.courses_attached = 'Основы программирования Python'

reviewer1 = Reviewer('Leam', 'Nilsson')
reviewer1.courses_attached = 'Основы программирования Python', 'Английский для программистов'
reviewer2 = Reviewer('Kosta', 'Rika')
reviewer2.courses_attached = 'Основы программирования Python'



student1.rate_hw(lecturer1, 'Основы программирования Python', 7)
student1.rate_hw(lecturer1, 'Английский для программистов', 1)
student2.rate_hw(lecturer1, 'Основы программирования Python', 10)
student1.rate_hw(lecturer2, 'Основы программирования Python', 5)
student2.rate_hw(lecturer2, 'Основы программирования Python', 9)

reviewer1.rate_hw(student1, 'Основы программирования Python', 8)
reviewer1.rate_hw(student2, 'Основы программирования Python', 3)
reviewer1.rate_hw(student1, 'Английский для программистов', 8)
reviewer2.rate_hw(student1, 'Основы программирования Python', 5)
reviewer2.rate_hw(student2, 'Основы программирования Python', 4)

#print(student1)
#print(student2)
#print(lecturer1)
#print(lecturer2)
#print(reviewer1)
#print(reviewer2)

#print(student1.grades)

def __gt__(self, other):
    return self.average_score() > other.average_score()

#print(__gt__(student1, student2))
#print(__gt__(lecturer1, lecturer2))

#функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);

def average_rating(list_students, course):
    rem2 = []
    for stud in list_students:
        for k, v in stud.grades.items():
            if course in k:
                rem2.extend(v)
    sum_va = sum(rem2) / len(rem2)
    return print(sum_va)

#average_rating([student1, student2], 'Английский для программистов')
#average_rating([student1, student2], 'Основы программирования Python')

#функция для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса);

def average_rating_lectors(list_lectors, course):
    rem3 = []
    for lect in list_lectors:
        for k, v in lect.grades.items():
            if course in k:
                rem3.extend(v)
    sum_va2 = sum(rem3) / len(rem3)
    return print(sum_va2)

average_rating_lectors([lecturer1, lecturer2], 'Основы программирования Python')