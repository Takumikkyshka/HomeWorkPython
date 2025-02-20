# 1 Пользователь вводит строку в консоль. Проверить, является ли данная строка палиндромом. Палиндром — это строка, которая читается одинаково слева направо и справа налево.
"""
word = input()
newword = ""
for lastletter in range(len(word) -1, -1, -1):
    newword += word[lastletter]
if word == newword:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
"""

# 2 Задание 2. Извлечь каждую цифру из трехзначного числа. Ввод: 751, вывод: сотни - 7, десятки - 5, единицы - 1
"""
num = input("Введите трехзначное число ")
sotni = num[0]
desyat = num[1]
odin = num[2]
print(f"Сотни - {sotni} Десятки - {desyat} Единицы - {odin}")
"""

# 3 Даны списки а и b. Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
"""
spisok1 = [4,6,1,2,14,5,12,6]
spisok2 = [6,1,51,6,14,5,12,122]
def poisk(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return False
def newspisok(spisok1, spisok2):
    newarr = []
    for i in range(0, len(spisok1)):
        povtor = poisk(spisok2, spisok1[i])
        if povtor != False:
            newarr.append(spisok2.pop(povtor))
    return newarr
print(newspisok(spisok1, spisok2))
"""

# 4 На входе имеем список строк разной длины. Необходимо код, которая создаст новый список из строк одинаковой длины. Длину итоговой строки определяем исходя из самой большой из них. Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов. Расположение элементов начального списка не менять.
"""
spisokstrok = ["Denislox", "Chtotoeshe", "NovayaStroka", "Ya"]
def newstr(spisokstrok):
    max_length = max(len(s) for s in spisokstrok)
    new_strings = []
    for s in spisokstrok:
        count = max_length - len(s)
        new_string = s + "_" * count
        new_strings.append(new_string)
    
    return new_strings
print(newstr(spisokstrok))
"""

#5 Вася хочет узнать, какую четвертную оценку по информатике он получит. Учитель придержтвается следующей системы оценки учащихся: вычисляется среднее арифметическое оценок за четверть и итогом становится округленное значение. При этом, если есть двойка, а следующая оценка за ней - не двойка, то двойка в подсчете не учитывается. Вводятся несколько чисел через запятую - оценки Васи. Необходимо вывести итоговую оценку за четверть.
"""
def calculateFinalGrade(grades_input):
    grades = list(map(int, grades_input.split(',')))
    final_grades = []
    for i in range(len(grades)):
        if grades[i] == 2:
            if i + 1 < len(grades) and grades[i + 1] != 2:
                continue
        final_grades.append(grades[i])
    if final_grades:
        average_grade = sum(final_grades) / len(final_grades)
        final_grade = round(average_grade)
    return final_grade
grades_input = input("Введите оценки через запятую: ")
print(f"Итоговая оценка за четверть {calculateFinalGrade(grades_input)}")
"""

# 6 Реализуйте программу-викторину, в которой пользователь может отвечать на вопросы по различным темам. Создайте список вопросов и ответов, затем используйте циклы и условные операторы для проверки правильности ответа.
"""
def quiz():
    questions = {
        "Как называется столица Франции?": "Париж",
        "Сколько планет в Солнечной системе?": "Восемь",
        "Как называется жидкость, заполняющая глазное яблоко?": "Слеза",
        "Помидор это овощ или ягода?": "Ягода"
    }

    score = 0

    print("Добро пожаловать в викторину! Ответьте на следующие вопросы:\n")

    for question, correct_answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. Правильный ответ: {correct_answer}.\n")
    print(f"\nВы ответили правильно на {score} из {len(questions)} вопросов.")

quiz()
"""

# 7 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так, как в словаре ниже. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские буквы.
"""
def Scrabble(word):
    points = {
        1: 'AEIOULNSTR',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JZ',
        10: 'QX'
    }
    
    score_map = {}
    for score, letters in points.items():
        for letter in letters:
            score_map[letter] = score

    total_score = 0
    for letter in word.upper():  
        if letter in score_map:
            total_score += score_map[letter]

    return total_score

user_word = input("Введите слово: ")
word_score = Scrabble(user_word)
print(f"Стоимость слова '{user_word}': {word_score} очков.")
"""

