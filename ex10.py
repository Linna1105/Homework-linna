# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0
number=""
for j in range(5):
    numbers=input("Enter number:")
    number+=str(numbers)
    maximum=number
    minimum=number
    for j in range(len(number)):
        if number[j]>maximum:
            maximum=number[j]
        elif number[j]<minimum:
            minimum=number[j]
print("max:",maximum)
print("min:",minimum)