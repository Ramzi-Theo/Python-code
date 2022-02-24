import json
file = 'final_students.txt'
dict1 = []
with open(file) as file1:
    for line in file1:
        dict2 = {}
        information = list(line.strip().split(','))
        for lines in information:
            information1 = lines.strip().split(':')
            dict2[information1[0]] = information1[1]
        dict1.append(dict2)
out_file = open("final_students.json", "w")
json.dump(dict1, out_file, indent=2)
out_file.close()