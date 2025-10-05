import datatime

def is_restaurant_open():
    now = datatime.datatime.now()
    current_day = now.weekday()
    current_time = now.time()


    weekday_open_time = datatime.time(9,0)
    weekday_close_time = datatime.time(22,0)
    weekend_open_time = datatime.time(10,0)
    weekend_close_time = datatime.time(23,0)

    if 0 <= current_day <= 4:
        return weekend_open_time <= current_time < weekday_close_time
    elif current_day in [5,6]:
        return weekend_open_time <= current_time < weekday_close_time
    return False