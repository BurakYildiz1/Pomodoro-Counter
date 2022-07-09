"""
POMODORO SAYACI
"""
import time 
import pygame

msg="I"
msg1="S"
sayi1=0
print("pomodoro tekniği sayacına hoş geldiniz ...") 
seans = str(input("bilgi almak için 'B' tuşuna, çalışmak istediğiniz seans sayısını ayarlamak için 2 veya 4 tuşlarına basın :"))

if seans == "b" or seans == "B":
    print("""
          pomodoro tekniği genelde 4 seanstan oluşan ve 25 dakikalık seanslara 5 dakika ara ile
          devam edilerek toplamda 2 saat çalışılarak verimliliği arttırmaya yarayan programdır 
          
          bu program ile kendinize uygun olan seans saatini seçerek( 2 veya 4 ) sayacı başlatabilirsiniz
          4 seansdan sonra bir 20 dakikalık mola verilmesi gerekmektedir
          """)
    seans = str(input("seans sayısını giriniz : "))
    
if seans == "2":
    print("sayaç başlatılıyor\nseçilen seans sayısı iki(2) olmak üzere çalışma süresi 1 saattir\naralar 5 dakika ")
  
    while sayi1 < 2 :
        print("ders başladı")
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(msg + '_morse_code.ogg')
        pygame.mixer.music.play()
        time.sleep(25)
        print("ara zamanı")
        pygame.mixer.music.load(msg1 + '_morse_code.ogg')
        pygame.mixer.music.play()
        time.sleep(5)
        sayi1 += 1
    print("çalışma bitti")
    
elif seans == "4":
    print("sayaç başlatılıyor\nseçilen seans sayısı dört(4) olmak üzere çalışma süresi 2 saattir\naralar 5 dakika ")
    while sayi1 < 4 :
        print("ders başladı")
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(msg + '_morse_code.ogg')
        pygame.mixer.music.play()
        time.sleep(25)
        print("ara zamanı")
        pygame.mixer.music.load(msg1 + '_morse_code.ogg')
        pygame.mixer.music.play()
        time.sleep(5)
        sayi1 += 1
    print("çalışma bitti")
    
else:
    print("yanlış harf veya rakam girdiniz lütfen tekrar deneyiniz")
