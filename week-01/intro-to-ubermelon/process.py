log_file = open("um-server-01.txt")  # open the log file


def sales_reports(log_file):  # name the function and variable it is calling
    for line in log_file:  # for loop to iterate through of line of the log
        line = line.rstrip()  # create a variable and assign it to one line of the log with all white space removed from the end of the line
        day = line[0:3]  # day of week is set to the first 3 characters of log (mon, tue, wed, etc)
        if day == "Wed":  # for entries with day of week "wedneday"
            print line  # print the log entry for that day of week


sales_reports(log_file)  # calls the function with the text of the open log file
