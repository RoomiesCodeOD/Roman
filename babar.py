#Dictionary to store the roman numerals and arabic equivalents
roman = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500,'M':1000}

print("This takes a user input Roman numeral and converts to equivalent Arabic Numeral")
conv = list(input("\nEnter Roman Numeral to convert [ROMAN NUMERAL IN ALL CAPS]! \n"))

sum = 0
for index,numeral in enumerate(conv):
    if (index+1) == len(conv) or roman[conv[index]] >= roman[conv[index+1]]:
        #print(index+1)
        sum += roman[numeral]
    else:
        sum -= roman[numeral]
print(sum)
    

