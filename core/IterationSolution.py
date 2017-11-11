import numpy as np
from numpy import linalg as LA


class IterationSolutionException(Exception):
    pass


class IterationSolution:
    def __init__(self, A, b):
        self.m = np.array(A, np.float64)
        shape = self.m.shape
        self.n = shape[0]
        self.b = np.array(b, np.float64).reshape(self.n, 1)

    def print(self):
        print(self.m)

    def jacobi(self, B, b):
        i = 0
        for row in B:
            bii = row[i] + 0.0
            if bii == 0:
                raise IterationSolutionException("element (%d,%d) equals to 0, cannot use jacobi" % (i, i))
            else:
                for j in range(0, len(row)):
                    row[j] = (-1.0 * row[j] / bii) if j != i else 0.0
                b[i, 0] /= bii

            i += 1
        return B, b

    def seidel(self, B, b):
        LD = np.asmatrix(np.copy(B), np.float64)
        R = np.asmatrix(np.copy(B), np.float64)
        i = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                LD[i, j] = 0 if j > i else LD[i, j]
                R[i, j] = R[i, j] if j > i else 0

        B = -1.0 * LD.I.dot(R)
        B = B.A

        b = LD.I.dot(b)
        b = b.A
        return B, b

    def sor(self, B, b, w):
        L = np.asmatrix(np.copy(B), np.float64)
        D = np.asmatrix(np.copy(B), np.float64)
        R = np.asmatrix(np.copy(B), np.float64)
        i = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                L[i, j] = L[i, j] if i > j else 0
                R[i, j] = R[i, j] if j > i else 0
                D[i, j] = D[i, j] if j == i else 0
        B = (D+w*L).I.dot((1-w)*D-w*R)
        B = B.A

        b = (w*(D + w*L).I).dot(b)
        b = b.A
        return B, b

    # stop_when: 'absolute'(default), 'relative', 'either', 'both'
    # init_solution: if None, then it will be fill with 0
    # method: 'jacobi'(default), 'seidel', 'sor'
    # relax_factor: set it when using SOR
    def solve(self, absolute_error_limit=0.001, relative_error_limit=None, stop_when='absolute', init_solution=None,
              method='jacobi', relax_factor=None):
        B = np.copy(self.m)
        b = np.copy(self.b)
        print("原始")
        print(B)
        print(b)
        print()

        if method == 'jacobi':
            B, b = self.jacobi(B, b)
        elif method == 'seidel':
            B, b = self.seidel(B, b)

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
            diff_norm = LA.norm(x - new_x, np.inf)
            new_x_norm = LA.norm(new_x)
            absolute_error_met = diff_norm < absolute_error_limit if absolute_error_limit is not None else False
            relative_error_met = diff_norm / new_x_norm < relative_error_limit if relative_error_limit is not None else False
            if (stop_when == 'absolute' and absolute_error_met) or (stop_when == 'relative' and relative_error_met):
                stop = True
            elif stop_when == 'both' and absolute_error_met and relative_error_met:
                stop = True
            elif stop_when == 'either' and (absolute_error_met or relative_error_met):
                stop = True
            else:
                x = new_x
            print()
        return x
