def palindrome(a_word):
    if str(a_word) == str(a_word)[::-1]:
        return "It's a palindrome"
    else:
        return "Not a palindrome"

print(palindrome("ressasser"))