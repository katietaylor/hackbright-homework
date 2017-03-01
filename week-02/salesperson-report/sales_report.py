"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople_totals = {}

# open file
text = open("sales-report.txt")

# iterate of each line and split in a list
for line in text:
    line = line.rstrip()
    entries = line.split("|")

    # create a variable from the list for salesperson and melons sold
    salesperson = entries[0]
    melons = int(entries[2])

    salespeople_totals[salesperson] = salespeople_totals.get(salesperson, 0) + melons

salespeople = sorted(salespeople_totals.keys())

for salesperson in salespeople:
    print "{} sold {} melons".format(salesperson, salespeople_totals[salesperson])
