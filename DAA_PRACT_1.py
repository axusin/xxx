import timeit

def fibonaci(n):
    for i in range(2, n+1):
        fib_list[i]=fib_list[i-1]+fib_list[i-2]
    return fib_list[n]

def fibonaci_recursive(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fib_recur_list[n]=fibonaci_recursive(n-1)+fibonaci_recursive(n-2)
    return fib_recur_list[n]

N=20
RUNS=1000
print(f"Given N = {N}\n{RUNS} runs")

fib_list=[0]*(N+1)
fib_list[0]=0
fib_list[1]=1
time=timeit.timeit("fibonaci(N)", setup=f"from __main__ import fibonaci;N={N}", number=RUNS)

print("Fibonacci non-recursive: ", fibonaci(N), "\tTime : ", f'{timeit.timeit("fibonaci(N)", setup=f"from __main__ import fibonaci;N={N}",number=RUNS):5f}',"O(n)\tSpace :O(1)")
print("Fibonacci non-recursive: ", fibonaci(N), "\tTime : ", f'{time:5f}',"O(n)\tSpace :O(1)")

# print("Fibonaci non-recursive ", fibonaci(N), "Time : ", time, "O(n) Space : O(1)")
fib_recur_list=[0]*(N+1)
fib_recur_list[0]=0
fib_recur_list[1]=1
print(
    "fibonaci recursive: \t",
    fibonaci_recursive(N),
    "\tTime:",
    f'{timeit.timeit("fibonaci_recursive(N)", setup=f"from __main__ import fibonaci_recursive; N={N}", number=RUNS, ):5f}',
    "O(2^n)\tSpace: O(n)"
)
