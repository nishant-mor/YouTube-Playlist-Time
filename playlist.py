import requests
from bs4 import BeautifulSoup

def comment():

		url = 'https://www.youtube.com/playlist?list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy'
		source_code = requests.get(url)   # source code of page
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		soup.encode('UTF-8')
		h , m , s = 0 , 0 , 0;

		for link in soup.findAll('div' , {'class' : 'timestamp'} ):      # a = find all links of the titles 
			#href = link.get('href')     # pulling links of this class
			         # here string is for <href = "something"...> Titlesndjsnd </href>   then it is Titlesndjsnd 
			time = link.string.split(':')
			if len(time)==3:
				h+= int(time[0])
				m+= int(time[1])
				s+=int(time[2])
			else:
				m+= int(time[0])
				s+= int(time[1])

		#print(h , m , s)
			

		ns = s//60
		nm = (ns+m)//60

		h+=nm
		d=h//24
		nh = nm%24 
		nm = (m+ns)%60
		ns = s%60

		#print(time , nh , nm , ns)
		print(d , "Days" , nh , "Hours" , nm , "Minutes" , ns , "Seconds")
# 			print(time , nh , nm , ns)



comment()