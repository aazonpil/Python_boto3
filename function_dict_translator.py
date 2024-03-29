
def dict_englist_french(word_english):
    dict_englist_french={"eat":"manger", "play":"jouer", "rain":"pluie", "water":"eau"}
    dict_englist_french["plum"]= "prune"
    return dict_englist_french.get(word_english)
# Main and Call the function
word_english= input("Enter the english word:")
french_word=dict_englist_french(word_english)

#Determine the whether or not the french word exist

if french_word:
    print(f'the english word {word_english} is {french_word} in french')
  
else:  
    print (f'word {word_english} is not in memory')