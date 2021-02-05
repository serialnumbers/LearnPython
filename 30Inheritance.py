# inheritance

# define attributes and functions inside of a class
# then create another class, that inherits all of the first
# classes attributes

from Chef import Chef

from ChineseChef import ChineseChef

from ChineseChefInherit import ChineseChefInherit

myChef = Chef()
myChineseChef = ChineseChef()
myChineseChefInherit = ChineseChefInherit()

print("Make chicken")
myChef.make_chicken()

print()
print("Make salad")
myChef.make_salad()

print()
print("Make bbq ribs")
myChef.make_special_dish()

print()
print("What special dish does the Chinese Chef make?")
myChineseChef.make_special_dish()

print()
print("What dish can the Chinese Chef make?")
myChineseChef.make_fried_rice()

# using inheritance to call a function

print()
print("What dish can the Chinese Chef make?")
myChineseChefInherit.make_fried_rice()




# by: serialnumbers