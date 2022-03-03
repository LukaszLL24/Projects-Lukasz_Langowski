#MORSE CODE TRANSLATOR
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '
	return cipher

def decrypt(message1):
	message1 += ' '
	decipher1 = ''
	citext1 = ''
	for letter1 in message1:
		if (letter1 != ' '):
			i = 0
			citext1 += letter1
		else:
			i += 1
			if i == 2 :
				decipher1 += ' '
			else:
				decipher1 += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext1)]
				citext1 = ''
	return decipher1

a = 'zaszyfrowac'
b = 'odszyfrowac'
ask = str(input('\nCzy chcesz zaszyfrowac czy odszyfrowac wiadomosc?: '))
if ask == a:
	def main():
		message = str(input('\nWpisz wiadomosc ktora chcesz zaszyfrowac: '))
		result = encrypt(message.upper())
		print (('\n') + result + ('\n'))
	if __name__=='__main__':
		main()
if ask == b:	
		message1 = str(input('\nWpisz wiadomosc ktora chcesz odszyfrowac: '))
		result1 = decrypt(message1)
		print (('\n') + result1 + ('\n'))


print('Dzieki, sproboj ponownie!')
	