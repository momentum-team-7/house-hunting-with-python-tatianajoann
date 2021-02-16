#annual_salary = int(input("What is your annual salary?"))


def current_savings():
    total_cost = int(input("what is the price of your dream home?"))
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    annual_salary = float(input("What is your annual salary?"))
    monthly_salary = annual_salary / 12
    months = 0
    portion_saved = float(input("How much do you intend to save each month?"))
    monthly_amt_added = monthly_salary * portion_saved
    while current_savings < portion_down_payment * total_cost:
        months += 1
        current_savings += monthly_amt_added + \
            ((current_savings*r)/12)
    print("Number of months: ", months)


current_savings()
