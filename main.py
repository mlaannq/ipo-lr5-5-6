with open('text.txt', 'r', encoding='utf-8') as infile: #открываем текст док. корректно его читаем и с помощью with автоматически закрывается
    tecst = infile.readlines() #считываем все строки и по отдельности каждую строку сохраняем в список
with open('output.txt', 'w', encoding='utf-8') as outfile: #открываем файл и предоставляем его для записи, после закроется автоматически
    for x in tecst: # проходимся по каждой строке в списке
        pomen= x.replace('о', 'a') #в каждой строке по очереди меняем букву о на а
        outfile.write(pomen) #записываем в файл изменения