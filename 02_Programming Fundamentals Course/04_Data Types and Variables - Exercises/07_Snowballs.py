import math

number_of_snowballs = int(input())
snowballsnow = 0
snowballtime = 0
snowballquality = 0
snowballvalue = 0
maxvalue = 0
for i in range(number_of_snowballs):
    snowballsnow = int(input())
    snowballtime = int(input())
    snowballquality = int(input())
    snowballvalue = math.pow(int(snowballsnow / snowballtime), snowballquality)
    if snowballvalue > maxvalue:
        maxsnowballsnow = snowballsnow
        maxvalue = snowballvalue
        maxsnowballtime = snowballtime
        maxsnowballquality = snowballquality
print(f'{maxsnowballsnow} : {maxsnowballtime} = {int(maxvalue)} ({maxsnowballquality})')