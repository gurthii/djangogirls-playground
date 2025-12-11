"""
Lists
"""
n = [1009, 19,8, 20, 1]
n.sort() # sorts and orders (ascending) value in the list permanently
n.reverse() # reverses the order (descending)
n.append(123) # adds value to the end of the list
n.pop() # removes last value
n.pop(1) # removes second value in n, n[1]

print(n)

"""
Dictionaries
"""
student = {
	'name' : 'Candace Owens',
	'age' : 14,
	'subjects' : ["Bio", "Phy", "Eng"] 
}

student["subjects"].append("Comp") # updates subjects value-list with a new item
student["age"] += 1 # updates key value "age
print(student)

for k, v in student.items():
	print(f"{k} --> {v}")

student.pop('age') # pop("key") also works here for deleting values


