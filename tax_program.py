salary = float(input("Enter your monthly salary: "))

if salary <= 30000:
    tax = 0
elif salary <= 60000:
    tax = salary * 0.10
elif salary <= 100000:
    tax = salary * 0.15
else:
    tax = salary * 0.20

net_salary = salary - tax

print("Tax to be paid:",  tax)
print("Net salary after tax:", net_salary)
      
