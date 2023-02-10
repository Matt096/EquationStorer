import numpy as np

def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("np.array("):
                line = line.strip().replace("np.array(", "").replace(")", "")
                data.append(np.array(eval(line)))
            else:
                data.append(eval(line))
    return data

if __name__ == '__main__':
    data = read_data_from_file('intermediate_file.txt')
    origiN, descR, struT, ordeR, tagS = data
    print(origiN)
    print(descR)
    print(struT)
    print(ordeR)
    print(tagS)
