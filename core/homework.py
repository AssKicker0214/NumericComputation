import math

from core.LinearSystemEquationSolution import IterationSolution
from core.NonLinearEquationSolution import SteffensenIteration
from core.NonLinearEquationSolution import NewtonIteration


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


def page_229_question_6_1():
    # steffensen iterative function
    print("\n ########## steffensen 算法 ##########")
    def fi(x):
        return (2.0 - math.e ** x + x ** 2) / 3

    si = SteffensenIteration(fi)
    si.solve(6, absolute_error_limit=0.00000001, stop_when_met='absolute')

    # newton function
    print("\n ########## newton 算法 ##########")
    def f(x):
        return (2.0 - math.e ** x + x ** 2) / 3 - x

    def df(x):
        return (1.0 / 3) * (-1 * math.e ** x + 2 * x) - 1

    ni = NewtonIteration(f, df)
    ni.solve(6, absolute_error_limit=0.00000001, stop_when_met='absolute')


def page_229_question_6_2():
    # steffensen
    print("\n ########## steffensen 算法 ##########")
    def fi(x):
        return math.acos((x ** 2) / -10.0)

    si = SteffensenIteration(fi)
    si.solve(2, absolute_error_limit=0.00000001, stop_when_met='absolute')

    print("\n ########## newton 算法 ##########")
    def f(x):
        return x ** 2 + 10 * math.cos(x)

    def df(x):
        return 2 * x - 10 * math.sin(x)

    ni = NewtonIteration(f, df)
    ni.solve(2, absolute_error_limit=0.00000001, stop_when_met='absolute')

# 以下是题目对应的程序运行入口
page_193_question_6()
page_194_question_9()
page_229_question_6_1()
page_229_question_6_2()
