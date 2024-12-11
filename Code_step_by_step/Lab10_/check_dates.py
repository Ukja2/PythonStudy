def check_dates():
    file = open("test2.txt")
    lines = file.readlines()
    for line in lines:
        date_calcurate(line)


def date_calcurate(lines):
    part = lines.split()
    month1 = part[0]
    day1 = part[1]
    month2 = part[2]
    day2 = part[3]

    month_cal = abs(int(month1)- int(month2))

    
    if month_cal > 1:
        print(month1+"/"+day1 + " and "+ month2 +"/"+day2 +" differ by one full month or more!")        
    
    elif month_cal == 0:
        print(month1+"/"+day1 + " and "+ month2 +"/"+day2 +" are within one month of each other.")        
    
    
    elif month_cal == 1:

        if int(month1) > int(month2):
            date = 30 - int(day2)
            date_result = date + int(day1)
            if date_result >= 30:
                print(month1+"/"+day1 + " and "+ month2 +"/"+day2 +" differ by one full month or more!")        
            elif date_result < 30:
                print(month1+"/"+day1 + " and "+ month2 +"/"+day2 +" are within one month of each other.")                
                    
        elif int(month1) < int(month2):
            date = 30 - int(day1)
            date_result = date + int(day2)
            if date_result < 30:
                print(month1+"/"+day1 + " and "+ month2 +"/"+day2 +" are within one month of each other.")
            elif date_result >= 30: 
                print(month1+"/"+day1 + " and "+ month2 +"/"+day2 +" differ by one full month or more!")        