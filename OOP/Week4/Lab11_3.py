def counto_list(list):
    count = 0
    for el in list:
        if el[0] == "o":
            count += 1
    return count

print(counto_list(['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']))

