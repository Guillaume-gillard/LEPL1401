### Code to complete [START] ###


def fine(authorized_speed, actual_speed):
    exces = actual_speed - authorized_speed
    fine_amount = 0
    for i in range(1, exces+1):
        fine_amount += 5
    if exces <= 0:
        return(0)
    elif fine_amount < 12.5 :
        return(12.5)
    elif exces <= 10 and fine_amount > 12.5 :
        return(fine_amount)
    else :
        return(fine_amount * 2)