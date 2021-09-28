time = int(input())
m = 60
h = 3600
d = 86400
if time > d:
    day = time // 86400
    hour = time // 3600 - day * 24
    mint = time // 60 - (hour * 60 + day * 1440)
    sec = time % 86400 - (mint * 60 + hour * 3600)
    print(f'{day} дней {hour} часов {mint} минут {sec} секунд')
elif time > h:
    hour = time // 3600
    mint = time // 60 - hour * 60
    sec = time % 3600 - mint * 60
    print(f'{hour} часов {mint} минут {sec} секунд')
elif time > m:
    mint = time // 60
    sec = time % 60
    print(f'{mint} минут {sec} секунд')