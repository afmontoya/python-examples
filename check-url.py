# check-url.py
# Use python check-url.py to run
# Python code to find the URL from an input string 
#
import re 

def Find(string): 
	# findall() has been used 
	# with valid conditions for urls in string 
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
	return url 
	
# Driver Code 
string = 'Some jibberish and artwork: https://albertmontoya.com/tag/bart-simpson in the website of http://albertmontoya.bigcartel.com/product/print-adults-suck-then-you-are-one' 
print("Urls: ", Find(string))