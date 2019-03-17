import csv

Pybankpath= r"C:\Users\laura\Desktop\LearnPython\Python.Challenge\PyBank\budget_data.csv"
with open(Pybankpath, newline='') as Pybankcsv:
    pyreader = csv.reader(Pybankcsv, delimiter=',')
    pyheader = next(pyreader, None)

    months = []
    profit = []
    change = []
    for row in pyreader:
        months.append(row[0])
        profit.append(int(row[1]))

prev = 0
change = list()
for i in profit:
    change.append(i - prev)
    prev = i
print(f'Total Months: {len(months)}')
print(f'Total: ${sum(profit)}')
print(f'Greatest Increase in Profits: {months[change.index(max(change))]}')
print(f'Greatest Decrease in Profits: {months[change.index(min(change))]}')



