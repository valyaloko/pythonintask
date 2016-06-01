# Задача 5. Вариант 48.
# Напишите программу, которая бы при запуске случайным образом отображала
# название одного из восьми категорий, на которые разделяются дорожные знаки в
# соответствии с Венской конвенцией о дорожных знаках и сигналах.

# Vinogradova J. 
# 31.03.2016

import random

print("Программа случайным образом отображает название одну из восьми категорий, на которые разделяются дорожные знаки в соответствии с Венской конвенцией о дорожных знаках и сигналах.")

name = random.randint(1,3)

print('\nОдна из восьми категорий, на которые разделяются дорожные знаки '+"-", end=' ')

if name == 1 :
    print('Предупреждающие знаки.')
elif name == 2 :
    print('Знаки преимущественного права проезда.')
elif name == 3 :
    print('Запрещающие и ограничивающие знаки.')
elif name == 4 :
    print('Предписывающие знаки.')
elif name == 5 :
    print('Знаки особых предписаний.')
elif name == 6 :
    print('Информационные знаки.')
elif name == 7 :
    print('Указатели направлений.')  
else :
    print('Дополнительные таблички.')


input("\n\nНажмите Enter для выхода.")