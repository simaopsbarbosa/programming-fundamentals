def get_positions(string, word_list):
    words_in_string = string.split()
    res = ""
    
    if not (words_in_string[0] in word_list):
        return ""
    if not (words_in_string[1] in word_list):
        return ""    
        
    for i in range(len(word_list)):
        if words_in_string[0] == word_list[i]:
            res = res + str(i)
    
    res = res + " "        
    
    for i in range(len(word_list)):
        if words_in_string[1] == word_list[i]:
            res = res + str(i)
        
    return res