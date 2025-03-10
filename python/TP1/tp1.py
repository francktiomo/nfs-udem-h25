VIGENERE = {
    'A': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'B': {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J', 'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y', 'Y': 'Z', 'Z': 'A'},
    'C': {'A': 'C', 'B': 'D', 'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T', 'S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'},
    'D': {'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'},
    'E': {'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I', 'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N', 'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S', 'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X', 'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C', 'Z': 'D'},
    'F': {'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'},
    'G': {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L', 'G': 'M', 'H': 'N', 'I': 'O', 'J': 'P', 'K': 'Q', 'L': 'R', 'M': 'S', 'N': 'T', 'O': 'U', 'P': 'V', 'Q': 'W', 'R': 'X', 'S': 'Y', 'T': 'Z', 'U': 'A', 'V': 'B', 'W': 'C', 'X': 'D', 'Y': 'E', 'Z': 'F'},
    'H': {'A': 'H', 'B': 'I', 'C': 'J', 'D': 'K', 'E': 'L', 'F': 'M', 'G': 'N', 'H': 'O', 'I': 'P', 'J': 'Q', 'K': 'R', 'L': 'S', 'M': 'T', 'N': 'U', 'O': 'V', 'P': 'W', 'Q': 'X', 'R': 'Y', 'S': 'Z', 'T': 'A', 'U': 'B', 'V': 'C', 'W': 'D', 'X': 'E', 'Y': 'F', 'Z': 'G'},
    'I': {'A': 'I', 'B': 'J', 'C': 'K', 'D': 'L', 'E': 'M', 'F': 'N', 'G': 'O', 'H': 'P', 'I': 'Q', 'J': 'R', 'K': 'S', 'L': 'T', 'M': 'U', 'N': 'V', 'O': 'W', 'P': 'X', 'Q': 'Y', 'R': 'Z', 'S': 'A', 'T': 'B', 'U': 'C', 'V': 'D', 'W': 'E', 'X': 'F', 'Y': 'G', 'Z': 'H'},
    'J': {'A': 'J', 'B': 'K', 'C': 'L', 'D': 'M', 'E': 'N', 'F': 'O', 'G': 'P', 'H': 'Q', 'I': 'R', 'J': 'S', 'K': 'T', 'L': 'U', 'M': 'V', 'N': 'W', 'O': 'X', 'P': 'Y', 'Q': 'Z', 'R': 'A', 'S': 'B', 'T': 'C', 'U': 'D', 'V': 'E', 'W': 'F', 'X': 'G', 'Y': 'H', 'Z': 'I'},
    'K': {'A': 'K', 'B': 'L', 'C': 'M', 'D': 'N', 'E': 'O', 'F': 'P', 'G': 'Q', 'H': 'R', 'I': 'S', 'J': 'T', 'K': 'U', 'L': 'V', 'M': 'W', 'N': 'X', 'O': 'Y', 'P': 'Z', 'Q': 'A', 'R': 'B', 'S': 'C', 'T': 'D', 'U': 'E', 'V': 'F', 'W': 'G', 'X': 'H', 'Y': 'I', 'Z': 'J'},
  	'L': {'A': 'L', 'B': 'M', 'C': 'N', 'D': 'O', 'E': 'P', 'F': 'Q', 'G': 'R', 'H': 'S', 'I': 'T', 'J': 'U', 'K': 'V', 'L': 'W', 'M': 'X', 'N': 'Y', 'O': 'Z', 'P': 'A', 'Q': 'B', 'R': 'C', 'S': 'D', 'T': 'E', 'U': 'F', 'V': 'G', 'W': 'H', 'X': 'I', 'Y': 'J', 'Z': 'K'},
    'M': {'A': 'M', 'B': 'N', 'C': 'O', 'D': 'P', 'E': 'Q', 'F': 'R', 'G': 'S', 'H': 'T', 'I': 'U', 'J': 'V', 'K': 'W', 'L': 'X', 'M': 'Y', 'N': 'Z', 'O': 'A', 'P': 'B', 'Q': 'C', 'R': 'D', 'S': 'E', 'T': 'F', 'U': 'G', 'V': 'H', 'W': 'I', 'X': 'J', 'Y': 'K', 'Z': 'L'}, 
  	'N': {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'},
    'O': {'A': 'O', 'B': 'P', 'C': 'Q', 'D': 'R', 'E': 'S', 'F': 'T', 'G': 'U', 'H': 'V', 'I': 'W', 'J': 'X', 'K': 'Y', 'L': 'Z', 'M': 'A', 'N': 'B', 'O': 'C', 'P': 'D', 'Q': 'E', 'R': 'F', 'S': 'G', 'T': 'H', 'U': 'I', 'V': 'J', 'W': 'K', 'X': 'L', 'Y': 'M', 'Z': 'N'},
    'P': {'A': 'P', 'B': 'Q', 'C': 'R', 'D': 'S', 'E': 'T', 'F': 'U', 'G': 'V', 'H': 'W', 'I': 'X', 'J': 'Y', 'K': 'Z', 'L': 'A', 'M': 'B', 'N': 'C', 'O': 'D', 'P': 'E', 'Q': 'F', 'R': 'G', 'S': 'H', 'T': 'I', 'U': 'J', 'V': 'K', 'W': 'L', 'X': 'M', 'Y': 'N', 'Z': 'O'},
    'Q': {'A': 'Q', 'B': 'R', 'C': 'S', 'D': 'T', 'E': 'U', 'F': 'V', 'G': 'W', 'H': 'X', 'I': 'Y', 'J': 'Z', 'K': 'A', 'L': 'B', 'M': 'C', 'N': 'D', 'O': 'E', 'P': 'F', 'Q': 'G', 'R': 'H', 'S': 'I', 'T': 'J', 'U': 'K', 'V': 'L', 'W': 'M', 'X': 'N', 'Y': 'O', 'Z': 'P'},
    'R': {'A': 'R', 'B': 'S', 'C': 'T', 'D': 'U', 'E': 'V', 'F': 'W', 'G': 'X', 'H': 'Y', 'I': 'Z', 'J': 'A', 'K': 'B', 'L': 'C', 'M': 'D', 'N': 'E', 'O': 'F', 'P': 'G', 'Q': 'H', 'R': 'I', 'S': 'J', 'T': 'K', 'U': 'L', 'V': 'M', 'W': 'N', 'X': 'O', 'Y': 'P', 'Z': 'Q'},
    'S': {'A': 'S', 'B': 'T', 'C': 'U', 'D': 'V', 'E': 'W', 'F': 'X', 'G': 'Y', 'H': 'Z', 'I': 'A', 'J': 'B', 'K': 'C', 'L': 'D', 'M': 'E', 'N': 'F', 'O': 'G', 'P': 'H', 'Q': 'I', 'R': 'J', 'S': 'K', 'T': 'L', 'U': 'M', 'V': 'N', 'W': 'O', 'X': 'P', 'Y': 'Q', 'Z': 'R'},
    'T': {'A': 'T', 'B': 'U', 'C': 'V', 'D': 'W', 'E': 'X', 'F': 'Y', 'G': 'Z', 'H': 'A', 'I': 'B', 'J': 'C', 'K': 'D', 'L': 'E', 'M': 'F', 'N': 'G', 'O': 'H', 'P': 'I', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'M', 'U': 'N', 'V': 'O', 'W': 'P', 'X': 'Q', 'Y': 'R', 'Z': 'S'},
    'U': {'A': 'U', 'B': 'V', 'C': 'W', 'D': 'X', 'E': 'Y', 'F': 'Z', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F', 'M': 'G', 'N': 'H', 'O': 'I', 'P': 'J', 'Q': 'K', 'R': 'L', 'S': 'M', 'T': 'N', 'U': 'O', 'V': 'P', 'W': 'Q', 'X': 'R', 'Y': 'S', 'Z': 'T'},
    'V': {'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': 'E', 'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I', 'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M', 'S': 'N', 'T': 'O', 'U': 'P', 'V': 'Q', 'W': 'R', 'X': 'S', 'Y': 'T', 'Z': 'U'},
    'W': {'A': 'W', 'B': 'X', 'C': 'Y', 'D': 'Z', 'E': 'A', 'F': 'B', 'G': 'C', 'H': 'D', 'I': 'E', 'J': 'F', 'K': 'G', 'L': 'H', 'M': 'I', 'N': 'J', 'O': 'K', 'P': 'L', 'Q': 'M', 'R': 'N', 'S': 'O', 'T': 'P', 'U': 'Q', 'V': 'R', 'W': 'S', 'X': 'T', 'Y': 'U', 'Z': 'V'},
    'X': {'A': 'X', 'B': 'Y', 'C': 'Z', 'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I', 'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W'},
    'Y': {'A': 'Y', 'B': 'Z', 'C': 'A', 'D': 'B', 'E': 'C', 'F': 'D', 'G': 'E', 'H': 'F', 'I': 'G', 'J': 'H', 'K': 'I', 'L': 'J', 'M': 'K', 'N': 'L', 'O': 'M', 'P': 'N', 'Q': 'O', 'R': 'P', 'S': 'Q', 'T': 'R', 'U': 'S', 'V': 'T', 'W': 'U', 'X': 'V', 'Y': 'W', 'Z': 'X'},
    'Z': {'A': 'Z', 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'E', 'G': 'F', 'H': 'G', 'I': 'H', 'J': 'I', 'K': 'J', 'L': 'K', 'M': 'L', 'N': 'M', 'O': 'N', 'P': 'O', 'Q': 'P', 'R': 'Q', 'S': 'R', 'T': 'S', 'U': 'T', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X', 'Z': 'Y'}
}

# Affichage table Vigenère sous forme d'un tableau
# print(' ', ' '.join(VIGENERE['A']))
# for k, v in VIGENERE.items():
# 	print(k, ' '.join(list(VIGENERE[k].values())))

########################### Message et clef ##################################
MESSAGE = "La vie est belle"
CLEFCESAR = 5
CLEF = "secret"

################################# Cesar #####################################
def cryptCesar(message, clef):
	"""Crypte un message et retourne le message crypté 
	
	Params:
	message -- Message en clair à crypter 
	clef -- clé de Cesar à utiliser pour crypter
	"""
	messageCrypt = ''
	for lettre in message:
		unicodeLettre = ord(lettre)
		if not lettre.isalpha() or unicodeLettre < 65 or unicodeLettre > 122: # Vérifier si le caractère et une lettre de l'aphabet (et pas une ponctuation par exemple)
			messageCrypt += lettre # Ne pas crypter le caractère dans ce cas
			continue
		unicodeLettreCrypt = unicodeLettre + clef%26
		if lettre.isupper() and unicodeLettreCrypt > 90: # MAJ
			unicodeLettreCrypt -= 26
		elif lettre.islower() and unicodeLettreCrypt > 122: # MIN
			unicodeLettreCrypt -= 26
		lettreCrypt = chr(unicodeLettreCrypt)
		messageCrypt += lettreCrypt
	return messageCrypt

cryptMsg = cryptCesar('Va là-bas', 50)
print(f'Message crypté: {cryptMsg}')

def decryptCesar(message, clef):
	"""Décrypte un message et retourne le message en clair

	Params:
	message -- Message à crypter
	clef -- clé de Cesar à utiliser pour décrypter
	"""
	messageDecrypt = ''
	for lettre in message:
		unicodeLettre = ord(lettre)
		if not lettre.isalpha() or unicodeLettre < 65 or unicodeLettre > 122: # Vérifier si le caractère et une lettre de l'aphabet (et pas une ponctuation par exemple)
			messageDecrypt += lettre # Ne pas decrypter le caractère dans ce cas
			continue
		unicodeLettreDecrypt = unicodeLettre - clef%26
		if lettre.isupper() and unicodeLettreDecrypt < 65: # MAJ
			unicodeLettreDecrypt += 26
		elif lettre.islower() and unicodeLettreDecrypt < 97: # MIN
			unicodeLettreDecrypt += 26
		lettreCrypt = chr(unicodeLettreDecrypt)
		messageDecrypt += lettreCrypt
	return messageDecrypt

print(f'Message décrypté: {decryptCesar(cryptMsg, 50)}')


# QUESTIONS
# 1. Prendre en compte les lettres avec ponctuation (à, è, etc) ?

############################### Vigenère #####################################
def cryptVigenere(message, clef):
	clefIndex = 0
	clefLen = len(clef)
	encryptedMessage = ''

	for letter in message:
		clefLetter = clef[clefIndex]
		if (clefIndex < clefLen - 1):
			clefIndex += 1
		else:
			clefIndex = 0 # reset the index to start from the first letter of the clef
		
		encryptedLetter = VIGENERE[letter][clefLetter]
		encryptedMessage += encryptedLetter
	
	return encryptedLetter


def decryptVigenere(message, clef):
	pass


################################# XOR ########################################
def getBinaire(char):
	pass

def opXor(char1, char2):
	pass

def cryptXor(message, clef):
	pass

def decryptXor(message, clef):
	pass

def cryptCesar(message, clef):
	pass

def decryptCesar(message, clef):
	pass


############################# Tortue XOR #####################################
def cryptCesar(message, clef):
	pass

def decryptCesar(message, clef):
	pass
