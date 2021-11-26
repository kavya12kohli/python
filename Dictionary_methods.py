#clear- removes all elements from the dictionary
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
capitals.clear()
print(capitals)

#copy- returns the copy of a specified dictionary
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
x=capitals.copy()
print(x)

#fromkeys- returns a dictionary with the specified keys and the specified values
places=("Palampur","Nawashahar","Chandigarh","Bareilly","Karnal","Mumbai")
lived_there=1
dictionary=dict.fromkeys(places,lived_there)
print(dictionary)

#get- returns the value of the specified key
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
print(capitals.get("Punjab"))

#items- returns the dictionary's key-value pairs
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
print(capitals.items())

#keys- returns the keys
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
print(capitals.keys())

#pop- removes specific items from the dictionary
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
capitals.pop("Uttar Pradesh")
print(capitals)

#popitem- removes the last item from the dictionary
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
capitals.popitem()
print(capitals)

#setdefault- returns the value of an item with a specific key
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
capitals.setdefault("Haryana","Chandigarh")
print(capitals)

#update- insets an item to the dictionary
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
capitals.update({"Gujarat":"Gandhinagar"})
print(capitals)

#values- returns a list of all the values in the list
capitals={"Himachal Pradesh":"Shimla","Punjab":"Chandigarh","Uttar Pradesh":"Lucknow","Maharashtra":"Mumbai"}
print(capitals.values())
