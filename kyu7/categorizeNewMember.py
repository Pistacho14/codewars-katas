def open_or_senior(data):
    placing_list = []
    for player in data:
        if  player[0] >= 55 and player[1] > 7:
            placing_list.append('Senior')
        else:
            placing_list.append('Open')
    return placing_list