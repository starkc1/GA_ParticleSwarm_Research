import numpy

def cal_pop_fitness(inputs, pop):
    return numpy.sum(pop*inputs, axis=1)

def select_mating_pool(pop, fit, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fit == numpy.max(fit))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fit[max_fitness_idx] = -999999999999 
    print("parents: ", parents)
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        parent1_idx = k%parents.shape[0]

        parent2_idx = (k+1)%parents.shape[0]

        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]

        offspring[k, crossover_point] = parents[parent2_idx, crossover_point]
    print('offspring: ', offspring)
    return offspring



def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover