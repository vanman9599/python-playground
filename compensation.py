class calculateCompensation:
    base_rate = 30
    base_pay_time = 1.5
    additional_rate = 20
    max_hours = 70
    bonus_rate = base_rate + (base_rate/2)  # base rate + 50%

    def __init__(self, hours_worked, tasks_completed):
        self.hours_worked = hours_worked
        self.tasks_completed = tasks_completed

    def calculatePay(self):
        additional_time = self.hours_worked - self.base_pay_time
        additional_pay = additional_time * self.additional_rate
        base_pay = self.base_rate * self.base_pay_time
        return base_pay + additional_pay

    def calculateBonus(self):
        if self.hours_worked > 70:
            self.hours_worked = 70
        if self.hours_worked > 40:
            return self.bonus_rate * (self.hours_worked - 40)
        else:
            return 0


if __name__ == '__main__':
    hours_worked = float(input("Enter the number of hours worked: "))
    tasks_completed = int(input("Enter the number of tasks completed: "))
    compensation = calculateCompensation(hours_worked, tasks_completed)
    pay = compensation.calculatePay()
    bonus = compensation.calculateBonus()
    print(f"Base pay: ${pay}")
    print(f"Bonus: ${bonus}")
    print(f"Total pay: ${pay + bonus}")
