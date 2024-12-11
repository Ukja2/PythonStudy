def average_value_in_file():
    file = open("test2.txt")
    lines = file.readlines()
    sum = 0
    for line in lines:
        if len(lines) == 0:
            return 0.0
    
        sum += float(avg(line))

    average = round(sum / len(lines),2)
    return average

def avg(line):
    part = line.strip()
    return float(part)
    
average_value_in_file()