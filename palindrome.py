# function to check if string is palindrome or not 
def is_palindrome(word): 
    #to tell Python we are ignoring uppercase and lowercase
    word = word.casefold()

    # Using predefined function to  
    # reverse to string print(word)
    rev = ''.join(reversed(word)) 
  
    # Checking if both string are  
    # equal or not 
    if (word == rev): 
        return True
    return False
  
# main function 
word = "Deleveled"
print(is_palindrome("Deleveled")) 