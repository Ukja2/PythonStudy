def election():
    filename = input("Input file? ")
    
    candidate1= 0
    candidate2 = 0
    
    
    file = open(filename)
    lines = file.readlines()
    for line in lines:
    
        data = line.split() 
            
        candidate1_percent = float(data[1])
        candidate2_percent = float(data[2])
        electoral_votes = int(data[3])
            
            
        if candidate1_percent > candidate2_percent:
            candidate1 += electoral_votes
        elif candidate2_percent > candidate1_percent:
            candidate2 += electoral_votes
            

    
    
    print(f"Candidate 1: {candidate1} votes")
    print(f"Candidate 2: {candidate2} votes")
