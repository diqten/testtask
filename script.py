import os
import pandas as pd

roots = []
dir = []
file = []

for root, dirs, files in os.walk("."):
    for filename in files:
        root = root.split('\\')
        root = root[-1]
        if root == ".":
            root = "testtask"
        type = filename.find(".")
        roots.append(root)
        dir.append(filename[:type])
        if type < 0:
            file.append(" ")
        else:
            file.append(filename[type:])


df = pd.DataFrame({'Папка с файлами': roots,
                   'Название файлов': dir,
                   'Расширение файлов': file })

df.to_excel('./result.xlsx')