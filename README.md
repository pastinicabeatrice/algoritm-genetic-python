# Algoritm genetic - problema rucsacului

Algoritm genetic care alege ce obiecte să iei într-o excursie, astfel încât valoarea totală să fie cât mai mare,
fără să depășești greutatea maximă a rucsacului.

## Cum funcționează

- **cromozom**: o listă de 0 și 1, câte o genă pentru fiecare obiect (1 = obiectul este luat)
- **fitness**: valoarea totală a obiectelor alese, sau 0 dacă rucsacul este prea greu
- **selecție**: turneu între 3 indivizi aleși aleator
- **încrucișare**: într-un punct aleator
- **mutație**: fiecare genă se inversează cu o probabilitate mică
- **elitism**: cei mai buni 2 indivizi trec neschimbați în generația următoare, deci soluția nu se poate înrăutăți

Pentru verificare, rezultatul este comparat cu soluția exactă, calculată prin programare dinamică.

## Rulare

Necesită Python 3.8 sau mai nou, fără alte dependențe.

```
python main.py
python -m unittest
```
