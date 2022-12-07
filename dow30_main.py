"""Description of Problem (The program allows users to create a hypothetical DOW 30 equity portfolio. It utilizes a step
by step format to guide users through its creation. Depending on the user input, the portfolio builder will give users
a summary of their hypothetical portfolio, which can include the tickers and shares they bought, the cost for each
position, the total cost of their equities, their equity vs cash asset allocation, their equity portfolio's weighted
average beta, weighted average p/e ratio, annual forward dividend, annual forward dividend yield, and a sector
weighted breakdown of their equity positions. It also includes a summary of their individual equity positions.)
"""

# From rating_class.py import Rating class
from rating_class import Rating


def average_beta():
    """Calculates the average beta for equity positions."""
    # Def percent_beta as dict, values for matching keys in the total_cost dictionary * their betas
    percent_beta = {k: total_cost[k] * beta_dict[k] for k in total_cost}
    # These become a list of the values and are summed then divided by the total cost values returning an avg beta
    total_beta = list(percent_beta.values())
    total_beta_values = sum(total_beta)
    avg_beta = (total_beta_values / total_cost_values)
    return avg_beta


def average_pe():
    """Calculates the average p/e ratio for equity positions."""
    # Def total_cost_pe as dict, values for matching keys in the equity dictionary * their prices if k is in pe_dict
    total_cost_pe = ({k: equity_dict[k] * prices_dict[k] for k in equity_dict if k in pe_dict})
    # Percent_pe values for matching keys in total_cost_pe dictionary * their values in pe dictionary if k in pe_dict
    percent_pe = {k: total_cost_pe[k] * pe_dict[k] for k in total_cost_pe if k in pe_dict}
    # Creates a list of the percent_pe values and sums them, creates a list of total cost pe values and sums them
    total_pe = list(percent_pe.values())
    total_pe_values = sum(total_pe)
    total_values_pe = list(total_cost_pe.values())
    total_cost_values_pe = sum(total_values_pe)
    # Divides total pe values by total cost values pe and returns the avg pe
    avg_pe = (total_pe_values / total_cost_values_pe)
    return avg_pe


def forward_yield():
    """Calculates the forward yield for equity positions."""
    # Def percent_forward dict, values in equity_dict * forward_div_dict for keys in the equity dict
    percent_forward = {k: equity_dict[k] * forward_div_dict[k] for k in equity_dict}
    # Creates a list of the percent_forward values, sums them, and returns the total_forward values
    total_forward = list(percent_forward.values())
    total_forward_values = sum(total_forward)
    return total_forward_values


def dividend_yield():
    """Calculates the dividend yield for equity positions."""
    # Def percent_forward dict, values in equity dict * forward_div_dict for keys in equity_dict
    percent_forward = {k: equity_dict[k] * forward_div_dict[k] for k in equity_dict}
    # Creates a list of percent_forward values, sums them then divides them by total_cost values * 100 returns function
    total_forward = list(percent_forward.values())
    total_forward_values = sum(total_forward)
    divided_yield = (total_forward_values / total_cost_values) * 100
    return divided_yield


def sector_percentages():
    """Calculates the sector percentage weighting for equity positions."""
    # Def user_sector_dict contains the keys then the sectors as the values
    user_sector_dict = {k: sectors_dict[k] for k in equity_dict}
    # Creates a new dictionary val_to_keys that takes the values of the user sector dict (the sectors) as the keys
    val_to_keys = {}
    # The values for this dictionary are the cost associated with each sector, summed if they are the same
    for k, v in user_sector_dict.items():
        val_to_keys[v] = val_to_keys.get(v, 0) + total_cost.get(k, 0)
    # Sector_percentages creates the final dict dividing the total amount in the sector by the total invested amount
    sector_percentages = {k: val_to_keys[k] / total_cost_values * 100 for k in val_to_keys}
    # This is then multiplied by 100 and returned as a properly formatted string
    return str('%, '.join("{}: {:.2f}".format(k, v) for k, v in sector_percentages.items()) + "%")


# DOW constant consisting of the 30 tickers
DOW = ['AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', \
       'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW']


# Defines the prices dictionary ie Ticker : Price
prices_dict = {'AXP': 175.15, 'AMGN': 208.95, 'AAPL': 142.90, 'BA': 226.39, 'CAT': 195.16, 'CSCO': 55.04, \
               'CVX': 108.05, 'GS': 392.81, 'HD': 334.34, 'HON': 217.70, 'IBM': 143.22, 'INTC': 53.81, 'JNJ': 160.93, \
               'KO': 54.12, 'JPM': 170.22, 'MCD': 247.70, 'MMM': 176.95, 'MRK': 80.63, 'MSFT': 294.85, 'NKE': 152.48, \
               'PG': 141.73, 'TRV': 157.33, 'UNH': 408.46, 'CRM': 272.48, 'VZ': 53.24, 'V': 230.27, 'WBA': 47.38, \
               'WMT': 139.50, 'DIS': 176.74, 'DOW': 58.71}

