import time
from sys import exit
from main import *

options = {
    'keyword': '',
    'maxVideoCount': 0,
    'maxVideoLen': 0,
    'createPlaylist': True,
    'startFrom': 0,
}

print('Lütfen ders çizelgenizin oluşturulması için gelecek sorulara tek tek cevap verin.')
time.sleep(2)
for kw in options.keys():
    choice = input(kw + ' :\t')
    options[kw] = choice 

print(options)
if input('Veriler alındı, onaylıyor musunuz?').lower() == 'evet':
    startTime = time.time()
    print('Sunucuya videoların aranıp biçimlendirilmesi için istek gönderildi, bekleyiniz.')
    find_suitable_videos(options=options)
    endTime = time.time()
    print('Dosya oluşturuldu. Geçen süre ', startTime - endTime, ' sn')
    pass
else:
    print('İşlem iptal edildi.')
    exit()