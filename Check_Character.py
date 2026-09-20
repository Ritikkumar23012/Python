# Check if a character is vowel or consonant
'''n = input("Enter Character: ")
if ('a'==n or 'e'==n or 'i'==n or 'o'==n or 'u'==n or
    'A'==n or 'E'==n or 'I'==n or 'O'==n or 'U'==n):
    print(f"{n} is vowel")
else:
    print(f"{n} is consonant")'''

ch = input("Enter character: ")
if ch in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")

