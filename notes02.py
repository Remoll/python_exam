# 1. Typy niemutowalne:
# - str
# - int
# - float
# - bool
# - None
# - bytes
# - tuple jeśli zawiera tylko niemutowalne elementy
# - frozenset
# Dla nich to zwykle nie robi różnicy, bo i tak nie da się ich zmienić „w miejscu”. Wygląda to jak kopia wartości, ale technicznie nadal są to te same obiekty.

# 2. Typy mutowalne:
# - list
# - dict
# - set
# - większość własnych klas / obiektów
# Dla nich w kopii zostaje ta sama referencja, więc zmiana w środku będzie widoczna w obu listach.