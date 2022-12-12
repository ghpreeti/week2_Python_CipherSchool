# define palindrome-->either we read from left or from right
# word reads same 
# example=madam

def is_palindrom(word):
    rev_word=word[::-1]
    if (word) == rev_word:
        return True
    else :
        return False

def is_palindrom(word):
    return word == word[::-1]

print(is_palindrom("naman"))
print(is_palindrom("horse"))








