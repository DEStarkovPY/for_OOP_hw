class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.half_grade = 0
        
    
    def self_half_grade(self):
        summ = 0
        i = 0
        for grades_on_course in self.grades.values():
            for grade in grades_on_course:
                summ += grade
                i += 1
        if i != 0:
            self.half_grade = round(summ / i,1)
            return self.half_grade
        else:
            self.half_grade = 'Нет оценок'
            return self.half_grade
    
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Другой человек не является студентом!')
        else:
            return print(self.half_grade < other.half_grade)
    
    
    
    
    def __str__(self):
        info = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.self_half_grade()}
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}'''
        return info
        
    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def rate_fight(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if self.half_grade > lecturer.half_grade:
                return print(f'Средняя оценка студента больше оценки лектора в {round(self.half_grade/lecturer.half_grade,1)} раза')
            elif self.half_grade < lecturer.half_grade:
                return print(f'Средняя оценка студента меньше оценки лектора в {round(lecturer.half_grade/self.half_grade,1)} раза')
            else:
                return print('Средние оценки студента и лектора равны')
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.half_grade = 0
        
        
        
    def rate_hw(self, student, course, grade):
        return print('Я не выставляю оценки, не беспокойте меня!')
    
    
    
    def self_half_grade(self):
        summ = 0
        i = 0
        for grades_on_course in self.grades.values():
            for grade in grades_on_course:
                summ += grade
                i += 1
        if i != 0:
            self.half_grade = round(summ / i,1)
            return self.half_grade
        else:
            self.half_grade = 'Нет оценок'
            return self.half_grade
    
    
    
    def __str__(self):
        info = f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.self_half_grade()}'''
        return info
    
    
    
    def rate_fight(self, student):
        if isinstance(student, Student):
            if self.half_grade > student.half_grade:
                return print(f'Средняя оценка лектора больше оценки студента в {round(self.half_grade/student.half_grade,1)} раза')
            elif self.half_grade < student.half_grade:
                return print(f'Средняя оценка лектора меньше оценки студента в {round(student.half_grade/self.half_grade,1)} раза')
            else:
                return print('Средние оценки студента и лектора равны')
        
        
        
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Другой человек не является лектором!')
        else:
            return print(self.half_grade < other.half_grade)
            
        
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_checking = []
    
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_checking and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info = f'''
        Имя: {self.name}
        Фамилия: {self.surname}'''
        return info
    
    

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C#']

second_student = Student('Ken', 'Grey', 'your_gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['C#']
second_student.courses_in_progress += ['C#']
second_student.courses_in_progress += ['Python']
 
cool_lecturer = Lecturer('Tom', 'Hard')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C#']

best_lecturer = Lecturer('Ben', 'Drip')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['C#']


cool_reviewer = Reviewer('Tim', 'Soft')
cool_reviewer.courses_checking += ['Python']
cool_reviewer.courses_checking += ['C#']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'C#', 9)
best_student.rate_lc(cool_lecturer, 'Python', 8)
best_student.rate_lc(cool_lecturer, 'C#', 8)
best_student.rate_lc(best_lecturer, 'Python', 10)
second_student.rate_lc(best_lecturer, 'C#', 10)

cool_reviewer.rate_hw(second_student, 'Python', 5)
cool_reviewer.rate_hw(second_student, 'C#', 6)


print(best_student)
print(cool_reviewer)
print(cool_lecturer)


best_lecturer.__lt__(cool_lecturer)
best_student.__lt__(second_student)

best_student.rate_fight(cool_lecturer)
cool_lecturer.rate_fight(best_student)


student_list = [best_student, second_student]
lecturer_list = [cool_lecturer, best_lecturer]

def half_all_student_grade(st_list, course):
    grade_sum = 0
    i = 0
    for student in st_list:
        for _course, grades in student.grades.items():
            if _course == course:
                for grade in grades:
                    grade_sum += grade
                    i += 1
    half_grade_sum =  grade_sum / i
    return print(f'Средняя оценка всех студентов за этот курс: {round(half_grade_sum,1)}')

def half_all_lecturer_grade(lc_list, course):
    grade_sum = 0
    i = 0
    for lecturer in lc_list:
        for _course, grades in lecturer.grades.items():
            if _course == course:
                for grade in grades:
                    grade_sum += grade
                    i += 1
    half_grade_sum =  grade_sum / i
    return print(f'Средняя оценка всех лекторов за этот курс: {round(half_grade_sum,1)}')
            
                
        

half_all_student_grade(student_list, 'C#')          
half_all_lecturer_grade(lecturer_list, 'C#')