# Defines the beta dictionary ie Ticker : Beta
beta_dict = {'AXP': 1.23, 'AMGN': 0.68, 'AAPL': 1.22, 'BA': 1.57, 'CAT': 0.93, 'CSCO': 0.92, 'CVX': 1.24, 'GS': 1.5, \
             'HD': 0.99, 'HON': 1.19, 'IBM': 1.18, 'INTC': 0.59, 'JNJ': 0.72, 'KO': 0.64, 'JPM': 1.14, 'MCD': 0.60, \
             'MMM': 0.98, 'MRK': 0.42, 'MSFT': 0.80, 'NKE': 0.90, 'PG': 0.42, 'TRV': 0.77, 'UNH': 0.79, 'CRM': 1.04, \
             'VZ': 0.45, 'V': 0.97, 'WBA': 0.50, 'WMT': 0.50, 'DIS': 1.20, 'DOW': 1.71}

# Defines the P/E dictionary ie Ticker : P/E
pe_dict = {'AXP': 20.37, 'AMGN': 21.19, 'AAPL': 27.98, 'CAT': 24.50, 'CSCO': 22.1, 'CVX': 57.35, 'GS': 54.46, \
           'HD': 23.55, 'HON': 31.38, 'IBM': 24.20, 'INTC': 11.95, 'JNJ': 24.19, 'KO': 28.93, 'JPM': 11.36, \
           'MCD': 26.96, 'MMM': 17.50, 'MRK': 36.72, 'MSFT': 37.79, 'NKE': 40.43, 'PG': 25.77, 'TRV': 10.58, \
           'UNH': 26.98, 'CRM': 109.12, 'VZ': 11.03, 'V': 46.57, 'WBA': 17.91, 'WMT': 39.31, 'DIS': 289.74, \
           'DOW': 10.74}

# Defines the forward divided dictionary ie Ticker : Forward Dividend
forward_div_dict = {'AXP': 1.72, 'AMGN': 7.04, 'AAPL': 0.88, 'BA': 0.0, 'CAT': 4.44, 'CSCO': 1.48, 'CVX': 5.36, \
                    'GS': 8.0, 'HD': 6.6, 'HON': 3.92, 'IBM': 6.56, 'INTC': 1.39, 'JNJ': 4.24, 'KO': 1.68, 'JPM': 4.0, \
                    'MCD': 5.52, 'MMM': 5.92, 'MRK': 2.6, 'MSFT': 2.48, 'NKE': 1.1, 'PG': 3.48, 'TRV': 3.52, \
                    'UNH': 5.8, 'CRM': 0, 'VZ': 2.56, 'V': 1.28, 'WBA': 1.91, 'WMT': 2.2, 'DIS': 0, 'DOW': 2.8}

# Defines the sector dictionary ie Ticker : Sector
sectors_dict = {'AXP': "Financial Services", 'AMGN': "Healthcare", 'AAPL': "Technology", 'BA': "Industrials", \
                'CAT': "Industrials", 'CSCO': "Technology", 'CVX': "Energy", 'GS': "Financial Services", \
                'HD': "Consumer Cyclical", 'HON': "Industrials", 'IBM': "Technology", 'INTC': "Technology", \
                'JNJ': "Healthcare", 'KO': "Consumer Defensive", 'JPM': "Financial Services", \
                'MCD': "Consumer Cyclical", 'MMM': "Industrials", 'MRK': "Healthcare", 'MSFT': "Technology", \
                'NKE': "Consumer Cyclical", 'PG': "Consumer Defensive", 'TRV': "Financial Services", \
                'UNH': "Healthcare", 'CRM': "Technology", 'VZ': "Communication Services", 'V': "Financial Services", \
                'WBA': "Healthcare", 'WMT': "Consumer Defensive",'DIS': "Communication Services", \
                'DOW': "Basic Materials"}

# Defines the line dictionary used for external file, equity data.txt, it defines the line for which a ticker appears
# Ie Ticker : Line number in file
lines_dict = {'AXP': 0, 'AMGN': 1, 'AAPL': 2, 'BA': 3, 'CAT': 4, 'CSCO': 5, 'CVX': 6, 'GS': 7, 'HD': 8, 'HON': 9, \
              'IBM': 10, 'INTC': 11, 'JNJ': 12, 'KO': 13, 'JPM': 14, 'MCD': 15, 'MMM': 16, 'MRK': 17, 'MSFT': 18, \
              'NKE': 19, 'PG': 20, 'TRV': 21, 'UNH': 22, 'CRM': 23, 'VZ': 24, 'V': 25, 'WBA': 26, 'WMT': 27,'DIS': 28, \
              'DOW': 29}

