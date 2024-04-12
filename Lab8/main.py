import random


def ga_tsp(initial_population, distances, generations):
    if not valid_inputs(initial_population, distances, generations):
        return None
    
    p_size = len(initial_population)
    
    current_population = initial_population
    
    # print("Current population= ", current_population)
    times_equal = 0
    for i in range (0, generations):
        child_list = []
        
        
        for j in range(0, len(current_population)):
            
            parent_A, parent_B = None, None
            while parent_A == parent_B:
                parent_A = current_population[random.randrange(p_size)]
                parent_B = current_population[random.randrange(p_size)]
                
            child_list.append(crossover(parent_A, parent_B))
        
        # print("Current: ", current_population)
        # print("Children: ", child_list)
        
        print("Generation: ", i)
        for k in current_population:
            for f in child_list:
                if k == f:
                    print("Match: ", k , " and ", f)
        

    print("Times equal: ", times_equal)
    return (0,0)
    

def valid_inputs(initial_population, distances, generations):
    if initial_population is None \
            or distances is None \
            or generations is None \
            or generations <= 0:       
        return False
    
    return True


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
        


        
            
    
    
    
# python3 tsp.py DIST6-simple