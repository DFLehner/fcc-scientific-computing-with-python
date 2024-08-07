#Function to track time. Input a start time (and optionally day of week) and duration to wait and it will return end time
#days passed, and day of week.


def add_time(start, duration, day=False):
    
    start_hours = int(start.split(':')[0])
    start_minutes = int(start.split(':')[1][:2])
    AM_or_PM = start.split(' ')[1]
    print(start_minutes)
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    print(duration_hours)
    end_minutes = start_minutes + duration_minutes
    if end_minutes >= 60:
        start_hours += 1
        end_minutes -= 60
    end_hours = start_hours + duration_hours
    day_count = end_hours//24
    end_hours = end_hours%24
    if end_hours >= 12:
        if AM_or_PM == 'AM':
            end_hours -= 12
            AM_or_PM = 'PM'
        else:
            day_count += 1
            end_hours -= 12
            AM_or_PM = 'AM'

    if end_hours == 0:
        end_hours = 12    

    output_string = str(end_hours) + ":" + str(end_minutes).rjust(2,'0') + ' ' + AM_or_PM

    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if day:
        parsed_day = day[0].upper() + day[1:].lower()
        day_index = days_of_week.index(parsed_day)
        day_index = (day_index + day_count)%7
        output_string += ', ' + days_of_week[day_index]

    if day_count == 1:
        output_string += ' (next day)'
    
    if day_count > 1:
        output_string += ' (%s days later)' % day_count
    


    return output_string  
    

print(add_time('11:59 PM', '24:05', 'monDay'))
    


