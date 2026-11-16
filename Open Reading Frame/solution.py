#>Rosalind_99
#AGCCATGTAGCATCATGGTAGGGAGGCCGCCGCGGAGTGATGTCTTGTGATAAGCCTAGGAGTGAGTAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGAGAGAGAGAGGAGGAGGAGTAGAGGAGGAGGAGTAGAGAGAGAGAG

codons = {
"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
"TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
"TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
"TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
"TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
"TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
"TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
"TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
"TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
"TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
"TAA": "Stop1", "CAA": "Q", "AAA": "K", "GAA": "E",
"TAG": "Stop2", "CAG": "Q", "AAG": "K", "GAG": "E",
"TGT": "C","CGT": "R", "AGT": "S", "GGT": "G",
"TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
"TGA": "Stop3", "CGA": "R", "AGA": "R", "GGA": "G",
"TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
} 

#Funktionen, die ich benötige

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

def auslesen():
    '''
      Die Datei liest die erste und einzige Zeile aus der Datei aus
    '''
    sequenz=""
    with open("openreadingframes.txt", "r", encoding="utf-8") as file:
        zeilen=file.readlines()
        for i in range(1, len(zeilen)): #die 0. Zeile ist der Name der Sequenz
            sequenz+=zeilen[i].rstrip() #die Sequenz kann über mehrere Zeilen gehen
    return sequenz


def readingframes(sequenz):
    '''
    Diese Funktion liest alle möglichen Proteine mit Start und Stop Codon aus, dabei arbeiten wir nicht in festen 3er Rastern, sondern betrachten alle Möglichkeiten, da wir sonst Start Codons übersehen können
    '''
    protein_sequenz=set()  #um Doppelungen zu vermeiden
    for i in range(0, len(sequenz)):
        triplett=sequenz[i:i+3] #so gehen wir alle möglichen Tripletts durch
        if triplett=="ATG": #ATG ist ein Startcodon
            stop=False 
            protein="" 
            j=i #Counter für die while Schleif, damit i unabhängig davon läuft
            while not (triplett=="TAA" or triplett=="TAG" or triplett=="TGA"): #solange kein Stop Codon da ist
                protein+=codons[triplett] #passende AS wird dem Protein hinzugefügt
                j+=3 #Counter auf nächstes Triplett
                if len(sequenz[j:j+3])==3: #wenn ein Triplett noch existiert
                    triplett=sequenz[j:j+3] #ein Triplett weiter gehen
                    if triplett=="TAA" or triplett=="TAG" or triplett=="TGA": #wenn Triplett==Stop Codon
                        stop=True 
                else:
                    break
            if stop: #wenn wir am Ende sind
                protein_sequenz.add(protein) #dem Set mit den Proteinen wird ein einzelnes Protein hinzugefügt
    return protein_sequenz

def output(sequenz):
    '''
    gibt das Ergebnis nach Vorgabe von Rosalind aus
    '''
    set1=readingframes(sequenz) #normaler DNA-Strang
    set2=readingframes(reverse_dna(sequenz)) #der reversed DNA-Strang
    ausgabe=""
    for element in set1:
        if element:
            ausgabe+=(element+"\n")
    for element in set2:
        if not(element in set1) and element: #wenn das Element nicht schon in Menge 1 drin ist
            ausgabe+=(element+"\n")
    return ausgabe
    

            

if __name__ == "__main__":
    sequenz=auslesen()
    print(output(sequenz))

