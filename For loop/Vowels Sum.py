# text = "SoftUni"
# length = len(text)
# print(length)
#
# text = "SoftUni"
# letter = text[4]
# print(letter)

# text = input()
#
# length = len(text)
#
# for symbol in length:
#     if symbol ==
#
#
# length = input()
# for i in range(0, le)

# length = input()
# for i in range(0,len(length)):
#     print(length[i])


# Въвеждаш текста и натискаш ентер,започва да итерира и първо прочита символа в инедкс 0,демек h,но директно ти изписва че буквата/символа е h.
# След това го държи,държи на него и започва да влиза в проверките.Ако има съвпадение,присвоява съответната стойност към стойността
# на променливата total.След което отново влиза в цикъла и отново започва да итерира през
# текста.Следващия индекс е 1,а буквата е "е",ако има съвпадение,събира стойността и със стойността на total.
# И така докато обходи/мине през всички инедкси/символи на текста. Накрая отпечатва резултата.
# from datetime import datetime
# startTime = datetime.now()
#
# text = input()
# total = 0
#
# for iterator in text:
#     if iterator == "a":
#         total += 1
#     elif iterator == "e":
#         total += 2
#     elif iterator == "i":
#         total += 3
#     elif iterator == "o":
#         total += 4
#     elif iterator == "u":
#         total += 5
#
# print(total)
#
# print(datetime.now() - startTime)



#ЗА индекс във обхват,от нулев индекс до крайния инедкс през дължината на целия текст,итерирай:
#АКО индекса който си прочел по време на този цикъл е еднакъв на символа "а",
#Тогава стойността на променливана е равна на досегашната и плюс едно.
#така обхожда/итерира целия текст и търси има ли символ "а",ако има увеличава сумата с 1.
#по този начин итерира през целия текст и "изважда" символите "а",и ги събира.
#когато думата свърши,цикъла свършва също и се принтира резултата.
#Ако има за търсене друга буква,то тогава ще търси и за нея и ще добавя еквивалентната и стойност в сумата.

# Въвеждаш текста и натискаш ентер,започва да итерира и първо прочита символа в инедкс 0,демек h,но директно ти изписва 0.
# След това го държи,държи на него и започва да влиза в проверките.Ако има съвпадение,присвоява съответната стойност към стойността
# на променливата total.След което отново влиза в цикъла и отново започва да итерира през текста.
# Следващия индекс е 1,а буквата е "е",ако има съвпадение,събира стойността и със стойността на total.
# И така докато обходи/мине през всички инедкси/символи на текста. Накрая отпечатва резултата.

from datetime import datetime
startTime = datetime.now()
text = input()
summ = 0

for iterator in range(0, len(text)):
    if text[iterator] == "a":
        summ += 1
    elif text[iterator] == "e":
        summ += 2
    elif text[iterator] == "i":
        summ += 3
    elif text[iterator] == "o":
        summ += 4
    elif text[iterator] == "u":
        summ += 5
print(summ)
print(datetime.now() - startTime)

# Разликата между двата кода е че при първия ти изписва директо буквата която е във индекса на който е в момента.
# Докато при втория код,ти изписва номера на индекса в който се намира,демек 0,1,2,3... и т.н. и сравнява стойността на този индекс,демек каква буква съдържа той,
# със буквите във всяка една проверка поотделно.
# Разликите: при първия вариант кода работи по-бавно в сравнение с втория вариант. Първи:0:00:04.244 / Втори: 0:00:03.923
# при първия вариант сложността на синтаксиса е по-малка,тоест кода е по-прост за писане.Но е по-труден за интерпретиране от микропроцесора на компютъра,
# затова се изпълнява и по-бавно.
