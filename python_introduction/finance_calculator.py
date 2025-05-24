monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")
m1 = (monthly_income)
m2 = (monthly_expenses)
monthly_savings = float(m1) - float(m2)
#simple intrerest is  (i = p * r * t)
# principle =monthly_savings
# rate = o.05
# time = 12
interest = monthly_savings * 0.05 * 12
print("your monthly savings are", monthly_savings)
print("projected savings after one year, with interest, is:", interest) 
