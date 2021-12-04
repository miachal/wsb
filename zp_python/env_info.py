from os import cpu_count
from platform import release, processor, system,\
    python_implementation, python_version
from sys import version as interpreter_version


class EnvInfo():
    def __init__(self):
        self._info = [
            ('Python version', python_version()),
            ('Interpreter', python_implementation()),
            ('Interpreter version', interpreter_version),
            ('Operating system', system()),
            ('Operating system version', release()),
            ('Processor', processor()),
            ('CPUs', cpu_count())
        ]

    def show(self):
        for key, value in self._info:
            print(f'{key}: {value}')

    def _transform(self, str):
        return '_'.join(str.split(' ')).lower()

    def get(self, property):
        for key, value in self._info:
            if property == self._transform(key):
                return value

    def get_as_html(self):
        return '<br />'.join([
            ' '.join([f'{key}:', str(value)]) for key, value in self._info
        ])


if __name__ == '__main__':
    env = EnvInfo()
    env.show()

    print(env.get_as_html())

    cpu = env.get('cpus')
    print(cpu)
