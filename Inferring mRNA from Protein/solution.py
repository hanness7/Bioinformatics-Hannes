def auslesen():
    '''
      Die Datei liest die erste und einzige Zeile aus der Datei aus
    '''
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        zeilen=file.readlines()
        sequenz=zeilen[0].rstrip() #nimm nur die erste Zeile
    return sequenz

def replace(sequenz):
    '''
    alle Ts durch Us ersetzen in der gegebenen Basenfolge
    '''
    ausgabe_sequenz=""
    for char in sequenz:
        if char=="T": #wenn die Base Thymin ist, dann ersetze durch Uracil
            ausgabe_sequenz+="U"
        else:
            ausgabe_sequenz+=char
    return ausgabe_sequenz


if __name__ == "__main__":
  sequenz=auslesen()
  print(replace(sequenz))
