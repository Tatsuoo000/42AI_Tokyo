import sys

def whois(n):
	if n == 0:
		print('I\'m Zero.')
	elif n % 2 == 0:
		print('I\'m Even.')
	else:
		print('I\'m Odd.')
	return ()


if __name__ == '__main__'
args = sys.argv
if 2 <= len(args)
	try:
		args[1].isdigit()
		whois(int(args[1]))
	except ERROR as e:
		print (e)
else
	print('ERROR')