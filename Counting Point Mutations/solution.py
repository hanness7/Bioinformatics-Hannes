#Counting Point Mutations
def auslesen():
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        zeilen=file.readlines()
        seq1=zeilen[0].rstrip()
        seq2=zeilen[1].rstrip()
        return (seq1, seq2)
                

def count_pointmutations(seq1, seq2):
    '''
    2 Sequenzen der selben Länge werden Base für Base verglichen, Mutationen an selber Stelle werden gezählt
    '''
    mismatch_counter=0
    for i in range(len(seq1)):
        if not seq1[i]==seq2[i]: #wenn an der selben Stelle unterschiedliche Basen
            mismatch_counter+=1  #erhöhe die Anzahl der Nichtübereinstimmungen
    return mismatch_counter

if __name__ == "__main__":
    seq1=auslesen()[0]
    seq2=auslesen()[1]
    print(count_pointmutations(seq1, seq2))
