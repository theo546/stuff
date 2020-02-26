# Cheat list
cheat_list = [0xDE4B237D, 0xB22A28D1, 0x5A783FAE, 0xEECCEA2B, 0x42AF1E28, 0x555FC201, 0x2A845345, 0xE1EF01EA, 0x771B83FC, 0x5BF12848, 0x44453A17, 0xFCFF1D08, 0xB69E8532, 0x8B828076, 0xDD6ED9E9, 0xA290FD8C, 
0x3484B5A7, 0x43DB914E, 0xDBC0DD65, 0xD08A30FE, 0x37BF1B4E, 0xB5D40866, 0xE63B0D99, 0x675B8945, 0x4987D5EE, 0x2E8F84E8, 0x1A9AA3D6, 0xE842F3BC, 0x0D5C6A4E, 0x74D4FCB1, 0xB01D13B8, 0x66516EBC,
0x4B137E45, 0x78520E33, 0x3A577325, 0xD4966D59, 0x5FD1B49D, 0xA7613F99, 0x1792D871, 0xCBC579DF, 0x4FEDCCFF, 0x44B34866, 0x2EF877DB, 0x2781E797, 0x2BC1A045, 0xB2AFE368, 0xFA8DD45B, 0x8DED75BD, 0x1A5526BC,
0xA48A770B, 0xB07D3B32, 0x80C1E54B, 0x5DAD0087, 0x7F80B950, 0x6C0FA650, 0xF46F2FA4, 0x70164385, 0x885D0B50, 0x151BDCB3, 0xADFA640A, 0xE57F96CE, 0x040CF761, 0xE1B33EB9, 0xFEDA77F7, 0x8CA870DD, 0x9A629401,
0xF53EF5A5, 0xF2AA0C1D, 0xF36345A8, 0x8990D5E1, 0xB7013B1B, 0xCAEC94EE, 0x31F0C3CC, 0xB3B3E72A, 0xC25CDBFF, 0xD5CF4EFF, 0x680416B1, 0xCF5FDA18, 0xF01286E9, 0xA841CC0A, 0x31EA09CF, 0xE958788A, 0x02C83A7C,
0xE49C3ED4, 0x171BA8CC, 0x86988DAE, 0x2BDD2FA1]

import binascii, string
max_char = 12 # max should be 29
cheat_string = 'BENSUPERPC'[::-1] # The beginning / the end of the desired custom cheat (gonna be reversed)
insert_string_before = False
alphabet = list(string.ascii_uppercase)
count_alphabet = len(alphabet)

now = 1
list_characters = []
while True:
	if now > max_char:
		break
	if now == 1:
		# Add an entry that contain '0' in the array list "list_characters" if it's the first character
		list_characters.append(0)
	else: 
		# Otherwise, add a '-1' entry for the next ones
		list_characters.append(-1)
	now += 1
# the array should be like this with "max_char" set on 12: [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

final_list = []
while True:
	str = cheat_string
	current_list_char = 0
	while True:
		# Once the current_list_char value has reached the 
		if current_list_char == max_char:
			break
		# If the current character has reached the top of the alphabet, reset the current char int to zero
		if list_characters[current_list_char] == count_alphabet:
			list_characters[current_list_char] = 0
			try:
				# then increase the next array entry by one
				list_characters[current_list_char+1] += 1
			except:
				# If an error is detected (like the out of bound error), return the final list then exit
				print(final_list)
				quit()
		# If the current char value is set to '-1', break
		if list_characters[current_list_char] == -1:
			break
		if insert_string_before == True:
			# If the "insert_string_before" value is set to True, put the "cheat_string" value at the end of the current alphabet character (because GTA SA cheats check is reversed!).
			str = alphabet[list_characters[current_list_char]] + str
		else:
			# Otherwise, do the same as above, reversed.
			str = str + alphabet[list_characters[current_list_char]]
		# If the current char is set on '0', increase the '0' entry in the "list_characters" by one.
		if current_list_char == 0:
			list_characters[0] += 1
		# Increase the current char by one.
		current_list_char += 1
	
	# bitwise left shift by 32 the crc32 hash
	crcjam = ~binascii.crc32(str.encode('utf8')) % (1<<32)
	
	# Check if the crcjam hash exist in the "cheat_list" array, then append the cheat combination to the "final_list" array, then print it
	if crcjam in cheat_list:
		final_list.append(str[::-1])
		print(str[::-1])