import sys
import re
from math import *

def main():
    if len(sys.argv) != 3:
        print('Wrong arguments: first argument must be path to input XML!')
        print('Wrong arguments: second argument must be output path for XML!')
        return

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    f = open(in_path, 'r')
    data = f.read()
    f.close()

    mappings = {}

    for index in range(20):
        mappings['theta' + str(index) + '\[t\]'] = 'angles(' +  str(index) + ')'
        mappings['Derivative\[1\]\[theta' + str(index) + '\]\[t\]'] = 'anglesD(' +  str(index) + ')'
        mappings['Derivative\[2\]\[theta' + str(index) + '\]\[t\]'] = 'anglesDD(' +  str(index) + ')'

    mappings['\n'] = ';'
    mappings['\{'] = ''
    mappings['\}'] = ''
    mappings['Sin'] = 'sin'
    mappings['Cos'] = 'cos'
    mappings['Sqrt'] = 'sqrt'
    mappings['\['] = '('
    mappings['\]'] = ')'

    for regex, replace in mappings.items():
        data = re.sub(regex, replace, data)

    f = open(out_path, 'w')
    f.write('[' + data + ']')
    f.close()

if __name__ == '__main__':
    main()