# Prints welcome statement
print("Welcome to the DOW 30 Portfolio Builder... Note: All equity information is based on the close of market on " \
      "October 8th, 2021.")

# User input to see the dow components or not
dow_input = (input("Would you like to see the DOW 30 components before we start? If yes, type yes, " \
                   "if no, type anything."))

# If yes, opens and reads the equitydata.txt file, prints the heading string and the file contents, closes the file
# Else, prints string
if dow_input == "yes":
    f = open("equitydata.txt", "r")
    print("\nTicker | Company | Price | Beta | P / E | Forward Dividend | Dividend Yield | Sector")
    print("------------------------------------------------------------------------------------")
    print(f.read())
    f.close()
else:
    print("Ok. Let's get started")

# While True, try for input for dollars to invest as integer, except value error print string and loop
# If input is less than 1, print string and loop, if input correct, breaks
while True:
    try:
        total_dollars = int(input("Please enter the total amount you would like to invest in whole dollars:"))
        if total_dollars < 1:
            print("Value must be greater than 0.")
            continue
        else:
            break
    except ValueError:
        print("Remember your input must be a whole number greater than 0.")
        continue

# Print string with formatted total_dollars from user input
print("So you plan on investing " + "$" + "{0:,.0f}".format(total_dollars) + " dollars. That's great!")

# User input and string to add equities or not to the portfolio
add_companies = input("Would you like to add equities to your portfolio? If no, type no, if yes, type anything.")

# Opens a file to write to called newtext.txt, if answer is no, will go to else print a line break and close file
# If answer is not = to no, will print two strings then enter a while True statement
# It will try for shares input as an integer, if not will loop
file_object = open('newtext.txt', 'w+')
if add_companies != "no":
    print("Entering a ticker twice will replace the previous share count for that equity.")
    print("Non DOW 30 companies will not be accepted.")
    while True:
        try:
            # Try for shares input as an integer whole number, if not will loop
            shares_input = int(input("Enter the amount of whole shares you would like to buy of the equity:"))
            # User input ticker, change to upper, if in dow will write the shares input and ticker to file
            ticker_input = input("Enter the ticker of the equity you would like to buy for the previous shares:")
            ticker_input = ticker_input.upper()
            if ticker_input in DOW:
                file_object.write(str(shares_input) + " ")
                file_object.write(ticker_input + "\n")
            # Else ticker is not in DOW and loops
            else:
                print("Ticker entered is not in the DOW 30.")
                continue
            # If ticker and share values are correct, will prompt for more equities
            more_companies = input \
                ("Would you like to add more equities to your portfolio? If no type no, if yes, type anything.")
            # If input is no, will print a line break and close the file and break
            # If input is not no, will loop to add more equities until more companies = no
            if more_companies == "no":
                print("\n")
                file_object.close()
                break
        except ValueError:
            print("Please enter an integer value for whole shares.")
            continue
# If not adding companies will print line break and close the file
else:
    print("\n")
    file_object.close()

# Opens the newtext.txt file, reads it, adding the ticker and share amounts to a dictionary at line splits, closes file
file_object = open("newtext.txt", 'r')
equity_dict = {}
for line in file_object:
    value, key = line.split()
    equity_dict[key] = value
equity_dict = {k: int(v) for k, v in equity_dict.items()}
file_object.close()

# Defines total_cost as the equity dict values * prices dict values
total_cost = ({k: equity_dict[k]*prices_dict[k] for k in equity_dict})

# Defines total_values as a list of total_cost values
total_values = list(total_cost.values())

# Defines total_cost_values as the sum of total_values
total_cost_values = sum(total_values)

# Defines no_build if the total_cost_values or cost of equity positions exceeds total dollars invested
no_build = total_cost_values - total_dollars

# Defines remaining_cash as equal to the no_build * -1
remaining_cash = no_build * -1

# Defines asset_allocation_equity as a float of total_cost_values divided by total_dollars, then * 100
asset_allocation_equity = float((total_cost_values/total_dollars) * 100)

# Defines asset_allocation_cash as a float of total_dollars - total_cost_values divided by total_dollars, then * 100
asset_allocation_cash = float((total_dollars - total_cost_values) / total_dollars * 100)

# Defines total_keys as a list of the total_cost keys
total_keys = list(total_cost.keys())

# If the total_cost_values > total_dollars ie cost of equities > amount having to invest
# Prints string and formatted version of how much more money they need to build the portfolio
if total_cost_values > total_dollars:
    print("You do not have enough money to build this portfolio. You are short $" + "{:,.2f}".format(no_build) + ".")
