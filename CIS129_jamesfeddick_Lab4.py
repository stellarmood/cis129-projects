# Module 4
# Author: James Feddick
# Date: 3/5/25
# This program calculates store and employee bonuses based on sales and sales increase.

def main():
    # declare local variables
    monthlySales = getSales("Enter the monthly sales amount: ")  # monthly sales amount
    storeAmount = calcStoreBonus(monthlySales)  # store bonus amount
    salesIncrease = getIncrease("Enter the percent of sales increase: ")  # percent of sales increase
    empAmount = calcEmpBonus(salesIncrease)  # employee bonus amount
    printBonus(storeAmount, empAmount)  # print both bonuses

# monthly sales
def getSales(prompt):
    monthlySales = float(input(prompt))
    return monthlySales

# percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100  # Convert percentage to decimal
    return salesIncrease

# storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# calls main
main()
