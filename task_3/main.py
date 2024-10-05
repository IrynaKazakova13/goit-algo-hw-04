import sys
from pathlib import Path
from colorama import Fore

path = sys.argv[1]

p = Path(path)

def parse_folder(path):
    if path.exists():
        for el in path.iterdir():
            if el.is_dir():
                print(Fore.GREEN + f"This is a folder - {el.name}")
            if el.is_file():
                print(Fore.BLUE + f"This is a file - {el.name}")
    else:
        print(f"The specified path {path} doesn't exist")                

parse_folder(p)

#python3 task_3/main.py ./task_2 -> выведет список файлов и папок директории task_2

#python3 task_3/main.py ./task_5 -> реализует блок "else" и выведет сообщение об "ошибке"