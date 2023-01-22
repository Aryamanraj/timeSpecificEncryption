from itertools import combinations

def bounding_box_count(n, x, y):
    count = 0
    for i in range(1, n+1):
        for subset in combinations(range(n), i):
            min_x = min(x[j] for j in subset)
            max_x = max(x[j] for j in subset)
            min_y = min(y[j] for j in subset)
            max_y = max(y[j] for j in subset)
            if (max_x - min_x) * (max_y - min_y) > 0:
                count += 1
    return count
