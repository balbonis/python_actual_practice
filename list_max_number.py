# This program finds the maximum number from a list of numbers entered by the user. It takes input as a string, splits it into individual numbers, converts them to integers, and iterates through the list to find the maximum value. Finally, it prints the maximum number found.
# Example:
# Input: "3 5 7 2 8"
# Output: "The max number is 8" 

numbers = [int (n) for n in input ("Enter Numbers sep by space: ").split()]
print (f"The max number is: ", max(numbers))


#List the number from 1 to max_numbe automatically
my_range = int(max_number) 
for n in range (1, my_range+1):
    print(n)    
