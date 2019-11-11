# Calculating number of vowels, digits and words using for loop
v = 0
d = 0
w = 1
txt = input("Enter some text:")
for ch in txt:
    if ch in "aeiou":
        v += 1
    elif ch in "0123456789":
        d += 1

for i in range(len(txt)):
    if(txt[i] == ' ' or txt == '\n' or txt == '\t'):
        w = w + 1    
print ("The number of vowels are: %d , number of digits are: %d  and number of words are: %d" %(v, d, w))
