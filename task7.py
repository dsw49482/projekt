import argparse
import xml.etree.ElementTree as ET

# Task 7: Zapis danych do pliku XML
parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)')
parser.add_argument('--input', help='Ścieżka pliku wejściowego')
parser.add_argument('--output', help='Ścieżka pliku wyjściowego')
args = parser.parse_args()

input_path = args.input
output_path = args.output

try:
    tree = ET.parse(input_path)
    root = tree.getroot()
    print('Dane zostały wczytane poprawnie.')

    tree.write(output_path)
    print(f'Dane zostały zapisane do pliku: {output_path}')
except FileNotFoundError:
    print(f'Plik o ścieżce {input_path} nie istnieje.')
except ET.ParseError as e:
    print(f'Błąd podczas wczytywania danych XML: {e}')
