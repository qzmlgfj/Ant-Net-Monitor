def date_range(start, end, delta):
    current = start.replace(second=0, microsecond=0)
    while current < end.replace(second=0, microsecond=0):
        yield current
        current += delta