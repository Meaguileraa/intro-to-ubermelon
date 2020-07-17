log_file = open("um-server-01.txt") #opening the file 


def sales_reports(log_file): #function taking file as parameter
    """Print sales info for Monday"""
    for line in log_file: #looping through each line of the file
        line = line.rstrip() #removing characters in each line
        day = line[0:3] #identifying the first three characters as day
        if day == "Mon": #if day is Monday 
            print(line) #print that line 


sales_reports(log_file) #calling the function with file as arg
