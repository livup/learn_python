#python3 main.py
from utils import Util
from student import Student

def main(): 
	
	Util.welcome();
	show_results = False
	students = []

	while (show_results == False): 
		new_student = input('Do you want to create a new student? (y) or type anything to show results')

		if (new_student == 'y'):
			print(' >> New student <<	')
			stu = create_new_student()
			students.append(stu)
			stu.show_student_name()
		else :
			show_results = True;
			show_final_results(students)
	

def create_new_student():
	student_name = input('What is your student name?')
	student_score = input('Type ' + student_name + ' score:')
	return Student(student_name, student_score)

def show_final_results(students):
	print('Total of students: ' + str(len(students)))
	try:
  		avg = Util.average_from_students(students)
  		print('The class avg is: ' + str(avg))
	except:
  		print("You need to type the correct input types to calculate metrics")
	
	Util.byeBye()


    #return  reduce(lambda a, b: a.get_score() + b, lst) / len(lst) 

main();