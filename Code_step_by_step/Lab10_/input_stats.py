def input_stats(text):
    file = open(text)
    lines = file.readlines()

    total_line = len(lines)

    longest = 0
    sum = 0
    average = 0

    for i in range(total_line):
        word = len(lines[i].strip())
        print(f"Line {i + 1} has {word} chars")
        if longest < word:
            longest = word
        sum += word
    average = round(sum / total_line, 1)
    print(f"{total_line} lines; longest = {longest}, average = {average} ")


