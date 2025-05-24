monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")
monthly_income = monthly_income
monthly_expenses = monthly_expenses
monthly_savings = float(monthly_income) - float(monthly_expenses)
#simple intrerest is  (i = p * r * t)
# principle =monthly_savings
# rate = o.05
# time = 12
interest = monthly_savings * 0.05 * 12
print("your monthly savings are", monthly_savings)
print("projected savings after one year, with interest, is:", interest) 
