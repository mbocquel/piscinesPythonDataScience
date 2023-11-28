def NULL_not_found(object: any) -> int:
	if (object is None):
		print("Nothing: None ", type(object))
	elif (type(object) is float and object != object):
		print("Cheese: nan ", type(object))
	elif (type(object) is int and object == 0):
		print("Zero: 0 ", type(object))
	elif (type(object) is str and object == ''):
		print("Empty: ", type(object))
	elif (type(object) is bool and object == False):
		print("Fake: False", type(object))
	else:
		print("Type not Found")
		return 1
	return 0


#from NULL_not_found import NULL_not_found

#Nothing = None
#Garlic = float("NaN")
#Zero = 0
#Empty = ''
#Fake = False

#NULL_not_found(Nothing)
#NULL_not_found(Garlic)
#NULL_not_found(Zero)
#NULL_not_found(Empty)
#NULL_not_found(False)
#print(NULL_not_found("Brian"))