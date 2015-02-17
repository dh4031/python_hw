from bs4 import BeautifulSoup

soup = BeautifulSoup(open("634.html"))

div_id = soup
column = div_id.find_all(id="secondary-nav")

for nav in column:
	nav = nav.find("p", class_="subnavlinks")
	names = p.a
	print names.string
