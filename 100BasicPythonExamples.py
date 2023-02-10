# *********************************************** #
# *********************GİRİŞ********************* #
# *********************************************** #

# Berkay Kaan Gedikli
# bkgedikli@gmail.com
# https://github.com/bkaan7

from random import randint

# *********************************************** #


# 1 - ilk ornek tabii ki hello world :)

print("hello,world!")

# 2 - kullanici ismi al ve print et

name = "kaan"

print("hello " + name)

# 3 - girilen 2 sayiyi topla

sayi1 = input('1. Sayı : ')
sayi2 = input('2.sayi: ')

print(float(sayi1) + float(sayi2))

# 4 - girilen 2 sayinin ortalamasi

sayi1 = input("sayi1: ")
sayi2 = input("sayi2: ")
ortalama = (int(sayi1) + int(sayi2)) / 2

print("ortamala:{0}".format(ortalama))

# 5 - vize sonucu ortalamasi

vize = input("vize notu: ")
final = input("final notu: ")

ortalama = int(vize) * 0.3 + int(final) * 0.7

print("sınav ortalaman:{0}".format(ortalama))

# 6 - 3 yazili notunun ortalamasini bul

sayi1 = input("sayi1: ")
sayi2 = input("sayi2: ")
sayi3 = input("sayi3: ")

ortalama = (int(sayi1) + int(sayi2) + int(sayi3)) / 3

print("3 sayinin ortalamasi:{0} ".format(ortalama))

# 7 - not sonucuna gore gecti/kaldi 50 > gecti

ogrenci_notu = input("notu giriniz: ")

if (int(ogrenci_notu) >= 50):
    print("geçti")
else:
    print("kaldi")

# 8 - girilen sayi tek mi cift mi?

sayi = input("sayiyi giriniz: ")

if (int(sayi) % 2 == 0):
    print("sayi çift")
else:
    print("sayi tek")

# 9 - girilen sayi negatif / pozitif ya da 0?

sayi = input("sayiyi giriniz: ")

if (int(sayi) > 0):
    print("sayi pozitif")
elif (int(sayi) < 0):
    print("sayi negarif")
else:
    print("sayi sifir")

# 10 - Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız. VKİ 18 ile < 25 aralığındaysa normal, VKİ 25 ile <30 aralığındaysa kilolu, VKİ 30 ve daha yüksekse obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. VKİ’ni hesaplayarak kişinin durumunu yazdırınız.

boy = input("boy giriniz(m): ")
kilo = input("kilo giriniz(kg): ")

vki = int(kilo) / (float(boy) * 2)


if (int(vki) < 18):
    print("zayifsiniz")
elif (18 < float(vki) <= 25):
    print("normalsiniz")
elif (25 < float(vki) <= 30):
    print("kilolusunuz")
elif (30 < float(vki) <= 35):
    print("obezsiniz")
else:
    print("ciddi derecede obezsiniz")

# 11 - Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Gösteren Python Örneği

yas = input("yasinizi giriniz: ")

if (int(yas) >= 18):
    print("ehliyet alabilirsin")
else:
    print("ehliyet alamazsiniz")

# 12 - 1-100 Arası Sayıları Ekranda Listeleyen Python Örneği.

for sayi in range(1, 101):
    print(sayi)

# 13 - 1-100 arasindaki çift sayilari yaziniz.

for sayi in range(1, 101):
    if (sayi % 2 == 0):
        print(sayi)

# 14 - 1-100 Arası Tek Sayıları Listeleyen Python Örneği

for sayi in range(1, 101):
    if (sayi % 2 != 0):
        print(sayi)

# 15 - 1-100 Arası 3′ e ve 5′ e tam bölünen sayılar

for sayi in range(1, 101):
    if (sayi % 3 == 0 and sayi % 5 == 0):
        print(sayi)

# 16 - 1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python Örneği

sayi = input("sayi giriniz: ")

for i in range(1, int(sayi)):
    print(i)

# 17 - Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bulan Python Örneği

uzun = input("uzun kenar(cm): ")
kisa = input("kisa kenar(cm)")

alan = int(kisa) * int(uzun)
cevre = 2 * (int(kisa)+int(uzun))

print(f"dikdörtgenin alanı:{alan} dikdörtgenin çevresi: {cevre}")

# 18 - Girilen metnin harflerini alt alta yazdıran Python Örneği

metin = "kaangedikli"
sayac = 0
while sayac < len(metin):
    print(metin[sayac])
    sayac += 1

# 19 - Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python Örneği.

toplam = 0
sayi1 = input("birinci sayi: ")
sayi2 = input("ikinci sayi: ")

for i in range(int(sayi1)+1, int(sayi2)):
    toplam += i

print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1, sayi2, toplam))

# 20 - 18'i for ile yap

metin = "kaan"

for i in metin:
    print(i)

# 21 -  Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız.

sinema = 1
tiyatro = 2
print("sinema için 1, tiyatro için 2'yi seçiniz.")
secim = input("seçiniz: ")


sinema_price = 15
tiyatro_price = 10
if (int(secim) == 1):
    ogrenci = 15 + 15/2
    yetiskin = 15
    print(f"öğrenci iseniz bilet fiyatı: {ogrenci}, degilseniz {yetiskin}")

else:
    ogrenci = 10 + 10/2
    yetiskin = 10
    print(f"öğrenci iseniz bilet fiyatı: {ogrenci}, yetiskinseniz {yetiskin}")


#  22 - Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python örneği:

maas = input("maasi gir: ")
zam_orani = input("zam orani: ")

yeni_maas = int(maas) + (int(maas) * float(zam_orani)/100)

print(int(yeni_maas))

# 23 -  Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan Python örneği:


def dikdortgenalan(gen, yuk):
    alan = float(gen) * float(yuk)
    print(f"diktörtgenin alanı:{alan}")

    return alan


gen = input("genislik: ")
yuk = input("yukseklik: ")

dikdortgenalan(gen, yuk)

#  24 - Python ile Sayı Tahmin Oyunu Yapımı.


rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında değer girin (0 çıkış):"))
    if (sayi == 0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))

#  25 - Python ile bir liste içinde 5’in katları olan sayıları listeleme.

sayilar = [18, 22, 15, 85, 65, 30, 10, 20, 32, 34, 28, 101, 5, 4, 32]
# bu sayac koyulmasa da olur, sadece listede 5'e bolunen kac sayi oldugunu sayiyor.
sayac = 0
for sayi in sayilar:
    if sayi % 5 == 0:
        print(str(sayi) + (" : 5'in katıdır."))
        sayac = sayac+1
else:
    print('Döngü Bitti')
print("5'in katı olan sayı adeti : "+str(sayac))


# 26 - Bir string içerisinde belirlenen bir karakterin olup olmadığını kontrol eden Python programı kodları. Kontrol etme işlemi fonksiyon içinde yapılmıştır.

def kontrol(str):
    sayac = 0
    for ch in str:
        if ch == 'k':
            sayac = sayac + 1
            return True
            break


metin = input('Metin : ')
if (kontrol(metin) == True):
    print('k karakteri metin içinde var')
else:
    print('k karakteri metin içinde yok')

#  27 - En sevdiğiniz 3 meyveyi liste hâline getirerek ekrana yazdırınız.

meyveler = input("meyve1: "), input("meyve2: "), input("meyve3: ")

print(meyveler)

#  28 - Haftanın günlerinden Pazartesi ile başlayan ve Cuma ile biten bir liste oluşturunuz. Oluşturduğunuz listenin indeksi 4 olan elemanını ekrana yazdırınız.

gunler = ["pazartesi", "sali", "carsamba","persembe", "cuma", "cumartesi", "pazar"]

