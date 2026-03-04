try:

    while True:
        
        #max number and range
        numbers = [int(n) for n in input ("Enter numbers:").split()]
        print (f"Max number is ", max(numbers))
        for ctr in range(1,max(numbers)+1):
            print (f"count {ctr}")
        
        
        
        #palindrome
        text = input("Enter word:").replace(' ','').lower()
        if text==text[::-1]:
            print ("Palindrome")
        else:
            print ("Not Palindrome")
            
            
            
        #word frequency
        from collections import Counter
        text = input("Enter words:")
        counts = Counter(text.split())
        
        print (counts)
        print (list(counts.keys())," ",list(counts.values()))
        
        
        #remove duplicates
        numbers = [int(n) for n in input("Enter numbers:").split()]
        print (f"removing duplicates",list(set(numbers)))
        
        
            
            
        
except KeyboardInterrupt:
    
    print("App closed")
