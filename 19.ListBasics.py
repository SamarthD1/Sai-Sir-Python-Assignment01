l=int(input("enter length of list"))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(l)]
print("List:", numbers)
print("Length of list:", len(numbers))