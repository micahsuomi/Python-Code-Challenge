
#CODE CHALLENGE

#PALINDROME

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

#Merge Names

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
names3 = names1 + names2

unique_list = [] 

 # intilize a null list 
      
    # traverse for all elements 
for name in (names3): 
        # check if exists in unique_list or not 
    if name not in unique_list: 
        unique_list.append(name) 
    # print list 
    else:
        continue

print(unique_list)
#prints Ava, Emma, Olivia, Sophia

#Ice Cream Machine

class IceCreamMachine:
    all={}
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        res = []
        for x in self.ingredients:
            for y in self.toppings:
                res.append([x, y])
        return res

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
#should print
# [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())
# this should print
#[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce'], ['vanilla','orange'], ['chocolate','orange']]




