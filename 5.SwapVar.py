a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))
print("before swap a = ",a,"b = ",b)
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")