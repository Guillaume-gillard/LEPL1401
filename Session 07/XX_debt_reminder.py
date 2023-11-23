
def give_money(borrowed_money, from_person, to_person, amount):
    if not isinstance(borrowed_money, dict):
        raise ValueError("borrowed_money should be a dictionnary !")
    if not isinstance(from_person, str):
        raise ValueError("from_person should be a string !")
    if not isinstance(to_person, str):
        raise ValueError("to_person should be a string !")
    if not isinstance(amount, (int, float)):
        raise ValueError("amount should be a float or integer !")
    if from_person and to_person not in borrowed_money:
        borrowed_money[from_person] = {to_person : -amount}
        borrowed_money[to_person] = {from_person : amount}
    else :        
        borrowed_money[from_person][to_person] -= amount
        borrowed_money[to_person][from_person] += amount
    if from_person == to_person :
        raise ValueError("You cannot give money to yourself !")

def total_money_borrowed(borrowed_money):
    if not isinstance(borrowed_money, dict):
        raise ValueError("borrowed_money should be a dictionnary !")    
    total = 0
    for dic in borrowed_money:
        for person, amount in dic.items():
            if amount > 0 :
                total += amount
    return total

