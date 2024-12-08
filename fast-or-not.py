import timeit
def normal_loop():
    x = []
    for i in range(1_000_000):
        x.append(i**2)
    return x

def list_comprehension():
    return [i**2 for i in range(1_000)]
#execution_time = timeit.timeit("normal_loop()", number=10) 
execution_time = timeit.timeit("normal_loop()", globals=globals(), number=1_000_000)
print(f"Execution time: {execution_time} seconds")

## Results

## via 🐍 v3.10.5 on
❯ python how-fast.py
Execution time: 2.261008583009243 seconds

##via 🐍 v3.12.0 
❯ python how-fast.py
Execution time: 0.6567025419790298 seconds
