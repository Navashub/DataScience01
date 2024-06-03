# Challenge 2
# Let's get the power of 6 from our already created powers dictionary
#

dict1 = {'A': 2,'B': 4,'C': 6}

dict2 = {key: value ** 2 for key, value in dict1.items()}

print(dict2)