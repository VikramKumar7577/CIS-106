class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def calculate_bonus(self, bonus_rate):
        return self.pay * bonus_rate

def main():
    emp1 = Employee('Lee', 'Giddy', 50000)
    emp2 = Employee('Test', 'Employee', 60000)

    print(f"Employee 1: {emp1.fullname()} - {emp1.email} - Salary: ${emp1.pay}")
    print(f"Employee 2: {emp2.fullname()} - {emp2.email} - Salary: ${emp2.pay}")

    bonus_rate = float(input("Enter bonus rate (e.g., 0.10 for 10%): "))

    bonus1 = emp1.calculate_bonus(bonus_rate)
    bonus2 = emp2.calculate_bonus(bonus_rate)

    print(f"Bonus for {emp1.fullname()} is: ${bonus1:.2f}")
    print(f"Bonus for {emp2.fullname()} is: ${bonus2:.2f}")

if __name__ == "__main__":
    main()