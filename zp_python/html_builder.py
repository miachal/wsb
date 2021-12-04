class HTMLBuilder():
    def __init__(self, report_name, title, styles):
        self._report_name = report_name
        self._title = title
        self._styles = styles
        self._elements = []

    def _tag(self, tag, ctx):
        return f'<{tag}>{ctx}</{tag}>'

    def add_section(self, title, ctx=''):
        self._elements.append(f'{self._tag(title[0], title[1])}<p>{ctx}</p>')

    def add_table(self, data):
        table = ['<table>', '<tr>']
        header = data[0]
        for field in header:
            table.append(f'<th>{field}</th>')
        table.append('</th>')
        rows = data[1:]
        for row in rows:
            table.append('<tr>')
            for field in row:
                table.append(f'<td>{field}</td>')
            table.append('</tr>')
        table.append('</table>')
        self._elements.append(''.join(table))

    def add_tag(self, tag, ctx):
        self._elements.append(self._tag(tag, ctx))

    def _headers(self):
        return ''.join([
            '<head>',
            self._tag('title', self._title),
            self._tag('style', self._styles),
            '</head>'
        ])

    def _body(self):
        return f'<body>{"".join(self._elements)}</body>'

    def save(self):
        with open(f'{self._report_name}.html', 'w') as file:
            file.write('<!doctype html><html>')
            file.write(self._headers())
            file.write(self._body())
            file.write('</html>')


if __name__ == '__main__':
    from utils import styles

    html = HTMLBuilder('test_report', 'test', styles)

    html.add_section(('h1', 'Test section'))
    html.add_section(('h2', 'Test section'), 'paragraph')

    table = [['A', 'B', 'C'], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    html.add_table(table)

    html.add_tag('p', 'Bziuuuum')
    html.add_tag('b', 'io, io, io')

    html.save()
