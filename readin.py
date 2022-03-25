import argparse

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+')

yaml_files = parser.parse_args().files
for fi in yaml_files:
    print(fi)