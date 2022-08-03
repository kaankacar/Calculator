print("""*****************************************************
Welcome to my first calculator!

It can add, subtract, multiply and divide.

1. Add

2. Subtract

3. Multiply

4. Divide

*****************************************************
""")

a = int(input("First Number:"))
b = int(input("Second Number:"))
i = int(input("What do you want to do? input the number that corresponds with the function as listed above:"))

if i == 1:
    print("{} added by {} equals {}.".format(a, b, a + b))
elif i == 2:
    print("{} subtracted by {} equals {}.".format(a, b, a - b))
elif i == 3:
    print("{} multiplied by {} equals {}".format(a, b, a * b))
elif i == 4:
    print("{} divided by {} equals {}".format(a, b, a / b))
else:
    print("Wrong input. Try again.")
