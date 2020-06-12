def abc(base,powe):
	result = 1
	for index in range(powe):
		result = result * base

	return result

def add(a,b):
	sumb = a + b
	return sumb 	

print(abc( int(input("Enter the base num : ")),int(input("Enter the power num : "))))

print(add( int(input("Enter num1 : ")),int(input("Enter num2 : "))))