print(gunler[2])  # carsamba ciktisi verir, index 0'dan baslar unutma!

#  29 - Değerleri sırasıyla 3,1,2 olan listeyi 1,1,2 olarak değiştiriniz.

liste1 = [3, 1, 2]
liste2 = [1, 1, 2]

liste1 = liste2

print(liste1)  # ya da

liste1 = [3, 1, 2]

liste1[0] = 1
liste1[1] = 1
liste1[2] = 2

print(liste1)

# 30 - hafta_ici isimli bir liste oluşturarak haftanın günlerini ekleyiniz. Daha sonra sırasıyla cuma ve cumartesi günlerinin listede olup olmadığını kontrol ediniz.

hafta_ici = ["pazartesi", "sali", "carsamba", "persembe", "cuma"]

print("cuma" in hafta_ici)
print("cumartesi" in hafta_ici)

# 31 - 10-20 arası sayılardan oluşan sayilar isimli bir liste oluşturun. Ardından bu listede bulunan çift sayıları ekrana yazdırınız.

sayilar = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for sayi in sayilar:
    if (sayi % 2 == 0):
        print(sayi)

# 32 - 10-20 arası sayılardan oluşan sayilar isimli bir liste oluşturun. Oluşturulan liste ile sayilar2=[21,22,23,24,25] listesini birleştirerek 4’e tam bölünen sayıları ekrana yazdırınız.

sayilar1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sayilar2 = [21, 22, 23, 24, 25]

yeni_kume = sayilar1 + sayilar2

for sayi in yeni_kume:
    if (sayi % 4 == 0):
        print(sayi)

# 33 - while dongusu ile 1.sınıftan 12.sınıfa kadar yazdir.

i = 1

while i <= 12:
    print(f"{i}. sınıf")
    i += 1

# 34 - Kullanıcının girdiği sayının rakamlarını toplayan python örneği

sayi = input("Bir sayı girin: ")  # str formatında giriş yapar
toplam = 0
for rakam in sayi:
    toplam += int(rakam)

print(f"sayinin rakamlarinin toplami: {toplam}")

#  35 - for döngüsü kullanarak adinizi ekrana yazdirin.

adiniz = input("adinizi girin: ")

for i in adiniz:
    print(adiniz)

#  36 - while dongusu ile kullanici adini 10 defa yazdir.
isim = input("isminizi girin: ")

i = 1
while i <= 10:
    print(f"adiniz: {isim} ")
    i += 1

#  37 - sum() ve len() kullanarak ortalamayı bulma


liste = [10, 20, 30, 40, 50, 60]

toplam = sum(liste)
uzunluk = len(liste)

ort = toplam / uzunluk

print(ort)

# BURAYA KADAR OLAN KISIMDA KAYNAK OLARAK BU WEB ADRESI KULLANILMISTIR:
# https://www.yazilimkodlama.com/programlama/python-ornekleri/

#  38 - mail / parola bilgisi eslestirme

mail = "admin@python.com"
password = 12345

mail_sor = input("mail giriniz: ")
password_sor = input("password giriniz: ")

if (mail == mail_sor and password == int(password_sor)):
    print("giriş başarılı")
else:
    print("bilgileri kontrol ederek tekrar deneyin.")

# 39 - python pizza siparisi

print("python pizza'ya hos geldiniz")

pizza_sec = input("hangi boy olsun? S/M/L olarak giriniz: ")
ekstra_peynir = input("ekstra peynir? E/H: ")
icecek = input("icecek olsun mu? E/H: ")

hesap = 0

if pizza_sec == "S":
    hesap += 20
elif pizza_sec == "M":
    hesap += 25
else:
    hesap += 30

if ekstra_peynir == "E":
    hesap += 2
else:
    hesap +=0

if icecek == "E":
    hesap += 2
else:
    hesap += 0

print(f"odemeniz gereken hesap {hesap} lira!")

