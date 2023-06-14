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


def convert_data(input_file_path, output_file_path):
    file_extension = input_file_path.split('.')[-1].lower()

    if file_extension == 'json':
        data = read_json(input_file_path)
        write_json(output_file_path, data)
    elif file_extension in ['yml', 'yaml']:
        data = read_yaml(input_file_path)
        write_yaml(output_file_path, data)
    elif file_extension == 'xml':
        root = read_xml(input_file_path)
        write_xml(output_file_path, root)
    else:
        print(f"Unsupported file format: {file_extension}")
        return

    print(f"Data converted successfully. Saved to {output_file_path}")


if __name__ == '__main__':
    args = parse_arguments()
    convert_data(args.input_file, args.output_file)
