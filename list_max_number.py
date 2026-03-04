# This program finds the maximum number from a list of numbers entered by the user. It takes input as a string, splits it into individual numbers, converts them to integers, and iterates through the list to find the maximum value. Finally, it prints the maximum number found.
# Example:
# Input: "3 5 7 2 8"
# Output: "The max number is 8" 
numbers = [int(n) for n in input("Enter # sep by space:").split()]
print (f"The max number is: ", max(numbers))

# Range function to print numbers from 1 to the maximum number found in the list. It uses the built-in max() function to determine the maximum value and then iterates through a range starting from 1 up to and including that maximum number, printing each number in the range.
my_range = max(numbers)
for ctr in range(1, my_range+1):
    print (ctr)

