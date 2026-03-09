import re
def uses_none(word, forbidden):
    for forbidden_letters in word.lower():
        if  forbidden_letters in forbidden.lower():
            return False
    return True

def check_word(word):
    lowercase = word.lower()
    if len(word) != 5:
        return False
    
    if uses_none(lowercase,"SPADCLRK") and "e" != lowercase[4] and "e" != lowercase[2] and "e" in lowercase:
        return True
    else:
        return False
    
    
    
    
    

print(check_word("eeeee"))
    