# 40 - Bu örneğimizde Python FizzBuzz mülakat sorusu çözülecektir. Öncelikle bu soruyu tanıtalım: Programınız sırayla 1’den 100’e kadar her sayıyı yazdırmalıdır. Sayı 3’e bölündüğünde, (örneğin 3) sayıyı yazdırmak yerine “Fizz” yazmalıdır. Sayı 5’e bölünebiliyorsa, (örneğin 5) sayıyı yazdırmak yerine “Buzz” yazmalıdır.Ve eğer sayı hem 3’e hem de 5’e bölünebiliyorsa, (örneğin 15) sayıyı yazdırmak yerine “FizzBuzz” yazmalıdır.
#  kaynak: https://1kodum.com/python-fizzbuzz-mulakat-sorusu/

for i in range(1,100):
    if i %3 == 0 and i %5 == 0:
        print("FizzBuzz")
    elif i %5 == 0:
        print("Buzz")
    elif i %3 == 0:
        print("Fizz")
    else:
        print(i)

# 41 - yazi mi tura mi?

import random

options = ["yazi", "tura"]
random_choice = random.choice(options)
print(random_choice)

#  42 - for döngüsü ile 1-10 arası sayıları bir listeye yazdır.

numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)

# 43 - Klavyeden başlangıç değeri, bitiş değeri ve artış miktarı girilen sayıları alt alta yazdıran python kodunu yazınız.

ilk_sayi = int(input("ilk sayiyi gir: "))
iki_sayi = int(input("ikinci sayiyi gir: "))

for i in range(ilk_sayi, iki_sayi, 5):#üçüncü değer range aralığını kaçar arttıracağını belirler unutma!
    print(i)

# 44 - Fonksiyonlar için 5 örnek:

def hello_world():
    print("merhaba dünya!")

hello_world()

# 45 - sayilari topla:

def topla(a,b):
    return (a + b)

result = topla(5,6)
print(result)

# 46 - listedeki en buyuk sayi:

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = find_max(numbers)
print(result)

#  47 - stringi ters cevir:

def reverse_string(string):
    return string[::-1]

result = reverse_string("python")
print(result)

# 48 - iki listeyi birlestir:

def combine_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = combine_lists(list1, list2)
print(result)

#  49 - bir ifadede hangi harf kaç defa kullanilmis?

def letter_frequency(word):
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency

result = letter_frequency("berkaykaangedikli")
print(result)

# 50 - bir sayinin karesini alan fonksiyon:

def kare_al(sayi):
    return sayi**2

sonuc = kare_al(5)
print(sonuc)

# 51 - bir listenin uzunluğu?

liste = [1,2,3,4,5]

print(len(liste))

#  52 - bir listedeki tüm sayıların toplami:

liste = [1,2,3,4,5]

print(sum(liste))

# 53 - bir lisedeki min sayi:
liste = [1,2,3,4,5]

print(min(liste))

# 54 - bir listedeki max sayi:

liste = [1,2,3,4,5]

print(max(liste))

# 55 - liste sonuna eleman ekle

liste = [1,2,3,4,5]
liste.append(6)
print(liste)

# 56 - listeden eleman sil

liste = [1,2,3,4,5]
liste.remove(2)
print(liste)

#  57 - listedeki elemanı index ile sil:

liste = [1,2,3,4,5]
liste.pop(2)
print(liste)

#  58 - listeyi boşalt

liste = [1,2,3,4,5]
liste.clear()
print(liste)

#  59 - listeyi sırala

liste = [5,3,1,4,2]
liste.sort()
print(liste)

# 60 - listeyi ters çevir:

liste = [1,2,3,4,5]
liste.reverse()
print(liste)

# 61 - while döngüsü örnekleri:

sayac = 1
while sayac <= 10:
    print(sayac)
    sayac += 1

# 62 - verilen metin kac defa yazilsin?

