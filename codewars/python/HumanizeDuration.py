def pluralize(n, word):
    if n == 1:
        return '%d %s' % (n, word)
        
    return '%d %ss' % (n, word)
        
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    ONE_MINUTE = 60
    ONE_HOUR = 60 * ONE_MINUTE
    ONE_DAY = 24 * ONE_HOUR
    ONE_YEAR = 365 * ONE_DAY
    
    units = (
        (ONE_YEAR, 'year'),
        (ONE_DAY, 'day'),
        (ONE_HOUR, 'hour'),
        (ONE_MINUTE, 'minute'),
        (1, 'second'),
    )
        
    r = []
    for unit in units:
        time_period, word = unit
        if seconds >= time_period:
            n = int(seconds / time_period)
            r.append(pluralize(n, word))
            seconds -= n * time_period
    
    return ' and'.join(', '.join(r).rsplit(',', 1))
