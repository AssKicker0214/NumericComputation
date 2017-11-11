class SteffensenIteration:
    def __init__(self, iterate_function):
        self.iterate_function = iterate_function

    def solve(self, init_x, absolute_error_limit=0.0001, relative_error_limit=None, stop_when_met='absolute',
              max=10000):
        stop = False
        k = 0
        x = float(init_x)
        while not stop:
            x1 = self.iterate_function(x)
            x2 = self.iterate_function(x1)
            x3 = x2 - ((x2 - x1) ** 2 / (x2 - 2 * x1 + x))

            met_absolute_error_limit = abs(x3 - x) < absolute_error_limit if absolute_error_limit is not None else False
            met_relative_error_limit = abs(
                (x3 - x) / x3) < relative_error_limit if relative_error_limit is not None else False

            if stop_when_met == 'absolute' and met_absolute_error_limit:
                stop = True
            elif stop_when_met == 'relative' and met_relative_error_limit:
                stop = True
            elif stop_when_met == 'either' and (met_absolute_error_limit or met_relative_error_limit):
                stop = True
            elif stop_when_met == 'both' and met_relative_error_limit and met_absolute_error_limit:
                stop = True
            elif k > max:
                stop = True
                print("达到最大迭代限制")

            k += 1
            print("迭代%d" % k)
            print("x = %.10f" % x3)
            if met_absolute_error_limit is not None:
                print("absolute error limit = %.10f" % abs(x3 - x))

            if met_relative_error_limit is not None:
                print("relative error limit = %.10f" % abs((x3 - x) / x3))
            print()

            x = x3
        return x


class NewtonIteration:
    def __init__(self, function, derivative_function):
        self.f = function
        self.df = derivative_function

    def solve(self, init_x, absolute_error_limit=0.0001, relative_error_limit=None, stop_when_met='absolute',
              max=10000):
        stop = False
        x = float(init_x)
        k = 0
        while not stop:
            new_x = x - (self.f(x) / self.df(x))
            met_absolute_error_limit = abs(
                new_x - x) < absolute_error_limit if absolute_error_limit is not None else False
            met_relative_error_limit = abs(
                (new_x - x) / new_x) < relative_error_limit if relative_error_limit is not None else False

            if stop_when_met == 'absolute' and met_absolute_error_limit:
                stop = True
            elif stop_when_met == 'relative' and met_relative_error_limit:
                stop = True
            elif stop_when_met == 'either' and (met_absolute_error_limit or met_relative_error_limit):
                stop = True
            elif stop_when_met == 'both' and met_relative_error_limit and met_absolute_error_limit:
                stop = True
            elif k > max:
                stop = True
                print("达到最大迭代限制")

            k += 1
            print("迭代%d" % k)
            print("x = %.10f" % new_x)
            if met_absolute_error_limit is not None:
                print("absolute error limit = %.10f" % abs(new_x - x))

            if met_relative_error_limit is not None:
                print("relative error limit = %.10f" % abs((new_x - x) / new_x))
            print()

            x = new_x

        return x

