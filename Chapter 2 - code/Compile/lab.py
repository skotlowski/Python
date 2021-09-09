import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []
for i in range(1000000):
    argument_list.append(i/10)

results_list = []

for formula in formulas_list:
    start = time.time()
    [exec(formula) for x in argument_list]
    stop = time.time()
    not_compiled_result = stop - start
    print(f"Time of NOT COMPILED source: {not_compiled_result}")

    start = time.time()
    compiled = compile(formula, 'internal code source', 'exec')
    [exec(compiled) for x in argument_list]
    stop = time.time()
    compiled_result = stop-start
    print(f"Time of COMPILED source: {compiled_result}",
          f"It's {not_compiled_result/compiled_result} times faster ")
