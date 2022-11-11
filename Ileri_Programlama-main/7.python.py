7.python
'''
liste=[10,20,30]
elemansayisi=len(liste)
print("listenin eleman sayisi:",elemansayisi)
'''
'''
liste=[10,20,30]
for x in liste:
x*2
print(liste)
'''
'''
liste=[10,20,30]
for i in range (0,len(liste)):
liste[i]*=2
'''
'''
#elemana=ile yeni deger atar
liste=[10,20,30,40,50,60]
liste[2]=25
print(liste)
'''
'''
#belirli aralık secilerek deger atar
liste=[10,20,30,40,50,60]
liste[2.5]=[25,26,27]
print(liste)
'''
'''
#+ oparötörü ile yan yana getirip tek dizi haline getirir
liste1=[10,20,30]
liste2=[40,50,60]
liste3=liste1+liste2
print(liste3)
'''
'''
#sonuna yeni eleman eklemek için
liste[10,20,30]
liste.append(40)
print(liste)
'''
'''
#yeni yeleman eklemek için insert kullanılır
liste[10,20,30]
liste.insert(2,25)
print(liste)
'''
'''
#silmek için
liste=[10,20,30]
liste.remove(20)
print(liste)
'''
'''
liste[10,20,30]
del liste[2]
print(liste)
'''
'''
#belirli aralıktaki kodları 
liste=[10,20,30,40,50,60]
del liste[2.5]
print(liste)
'''
'''
#tüm komutu silmek için
liste=[10,20,30]
del liste
print(liste)
'''
'''
#klavyeden girilen sayılarla liste olusturma
liste=[]
 
 elemansayisi=int(input("eleman sayısını girin"))
 toplam=0
 for i in range(0,elemansayisi):
    eleman=int(input("elemanı girin"))
    liste.append(eleman)
    toplam=toplam+eleman
    print("liste=",liste)
    print("elemanların toplamı=",toplam)
    ''' 
    '''
    import random
  

liste=[]
count=0
 

 for i in range(0,100):
   sayi=random.randint(0,100)
    liste.append(sayi)

    
 for i in range(0,10):
    if liste[i]<50:
        count=count+1
print("50'den kucuk eleman sayisi=",count)
print(liste)
'''
    
