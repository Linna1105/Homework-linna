# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"
text = int(input("Enter number: "))
for i in range(int(text)):
    if int(text) %2 == 1:
        result = ("odd" )
    else:
        result = ("even")
print(result)