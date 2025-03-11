def getBinaire(char):
	""" Convertit un caractère en sa représentation binaire

	:param char: Caractère à convertir
  	:return: Représentation binaire du caractère
	"""
	result = bin(ord(char))[2:]
	if len(result) < 8:
		result = '0'*(8-len(result)) + result
	return result

def opXor(char1, char2):
	""" Opération XOR entre deux caractères

	:param char1: Premier caractère
	:param char2: Deuxième caractère
	:return: Résultat de l'opération XOR
	"""
	result = ''
	for i in range(8):
		result += '1' if char1[i] != char2[i] else '0'
	return result

def cryptXor(message, clef):
	pass

def decryptXor(message, clef):
	pass

def testGetBinaire():
	assert(getBinaire('A') == '01000001')
	assert(getBinaire('a') == '01100001')
	assert(getBinaire(' ') == '00100000')
	assert(getBinaire('é') == '11101001')
	assert(getBinaire('@') == '01000000')
	assert(getBinaire(':') == '00111010')

def testOpXor():
	assert(opXor('01101100', '01100001') == '00001101')
	assert(opXor('01101100', '01101100') == '00000000')
	assert(opXor('01101100', '00000000') == '01101100')

def testCryptXor():
  pass

def testDecryptXor():
	pass


testGetBinaire()
testOpXor()
