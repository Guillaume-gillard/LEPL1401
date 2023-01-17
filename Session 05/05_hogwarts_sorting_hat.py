# Guillaume Gillard
# 17/01/2022

knowledge = [['Gryffindor', ['brave', 'strong', 'bold']],
             ['Ravenclaw', ['smart', 'wise', 'curious']],
             ['Hufflepuff', ['loyal', 'patient', 'hard-working']],
             ['Slytherin', ['cunning', 'wily', 'malignant']]]

### Code to complete [START] ###

def house_designation(student_qualities):
    house_score = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}
     # Attributing points to houses with regards to the student qualities
    for quality in student_qualities:
        for house in knowledge :
            if quality in house[1]:
                house_score[house[0]] += 1
    # Sorting the houses
    house_classement = sorted(house_score, key=house_score.get, reverse=True) # No brackets to get because we are just passing a reference to the method and not the result of the method
    return house_classement
