import re

#Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)


#RegEx Functions

"""
*findall*	Returns a list containing all matches
*search*	Returns a Match object if there is a match anywhere in the string
*split*	Returns a list where the string has been split at each match
*sub*	Replaces one or many matches with a string
"""

#Metacharacters

"""
[]	A set of characters
\	Signals a special sequence (can also be used to escape special characters)
.	Any character (except newline character)
^	Starts with
$	Ends with
*	Zero or more occurrences
+	One or more occurrences
?	Zero or one occurrences
{}	Exactly the specified number of occurrences
|	Either or
()	Capture and group
"""

#Special Sequences

"""
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
"""

#Sets

"""
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
(?=..) A lookahead checks if a pattern exists ahead in the string without consuming it.
"""

#The findall() function returns a list containing all matches.
#The search() function searches the string for a match, and returns a Match object if there is a match
#The split() function returns a list where the string has been split at each match:
#maxsplit parameter: You can control the number of occurrences by specifying re.split(\s, txt, 1) 1-st occurence and gone
#The sub() function replaces the matches with the text of your choice:
#The sub() function replaces the matches with the text of your choice:

"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

a = "Valid one"
b = "Invalid one"


#1st task
pattern1 = "a*b"
string1 = input()

if(re.search(pattern1, string1)):
    print(a)
else:
    print(b)
    
#2nd task
pattern2 = "ab{2,3}"
string2 = input()
if(re.search(pattern2, string2)):
    print(a)
else:
    print(b)
    
#3rd task
pattern3 = "[a-z]+_"
string3 = input()
if(re.search(pattern3, string3)):
    print(a)
else:
    print(b)
    
#4th task
pattern4 = "[A-Z]{1}+[a-z]"
string4 = input()
if(re.search(pattern4, string4)):
    print(a)
else:
    print(b)
    
#5th task
pattern5 = "a.*b$"
string5 = input()

if(re.search(pattern5, string5)):
    print(a)
else:
    print(b)
    
#6th task
pattern6 = "[ |,|.]"
replacement = ":"
string6 = input()
x = re.sub(pattern6, replacement, string6)
print(x)

#7th task
pattern7 = "_([a-z])"
string7 = input()
x = re.sub(pattern7, lambda x: x.group(1).upper(), string7)
print(x)

#8th task
pattern8 = "(?=[A-Z])"
string8 = input()
print(re.split(pattern8, string8))

#9th task
pattern9 = "(?=[A-Z])"
replacement9 = " "
string9 = input()
print(re.sub(pattern9, replacement9, string9))

#10th task
pattern10 = "([A-Z])"
replacement10 = "_"
string10 = input()
x10 = re.sub(pattern10, lambda y: y.group(1).lower(), string10)
print(x10)