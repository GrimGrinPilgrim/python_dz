def pirosiki_orig():
  with open("lesson1/pirosiki.txt",  encoding='utf-8') as infile:
    pir_list= infile.readlines()
  return pir_list

def res():
  new_list = []
  with open("lesson1/pirosiki.txt",  encoding='utf-8') as infile:
    for line in infile:
      if line[0] !="x":
        new_list.append(line)
    return new_list

def listImg():
  with open("lesson1/img.txt",  encoding='utf-8') as infile:
    pir_listImg = infile.readlines()
  return pir_listImg

def img(word,allpirozoki):
  for x in allpirozoki:
    if x == word:
      i = allpirozoki.index(x)
  return i

def add_pir(word):
  with open("lesson1/pirosiki.txt", "a",  encoding='utf-8') as outfile:
    outfile.write(word + "\n")

def add_img(word):
  with open("lesson1/img.txt", "a",  encoding='utf-8') as outfile:
    outfile.write(word + "\n")

def ready(number):
  
  with open("lesson1/pirosiki.txt", encoding='utf-8') as file:

    pir_readylist = file.readlines()
    oldlist = res()
    item=oldlist.index(""+pir_readylist[number]+"")
    readiimg(item)
    a = "x "+pir_readylist[number][0:] 
    pir_readylist[number]=pir_readylist[number].replace(pir_readylist[number],a)
    new_pir(pir_readylist)

def readiimg(number):
   with open("lesson1/img.txt", encoding='utf-8') as file:
     pir_readylistImg = file.readlines()
     pir_readylistImg.remove(pir_readylistImg[number])
     new_imgpir(pir_readylistImg)

def new_pir(list):
  with open("lesson1/pirosiki.txt", "w",  encoding='utf-8') as outfile:
    for y in list:
      outfile.write(y)

def new_imgpir(list):  
  with open("lesson1/img.txt", "w",  encoding='utf-8') as outfile:
    for y in list:
      outfile.write(y)

# +По адресу / сервис показывает содержимое файла с пирожками, но только тех его строк, которые не начинаются с "x ". (Файл с пирожками содержит по одному пирожку на строку).
# +У страницы с пирожками есть красивая шапка с рисунком пирожка и к ней приделан стиль в отдельном файле. (Так как я не дизайнер, мне хватит, чтобы в стиле было сказано ul { border: solid 1px black; boder-radius: 5px; }).
# +По адресу /all видны все пирожки. Сделайте на странице ссылки, чтобы можно было переключаться между двумя видами.
# +Сервис предоставляет поле ввода и кнопочку "добавить пирожок", по нажатию на которую в файл с пирожками дописывается ещё один пирожок.
# Около каждого пирожка есть кнопка "готов". По нажатию на эту кнопку на адрес /done/<номер> отправляется запрос. По его получении программа читает файл с пирожками построчно, к строке с номером номер приписывает в начало "x ", и записывает в файл с пирожками все пирожки.