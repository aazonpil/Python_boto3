

##Method Join()

Word2 = input("The original word is : ")

reversed_word2= reversed(Word2) # We resevered by print each letter  in the word as an isolated string

join_reversed= ''.join(reversed_word2) # This allows to concatenate the reversed letter to form a word

print(f"the reverse of the word {Word2} is {join_reversed}")



