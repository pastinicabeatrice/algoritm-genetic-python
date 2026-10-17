import random
import unittest

from genetic import crossover, evolve, fitness, mutate, optimal_value

ITEMS = [("a", 5, 10), ("b", 4, 40), ("c", 6, 30), ("d", 3, 50)]


class GeneticTest(unittest.TestCase):
    def test_fitness_rejects_overweight(self):
        self.assertEqual(fitness([0, 1, 0, 1], ITEMS, 10), 90)
        self.assertEqual(fitness([1, 1, 1, 1], ITEMS, 10), 0)

    def test_optimal_value(self):
        self.assertEqual(optimal_value(ITEMS, 10), 90)

    def test_crossover_and_mutation_keep_length(self):
        rng = random.Random(0)
        child = crossover([0] * 6, [1] * 6, rng)
        self.assertEqual(len(child), 6)
        self.assertEqual(mutate(child, 1.0, rng), [1 - gene for gene in child])

    def test_evolve_finds_optimum_and_never_gets_worse(self):
        best, history = evolve(ITEMS, 10, population_size=20, generations=30)
        self.assertEqual(fitness(best, ITEMS, 10), optimal_value(ITEMS, 10))
        self.assertEqual(history, sorted(history))


if __name__ == "__main__":
    unittest.main()
