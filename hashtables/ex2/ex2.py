#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    for ticket in tickets:
        if ticket.source not in cache:
            cache[ticket.source] = ticket.destination
    s = "NONE"
    n = 1
    e = 1
    while n == 1:
        route.append(cache[s])
        s = cache[s]
        e = cache[s]
        if e == "NONE":
            route.append("NONE")
            return route

    

    

    return route
