def compute_approximation():
    for i in range(10000, 100001, 10000):
        result = 0
        for j in range(1, i + 1):
            result += ((-1) ** (j + 1)) / (2 * j - 1)
        approximation = 4 * result
        print(f"i = {i}: Approximation = {approximation}")

compute_approximation()
