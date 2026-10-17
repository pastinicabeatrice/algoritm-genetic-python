from genetic import evolve, fitness, optimal_value

CAPACITY = 15

ITEMS = [
    ("cort", 4, 20),
    ("sac de dormit", 3, 15),
    ("apa", 2, 18),
    ("mancare", 3, 17),
    ("lanterna", 1, 8),
    ("trusa medicala", 1, 12),
    ("aragaz", 3, 10),
    ("haine de ploaie", 2, 9),
    ("carte", 1, 2),
    ("aparat foto", 2, 6),
    ("briceag", 1, 7),
    ("harta", 1, 5),
    ("baterie externa", 1, 4),
    ("scaun pliant", 4, 5),
    ("chitara", 5, 3),
]


def main():
    best, history = evolve(ITEMS, CAPACITY)
    print(f"Problema rucsacului: {len(ITEMS)} obiecte, capacitate {CAPACITY} kg\n")
    for generation in range(0, len(history), 10):
        print(f"  generatia {generation:>3}: cea mai buna valoare {history[generation]}")

    chosen = [item for item, gene in zip(ITEMS, best) if gene]
    print(f"\nObiecte alese ({sum(item[1] for item in chosen)} kg):")
    for name, weight, value in chosen:
        print(f"  {name:<16}{weight:>3} kg{value:>5} puncte")
    print(f"\nValoare gasita de algoritmul genetic: {fitness(best, ITEMS, CAPACITY)}")
    print(f"Valoare optima (programare dinamica): {optimal_value(ITEMS, CAPACITY)}")


if __name__ == "__main__":
    main()
