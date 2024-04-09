

def ga_tsp(initial_population, distances, generations):
    if initial_population is None \
            or distances is None \
            or generations is None:
        return None