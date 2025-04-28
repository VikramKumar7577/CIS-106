class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.enrolled_credits = enrolled_credits

    def compute_tuition(self):
        if self.district_code == 'I':
            cost_per_credit = 250
        else:
            cost_per_credit = 500
        tuition = self.enrolled_credits * cost_per_credit
        return tuition

def main():
    student1 = Student("Kim", "Jung", "I", 12)

    tuition = student1.compute_tuition()

    print(f"Student: {student1.first_name} {student1.last_name}")
    print(f"District Code: {student1.district_code}")
    print(f"Credits Enrolled: {student1.enrolled_credits}")
    print(f"Tuition Owed: ${tuition:.2f}")

if __name__ == "__main__":
    main()