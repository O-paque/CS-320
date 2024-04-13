import random


# Genetric Algorithm to solve a symmetric and complete TSP
def ga_tsp(initial_population, distances, generations):
    if not valid_inputs(initial_population, distances, generations):
        return None
    
    p_size = len(initial_population)
    current_population = initial_population
    
    for i in range (0, generations):
        child_list = []
        
        
        for j in range(0, len(current_population)):
            
            parent_A, parent_B = None, None
            while parent_A == parent_B:
                parent_A = current_population[random.randrange(p_size)]
                parent_B = current_population[random.randrange(p_size)]
                
            child_list.append(crossover(parent_A, parent_B))
        
        
        current_population = next_gen(current_population, child_list)
        
    return (0,0)
    

# Checks for input validations per assignment guidelines
def valid_inputs(initial_population, distances, generations):
    if initial_population is None \
            or distances is None \
            or generations is None \
            or generations <= 0:       
        return False
    
    return True


# Takes part of a path from parents A and B and combines them into a child
def crossover(A, B):
    split_index = random.randint(1, len(A) - 2)     #-2 to always include A & B
    child = A[:split_index]
    
    temp_child = list(child)
    
    while len(temp_child) < len(A):
        rand_add = B[random.randint(0,len(B)-1)]
        
        if rand_add not in temp_child:
            temp_child.append(rand_add)
    
    child = tuple(temp_child)
    return child
        

# Determines the next generation's population for the Genetic Algorithm
# Parent selection was random in crossover so we choose the "best"
# cost across both parents and children for next_gen
def next_gen(current, children):
    #remove duplicate paths, more likely in smaller solution spaces
    for i in current:
        for j in children:
            if i == j:
                children.remove(f)
    
    return 0

# python3 tsp.py DIST6-simple