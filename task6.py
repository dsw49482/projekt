import argparse
import xml.etree.ElementTree as ET

# Task 6: Wczytywanie danych z pliku XML i weryfikacja poprawności składni pliku
parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)')
parser.add_argument('--input', help='Ścieżka pliku wejściowego')
args = parser.parse_args()

input_path = args.input

try:
    tree = ET.parse(input_path)
    root = tree.getroot()
    print('Dane zostały wczytane poprawnie.')
    print('Wczytane dane:', root)
except FileNotFoundError:
    print(f'Plik o ścieżce {input_path} nie istnieje.')
except ET.ParseError as e:
    print(f'Błąd podczas wczytywania danych XML: {e}')
