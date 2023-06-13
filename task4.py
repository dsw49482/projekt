import argparse
import yaml

parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)')
parser.add_argument('--input', help='Ścieżka pliku wejściowego')
args = parser.parse_args()

input_path = args.input

try:
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
        print('Dane zostały wczytane poprawnie.')
        print('Wczytane dane:', data)
except FileNotFoundError:
    print(f'Plik o ścieżce {input_path} nie istnieje.')
except yaml.YAMLError as e:
    print(f'Błąd podczas wczytywania danych YAML: {e}')
