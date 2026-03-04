# This program finds the maximum number from a list of numbers entered by the user. It takes input as a string, splits it into individual numbers, converts them to integers, and iterates through the list to find the maximum value. Finally, it prints the maximum number found.
# Example:
# Input: "3 5 7 2 8"
# Output: "The max number is 8" 

text = input ("enter number sep by space: ")
numbers = text.split()
max_number = numbers[0]

for ctr in numbers:
    max_number = max(max_number,ctr)

print(f"The max number is : {max_number}")


#now , print the number range based deonding on the max number
for ctr in range(1, int(max_number) + 1):
    print(ctr)


