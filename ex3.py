text = input ("Enter text: ")
is_Found = False
for i in range(len(text)):
    if text[i].isupper():
        is_Found = True
if is_Found:
    print("yes")
else:
    print("No!")

