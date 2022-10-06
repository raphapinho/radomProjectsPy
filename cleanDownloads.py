import os

files = []

for dirname, dirnames, filenames in os.walk("../../Downloads"):
    for filename in filenames:
        files.append(os.path.join(dirname,filename))

for i in range(len(files)):
    print(f"Removendo o arquivo: {files[i]} \n")
    os.remove(files[i])