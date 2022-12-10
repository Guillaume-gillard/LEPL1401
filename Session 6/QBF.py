# Guillaume Gillard
# 04/11/2022

### Code to complete [START] ###

def get_max(filename):
    max_value = 0
    count_line = 0
    try :
        with open(filename, "r") as file :
            max_value = 0
            for number in file :
                try :
                    number = float(number)
                    if number > max_value :
                        max_value = number
                except :
                    pass
            if max_value == 0:
                return(-1)
            return (max_value)
    except :
        print("Error")
        return(-1)