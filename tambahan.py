import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  By: Gar2007@Dark Skeleton Team')
print('\t Web : http://darkskeletonteam.site')
print('\t Github : https://github.com/Dark-Skeleton-Team')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!]Menambahkan File Tambahan..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
dst = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
dst.write(key)
dst.close()
sleep(1)
print(a+'[!] PROSES  !')
sleep(1)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^_^'+c+'\n\nDark Skeleton Team\n\n')