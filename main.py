#degiskenler 

baslik = "HABERİNİZ OLSUN"  #string
vade = 12  #integer
faizOrani1 = 1.47  #float
faizOrani2 = 1.44
faizOrani = 1.47

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldiniz"
musteriAdi = "Aleyna"
musteriSoyadi = "Kaya"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!"

print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)

print(sonucMesaj)


#sartBloklari 

dolarDun = 7.78
dolarBugun = 7.95

if dolarDun < dolarBugun :
    print("Artis Oku")
elif dolarDun > dolarBugun : 
    print("Azalis Oku")
else:
    print("ESittir Oku")

#if dolarDun < dolarBugun:
#print("Azalış Oku")

#if dolarDun == dolarBugun:
#print("Eşittir Oku")

print("Bitti")



#listeler 

krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi"]

print(krediler)

print(krediler[0])
print(krediler[1])
print(krediler[2])

print(len(krediler)) #lenght

krediler[0] = "Çabuk kredi"

print(krediler)



#donguler 

krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi"]


#alias
for kredi in krediler:
  print("<option>"+kredi+"<option>")

for i in range(len(krediler)):
   print(krediler[i])
   
for i in range(3,10):
  print(i)

for i in range(0,11,2):
  print(i)

#fonksiyonlar 

def kredileriListele():
  krediler = ["Hızlı kredi" , "Maaşını Halkbank'tan alanlara özel" , "Mutlu emekli ihtiyaç kredisi"]
  for kredi in krediler:
    print("<option>"+kredi+"<option>")


kredileriListele()
kredileriListele();
kredileriListele();
kredileriListele();
kredileriListele();

