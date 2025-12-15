# --------------------1 - Palindrome Checker--------------------

def palindrome_checker(word):
    word_rev = word[::-1]

    for i in range(len(word)):
        if word[i] != word_rev[i]:
            return False

    return True

if palindrome_checker("civic"):
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")



# --------------------2 - FizzBuzz--------------------

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
