import pyperclip

def main():
	myMessage = 'Common sense is not so common'
	myKey = 8
	
	ciphertext = encryptMessage(myKey, myMessage)
	print(ciphertext)
	
	
def encryptMessage(key, message):
	ciphertext = [''] * key  # create a list of empty spaces
	
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)



#run main if this program is being run rather than imported
if __init__ = '__main__':
	main()
	