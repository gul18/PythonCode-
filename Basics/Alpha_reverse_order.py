#to print the text in reverse order
txt = input("Enter some text:")
length = len(txt)
rev = ""
while length>0:
   rev += txt[length-1]
   length = length-1

print (rev)
