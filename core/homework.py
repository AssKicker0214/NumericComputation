import numpy as np
from numpy import linalg as LA

from core.IterationSolution import IterationSolution


def page_193_question_6():
    A = [
        [8.3, 2.1, -1.2, 0.5],
        [0.8, 10.2, 3.5, -1.8],
        [1.2, 0.2, -4, -0.5],
        [-0.2, 0.3, 0.4, -2]
    ]

    b = [-3.02, 4.79, -6.72, 8.89]
    slt = IterationSolution(A, b)
    slt.solve(absolute_error_limit=0.001, stop_when='absolute', method='jacobi')
    slt.solve(absolute_error_limit=0.001, stop_when='absolute', method='seidel')


def page_194_question_9():
    A = [
        [5, 2, 1],
        [-1, 4, 1],
        [2, -3, -4]
    ]

    b = [5.2, -6.2, -4.9]

    slt = IterationSolution(A, b)
    slt.solve(absolute_error_limit=0.01, stop_when='absolute', method='sor', relax_factor=1.25)


# page_193_question_6()
# page_194_question_9()
