def auslesen():
    '''
      Die Datei liest die erste und einzige Zeile aus der Datei aus
    '''
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        zeilen=file.readlines()
        sequenz=zeilen[0].rstrip() #nimm nur die erste Zeile
    return sequenz

def reverse_dna(sequenz):
    '''
    Die Funktion ermittelt die komplementären Basen und dreht die Sequenz einmal um
    '''
    dict_basen={"A":"T", "T":"A", "G":"C", "C":"G"} #Dicitonary mit Komplementärbasen
    seq_kompl=""
    for basen in sequenz:
        if dict_basen[basen]:
            seq_kompl=dict_basen[basen]+seq_kompl #wird gleich reversed zusammengeführt
    return seq_kompl

if __name__ == "__main__":
    sequenz=auslesen()
    print(reverse_dna(sequenz))
