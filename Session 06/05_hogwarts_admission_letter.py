# Guillaume Gillard
# 17/01/2022

### Code to complete [START] ###

def write(letter_template, name):
    try :
        with open(letter_template, "r") as file :
            text = file.read()
            text = text.replace("#", name)
        with open(letter_template, "w") as file:
                  file.write(text)
    except :
        raise FileNotFoundError("File not Found !")