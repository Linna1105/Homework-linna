# Ex1 - String 
# Enter text and display it one by one

# Ex2 - String
# Enter text and display number of letter

# Ex3 - String
# Enter text and check if it contains capital letter or not

# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
text = "3 4 5 6"
for i in range(len(text)):
    if text[i] != " ":
        print(text[i])
# Q2 - Sum all number (Total: 18)
text = "3 4 5 6"
sum=0
for i in range(len(text)):
    if text[i] != " ":
        sum += int(text[i])
print(sum)



# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse