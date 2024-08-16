# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
text = input("Enter text: ")
count_odd = 0
count_even = 0
for i in range(len(text)):
    if int(text[i]) %2 == 0:
        count_even += 1
    elif int(text[i]) %2 == 1:
        count_odd += 1
print("count even :",count_even)
print("count odd :",count_odd)
# Q2 - Sum all number 
text = "454639"
total = 0
for i in range(len(text)):
    total += int(text[i])
print(total)
# Q3 - Sum only even number 
text = "454639"
sum = 0
for i in range(len(text)):
    if int(text[i]) %2 == 0:
        sum += int(text[i])
print(sum)

# Q4 - Reverse 
text = "454639"
reversed = len(text)-1
result = ""
for i in range(len(text)):
    result += text[reversed-i]
print(result)
