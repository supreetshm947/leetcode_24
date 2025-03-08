def coloredCells(n: int) -> int:
    return 1 + 4*((n-1)*n//2)

print(coloredCells(3))