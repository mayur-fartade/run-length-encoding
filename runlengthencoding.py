
def encode(text):
    new =""
    for i in range(0,len(text) ):
        if i!=0 and text[i] == text[i-1]:
            continue
        count = 1
        for j in range(i+1, len(text)):
            if text[i] != text[j]:
                break
            else:
                count += 1
                
        new += str(count) + text[i]
    return new

print("Encoded text is ", encode("CCCCCABCCCAAACC") )

#Try with different values 
