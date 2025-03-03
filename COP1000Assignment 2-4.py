salary = 1250
numDependents = 2

print("The employee's salary is", salary)
print ('The number of dependents is', numDependents)

stateTax= salary * 0.065
federalTax= salary * 0.28
dependentsDeduction= salary * 0.025 * numDependents
totalWithholding= stateTax + federalTax + dependentsDeduction
takeHomePay= salary - totalWithholding

print("State Withholding Tax:", stateTax)
print("Federal Withholding Tax:", federalTax)
print("Dependents Deduction:", dependentsDeduction)
print("Total Withholding:", totalWithholding)
print("Take Home Pay:", takeHomePay)

salary = float(input("Enter the employee's salary: "))
numDependents = int(input("Enter the number of dependents: "))

stateTax= salary * 0.065
federalTax= salary * 0.28
dependentsDeduction= salary * 0.025 * numDependents
totalWithholding= stateTax + federalTax + dependentsDeduction
takeHomePay= salary - totalWithholding

print("The employee's salary is", salary)
print("The number of dependents is", numDependents)
print("State Withholding Tax:", stateTax)
print("Federal Withholding Tax:", federalTax)
print("Dependents Deduction:", dependentsDeduction)
print("Total Withholding:", totalWithholding)
print("Take Home Pay:", takeHomePay)