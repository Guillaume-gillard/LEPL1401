def diff_count(lst):

    ### Code to complete [START] ###

    allreadycounted = []
    count = 0
    item_2 = ""
    for item in lst :
        item_1 = item
        if item_1 != item_2 and item_1 not in allreadycounted:
            allreadycounted.append(item)
            count +=1
        item_2 = item_1
    return count
