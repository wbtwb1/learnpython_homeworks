"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
from collections import Counter  
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('/Users/vladlenakoroleva/projects/referat.txt', 'r', encoding = 'utf-8') as f:
        content = f.read()
        count= Counter(content)
        print(len(content))
        print(count)
        words = content.split()
        words_num =(len(words))
        print(words_num)
        print(content.replace (".", "!"))

if __name__ == "__main__":
    main()
