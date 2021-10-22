import configparser


def return_standard_structure(standard_file):
    config = configparser.ConfigParser()
    with open(standard_file) as f:
        config.read_file(f)

    return config