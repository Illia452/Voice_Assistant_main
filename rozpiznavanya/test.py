import time

loc_time = time.localtime()
min = loc_time.tm_min
hour = loc_time.tm_hour
mon = loc_time.tm_mon
year = loc_time.tm_year

timmee = (f"{year}.{mon} - {hour}:{min}")

print(timmee)