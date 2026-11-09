#Overlap Graphs
def auslesen():
    with open("overlapgraphs.txt", "r", encoding="utf-8") as file:
        zeilen=file.readlines()
        sequenz=""
        dic_seq={}
        merk_index=0
        for i in range(len(zeilen)):
            if zeilen[i].startswith(">"):
                if sequenz:
                    dic_seq[zeilen[merk_index][1:].rstrip()]=sequenz
                    sequenz=""
                merk_index=i
            else:
                #while not zeilen[i].startswith(">"):
                sequenz+=zeilen[i].rstrip()
        dic_seq[zeilen[merk_index][1:].rstrip()]=sequenz

        return dic_seq
      
def overlap(dic_seq):
    ausgabe=""
    for element1 in dic_seq.items():
        for element2 in dic_seq.items():
            if element1[1][len(element1[1])-3:]==element2[1][:3]:
                #print(element1[1][len(element1[1])-3:],element2[1][:3])
                if not element1[0]==element2[0]:
                    ausgabe+=str(element1[0])+" "+str(element2[0])+"\n"
   
    return ausgabe

if __name__ == "__main__":
    dic_seq=auslesen()
    print(overlap(dic_seq))
