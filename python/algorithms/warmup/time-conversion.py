#!/bin/python3

time = input().strip()

if time[len(time) - 2:].lower() == 'pm':
    if int(time[0:2]) == 12:
        hr = '12'
    else:
        hr = int(time[0:2]) + 12
    ans = str(hr) + str(time[2:len(time) - 2])
elif time[len(time) - 2:].lower() == 'am':
    if int(time[0:2]) == 12:
        hr = '00'
    else:
        hr = time[0:2]
    ans = str(hr) + str(time[2:len(time) - 2])
print(ans)
