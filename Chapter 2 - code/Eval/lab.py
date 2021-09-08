import math

argument_list = [x/10 for x in range(0, 100)]

formula = '2*x'
[print(eval(formula)) for x in argument_list]

formula = 'math.sin(x)'
[print(eval(formula)) for x in argument_list]

formula = '3*x**2+2*x-4'
[print(eval(formula)) for x in argument_list]
