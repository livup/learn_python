class Student:
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def show_student_name(self):
    print("Student name is " + self.name)
    print("Student score is " + self.score)

  def get_score(self):
  	return self.score;

