import numpy as np

def write_data_to_file(file_path, data):
    with open(file_path, 'w') as f:
        for item in data:
            if isinstance(item, np.ndarray):
                f.write("np.array(" + str(item.tolist()) + ")\n")
            else:
                f.write(str(item) + "\n")

if __name__ == '__main__':
    origiN = [0.,0.,0.]
    descR = ['local',53,7.25]
    struT = [[5.3,6.2,3.141592653589793],[2.718281828459045,17.,1.618033988749895]]
    ordeR = np.array([[4,2],[8,3]])
    tagS = np.array([45.328043,-57.3217607])

    data = [origiN, descR, struT, ordeR, tagS]
    write_data_to_file('intermediate_file.txt', data)
