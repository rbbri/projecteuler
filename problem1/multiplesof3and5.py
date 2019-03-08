def multiple_of(number, multiple):
    return True if number % multiple == 0 else False

def solution():
    sol = sum(x for x in range(1000) if (multiple_of(x, 3) or multiple_of(x, 5)))
    return str(sol)
