
def add_time(start, duration, day=None):

    #  startList = [(eval(start[0:-6] + '+' + start[-2:] {'AM': AM, 'PM': PM})), int(start[-5:-3])]  # this is too complicated because of the 12 am/pm outlier

    weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    if start[0:-6] != '12':
        startList = [eval(start[0:-6] + '+' + start[-2:], {'AM': 0, 'PM': 12}), int(start[-5:-3])]
    else:
        startList = [eval(start[0:-6] + '-' + start[-2:], {'AM': 12, 'PM': 0}), int(start[-5:-3])]

    durList = [int(duration[0:-3]), int(duration[-2:])]

    newList = [((startList[0]+durList[0]) + ((startList[1]+durList[1]) // 60)) // 24,  # days
               ((startList[0]+durList[0]) + (startList[1]+durList[1]) // 60) % 24,  # hours
               (startList[1]+durList[1]) % 60]  # minutes

    newAMPM = 'AM' if newList[1] < 12 else 'PM'

    newMinutes = str(newList[2]) if newList[2] > 9 else '0' + str(newList[2])

    if newList[1] == 0:
        newHours = '12'
    elif newList[1] > 12:
        newHours = str(newList[1] - 12)
    else:
        newHours = str(newList[1])

    if day:
        newDay = ', ' + (weekdays[(weekdays.index(day.lower()) + newList[0]) % 7]).capitalize()
    else:
        newDay = ''

    if newList[0] == 0:
        new_time = newHours + ':' + newMinutes + ' ' + newAMPM + newDay
    elif newList[0] == 1:
        new_time = newHours + ':' + newMinutes + ' ' + newAMPM + newDay + ' (next day)'
    else:
        new_time = newHours + ':' + newMinutes + ' ' + newAMPM + newDay + ' (' + str(newList[0]) + ' days later)'

    print(startList)
    print(durList)
    print(newList)

    return new_time