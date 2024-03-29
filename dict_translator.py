dict_englist_french={"eat":"manger", "play":"jouer", "rain":"pluie", "water":"eau"}
dict_englist_french["plum"]= "prune"
print(dict_englist_french)

word_english= input("Enter the english word:")

french_word=dict_englist_french.get(word_english)

if french_word:
    print(f'the english word {word_english} is {french_word} in french')
  
else:  
    print (f'word {word_english} is not in memory')
    
    