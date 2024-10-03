from pathlib import Path
         
def total_salary(path): 
    """Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати. Функція приймає один аргумент - шлях до текстового файлу"""
    try:
        salary = list() 
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:
                salary.append(line.split(',')[1])
        """Оголошуємо змінну salary, яка є списком, построково накопичує інформацію про зарплату співробітників, попередньо очищену від прізвищ та імен"""
    
        salary_int = [int(x) for x in salary]
        """Перетворення формату з рядка на цілі числа"""
    
        total = round(sum(salary_int))
        """Розрахунок загальної суми зарплати працівників"""
           
        average = round(sum(salary_int) / len(salary_int))   
        """Розрахунок середньої суми зарплати працівників"""

        result = (total, average)
        print(result)
        return result
        """Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати"""
    
    except Exception as e:
        print(f'(e) with file')

total, average = total_salary('./task_1/salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")   