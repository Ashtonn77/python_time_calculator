def get_time(s, t):
    s = s.split()
    t = t.split(':')
    
    hour_min = s[0].split(':')
    hour_min.append(s[1])
    hour_min = hour_min + t
    
    if hour_min[2] == 'PM' : 
        hour_min[0] = int(hour_min[0]) + 12
    
    return hour_min


def get_seconds(k, h = True):
    if h : return k * 60 * 60
    else : return k * 60

def num_days_later(hm):
    c = 0
    h = get_seconds(int(hm[0])) + get_seconds(int(hm[3]))
    m = get_seconds(int(hm[1]), False) + get_seconds(int(hm[4]), False)
    
    h = h + m
    
    day_seconds = 24 * 60 * 60
    
    return int(h / day_seconds)
    
    
def get_day(d, l):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days_map = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
    
    return days[(days_map[d] + l) % 7]
    
    

def add_time_f(hm):
    h = (int(hm[0]) + int(hm[3]))
    m = (int(hm[1]) + int(hm[4]))
    h = (h + int(m / 60)) % 24
    m = m % 60
    
    p = "AM" if h < 12 else "PM"
    
    h = h - 12 if h > 12 else h
    h = 12 if h == 0 else h
    m = "0" + str(m) if m < 10 else str(m)
    
    return "{}:{} {}".format(str(h), m, p)  

def add_time(start, duration, day = ""):  
    hm = get_time(start, duration)
    t = add_time_f(hm)
    d = num_days_later(hm)
    
    if len(day) != 0:
        t = t + ", " + get_day(day.lower(), d).capitalize()
    
    if d == 0:
        return t
        
    elif d == 1:
        return "{} (next day)".format(t)
        
    else:
        return "{} ({} days later)".format(t, d)
