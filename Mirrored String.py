def mirrored_string(my_string):
    forwards=""
    backwards=""
    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
    if forwards.lower() == backwards.lower():
        return True
    return False
print(mirrored_string("12 noon"))