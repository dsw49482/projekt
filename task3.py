import argparse
import json

# Task 3: Zapis danych z obiektu do pliku w formacie JSON
parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty .xml, .json i .yml (.yaml)')
parser.add_argument('--input', help='Ścieżka pliku wejściowego')
parser.add_argument('--output', help='Ścieżka pliku wyjściowego')
args = parser.parse_args()

input_path = args.input
output_path = args.output

try:
    with open(input_path, 'r') as file:
        data = json.load(file)
        print('Dane zostały wczytane poprawnie.')
        print('Wczytane dane:', data)
except FileNotFoundError:
    print(f'Plik o ścieżce {input_path} nie istnieje.')
except json.JSONDecodeError as e:
    print(f'Błąd podczas wczytywania danych JSON: {e}')
else:
    try:
        with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f'Dane zostały zapisane do pliku {output_path} w formacie JSON.')
    except IOError:
        print(f'Błąd podczas zapisu danych do pliku {output_path}.')
