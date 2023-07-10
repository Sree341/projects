def count_the_chars(text):
    result={}
    for letter in text:
        if letter.isalpha():
            if letter not in result:
                result[letter]=0
            result[letter]+=1
        else:
            pass
    return result

print(count_the_chars("what is this?"))