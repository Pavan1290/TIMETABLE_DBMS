# ...existing imports...
from components import Settings  # Ensure Settings is imported

# ...existing code...
def loadOperatingTime(self):
    # Old hard‑coded values
    # school_start = 8
    # school_end = 16
    # New: load from project settings
    settings = Settings.getSettings()
    school_start = settings['starting_time']
    school_end = settings['ending_time']
    # ...existing code that uses school_start and school_end...
