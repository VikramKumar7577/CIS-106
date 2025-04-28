class Student:
   
    tuition_rates = {
        'I': 250, # In-District 
        'O': 500, # Out-of-District 
        'X': 800, # International 
        'G': 250   # Reciprocity 
    }

    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
       
        cost_per_credit = Student.tuition_rates.get(self.district_code, 500)  
        tuition = self.enrolled_credits * cost_per_credit
        return tuition

def main():
   
    student1 = Student("Kim", "Jung", "I", 12)  # In-District
    student2 = Student("Charlie", "Sheen", "O", 9)  # Out-of-District
    student3 = Student("Dennis", "Rodman", "X", 15)  # International
    student4 = Student("Ozzy", "Osbourne", "G", 6)  # Reciprocity

    students = [student1, student2, student3, student4]

    for student in students:
        tuition = student.compute_tuition()
        print(f"Student: {student.first_name} {student.last_name}")
        print(f"District Code: {student.district_code}")
        print(f"Credits Enrolled: {student.enrolled_credits}")
        print(f"Tuition Owed: ${tuition:.2f}")
        print("-" * 30)

if __name__ == "__main__":
    main()