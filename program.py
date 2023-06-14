import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import subprocess

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych')
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

def read_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data

def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml_file(file_path):
    with open(file_path) as file:
        data = yaml.safe_load(file)
    return data

def write_yaml_file(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def read_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
   
    data = {}
    return data

def write_xml_file(data, file_path):
    pass

def convert_data(input_file, output_file):
    if input_file.endswith('.json'):
        data = read_json_file(input_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        data = read_yaml_file(input_file)
    elif input_file.endswith('.xml'):
        data = read_xml_file(input_file)
    else:
        raise ValueError('Nieobsługiwany format pliku wejściowego')

    if output_file.endswith('.json'):
        write_json_file(data, output_file)
    elif output_file.endswith('.yaml') or output_file.endswith('.yml'):
        write_yaml_file(data, output_file)
    elif output_file.endswith('.xml'):
        write_xml_file(data, output_file)
    else:
        raise ValueError('Nieobsługiwany format pliku wyjściowego')

def main():
    args = parse_arguments()
    convert_data(args.input_file, args.output_file)

    # Wywołanie polecenia pyinstaller
    subprocess.run(['pyinstaller', '--onefile', 'program.py'])

if __name__ == '__main__':
    main()
