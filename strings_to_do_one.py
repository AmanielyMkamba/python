# Remove Blanks
# Create a function that, given a string, returns all of that string’s contents, but without blanks.
# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

"""
def remove_blanks(word):
    new_word = ""
    for i in word:
        if i != " ":
            new_word+=(i)
    return new_word

print(remove_blanks(" Pl ayTha tF u nkyM usi c "))
"""

# Get Digits
# Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.

"""
def get_digits(digit_num):
    new_digits = ""
    new_digits_arr1 = []
    new_digits_arr2 = []

    for i in digit_num:
        new_digits_arr1.append(ord(i))

    for i in new_digits_arr1:
        if i <= 57 and (i-48) >= 0:
            new_digits_arr2.append(i - 48)

    new_digits_arr2.pop(new_digits_arr2[0])
    for i in new_digits_arr2:
        new_digits = new_digits + str(i)

    get_digits(new_digits)

print(get_digits("0s1a3y5w7h9a2t4?6!8?0"))
"""

# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
# Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
# Given "Live from New York, it's Saturday Night!", return "LFNYISN".

"""
def acronym(string):

    acronym = string[0]
    remove = " "

    for i in range(1, len(string)):
        if string[i-1] == " ":
            acronym += string[i].capitalize()
    for i in remove:
        acronym = acronym.replace(i,"")
    return acronym

print(acronym(" there's no free lunch - gotta pay yer way. "))
"""

# Zip Arrays into Map
# Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

def zip_arrays(arr1, arr2):
    map = {}

    for i in arr1:
        map.append[i]

print(["abc", 3, "yo"], [42, "wassup", True])