# Guillaume Gillard

def search_time(l,t):
    """
    pre :  une liste d'événements l, un temps t
    post : l'index du premier élément dans l supérieur où égal à t; len(l) si un tel élément n'existe pas
    """
    pass

def absolute(v1,v2):
    """
    pre  : v1 et v2 deux nombres
    post : la fonction retourne |v1-v2|
    """
    pass

def euclidian_distance(c1,c2):
    """
    pre  : deux coordonnées c1=(x1,y1) et c2=(x2,y2)
    post : la fonction retourne la distance euclidienne entre c1 et c2
    """
    pass


### Code to complete [START] ###

def near(point_1, point_2, theta_2):
    dist = euclidian_distance(point_1, point_2)
    if dist <= theta_2 :
        return True 
    return False


def same_time(time_1, time_2, theta_1):
    delta = absolute(time_1, time_2)
    if delta <= theta_1:
        return True
    return False
    
    
def cross(trace_1, trace_2, theta_1, theta_2):
    for person_1 in trace_1:
        for person_2 in trace_2:
            time_1 = person_1[0]
            point_1 = person_1[1]
            time_2 = person_2[0]
            point_2 = person_2[1]
            if near(point_1, point_2, theta_2) and same_time(time_1, time_2, theta_1):
                return 1
            return 0

### Code en plus ###

def matrix_for_traces(l, theta_1, theta_2):
    matrix = []
    for trace_1 in l:
        line = []
        for trace_2 in l :
            if cross(trace_1, trace_2, theta_1, theta_2):
                line.append(1)
            else :
                line.append(0)
        matrix.append(line)
    return matrix