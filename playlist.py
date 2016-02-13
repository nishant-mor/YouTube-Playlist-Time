import requests
from bs4 import BeautifulSoup

def play(url):

		source_code = requests.get(url)   # source code of page
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text , "html.parser")
		soup.encode('UTF-8')
		h , m , s = 0 , 0 , 0;
		count = 0
		for link in soup.findAll('div' , {'class' : 'timestamp'} ):     
 
			count+=1
			time = link.string.split(':')
			if len(time)==3:
				h+= int(time[0])
				m+= int(time[1])
				s+=int(time[2])
			else:
				m+= int(time[0])
				s+= int(time[1])

		ts = h*60*60 + m*60 + s
		m, s = divmod(ts, 60)
		h, m = divmod(m, 60)
		d, h = divmod(h ,24)

		print("Total Videos : " , count)
		print(d , "Days" , h , "Hours" , m , "Minutes" , s , "Seconds")


if __name__ == "__main__":
	
	'''
	url example :  'https://www.youtube.com/playlist?list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy'
	'''

	url = input("Enter Url:   ")
	play(url)


