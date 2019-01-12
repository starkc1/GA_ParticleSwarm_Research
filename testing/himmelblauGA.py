import numpy

def cal_pop_fitness(inputs, population):
    return numpy.sum(population * inputs, axis=1)

def select_mating_pool(population, fitness, num_parents):
    parents = numpy.empty((num_parents, population.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_index = numpy.where(fitness == numpy.max(fitness))
        max_fitness_index = max_fitness_index[0][0]
        parents[parent_num, :] = population[max_fitness_index, :]
        fitness[max_fitness_index] = -999999999
    return parents

def crossover(parents, offspring_size):
    offspring_size = numpy.empty(offspring_size)
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        parent1_index = k%parents.shape[0]

        parent2_index = (K + 1)%
