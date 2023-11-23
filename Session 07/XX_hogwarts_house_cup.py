students = {'gryffindor': ['Harry', 'Hermione', 'Ron', 'Ginny', 'Fred', ' Georges', 'Neville'],
            'ravenclaw': ['Cho', 'Luna', 'Sybill', 'Marcus', 'Marietta', 'Terry', 'Penelope'],
            'hufflepuff': ['Pomona', 'Zacharias', 'Teddy', 'Cedric', 'Nymphadora', 'Newton', 'Justin'],
            'slytherin': ['Malfoy', 'Severus', 'Dolores', 'Horace', 'Blaise', 'Pansy', 'Bellatrix']}

### Code to complete [START] ###

def winning_house(scroll):
    try :
        with open(scroll, 'r') as file :
            classement = {"gryffindor" : 0, "ravenclaw" : 0, "hufflepuff" : 0, "slytherin" : 0}
            for line in file :
                for info in line.split():
                    student = info.strip()[0]
                    score = info.strip()[1]
                    for house in students :
                        if student in house :
                            classement[house] += score
                            break
            score_max = max(classement)
            winner = []
            for house, score in classement.items():
                if score == score_max :
                    winner.append(house)
            if len(winner) == 1 :
                return winner[0]
            return winner
    except  :
        raise FileNotFoundError("File not found !")
