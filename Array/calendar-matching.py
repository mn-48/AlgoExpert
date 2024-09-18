#  O(c1+c2) Time | O(c1+c2) Space
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updateCalender1 = updateCalender(calendar1, dailyBounds1)
    # print("updateCalender1: ",updateCalender1)
    updateCalender2 = updateCalender(calendar2, dailyBounds2)
    # print("updateCalender2: ", updateCalender2)
    mergeCalender = mergeCalenders(updateCalender1, updateCalender2)
    # print("mergeCalender: ", mergeCalender)
    flattenedCalender = flattenedCalenders(mergeCalender)
    # print("flattenedCalender: ", flattenedCalender)

    return getMatchingAvailabilities(flattenedCalender, meetingDuration)
    # return None

def updateCalender(calendar, dailyBounds):
    updatedCalender = calendar[:]
    updatedCalender.insert(0, ["0:00", dailyBounds[0]])
    updatedCalender.append([dailyBounds[1], "23:59"])
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])] , updatedCalender))


def mergeCalenders(calendar1, calendar2):
    merged = []
    i, j = 0, 0 
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i +=1
        else:
            merged.append(meeting2)
            j+=1
    while i< len(calendar1):
        merged.append(meeting1)
        i+=1
    while j< len(calendar2):
        merged.append(meeting2)
        j+=1
        
    return merged

def flattenedCalenders(calender):
    # print("flattenedCalenders --> calender:", calender)
    flattend = [calender[0][:]]
   
    for i in range(1, len(calender)):
        currentMetting = calender[i]
        previousMeeting = flattend[-1]
        currentStart, currentEnd = currentMetting
        previousStart, previousEnd = previousMeeting
        if previousEnd >= currentStart:
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
            flattend[-1] = newPreviousMeeting
        else:
            flattend.append(currentMetting[:])
    return flattend
    
def getMatchingAvailabilities(calender, meetingDuration):
    matchingAvailabilities = []
    for i in range(1, len(calender)):
        start = calender[i-1][1]
        end = calender[i][0]
        availAbilityDuration = end-start
        if availAbilityDuration >= meetingDuration:
            matchingAvailabilities.append([start, end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours*60+minutes

def minutesToTime(minutes):
    hours = minutes//60
    mins = minutes%60
    hoursString = str(hours)
    minutesString = "0"+str(mins) if mins<10 else str(mins)
    return hoursString+":"+minutesString


'''
calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30
expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]

print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))
# calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
'''
