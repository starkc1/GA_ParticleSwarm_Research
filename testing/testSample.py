import numpy
import GA

SOL_PER_POP = 8
NUM_PARENTS_MATING = 4
NUM_INPUTS = 2

POP_SIZE = (SOL_PER_POP, NUM_INPUTS)

new_population = numpy.random.uniform(-5.0, 5.0, size=POP_SIZE)

NUM_GENERATIONS = 5

for generation in range(NUM_GENERATIONS):
    print("Generation: ", generation)

    