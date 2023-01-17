#### Code to complete [START] ####


def referee(score_file):
    try :
        with open(score_file, "r") as file :
            score = {}
            count = 1
            teams = []
            for line in file :
                info = line.strip("\n").split(" ")
                #initializing the name of the teams                    
                if count <= 2 :
                    teams.append(info[0])
                    score[info[0]] = 0
                # adding points
                elif count > 2 :
                    score[str(info[0])] += int(info[1])
                    if int(info[1]) == 150 :
                        if score[teams[0]] > score[teams[1]]:
                            return teams[0]
                        return teams[1]
                count += 1
    except :
        raise FileNotFoundError("File not found !")