

def ga_tsp(initial_population, distances, generations):
    if not valid_inputs(initial_population, distances, generations):
        return None

    return (0,0)
    

def valid_inputs(initial_population, distances, generations):
    if initial_population is None \
            or distances is None \
            or generations is None \
            or generations <= 0:       
        return False
    
    return True
