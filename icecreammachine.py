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
