text = input ("enter number sep by space: ")
numbers = text.split()

max_number = numbers[0]


for ctr in numbers:
    max_number = max(max_number,ctr)

    print(f"The max number is : {max_number}")
