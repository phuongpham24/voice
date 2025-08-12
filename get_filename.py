import os
from ultis.ultis import *

ultis = Ultis()

files = os.listdir("./data/wav-data")

for file in files:
    file_name = ultis.get_file_info(file=file)
    print(file_name)