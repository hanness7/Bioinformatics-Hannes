def suche_sub(strang, sub_strang):
    '''
    sucht Substränge in einem großen Strang, es darf Überlappungen geben
    '''
    such_index=sub_strang[0] #die erste gesuchte Base
    index_counter=""
    for i in range(len(strang)):
        if strang[i]==such_index: #wenn ein gemeinsamer Start
            if strang[i:i+len(sub_strang)]==sub_strang: #wenn restliche Übereinstimmung
                index_counter+=str(i+1)+" " #merke die Startposition
    return index_counter

def auslesen():
    '''
    entnimmt der Datei den Strang und Substrang 
    '''
    with open("sample_input.txt", "r", encoding="utf-8") as file:
            line=file.readlines()
            strang=line[0].rstrip() #erste Zeile ist der Strang
            sub_strang=line[1].rstrip() #zweite Zeile ist der Substrang
    return (strang,sub_strang)

if __name__ == "__main__":
    strang=auslesen()[0]
    sub_strang=auslesen()[1]
    print(suche_sub(strang, sub_strang))


