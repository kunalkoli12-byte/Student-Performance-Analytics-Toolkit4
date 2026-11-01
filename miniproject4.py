#student performance analysis toolkit

students = {}


def addStudents() :
    n = int(input("Enter number of students to add : "))

    for i in range(n) :

        while True :
            id = input("Enter student id: ")

            if id in students:
                print("ID already exixts, enter another one")
            else:
                break

        name = input("Enter student's name: ")



        # i'll take marks for 3 subjects only.
        marks = []

        for i in range(1,4):
            mark = int(input(f"Enter marks of subject {i}: "))
            marks.append(mark)


        students[id] = {
            'name':name,
            'marks':marks
        }

def calculateTotal(marks):
    total_marks = sum(marks)
    average_marks = total_marks/len(marks)

    return total_marks,average_marks 


def getGrades(average):
    grade = ""
    if average >=75:
        grade = "Distinction"
    elif average >= 60:
        grade = "First Division"
    elif average >=40:
        grade = "Pass"
    else:
        grade = "Fail"

    return grade 





def buildReport(marks):
    
    total,average = calculateTotal(marks)
    grade = getGrades(average)
    report = {
        'Total_Marks' : total,
        'Average_Marks' : average,
        'Grade' : grade
    }
    return report 

def displayReport(students):
    print("\n=====STUDENT REPORT=====")

    for id, student in students.items() :
        name = student['name']
        marks = student['marks']
        report  = buildReport(marks)
        total = report['Total_Marks']
        average = report['Average_Marks']
        grade = report['Grade']

        
        print(f"\n{id} | {name} Marks: {marks} ")
        print(f"Total: {total} | Average: {average} | Grade: {grade}")

    

    

def get_top_students(students):

    top_students = list(filter( lambda student : calculateTotal(student['marks'])[1] >= 75,students.values() ))
    return top_students 

def displayTopStudents(top_students):

    print("\n===== TOP STUDENTS =====")

    for student in top_students:
        print(student['name'], student['marks'])






def calculateAverage(*marks):  #using positional arguments

    if len(marks) == 0:
        return 0

    total = sum(marks)
    average = total / len(marks)

    return average


 

def classSummary(**options):  # using keyword positional arguments

    title = options.get('title', 'Class Report')
    passing_mark = options.get('passing_mark', 40)

    print("\n====", title, "====")
    print("Passing Marks:", passing_mark)


 
def studentDetails(name, age=20):

    print("Name:", name)
    print("Age:", age)






def recursiveSum(n):

    if n == 0:
        return 0

    return n + recursiveSum(n - 1)







count = 0

def scopeDemo():

    local_variable = 100

    print("Local variable:", local_variable)

    global count
    count += 1





def runProgram():

    addStudents()

    displayReport(students)

    top_students = get_top_students(students)
    displayTopStudents(top_students)

    names = list(map(
        lambda student: student['name'],
        students.values()
    ))

    print("\nStudent Names:", names)

    all_marks = []

    for student in students.values():
        all_marks.extend(student['marks'])

    class_average = calculateAverage(*all_marks)

    print("\nClass Average:", round(class_average, 2))

    classSummary(
        title="Student Performance Analytics",
        passing_mark=40
    )

    print("\nRecursive Sum from 1 to 5:", recursiveSum(5))


runProgram()










