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
	""" Chiffre un message avec la méthode XOR
	
	:param message: Message à crypter
	:param clef: Clé de chiffrement
	:return: Message crypté
	"""
	msgBin = [getBinaire(char) for char in message]
	clefBin = [getBinaire(char) for char in clef]

	encryptedMsg = ''
	for i in range(len(msgBin)):
		encryptedChar = opXor(msgBin[i], clefBin[i])
		encryptedMsg += chr(int(encryptedChar))
	return encryptedMsg

def decryptXor(message, clef):
	""" Déchiffre un message avec la méthode XOR
	
	:param message: Message à décrypter
	:param clef: Clé de chiffrement
	:return: Message décrypté
	"""
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

print(cryptXor('leci', 'abri'))
