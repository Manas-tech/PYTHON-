myStr = "pyctchonfcorbegcinncers"
print("The original string is:", myStr)
charToDelete = 'p'
print("The character to delete:", charToDelete)
myList = [character for character in myStr if character != charToDelete]
print("The list of characters is:")
print(myList)