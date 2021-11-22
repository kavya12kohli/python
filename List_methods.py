friends=["Kavya","Shriya","Labdhi","Madhura","Sneha","Bhavna"]
#append-add an element
friends.append("Rucha")
print(friends)
#clear-delete all elements
friends.clear()
print(friends)
#copy-returns the copy of a list
friends=["Kavya","Shriya","Labdhi","Madhura","Sneha","Bhavna","Rucha"]
x=friends.copy()
print(x)
#count- counts the number of times a particular element appears in the list
y=friends.count("Shriya")
print(y)
#extend-add a list to the end of another list
drinks=["Juice","Cold Drinks","Soda","Limewater"]
friends.extend(drinks)
print(friends)
#index-tells the position of the element
z=friends.index("Madhura")
print(z)
#insert-adds an element to a specific position unlike append
friends.insert(3,"Shambhavee")
print(friends)
#pop-removes an element from a specific position
friends.pop(8)
friends.pop(8)
friends.pop(8)
friends.pop(8)
print(friends)
#remove-removes a particular element
friends.remove("Bhavna")
print(friends)
#reverse- reverses the order of list
friends.reverse()
print(friends)
#sort-sorts the list alphabetically
friends.sort()
print(friends)
