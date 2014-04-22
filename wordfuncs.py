def break_words(stuff):
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	return sorted(words)
	
def get_first_word(words):
	word = words.pop(0)
	return word
	
def get_last_word(words):
	word = words.pop(-1)
	return word
	
def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def get_first_and_last(sentence):
#returns the first and last words
	words_list = break_words(sentence)
	return print_first_word(words_list)
	return print_last_word(words_list)

