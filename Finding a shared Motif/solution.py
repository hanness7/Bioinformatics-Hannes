def liste_seq():
    '''
    Diese Funktion entnimmt dem FASTA-Format alle Sequenzen,
    unabhängig von Zeilenzahlen oder Umbrüchen.
    '''
    sequenzen = []
    with open("fasta.txt", "r", encoding="utf-8") as file:
        zeile=file.readlines()
        sequenzen=[]
        string="" #hier speichern wir die Sequenzen zwischen
        for element in zeile:
            if not element[0]==">":
                string+=str(element.rstrip())
            if element[0]==">": #wenn FASTA-Zeile
                if string: #wenn eine Sequenz gespeichert wurde
                    sequenzen.append(string)
                string=""
        if string: #wenn wir durch sind, es aber noch eine gespeicherte Sequenz gibt
            sequenzen.append(string.rstrip())
    return sequenzen
                
def vergleich_seq():
    '''
    vergleicht alle Sequenzen mit den gemeinsamen Substrings
    '''
    gemeinsam_vgl1=set() #als Menge, um Dopplungen zu meiden
    # wir wollen alle Kombis aus Seq1 erstellen, damit wir dann in den anderen Seq schauen können, ob ein Slice Teil der nschfolgenden Seq ist
    for i in range(0, len(liste_alle_seq[0])): 
        for j in range(0, len(liste_alle_seq[0])):
            if liste_alle_seq[0][i:j]: #falls ein Slice existiert
                gemeinsam_vgl1.add(liste_alle_seq[0][i:j]) #alle möglichen Kombis aus erster Seq erstellen
    #alle Sequenzen durchgehen
    for i in range(1,len(liste_alle_seq)): 
        gemeinsam_vgl2 = set() #zweites Vergleichsonjekt, auch als Menge
        aktuelle_seq = liste_alle_seq[i] 
        #print(aktuelle_seq)
        for element1 in gemeinsam_vgl1:
            if element1 in aktuelle_seq: #wenn ein gemeinsames Element in aktueller Seq, dann nehmen wir es mit 
                #print(element1)
                gemeinsam_vgl2.add(element1) #wie ein Sieb quasi, alle gemeinsamen elemente werden beibehalten
                #print(gemeinsam_vgl2)
        gemeinsam_vgl1 = gemeinsam_vgl2 #das neue Vergleichselement werden alle gemeinsamen Slices
    maximum_sub=max(gemeinsam_vgl1, key=len) #längste Subseq/Slice speichern
    return maximum_sub


if __name__=="__main__":
    liste_alle_seq=liste_seq()
    print(vergleich_seq())
