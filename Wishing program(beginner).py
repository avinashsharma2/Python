import time
hour = int(time.strftime('%H'))
min = int(time.strftime('%M'))
if(hour >= 4 and hour < 12):
    print("Good morning Sir!")
elif(hour == 12):
    if(min == 0):
        print("Good Noon Sir!")
    else:
        print("Good Afternoon Sir!")
elif(hour > 12 and hour <= 16):
    print("Good Afternoon Sir!")
elif(hour >= 17 and hour <= 19):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")
print("Thank You!!")