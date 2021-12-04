from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from timeit import timeit


class CalcMachine:
    def __init__(self, f, data):
        self._f = f
        self._data = data

    def calc_multithreading(self, threads=4):
        with ThreadPoolExecutor(max_workers=threads) as executor:
            results = list(executor.map(self._f, self._data))
        return results

    def calc_multiprocessing(self, processes=4):
        with ProcessPoolExecutor(max_workers=processes) as executor:
            results = list(executor.map(self._f, self._data))
        return results

    @staticmethod
    def measure_execution_time(f, arg, repeat=1):
        times = []
        for j in range(repeat):
            times.append(
                float('{:.3f}'.format(timeit(lambda: f(arg), number=1)))
            )
        return times


if __name__ == '__main__':
    from utils import numbers

    def calc_function(n):
        return n*n*n

    cm = CalcMachine(calc_function, numbers)
    time = cm.measure_execution_time(cm.calc_multiprocessing, 5, 30)
    print('Time: ', time)
