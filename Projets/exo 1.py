import sys


text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
def convert(sentence1):
	lst_mot1 = sentence1.split(". ")
	lst_mot2 = []
	sentence2 = ""

	for sentence in lst_mot1:
		for letter in sentence:
			if letter in [chr(x) for x in range(97,121)]:
				sentence2 += chr(ord(letter) + 2)
			elif letter == "y":
				sentence2 += "a"
			elif letter == "z":
				sentence2 += "b"
			else :
				sentence2 += letter
		lst_mot2.append(sentence2)
		sentence2 = ""
	return ", ".join(lst_mot2)

print(convert("map"))
"""

"""