n = int(input("Kaç kere yazdırılsın: "))
sayac = 0
while sayac < n:
    print("Merhaba")
    sayac += 1

# 63 - faktoryel hesapla

n = int(input("Faktöriyelini hesaplanacak sayı: "))
sonuc = 1
while n > 0:
    sonuc *= n
    n -= 1
print("Sonuç:", sonuc)

# 64 - girilen sayi asal mi?

n = int(input("Sayı: "))
i = 2
while i < n:
    if n % i == 0:
        print(n, "asal değildir.")
        break
    i += 1
else:
    print(n, "asaldır.")

# 65 - girilen sayiya kadar olan cift sayilari yazdir

n = int(input("Sayı: "))
sayac = 0
while sayac <= n:
    if sayac % 2 == 0:
        print(sayac)
    sayac += 1

# 66 - girilen sayiya kadar olan tek sayilari yazdir

n = int(input("Sayı: "))
sayac = 1
while sayac <= n:
    if sayac % 2 != 0:
        print(sayac)
    sayac += 1

#  67 - listedeki sayilari topla

sayilar = [1, 2, 3, 4, 5]
index = 0
toplam = 0
while index < len(sayilar):
    toplam = toplam + sayilar[index]
    index = index + 1
print("Toplam:", toplam)

#  68 - liste elemanlarını yazdir:

sehirler = ["Ankara", "İstanbul", "İzmir", "Adana"]
index = 0
while index < len(sehirler):
    print(sehirler[index])
    index = index + 1

#  69 - liste içinde arama

sehirler = ["ankara", "istanbul", "izmir", "adana"]
aranan = input("aranan eleman nedir?: ")
index = 0
bulundu = False
while index < len(sehirler):
    if sehirler[index] == aranan:
        bulundu = True
        break
    index = index + 1
if bulundu:
    print(aranan, "bulundu.")
else:
    print(aranan, "bulunamadı.")

#  70 - kullanicidan metin al

cumle = ""
while cumle != "çıkış":
    cumle = input("Bir cümle girin (çıkmak için çıkış yazınız): ")
    if cumle != "çıkış":
        print("Girilen cümle:", cumle)

#  71 - kullanici sayi girsin:

while True:
    sayi = int(input("Bir sayı girin(cikis icin 0 girin): "))
    if sayi == 0:
        break
    print("Girilen sayı:", sayi)

#  72 - tuple olusturma:

sehirler = ("Ankara", "İstanbul", "İzmir", "Adana", "Bursa")
print(sehirler)

#  73 - tuple üzerinde elemana erişme:
sehirler = ("Ankara", "İstanbul", "İzmir", "Adana", "Bursa")
print(sehirler[2])

#  74 - Set oluşturma
renkler = {"kırmızı", "yeşil", "mavi", "sarı"}
print(renkler)

# 75 -  Set üzerinde eleman ekleme
renkler.add("pembe")
print(renkler)

# 76 - Set üzerinde eleman silme
renkler.remove("sarı")
print(renkler)

# 77 - Set üzerinde eleman arama
renkler = {"kırmızı", "yeşil", "mavi", "sarı"}
print("kırmızı" in renkler)

# 78 - Set üzerinde eleman sayısı
renkler = {"kırmızı", "yeşil", "mavi", "sarı"}
print(len(renkler))

# 79 - DICTIONARY:

kisiler = {"Ada": 26, "Ahmet": 31, "Mehmet": 41, "Ayşe": 22}
print(kisiler)

# 80 - Dictionary üzerinde eleman ekleme
kisiler = {"Ada": 26, "Ahmet": 31, "Mehmet": 41, "Ayşe": 22}
kisiler["Fatma"] = 33
print(kisiler)

# 81 - Dictionary üzerinde eleman silme
kisiler = {"Ada": 26, "Ahmet": 31, "Mehmet": 41, "Ayşe": 22}
del kisiler["Ahmet"]
print(kisiler)

