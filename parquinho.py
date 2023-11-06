def get_count(sentence):
    list = []
    n = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            list.append(i)
            n +=1
    return n

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

getCountLambda = lambda inputStr: sum(1 for let in inputStr if let in "aeiouAEIOU")

print(getCount("aeioux"))
print(get_count("aeioux"))
print(getCountLambda("aeioux"))