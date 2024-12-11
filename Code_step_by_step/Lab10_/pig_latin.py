def pig_latin():
    file = open("test2.txt")
    lines = file.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if word[0] in 'aeiou':
                print(word + "yay", end=" ")
            else:
                print(word[1:] + word[0] + "ay", end=" ")
        print()


pig_latin()
 