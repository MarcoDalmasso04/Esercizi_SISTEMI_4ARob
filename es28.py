import math

quadratiPerfetti = [n for n in range(1001) if math.sqrt(n) % 1 == 0]
print(quadratiPerfetti)