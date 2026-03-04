text = input ("Enter Text: ")
text = text.replace(" ","")

if text.lower() == text[::-1].lower():
  print(f"{text} This is a palindrome.")
else:
  print(f"{text} This is not palindrome.")
