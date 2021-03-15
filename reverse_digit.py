def reverse_digit(a_digit):
	if a_digit >= 0:
		return int(str(a_digit)[::-1])
	else:
		return -1 * int(str(a_digit)[::-1])	

print(reverse_digit(56))