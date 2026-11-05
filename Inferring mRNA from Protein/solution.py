def auslesen():
    '''
    liest die RNA-Sequenz ab
    '''
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        zeilen=file.readlines()
        rna_eingabe=zeilen[0]
    return rna_eingabe

codons = {
"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
"UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
"UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
"UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
"UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
"UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
"UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
"UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
"UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
"UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
"UAA": "Stop1", "CAA": "Q", "AAA": "K", "GAA": "E",
"UAG": "Stop2", "CAG": "Q", "AAG": "K", "GAG": "E",
"UGU": "C","CGU": "R", "AGU": "S", "GGU": "G",
"UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
"UGA": "Stop3", "CGA": "R", "AGA": "R", "GGA": "G",
"UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
} 


def rna_to_protein(rna_eingabe):
    '''
    der RNA-Strang wird in ein Protein umgewandelt
    '''
    polypeptid=""
    for i in range(0,len(rna_eingabe), 3):
        triplett=rna_eingabe[i:i+3] #die RNA in Tripletts aufteilen
        if codons[triplett]=="Stop1" or codons[triplett]=="Stop2" or codons[triplett]=="Stop3": #wenn ein Stop-Codon, dann unterbrich das Umwandeln
            break
        polypeptid+=codons[triplett] #sonst, erweitere das Polypeptid
        #print(polypeptid)
    return polypeptid

if __name__ == "__main__":
    rna_eingabe=auslesen()
    print(rna_to_protein(rna_eingabe))
    
