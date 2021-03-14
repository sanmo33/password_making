import string
import random
import pyperclip
import sys

up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
digits = string.digits

length = random.randint(5,7)
secret_pass = ''

#making password
for i in range(length):
    secret_pass += random.choice(up_letters)
    secret_pass += random.choice(low_letters)
    secret_pass += random.choice(digits)

secret_pass = ''.join(random.sample(secret_pass, len(secret_pass)))

#コマンドラインからサイト名をsite_nameへ入れる
site_name = sys.argv[-1]

#pass_listにサイト名とpasswordを書き込む
with open('pass_list.txt', mode='a') as f:
    f.write(site_name + '\n')
    f.write(secret_pass+ '\n')
    f.write('\n')

pyperclip.copy(secret_pass)