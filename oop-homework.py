class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average()}\n\
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"

    def __lt__(self,other):
        return self.__average() < other.__average()
    def __gt__(self,other):
        return self.__average() > other.__average()
    def __le__(self,other):
        return self.__average() <= other.__average()
    def __ge__(self,other):
        return self.__average() >= other.__average()
    def __eq__(self,other):
        return self.__average() == other.__average()
    def __ne__(self,other):
        return self.__average() != other.__average()

    
    def __average(self):
        if self.grades:
            average = 0
            for grades in self.grades.values():
                average += sum(grades) / len(grades)
            return average / len(self.grades)
        else:
            return "оценок нет"
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]                
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average()}\n"
    
    def __average(self):
        if self.grades:
            average = 0
            for grades in self.grades.values():
                average += sum(grades) / len(grades)
            return average / len(self.grades)
        else:
            return "оценок нет"

    def __lt__(self,other):
        return self.__average() < other.__average()
    def __gt__(self,other):
        return self.__average() > other.__average()
    def __le__(self,other):
        return self.__average() <= other.__average()
    def __ge__(self,other):
        return self.__average() >= other.__average()
    def __eq__(self,other):
        return self.__average() == other.__average()
    def __ne__(self,other):
        return self.__average() != other.__average()

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

rovin_reviewer = Reviewer('Alexander', 'Rovin')
lavatin_reviewer = Reviewer('Mikhail', 'Lavatin')
markin_student = Student('Ivan', 'Markin', 'male')
averina_student = Student('Lera', 'Averina', 'female')
komarov_lecturer = Lecturer('Vasiliy', 'Komarov')
filatov_lecturer = Lecturer('Oleg', 'Filatov')

markov_student = Student('Anton', 'Markov', 'male')

markin_student.courses_in_progress += ['Python','Java']
markin_student.finished_courses += ['C++','Javascript']
averina_student.courses_in_progress += ['C++','Javascript']
averina_student.finished_courses += ['Python','Java']

markov_student.courses_in_progress += ['Python']

rovin_reviewer.courses_attached += ['Python','Java']
lavatin_reviewer.courses_attached += ['C++','Javascript']

komarov_lecturer.courses_attached += ['Python','Javascript']
filatov_lecturer.courses_attached += ['C++','Java']

markin_student.rate_lect(komarov_lecturer, 'Python', 10)
markin_student.rate_lect(filatov_lecturer, 'Java', 7)
markin_student.rate_lect(komarov_lecturer, 'Python', 5)
markin_student.rate_lect(filatov_lecturer, 'Java', 8)
averina_student.rate_lect(filatov_lecturer, 'C++', 5)
averina_student.rate_lect(komarov_lecturer, 'Javascript', 4)
averina_student.rate_lect(filatov_lecturer, 'C++', 7)
averina_student.rate_lect(komarov_lecturer, 'Javascript', 9)

markov_student.rate_lect(komarov_lecturer, 'Python', 9)
markov_student.rate_lect(komarov_lecturer, 'Python', 8)

rovin_reviewer.rate_hw(markin_student,'Python', 9)
rovin_reviewer.rate_hw(markin_student,'Python', 6)
rovin_reviewer.rate_hw(markin_student,'Java', 10)
rovin_reviewer.rate_hw(markin_student,'Java', 9)
lavatin_reviewer.rate_hw(averina_student,'C++', 9)
lavatin_reviewer.rate_hw(averina_student,'C++', 6)
lavatin_reviewer.rate_hw(averina_student,'Javascript', 10)
lavatin_reviewer.rate_hw(averina_student,'Javascript', 9)

rovin_reviewer.rate_hw(markov_student,'Python', 9)
rovin_reviewer.rate_hw(markov_student,'Python', 8)


print(markin_student)
print(averina_student)
print(markin_student == averina_student)
print(komarov_lecturer)
print(filatov_lecturer)
print(komarov_lecturer == filatov_lecturer)

students = [markin_student,markov_student,averina_student]
lecturers = [komarov_lecturer,filatov_lecturer]

def course_average(course,persons):
    average = 0
    count = 0
    for person in persons:
        grades = person.grades.get(course)
        if grades is not None:
            count += 1
            average += sum(grades) / len(grades)
    try:
        average /= count
    except:
        return "Нет курса с таким названием"
    return average


print(course_average('Python',students))
print(course_average('Python',lecturers))


