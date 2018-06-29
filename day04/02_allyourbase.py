import sys

def is_integer(nb):
	try:
		int(nb)
		return True
	except:
		return False

def printbits(base_10):
	compare = 2 ** 31
	k = []
	while compare > 0:
		if base_10 & compare:
			k.append('1')
		elif compare <= base_10:
			k.append('0')
		compare >>= 1
	print(''.join(k))

def scrub_input(argv):
	if len(argv) > 2:
		print("Too many arguments")
		return False
	elif not is_integer(argv[1]):
		print("Thats not a number!")
		return False
	elif int(argv[1]) < 0:
		print("This program only handles negative numbers")
		return False
	else:
		return True

def main(argv):
	if scrub_input(argv) == True:
		printbits(int(argv[1]))
	else:
		sys.exit()








main(sys.argv)



#base_10 = int((sys.argv[1]))
#if base_10 < 0:
	#print("Please enter a positive number")
#count = 0
#binary_representation = ""
#while 2 ** count < base_10:
	#if 2 ** (count) > base_10:
			#binary_representation = binary_representation + '1'
			#base_10 = base_10 - 2 ** (count - 1)
			#count = 0
	#else:
		#binary_representation = binary_representation + '0'
		#base_10 = base_10
		#count = count + 1

#print("Binary Value is : ", binary_representation)
