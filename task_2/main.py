from pathlib import Path
         
def get_cats_info(path): 
    """Функція приймає один аргумент - шлях до текстового файлу. Функція має точно обробляти дані та повертати правильний список словників"""
    try:
        cats_dict = list()
        """Оголошуємо змінну cats_dict, яка є списком і збиратиме інформацію про всіх котів у вигляді індивідуальних словників"""
        
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_dict = dict()
                cat_dict["id"] = line.split(',')[0]
                cat_dict["name"] = line.split(',')[1]
                cat_dict["age"] = line.split(',')[2]
                cats_dict.append(cat_dict)
        
        """Оголошуємо змінну cat_dict, яка є словником, построково накопичує інформацію про одного кота за допомогою ключів "id", "name", "age" та і додається до загального списку"""
        
        return cats_dict
        """Функція повертає список словників, де кожен словник містить інформацію про одного кота""" 

    except Exception as e:
        print(f'{e} with file')

cats_info = get_cats_info("./task_2/cats_info.txt")
print(cats_info)
