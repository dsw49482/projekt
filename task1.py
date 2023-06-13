import argparse

# Task 1: Parsowanie argumentów przekazywanych przy uruchomieniu programu
parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)')
parser.add_argument('--input', help='Ścieżka pliku wejściowego')
parser.add_argument('--output', help='Ścieżka pliku wyjściowego')
parser.add_argument('--format', choices=['xml', 'json', 'yaml'], help='Format pliku wejściowego (xml, json, yaml)')
args = parser.parse_args()

input_path = args.input
output_path = args.output
input_format = args.format

print(f'Ścieżka pliku wejściowego: {input_path}')
print(f'Ścieżka pliku wyjściowego: {output_path}')
print(f'Format pliku wejściowego: {input_format}')