# 82- Dictionary üzerinde eleman arama
kisiler = {"Ada": 26, "Ahmet": 31, "Mehmet": 41, "Ayşe": 22}
print("Mehmet" in kisiler)

# 83 - Dictionary üzerinde eleman sayısı
kisiler = {"Ada": 26, "Ahmet": 31, "Mehmet": 41, "Ayşe": 22}
print(len(kisiler))

# 84 - F STRING ORNEKLERI: 
# sayilarla islem yapmak
x = 10
y = 20
result = f"{x} + {y} = {x + y}"
print(result)

# 85 - veri tipleri arasında donusum yapmak:

name = "John"
age = 30
result = f"My name is {name} and I am {str(age)} years old."
print(result)

# 86 - matematiksel islem yapmak

pi = 3.14
r = 5
result = f"The area of a circle with radius {r} is {pi * r**2}"
print(result)

# 87 - oncelikli ifadeler kullanmak

language = "Python"
is_popular = True
result = f"{language} is {'' if is_popular else 'not'} popular."
print(result)

# 88 - fonksiyon cagirmak:

def get_greeting(name):
    return f"Hello, {name}!"

result = get_greeting("John")
print(result)

# 89 - listelerle calismak:
names = ["John", "Jane", "Jim"]
result = f"The first three names are: {', '.join(names[:3])}"
print(result)

# 90 - dict ile calismak:
person = {"name": "John", "age": 30, "city": "New York"}
result = f"{person['name']} is {person['age']} years old and lives in {person['city']}."
print(result)

# 91 - buradan sonrasinda sadece fonksiyon ornekleri olacak.
# stringi ters dondur:

def ters_cevir(s):
    return s[::-1]

# Fonksiyonu çağırma
sonuc = ters_cevir("Python")
print(sonuc)

# 92 - stringdeki harfleri sırala:
def harf_sirala(s):
    return ''.join(sorted(s))

# Fonksiyonu çağırma
sonuc = harf_sirala("Python")
print(sonuc)

# 93 - LAMBDA(ANONIM) fonksiyonlar:
# kare alma
square = lambda x: x**2
print(square(5))

# 94 - iki sayinin toplami:
add = lambda x, y: x + y
print(add(5, 10))

# 95 - listenin maks degeri?
find_max = lambda numbers: max(numbers)
print(find_max([1, 2, 3, 4, 5]))

# 96 - stringi ters cevir:
reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))

# 97 - iki sayi arasindaki fark?
difference = lambda x, y: abs(x - y)
print(difference(5, 12))

# 98 - liste içindeki elemanların toplamı?
list_sum = lambda numbers: sum(numbers)
print(list_sum([1, 2, 3, 4, 5])) # 15

#  99 - iki sayinin kucuk olanini bulma

minimum = lambda x, y: x if x < y else y
print(minimum(7, 5)) # 5

# 100 - DOSYA :

# Dosya oluşturma
file = open("sample.txt", "w")
file.write("Hello World")
file.close()

# Dosya okuma
file = open("sample.txt", "r")
content = file.read()
print(content) # Hello World
file.close()

# Dosya ekleme
file = open("sample.txt", "a")
file.write("\nThis is an added line.")
file.close()

# Dosya okuma
file = open("sample.txt", "r")
content = file.read()
print(content) # Hello World\nThis is an added line.
file.close()

# Bu örnekte, ilk olarak bir dosya oluşturduk ve "Hello World" yazdık. Sonra dosyayı okuduk ve içeriğini ekrana yazdırdık. Ardından, dosyaya bir satır daha ekledik ve tekrar okuduk. Dosyaları açtıktan sonra kapatmak için close metodunu kullandık.


# ********************************************* #
# *********************SON********************* #
# ********************************************* #

# Berkay Kaan Gedikli
# bkgedikli@gmail.com
# https://github.com/bkaan7