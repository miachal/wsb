numbers = [
    15972490,
    80247910,
    92031257,
    75940266,
    97986012,
    87599664,
    75231321,
    11138524,
    68870499,
    11872796,
    79132533,
    40649382,
    63886074,
    53146293,
    36914087,
    62770938,
]

styles = '''
body {
  font-size: 10pt;
}

h2 {
  padding-top: 10pt;
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
  table-layout: fixed ;
}

td, th {
  border: 2px solid #b9b9b9;
  padding: 10px;
  text-align: center;
  width: 25% ;
}

th {
  background-color: #d5d5d5;
}

td {
}

tr:nth-child(odd) {
  background-color: #eeeeee;
}
'''


def transposition(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
