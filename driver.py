from core.LinearSystemEquationSolution import IterationSolution
A = [
    [8.3, 2.1, -1.2, 0.5],
    [0.8, 10.2, 3.5, -1.8],
    [1.2, 0.2, -4, -0.5],
    [-0.2, 0.3, 0.4, -2]
]

b = [-3.02, 4.79, -6.72, 8.89]

# ji = JacobiIteration(A, b)
# ji.solve(0.001)

slt = IterationSolution(A, b)
slt.solve(0.001, method='sor', relax_factor=1.25)

