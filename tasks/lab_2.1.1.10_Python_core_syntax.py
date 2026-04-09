class TimeInterval:
    def __init__(self, hours = 0, minutes = 0, seconds = 0, is_nagative = False): # keyword parameters with default values
        if type(hours) is not int:
            raise TypeError(f'Expected hours to be an int, got: {hours}')
        if type(minutes) is not int:
            raise TypeError(f'Expected minutes to be an int, got: {minutes}')
        if type(seconds) is not int:
            raise TypeError(f'Expected seconds to be an int, got: {seconds}')
        if type(is_nagative) is not bool:
            raise TypeError(f'Expected is_negative to be a bool, got: {is_nagative}')
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.is_negative = is_nagative
    
    def get_seconds_from_all_units(self, time_interval):
        if not isinstance(time_interval, TimeInterval):
            raise TypeError("Wrong type during addition")
        seconds = time_interval.hours * 3600 + time_interval.minutes * 60 + time_interval.seconds
        if time_interval.is_negative:
            return -seconds
        return seconds
    
    def get_time_interval_from_seconds(self, total_seconds):
        is_negative = total_seconds < 0
        abs_total_seconds = abs(total_seconds)

        hours = abs_total_seconds // 3600
        minutes = abs_total_seconds % 3600 // 60
        seconds = abs_total_seconds % 60

        return TimeInterval(hours, minutes, seconds, is_negative)
    
    def __add__(self, other):
        if not isinstance(other, TimeInterval) and not isinstance(other, int):
            raise TypeError("Wrong type during addition")
        
        other_seconds = other if isinstance(other, int) else self.get_seconds_from_all_units(other)
        
        total_seconds = self.get_seconds_from_all_units(self) + other_seconds

        return self.get_time_interval_from_seconds(total_seconds)
    
    def __sub__(self, other):
        if not isinstance(other, TimeInterval) and not isinstance(other, int):
            raise TypeError("Wrong type during subtraction")
        
        other_seconds = other if isinstance(other, int) else self.get_seconds_from_all_units(other)
        
        total_seconds = self.get_seconds_from_all_units(self) - other_seconds

        return self.get_time_interval_from_seconds(total_seconds)
    
    def __str__(self):
        hours = str(self.hours) if self.hours > 9 else "0" + str(self.hours)
        minutes = str(self.minutes) if self.minutes > 9 else "0" + str(self.minutes)
        seconds = str(self.seconds) if self.seconds > 9 else "0" + str(self.seconds)

        if self.is_negative:
            return "-" + hours + ":" + minutes + ":" + seconds
        return hours + ":" + minutes + ":" + seconds
    
    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Wrong type during multiplication")
        total_seconds = self.get_seconds_from_all_units(self) * other
        return self.get_time_interval_from_seconds(total_seconds)

ti1 = TimeInterval(1, 20, 0)
ti2 = TimeInterval(0, 50, 30)
ti3 = TimeInterval(0, 30, 0, True)
ti4 = TimeInterval(0, 20, 0, True)
ti5 = TimeInterval(minutes = 2)
ti6 = TimeInterval(seconds = 30)

# print(str(ti1 + ti2))
# print(str(ti1 - ti2))
# print(str(ti2 - ti1))
# print(str(ti3 + ti4))
# print(str(ti3 - ti4))
# print(str(ti4 + ti3))
# print(str(ti4 - ti3))
# print(ti1 * 3)
# print(ti3 * 3)
# print(str(ti2 - 400))
# print(str(ti3 + 100000))
print(ti5 + ti6)