# 8 Напишите программу, которая будет создавать список из двух по следующему примеру: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
"""
def merge_lists(list1, list2):
    merged_list = []
    min_length = min(len(list1), len(list2))
    
    for i in range(min_length):
        merged_list.append(list1[i])
        merged_list.append(list2[i])
    
    if len(list1) > min_length:
        merged_list.extend(list1[min_length:]) # extend добавляет все выделенные элементы в конец массива
    elif len(list2) > min_length:
        merged_list.extend(list2[min_length:])

    return merged_list

list1 = [1, 2, 3]
list2 = [11, 22, 33]
result = merge_lists(list1, list2)
print(result) 
"""

# 9 Задание 9. Пользвоатель вводит 2 числа - индексы списка. Выведите список, который не содержит элементов по этим индексам.Дан список: [1, 44, 7, 9, 3, 2, 1, 44]Ввод: 0, 4Результат: [44, 7, 9, 2, 1, 44]
"""
def removeElByIndex(original_list, index1, index2):
    indexes = sorted([index1, index2], reverse=True)
    
    for index in indexes:
        del original_list[index]
    
    return original_list

# Исходный список
my_list = [1, 44, 7, 9, 3, 2, 1, 44]

input_index = input("Введите два индекса, разделенные запятой: ")
index1, index2 = map(int, input_index.split(','))
result_list = removeElByIndex(my_list, index1, index2)
print("Результат:", result_list)
"""

# 10 Пользователь вводит число. Вывести количество нулей в конце числа.18534290000 -> 3 ??????????? 6532036235001 -> 0 15 -> 0
"""
def Zeros(number):
    number_str = str(number)
    
    count = 0
    for digit in reversed(number_str): #reversed переворачивает массив 
        if digit == '0':
            count += 1
        else:
            break

    return count

# Запрашиваем ввод числа у пользователя
user_input = input("Введите число: ")
result = Zeros(user_input)

print("Количество нулей в конце числа:", result)
"""

# 11 Дан список. Пользователь вводит число. Вывести ближайшее число к введенному из списка[17, 4, 7, 10, 11, 12], 9 == 10 [17, 4, 7, 10, 11, 12], 8 == 7
"""
def Nearest_Number(arr, target):
    target = int(target)
    nearest = arr[0]
    min_diff = abs(nearest - target) 

    for i in arr:
        diff = abs(i - target)
        if diff < min_diff: 
            min_diff = diff
            nearest = i 
            
    return nearest

arr = [17, 4, 7, 10, 11, 12]
user_inp = input("Введите число: ")
print(Nearest_Number(arr, user_inp))
"""

# 12 Пользователем вводится строка, а затем 2 символа - ограничения. Напечатать в консоль строку, которая находтся между ограничений."What is >apple<", ">", "<" == "apple""[an apple]", "[", "]" == "an apple"
"""
str = input("Введите строку: ")
limitation1 = input("Введите первое ограничение: ")
limitation2 = input("Введите второе ограничение: ")

start_index = str.index(limitation1)
end_index = str.index(limitation2)

print(str[start_index + 1 : end_index])
"""

# CodeWars ex1 kyu6
"""
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list () that are present in the second list (). The order of elements in the first list should be preserved in the result.ab

Examples
If and , the result should be .a = [1, 2]b = [1][2]

If and , the result should be .a = [1, 2, 2, 2, 3]b = [2][1, 3]
"""
# Code
"""
def array_diff(a, b):
    c = []
    for el in a:
        if el not in b:
            c.append(el)
    return c
"""
# CodeWars ex2  kyu6
"""
Define a function that takes an integer argument and returns a logical value or depending on if the integer is a prime.truefalse

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than that has no positive divisors other than and itself.11

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or ).0
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to , or , will be too slow.nn/2
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""

# Code

"""
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
"""

# Codewars ex3 kyu7
"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata isn't considered a vowel.y
"""

# ^_^ Code ^_^

"""
def disemvowel(s):
    newstr = ""
    count = 0
    for el in s:
        if el == "a":
            continue
        elif el == "A":
            continue
        elif el == "E":
            continue
        elif el == "e":
            continue
        elif el == "O":
            continue
        elif el == "o":
            continue
        elif el == "U":
            continue
        elif el == "u":
            continue
        elif el == "I":
            continue
        elif el == "i":
            continue
        else:
            newstr += el
    return newstr
"""
