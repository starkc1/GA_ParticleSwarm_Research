import numpy
import holderGA as GA

#minima f(x,y) => f(+-8.05502, +-9.66459) = −19.2085

num_values = 2
num_parents = 4
solutions_per_pop = 10
population_size = (solutions_per_pop, num_values) #manager input
population = numpy.random.uniform(low=-10, high=10, size=population_size) #manager input
#population = [3.0, 2.0]

generations = 5 #manager input

print("Population: ", population)
for generation in range(generations):
    print("Generation: ", generation)

    fitness = GA.calc_fitness(population)
    
    parents = GA.select_parents(population, fitness, num_parents)

    crossover = GA.crossover(parents, children_size=(population_size[0] - parents.shape[0], num_values))

    mutation = GA.mutation(crossover)
    
    population[0:parents.shape[0],:] = parents
    population[parents.shape[0]:,:] = mutation

print("fitness: ", numpy.min(GA.calc_fitness(population)))
print("Population: ", population)




    