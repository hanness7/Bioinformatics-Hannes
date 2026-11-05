#Datensatz im FASTA-Format
#Ziel: Ausgabe der Sequenz mit dem höchsten GC-Anteil
def count_gc(zeile):
    '''
    berechnet gc anteil
    '''
    counter=0
    for char in zeile:
        if char=="G" or char=="C":
            counter+=1
    if len(zeile)>0:
        anteil=(counter/len(zeile))*100
    else:
        anteil=0
    return anteil

def gc3():
    '''
    liest alle Infos aus der Datei infos.txt
    '''
    liste_all=[] #Liste mit allen Sequenzen + FASTA-Format
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        for zeile in file:
            zeile=zeile.rstrip()
            if not zeile:
                continue  #Leerzeileen überspringen
            if zeile.startswith(">"): #also FASTA-Format
                liste_all.append(zeile)
                liste_all.append("")
            else:
                #Sequenz-Zeile an die letzte Position anhängen
                liste_all[-1] += zeile
    return liste_all

def zweierliste(liste):
    '''
    zusammengehörige Elemente in eine Liste tun und Maximum ermitteln
    '''
    liste_neu=[] #neue Liste mit Teillisten, bestehend aus FASTA-Format + Sequenz
    for i in range(0, len(liste),2):
        liste_neu.append(liste[i:i+2]) #erstellt die Zweierlisten
    maximum = -1.0
    bestes_element = None
    for element in liste_neu: #für alle Elemente den GC-Content vergleichen
        aktueller_gc = count_gc(element[1])
        if maximum < aktueller_gc:
            maximum = aktueller_gc #Maximum ermitteln
            bestes_element = element #zweier Liste mit höchstem GC-Gehalt wird ausgegeben
    rosalind = bestes_element[0].replace(">", "")

    return rosalind +"\n"+str(maximum)
    
if __name__ == "__main__":
    print(zweierliste(gc3()))
