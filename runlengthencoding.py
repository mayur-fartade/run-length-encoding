
def encode(text):
    new = []
    i = 1
    count = 1
    while i < len(text):
        if text[i] == text[i-1]:
            count += 1
        else:
            new.append(str(count)+text[i-1])
            count = 1
        i += 1
    new.append(str(count)+text[i-1])
    return ''.join(new)
    
print("Encoded text is ", encode("CCCCCABCCCAAACC") )