# Else user inputs a portfolio name which is changed to upper
# If the add_companies answer was originally not no, prints strings joined by formatted versions of the functions
# In order, the functions return Ticker : Shares, Ticker : Cost for those shares
# Equity percentage asset allocation % value, then dollar, cash percentage % value, then dollar
# Avg Beta, Avg PE, Forward Dividend, Dividend Yield, then sector : percentage exposure
else:
    portfolio_name = input("What would you like to name your portfolio?")
    print("\n" + portfolio_name.upper())
    if add_companies != "no":
        print("These are the companies you decided to buy and their share amounts: " + \
              (str(', '.join("{}: {:,.0f}".format(k, v) for k, v in equity_dict.items()))))
        print("These are the costs for those shares by company: " + \
              (', '.join("{}: ${:,.2f}".format(k, v) for k, v in total_cost.items())))
        print("This is the sum cost of all of your equity positions: " + \
              ("$" + "{:,.2f}".format(total_cost_values)))
        print("Your equity percentage asset allocation is " + "{:,.2f}".format(asset_allocation_equity) + "%, " + \
              "$" + str("{:,.2f}".format(total_cost_values)))
        print("Your cash percentage asset allocation is " + "{:,.2f}".format(asset_allocation_cash) + "%, " + \
              "$" + str("{:,.2f}".format(remaining_cash)))
        print("Your Weighted Average Beta for your equity positions is " + "{:,.2f}".format(average_beta()))
        print("Your Weighted Average P/E Ratio for your equity positions is " + "{:,.2f}".format(average_pe()))
        if "BA" in total_keys:
            print("Note: The Boeing Company is not included in your weighted average P/E Ratio because it has negative"\
                  " earnings")
        print("Your Annual Forward Divided for your equity positions is " + "$" + \
              "{:,.2f}".format(forward_yield()))
        print("Your Annual Dividend Yield for your equity positions is " + "{:,.2f}".format(dividend_yield()) + "%")
        print("Your Sector Percentage Exposure for your equity positions is " + sector_percentages())
        # Prints string and header strings, then reads equitydata.txt
        # For every key in the equity dict that is in the lines_dict items(), it prints the line in the file
        # Final output will be the equity information from equitydata.txt for each equity in the portfolio, closes file
        print("\nBelow is a summary of your individual equity positions:")
        print("\nTicker | Company | Price | Beta | P / E | Forward Dividend | Dividend Yield | Sector")
        print("------------------------------------------------------------------------------------")
        with open("equitydata.txt", "r") as f:
            lines = f.readlines()
            for k, v in lines_dict.items():
                if k in equity_dict:
                    print(lines[v].strip())
        f.close()
    # If answered no to the original more companies input, will print cash asset allocation and cash amount
    else:
        print("Your cash percentage asset allocation is " + "{:,.2f}".format(asset_allocation_cash) + "%, " + \
              "$" + str("{:,.2f}".format(remaining_cash)))
print("\n")

# While True, will try for a rating of the experience with the portfolio using the Rate class
# User input a rate, must be a whole number integer or exceptValue error, prints string and loops
# If __lt__ less than 11 is false, prints string and loops
# If __gt__ greater than 0 is false, prints string and loops
# These ensure input is between 1 and 10 inclusively
# Else string is printed with __repr__ of the score + a separate string depending on if the rate was high, mid, or low
while True:
    try:
        rate = int(input("Please rate your experience with the DOW 30 Portfolio Builder from 1 to 10."))
        p = Rating(rate=rate, upper_rate=11, lower_rate=0, score=rate)
        if (p.__lt__(rate=rate, upper_rate=11)) == False:
            print("Your input is greater than the scale.")
            continue
        if (p.__gt__(rate=rate, lower_rate=0)) == False:
            print("Your input is lower than scale.")
            continue
        else:
            print("\nWith a score of " + (p.__repr__()) + "," + \
                  (p.rating(rate=rate, low_rate=" I'm sorry you didn't enjoy the portfolio builder.", \
                    mid_rate=" hopefully I can get a higher rating in my next version.", \
                    high_rate=" I'm happy you enjoyed the portfolio builder.")))
            break
    except ValueError:
        print("Please enter a whole number from 1 to 10.")
        continue

# Prints a line break and defines signature as a set including my name, the name of the program, and the year
# Takes unordered set and changes to a tuple and prints tuple version of signature_set
print("\n")
signature = ("Built By Harrison Huston", "Dow 30 Portfolio Builder", "2021")
signature_set = (set(signature))
signature_tuple = tuple(signature_set)
print(signature_tuple)