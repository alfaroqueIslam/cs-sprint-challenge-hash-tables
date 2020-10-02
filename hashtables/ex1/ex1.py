
def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    for i in range(length):
        if weights[i] in cache:
            return (i, cache[limit-weights[i]])
        cache[weights[i]] = i
        try:
            if cache[limit-weights[i]]:
                    return (i, cache[limit-weights[i]])
        except KeyError:
            pass
    
  
    return None
