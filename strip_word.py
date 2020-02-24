# convert a word to lower-case and remove all punctuation
def strip_word( w ):
    w = w.lower()
    w = ''.join([i for i in w if i.isalpha()])
    return( w )
