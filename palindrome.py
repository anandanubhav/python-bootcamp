def is_palindrome(str):
	str = str.lower()
	orig = [s for s in str if s != " "]
	rev = orig[::-1]
	b = orig == rev
	return b

def is_palindrome(str):
	stripped = str.replace(" ","")
	return str == str[::-1]
	
print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama')) # True
