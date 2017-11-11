import numpy as np
from numpy import linalg as LA


class JacobiException(Exception):
    pass


class JacobiIteration:
    def __init__(self, A, b):
        self.m = np.array(A, np.float64)
        shape = self.m.shape
        self.n = shape[0]
        self.b = np.array(b, np.float64).reshape(self.n, 1)

    def print(self):
        print(self.m)

    def solve(self, error_limit, init_solution=None):
        B = np.copy(self.m)
        b = np.copy(self.b)
        print("原始")
        print(B)
        print(b)
        print()

        i = 0
        for row in B:
            bii = row[i] + 0.0
            if bii == 0:
                raise JacobiException("element (%d,%d) equals to 0, cannot use jacobi" % (i, i))
            else:
                for j in range(0, len(row)):
                    row[j] = (-1.0 * row[j] / bii) if j != i else 0.0
                b[i, 0] /= bii

            i += 1

        if init_solution is None:
            init_solution = np.array([0 for i in range(self.n)])
            init_solution = init_solution.reshape(self.n, 1)

        print("迭代矩阵")
        print(B)
        print()
        print(b)

        x = init_solution
        stop = False
        itr_cnt = 0
        while not stop:
            print("迭代 %d" % itr_cnt)
            print(x)
            itr_cnt += 1
            new_x = B.dot(x) + b
            error = LA.norm(x - new_x, np.inf)
            print("绝对误差 "+str(error))
            if error < error_limit:
                stop = True
            else:
                x = new_x
            print()
