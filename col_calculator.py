#!/usr/bin/python3

print("For all values entered please use whole numbers. Do not use dollar signs, only integers.")

monthly_rent = input("Please enter your monthly rent ")

yearly_rental_expense = int(monthly_rent) * 12

print("Your annual housing is %i" % yearly_rental_expense)

annual_household_salary = input("Please enter your salary ")

current_housing_percentage = int(yearly_rental_expense) * 100 / int(annual_household_salary)

print("Your current annual housing percentage is %i" % current_housing_percentage)

monthly_mortgage_payment = input("Enter your monthly mortgage payment ")

yearly_mortgage_expense = int(monthly_mortgage_payment) * 12

print("Your annual housing expense with this mortgage value is ", yearly_mortgage_expense)

new_annual_household_salary = input("Please enter your salary at different location ")

new_housing_percentage = int(yearly_mortgage_expense) * 100 / int(new_annual_household_salary)

print("If you move your new housing percentage will be %i" % new_housing_percentage)

print("Now you have an idea of what housing prices are equivalent at different payscales. If the percentage is mostly the same, with no other changes COL/lifestyle may be roughly similar. Currently your housing costs are %i of your income, if you relocate housing costs will be %i." % (current_housing_percentage, new_housing_percentage))
