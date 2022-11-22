my_string = "Live happily"

i = int(input("Enter index: "))

if not my_string:
    print("Empty string")

elif i not in range(len(my_string)):
    print("i is out of range")

else:
    print(my_string[i])