MESSAGE = "La vie est belle"
CLEFCESAR = 5
CLEF = "secret"

def cryptCesar(message, clef):
	"""Crypte un message avec le chiffrement de César
	
	:param message: Message en clair à crypter 
	:param clef: Clé de Cesar à utiliser pour crypter
	:return Message crypté
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

def decryptCesar(message, clef):
	"""Décrypte un message avec le chiffrement de César

	:param: message: Message à crypter
	:param: clef: Clé de Cesar à utiliser pour décrypter
	:return Message décrypté
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


def testCryptCesar():
  assert(cryptCesar('La vie est belle', 5) == 'Qf anj jxy gjqqj')

def testDecryptCesar():
  assert(decryptCesar('Qf anj jxy gjqqj', 5) == 'La vie est belle')

testCryptCesar()
testDecryptCesar()

# QUESTIONS
# 1. Prendre en compte les lettres avec ponctuation (à, è, etc) ?
