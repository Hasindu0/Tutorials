meal_cost = float(input("Enter the cost of the meal:"))

satisfaction_level = int(input("Rate satisfaction (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))

if satisfaction_level == 1:
    tip_percentage = 20
elif satisfaction_level == 2:
    tip_percentage = 15
else:
    tip_percentage = 10

tip = (tip_percentage / 100) * meal_cost

print("Satisfaction level:",satisfaction_level)
print("Tip amount:",tip)
