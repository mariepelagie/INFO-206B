# sort dictionary from most to least frequent entry count
def sort_dictionary( D ):
    Ds = sorted(D.items(), key=lambda x:x[1], reverse=True)               
    return Ds
