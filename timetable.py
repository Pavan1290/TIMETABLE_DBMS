class Timetable:
    def __init__(self):
        self.lunch_break_start = 13  # Default lunch break start time (1 PM)
        self.lunch_break_end = 14    # Default lunch break end time (2 PM)

    def set_lunch_break(self, start, end):
        """Set custom lunch break time."""
        self.lunch_break_start = start
        self.lunch_break_end = end

    def generate_timetable(self):
        for day in self.days:
            for hour in range(self.start_hour, self.end_hour):
                if self.lunch_break_start <= hour < self.lunch_break_end:
                    self.timetable[day][hour] = 'Lunch Break'
                else:
                    if self.is_lab(hour):
                        self.timetable[day][hour] = 'Lab'
                        hour += 1  # Labs are 2 hours
                    else:
                        self.timetable[day][hour] = 'Class'

    def is_lab(self, hour):
        """Determine if the current hour should be a lab."""
        return hour % 2 == 0
