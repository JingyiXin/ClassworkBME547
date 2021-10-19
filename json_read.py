import json


def input_json(filename):
    #'r' means read the file filename
    in_file = open(filename, 'r')
    #load in_file into new var
    new_variable = json.load(in_file)
    in_file.close()
    return new_variable


if __name__ == "__main__":
    #filename = "patient.json"
    filename = "my_booleans.json"
    x = input_json(filename)
    print(x)
    print(type(x))