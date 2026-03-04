text = input("Enter numbers separated by space:")
numbers = text.split()

numbers = [int(n) for n in numbers]
max_number = numbers[0]  
print (f"Max number is {max_number}")
