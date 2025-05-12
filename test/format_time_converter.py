

# convertitore minuti => HH:MM
def format_time(minutes):
    if minutes is None:
        return "00:00"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"
























