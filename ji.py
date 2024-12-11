def convert_to_alt_caps(text):
    convert=0
    count = False
    
    for i in text:
        if i != " ":
            if not count:
                convert += 1
                count = True
        else:
            count = False
    print(convert)

convert_to_alt_caps(       "hello mr my my       ")
