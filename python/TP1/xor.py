def expand_key(clef, desiredLength):
	""" Assure que la clef a la taille désirée """
	clef = clef*desiredLength
	clef = clef[:desiredLength]
	return clef

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
	# Assure que la clé et le message ont la même taille
	clef = expand_key(clef, len(message))

	msgBin = []
	for char in message:
		msgBin.append(getBinaire(char))

	clefBin = []
	for char in clef:
		clefBin.append(getBinaire(char))

	encryptedMsg = ''
	for i in range(len(msgBin)):
		encryptedChar = opXor(msgBin[i], clefBin[i])
		encryptedMsg += chr(int(encryptedChar, 2))
	return encryptedMsg

def decryptXor(message, clef):
	""" Déchiffre un message avec la méthode XOR
	
	:param message: Message à décrypter
	:param clef: Clé de chiffrement
	:return: Message décrypté
	"""
	# Assure que la clé et le message ont la même taille
	clef = expand_key(clef, len(message))

	msgBin = []
	for char in message:
		msgBin.append(getBinaire(char))

	clefBin = []
	for char in clef:
		clefBin.append(getBinaire(char))

	decryptedMsg = ''
	for i in range(len(msgBin)):
		decryptedChar = opXor(msgBin[i], clefBin[i])
		decryptedMsg += chr(int(decryptedChar, 2))
	return decryptedMsg

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
  # Pas sur de comment tester a cause des caracteres speciaux
  pass

def testDecryptXor():
	clef = 'abri'
	message = 'leci'
	messageCrypte = cryptXor(message, clef)
	messageDecrypte = decryptXor(messageCrypte, clef)
	assert(messageDecrypte == message)

	clef = 'secret'
	message = 'La vie est belle'
	messageCrypte = cryptXor(message, clef)
	messageDecrypte = decryptXor(messageCrypte, clef)
	assert(messageDecrypte == message)


testGetBinaire()
testOpXor()
testCryptXor()
testDecryptXor()


# Driver code

if __name__ == '__main__':
	sampleString = 'La vie est belle'
	xorKey = 'secret'
	cipherText = cryptXor(sampleString, xorKey)
	print(len(cipherText))
	for c in cipherText:
		print(f'{c} --> {ord(c)}')
	print(f'Encrypted text: {cipherText}')
	print(f'Decrypted text: {decryptXor(cipherText, xorKey)}')
