def data_type(typ):
	if type(typ) == str:
		return len(typ)
	elif type(typ) == None.__class__:
		return 'no value'
	elif type(typ) == bool:
		return typ
	elif type(typ) == int:
		if typ > 100:
			return 'more than 100'
		elif typ < 100:
			return 'less than 100'
		else:
			return 'equal to 100'
	elif type(typ) == list:
		if 0 <= 3 < len(typ):
			return typ[3]
		else:
			return None

print(data_type(None))
