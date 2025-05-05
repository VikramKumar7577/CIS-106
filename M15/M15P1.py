class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"

class Manager(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)  

    def long_term_bonus(self):
        return self.pay * 0.40

def main():    
    emp1 = Employee('Pablo', 'Escobar', 50000)
    emp2 = Employee('Mike', 'Skittle', 55000)

    mgr1 = Manager('George', 'Michael', 80000)
    mgr2 = Manager('Michael', 'Jordan', 90000)

    print("Employees:")
    print(f"Name: {emp1.fullname()}, Email: {emp1.email}, Salary: ${emp1.pay}")
    print(f"Name: {emp2.fullname()}, Email: {emp2.email}, Salary: ${emp2.pay}")
    print()

    print("Managers:")
    print(f"Name: {mgr1.fullname()}, Email: {mgr1.email}, Salary: ${mgr1.pay}, Long-Term Bonus: ${mgr1.long_term_bonus():.2f}")
    print(f"Name: {mgr2.fullname()}, Email: {mgr2.email}, Salary: ${mgr2.pay}, Long-Term Bonus: ${mgr2.long_term_bonus():.2f}")

if __name__ == "__main__":
    main()