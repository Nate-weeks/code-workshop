"""
	piggy.py

	tests
-----------------------------

 >>> Translate("elegant")		# word starts with vowel
 'elegantway'

 >>> Translate("tart")		# word that starts with consonant
 'arttay'

 >>> Translate("stromboli")		# word that starts with consonant cluster
 'ombolistray'

 >>> Translate("queen")		# qu treated as one letter
 'eenquay'

>>> Translate("going to school")		# mulitple words
'oinggay otay oolschay'

>>> Translate("i'm going to school, tomorrow!")  # punctuation
"i'mway oinggay otay oolschay, omorrowtay!"

>>> Translate("107")	# numbers
'107way'

>>> Translate("The 16th of May")	#capitals and number with th
'Ethay 16thway ofway Aymay'

>>> Translate("änother škit")	# characters with accents on vowels and consonants
'änotherway itškay'

>>> Translate('(foo) [bar]')		#brackets and parens
'(oofay) [arbay]'

>>> Translate('It is 20.5 degrees today')	#decimals
'Itway isay 20.5 egreesday odaytay'

"""

def ValidChars():
	letters = []
	for i in range(65,91): #caps
		letters.append(chr(i))
	for i in range(97,123): #lowercase
		letters.append(chr(i))
	for i in range(192,384): #extra letters
		if i in [215,247,329]:
			pass
		else:
			letters.append(chr(i))

	vowels = 	[	65,69,73,79,85,
					97,101,105,111,117,

					192,193,194,195,196,197,198,
					200,201,202,203,
					204,205,206,207,
					210,211,212,213,214,216,
					217,218,219,220,

					224,225,226,227,228,229,230,
					232,233,234,235,
					236,237,238,239,
					242,243,244,245,246,248,
					249,250,251,252,

					256,257,258,259,260,261,
					274,275,276,277,278,279,280,281,282,283,
					296,297,298,299,300,301,302,303,304,305,306,307,
					332,333,334,335,336,337,338,339,
					360,361,361,362,363,364,365,366,367,368,369,370,371
				]

	for i in range(len(vowels)):
		vowels[i] = chr(vowels[i])

	return letters, vowels

#global constants
g_letters, g_vowels = ValidChars()
#infile = open("pigin.txt","r")
#outfile = open("pigout.txt","w")

def GetText():
	"""Get text from user."""
	result = input("Enter a word or phrase. ")
	#result = infile.read()
	return str(result)

# def ToWords(text):
# 	"""Break text into words."""
# 	words = text.split()
# 	return words

def TranslateWord(word):

	"""
	Function translates one word

	>>> TranslateWord('potatoe')
	'otatoepay'
	"""
	uppers = []
	vowels = []
	start = ""
	end = ""
	try:
		#check for punctuation

		if word[-1] not in g_letters:
			end = word[-1]
			word = word[:-1]

		if word[0] not in g_letters:
			start = word[0]
			word = word[1:]

		#get case pattern
		for w in word:
			if w.isupper() == True: uppers.append(1)
			elif w not in g_letters: uppers.append(2)
			else: uppers.append(0)

		#translate word based on first letter(s)
		for w in word:
			if w in g_vowels: vowels.append(1)
			else: vowels.append(0)


		if vowels[:2] == [0,1] and word[:2].lower() != "qu":
			pl_list = list(word[1:] + word[0] + "ay")
		elif vowels[:3] == [0,0,1] or word[:2].lower() == "qu":
			pl_list = list(word[2:] + word[:2] + "ay")
		elif vowels[:4] == [0,0,0,1]:
			pl_list = list(word[3:] + word[:3] + "ay")
		else:
			pl_list = list(word + "way")

		if 0 not in uppers and len(uppers) > 1:
			for i in range(len(pl_list)): pl_list[i] = pl_list[i].upper()
		else:
			for u in range(len(uppers)):
				if uppers[u] == 1: pl_list[u] = pl_list[u].upper()
				else: pl_list[u] = pl_list[u].lower()

		pl_list.insert(0,start)
		pl_list.append(end)
		pl_word = "".join(pl_list)
		return pl_word
	except:
		return word


def Translate(text):
	"""Return Pig Latin translation of a word or phrase"""
	words = text.split()
	pl_words = []
	for w in words:
		pl_words.append(TranslateWord(w))
	pl_text = " ".join(pl_words)
	return pl_text


def main():
	print ("~ Pig Latin ~")
	text = GetText()
	pl_text = Translate(text)
	print (pl_text)
	#outfile.write(pl_text)


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
