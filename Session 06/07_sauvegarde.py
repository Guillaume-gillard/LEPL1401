# Guillaume Gillard 
# 20/12/2022

### Code to complete [START] ###

#save the 4 integer to the file named filename
def save_data(filename, life, mana, position_x, position_y):
    with open(filename, 'w') as file:
        s = str(life) + "\n" + str(mana) + "\n" + str(position_x) + "\n" + str(position_y) + "\n"
        file.write(s)


#return a tuple containing (life, mana, position_x, position_y) previously saved
def load_data(filename):
    try :
        with open(filename, "r") as file:
            info = file.readlines()
            t = (int(info[0]), int(info[1]), int(info[2]), int(info[3]))
            return t
    except :
        raise FileNotFoundError("File not found !")