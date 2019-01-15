import numpy
import GA

#sample from: https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6
#Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
#Trying to find the optimum weights (w) for the equation with the following inputs
equation_inputs = [4,-2,3.5,5,-11,-4.7]

num_weights = 6

<<<<<<< HEAD
sol_per_pop = 8
num_parents_mating = 2
=======
sol_per_pop = 4
num_parents_mating = 4
>>>>>>> 002f504713ffb54ef899245954af7ee41b6ae0ef

pop_size = (sol_per_pop,num_weights)
print(pop_size)
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)
<<<<<<< HEAD

num_generations = 10
=======
print(new_population)
num_generations = 5
>>>>>>> 002f504713ffb54ef899245954af7ee41b6ae0ef

for generation in range(num_generations):
    #print("Generation : ", generation)

    fitness = GA.cal_pop_fitness(equation_inputs, new_population)
    #print(fitness)
    parents = GA.select_mating_pool(new_population, fitness, num_parents_mating)

    offspring_crossover = GA.crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    offspring_mutation = GA.mutation(offspring_crossover)

    new_population[0:parents.shape[0],:] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    #print("Best result : ", numpy.max(numpy.sum(new_population * equation_inputs, axis = 1)))

fitness = GA.cal_pop_fitness(equation_inputs, new_population)


best_match_idx = numpy.where(fitness == numpy.max(fitness))

#print("Best solution : ", new_population[best_match_idx, :])
#print("Best solution fitness : ", fitness[best_match_idx])
