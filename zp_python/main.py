from statistics import median

from utils import styles, numbers, transposition
from env_info import EnvInfo
from calc_machine import CalcMachine
from html_builder import HTMLBuilder

REPEATS = 5


def f(n):
    suma = 0
    for i in range(1, n+1):
        suma += (n - i) * i
    return suma


env = EnvInfo()

cm = CalcMachine(f, numbers)
one_thread = cm.measure_execution_time(cm.calc_multithreading, 1, REPEATS)
four_threads = cm.measure_execution_time(cm.calc_multithreading, 4, REPEATS)
four_cpus = cm.measure_execution_time(cm.calc_multiprocessing, 4, REPEATS)
max_cpus = cm.measure_execution_time(
    cm.calc_multiprocessing,
    env.get('cpus'),
    REPEATS
)

one_thread_median = median(one_thread)
four_threads_median = median(four_threads)
four_cpus_median = median(four_cpus)
max_cpus_median = median(max_cpus)


title = 'Multithreading/Multiprocessing benchmark results'

html = HTMLBuilder('report', title, styles)

html.add_section(('h1', title))
html.add_section(('h2', 'Execution environment'), env.get_as_html())

html.add_section(
    ('h2', 'Test results'),
    'The following table shows detailed test results:'
)
executions = [j for j in range(1, REPEATS+1)]
table_header = [
    'Execution',
    '1 thread (s)',
    '4 threads (s)',
    '4 processes (s)',
    'processes based on number of CPUs (s)'
]
results_table = transposition([
    executions,
    one_thread,
    four_threads,
    four_cpus,
    max_cpus
])
html.add_table([table_header] + results_table)

html.add_section(
    ('h2', 'Summary'),
    'The following table shows the median of all results:'
)
medians_table = transposition([
    ['Median:'],
    [one_thread_median],
    [four_threads_median],
    [four_cpus_median],
    [max_cpus_median]
])
html.add_table([table_header] + medians_table)

html.add_tag('p', 'App author: miachal')

html.save()
