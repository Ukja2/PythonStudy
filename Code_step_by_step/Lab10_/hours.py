def hours():

    file = open("test2.txt")
    lines = file.readlines()

    for line in lines:
        subject(line)    


def subject(line):
    data = line.split()
    
    ID = data[0]
    name = data[1]
    total_hour = 0
    
    for i in range(2,len(data)):
        total_hour += float(data[i])
    

    total_hour = round(total_hour,1)
    avg_day = round(total_hour/(len(data)-2),1)
    print(f"{name} (ID#{ID}) worked {total_hour} hours ({avg_day}/day) ")

    


hours()