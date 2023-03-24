# This program determines whether salesman met his quota

MIN_SALES = 50000.0    # The minimum sales quota

# Get the salesman's sale.
sales = float(input('Enter your amount of sales: '))

# Determine whether the salesman sales enough.
if sales >= 50000.0:
    sales_quota_met = True
    print('You have met your sales quota!')
else:
    sales_quota_met = False
    print('You did not meet your sales quota.')