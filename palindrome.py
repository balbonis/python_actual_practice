#This program checks if the input text is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# The program takes user input, removes spaces, and compares the original text with its reverse to determine if it is a palindrome.
# Example:
# Input: "A man a plan a canal Panama"
# Output: "AmanaplanacanalPanama is a palindrome" 
# Achievment: This program successfully identifies palindromic phrases, demonstrating the use of string manipulation and conditional statements in Python.  

try:
  while True:
    text = input ("Enter text: ").replace(" ","").lower()

    if text == text[::-1]:
      print (f"This is palindrome")
    else:
      print (f"This is not palindrome")


except KeyboardInterrupt:
    print (f"App terminated")
