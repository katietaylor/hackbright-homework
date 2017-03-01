"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople_totals = {}

# open file
text = open("sales-report.txt")

# iterate of each line, split line into a list, and unpack into variables
for line in text:
    line = line.rstrip()
    salesperson, price, melons = line.split("|")

    # add salesperson to dictionary with initial melon count and then add to
    # melon count every time the salesperson is found in the list
    salespeople_totals[salesperson] = salespeople_totals.get(salesperson, 0
        ) + int(melons)

# sort the salespeople alphabetically for easier reading
salespeople = sorted(salespeople_totals.keys())

# for each salesperson in the dictionary, print their melon counts
for salesperson in salespeople:
    print "{} sold {} melons".format(salesperson, salespeople_totals[salesperson])
