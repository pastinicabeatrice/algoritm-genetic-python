import random


def fitness(genes, items, capacity):
    chosen = [item for item, gene in zip(items, genes) if gene]
    weight = sum(item[1] for item in chosen)
    return sum(item[2] for item in chosen) if weight <= capacity else 0


def select(population, score, rng, size=3):
    return max(rng.sample(population, size), key=score)


def crossover(a, b, rng):
    cut = rng.randrange(1, len(a))
    return a[:cut] + b[cut:]


def mutate(genes, rate, rng):
    return [1 - gene if rng.random() < rate else gene for gene in genes]


def evolve(items, capacity, population_size=100, generations=100, mutation_rate=0.05, elite=2, seed=0):
    rng = random.Random(seed)
    score = lambda genes: fitness(genes, items, capacity)
    population = [[int(rng.random() < 0.3) for _ in items] for _ in range(population_size)]
    history = []
    for _ in range(generations):
        population.sort(key=score, reverse=True)
        history.append(score(population[0]))
        children = [
            mutate(crossover(select(population, score, rng), select(population, score, rng), rng), mutation_rate, rng)
            for _ in range(population_size - elite)
        ]
        population = population[:elite] + children
    return max(population, key=score), history


def optimal_value(items, capacity):
    best = [0] * (capacity + 1)
    for _, weight, value in items:
        for c in range(capacity, weight - 1, -1):
            best[c] = max(best[c], best[c - weight] + value)
    return best[capacity]
