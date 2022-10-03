def past(h, m, s):
    if h >= 0:
        h = h * 3600000
    if m >=0:
        m = m * 60000
    if s >= 0:
        s = s * 1000
        
    return(h + m + s)


"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
Example:

h = 0
m = 1
s = 1

result = 61000
"""

