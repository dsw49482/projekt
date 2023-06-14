import argparse
import json
import xml.etree.ElementTree as ET
import yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)')
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
    return parser.parse_args()

def read_json(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data

def write_json(output_file, data):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def read_yaml(input_file):
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(output_file, data):
    with open(output_file, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def read_xml(input_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    return root

def write_xml(output_file, root):
    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

def convert_xml_to_json(root):
    data = {}
    for child in root:
        if child:
            data[child.tag] = child.text.strip()
    return data

def convert_json_to_xml(data):
    root = ET.Element('root')
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return root

def convert_yaml_to_xml(data):
    root = ET.Element('root')
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return root

def main():
    args = parse_arguments()

    # Rozpoznawanie formatu pliku na podstawie rozszerzenia
    input_format = args.input_file.split('.')[-1].lower()
    output_format = args.output_file.split('.')[-1].lower()

    if input_format == 'json':
        data = read_json(args.input_file)
    elif input_format == 'yaml' or input_format == 'yml':
        data = read_yaml(args.input_file)
    elif input_format == 'xml':
        root = read_xml(args.input_file)
    else:
        print(f'Nieobsługiwany format pliku wejściowego: {input_format}')
        return

    if output_format == 'json':
        if input_format == 'xml':
            # Konwersja danych z XML do JSON
            data = convert_xml_to_json(root)
        write_json(args.output_file, data)
    elif output_format == 'yaml' or output_format == 'yml':
        if input_format == 'xml':
            # Konwersja danych z XML do YAML
            data = convert_xml_to_json(root)
            data = yaml.dump(data)
        write_yaml(args.output_file, data)
    elif output_format == 'xml':
        if input_format == 'json':
            # Konwersja danych z JSON do XML
            root = convert_json_to_xml(data)
        elif input_format == 'yaml' or input_format == 'yml':
            # Konwersja danych z YAML do XML
            root = convert_yaml_to_xml(data)
        write_xml(args.output_file, root)
    else:
        print(f'Nieobsługiwany format pliku wyjściowego: {output_format}')

if __name__ == '__main__':
    main()
