# Guillaume Gillard 
# 15/11/2022

### Code to complete [START] ###

def get_country(l, name):
    for d in l:
        if d["City"] == name:
            return d["Country"]
    return False