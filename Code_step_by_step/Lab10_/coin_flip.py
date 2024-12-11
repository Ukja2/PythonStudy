def coin_flip():
    file = open("test2.txt")
    lines = file.readlines()
    h_count = 0
    t_count = 0

    for line in lines:
        part = line.split()

        for i in part:
            a = i.upper()
            if a[0] == "H":
                h_count += 1
            elif a[0] == "T":
                t_count += 1
        
    total = h_count + t_count

    percentage = round((h_count / total) * 100, 1)

    print(f"{h_count} heads ({percentage}%)")

    if percentage >= 50:
        print("You win!")
    else:
        print("You lose!")


coin_flip()