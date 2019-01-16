import numpy
import math

def himmelblau(population):
    return (pow((pow(population[0], 2) + population[1] - 11), 2) + pow((population[0] + pow(population[1], 2) - 7), 2))

def holderTable(population):
    return -abs(math.sin(population[0]) * math.cos(population[1]) * math.exp(abs(1 - (math.sqrt(pow(population[0], 2) + pow(population[1], 2)) / math.pi))))

def calc_fitness(population):
    result = []
    for pop in range(len(population)):
        result.append(holderTable(population[pop]))
    print("fitness: ", result)
    return result

def select_parents(population, fitness, num_parents):
    parents = numpy.empty((num_parents, population.shape[1]))
    for parent_num in range(num_parents):
        min_fitness_index = numpy.where(fitness == numpy.min(fitness))
        min_fitness_index = min_fitness_index[0][0]
        parents[parent_num, :] = population[min_fitness_index, :]
        fitness[min_fitness_index] = 99999999999
    print("parents: ", parents)
    return parents

def crossover(parents, children_size):
    children = numpy.empty(children_size)
    crossover_point = numpy.uint8(children_size[1]/2)

    for k in range(children_size[0]):
        parent1_index = k%parents.shape[0]
        parent2_index= (k+1)%parents.shape[0]
        children[k, 0:crossover_point] = parents[parent1_index, 0:crossover_point]
        children[k, crossover_point] = parents[parent2_index, crossover_point]
    print('children: ', children)
    return children

def mutation(children_crossover):
    print(children_crossover[1, 2])
    # for index in range(children_crossover.shape[0]):
    #     random_val= numpy.random.uniform(-1.0, 1.0, 1)
    #     children_crossover[index, 2] = children_crossover[index, 2] + random_val
    # print("mutated: ", children_crossover)
