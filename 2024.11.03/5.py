a = input()
one_word = 30

message = a.replace(" ","")
total = len(message) * one_word
     
rub = total//100
kop = total%100

print(f"{rub} руб. {kop} коп.")

#грузите апельсины бочках братья карамазовы
#11 руб. 40 коп.