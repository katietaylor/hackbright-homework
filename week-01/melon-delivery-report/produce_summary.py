
def print_report(file, day):
    print "Day %s" % (day)
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            count, melon, amount)
    the_file.close()

print_report("um-deliveries-20140519.txt", 1)
print_report("um-deliveries-20140520.txt", 2)
print_report("um-deliveries-20140521.txt", 3)
