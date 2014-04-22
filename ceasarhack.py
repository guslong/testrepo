message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)): 
	translated = ''
	# loop through the message character by character
	for char in message:
		if char in LETTERS:
			num = LETTERS.find(char) # get the number of the character
			num = num - key
			
			#handle the wrap
			if num < 0:
				num = num + len(LETTERS)
	
			translated = translated + LETTERS[num]
		else:
			#just add the symbol
			translated = translated + char
	print('key: #%s: %s' % (key, translated) + '\n')

