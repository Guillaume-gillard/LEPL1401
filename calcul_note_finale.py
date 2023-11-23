def note_finale(interro, examen, bonus): # /20 /20 /1
    if examen > interro :
        note = examen + bonus
    else : 
        note = interro * (1/3) + examen * (2/3) + bonus
    return round(note)

