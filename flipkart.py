from urllib import urlopen as ureq
from bs4 import BeautifulSoup as soup

#file opening and writing
flip_file = "flip_mob.csv"
headers = "Product,Price,Rating \n"
f = open(flip_file, "w")
f.write(headers)

#extracting the datas
for i in range(1,2):
 page = ureq("https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.serviceability%5B%5D%3Dfalse%22%29%5C&page="+str(i))
 page_soup = soup(page, "html.parser")

 division = page_soup.find_all("div",{"class":'_1UoZlX'})


 for tit in division:
  title_all = tit.find("div",{"class" :'_3BTv9X'})
  title = title_all.img["alt"]
  rate_all =  tit.find("div",{"class":'hGSR34'})
  rating = rate_all.get_text()	
  price_all = tit.find("div",{"class":'_1vC4OE _2rQ-NK'})
  price = price_all.text[1:10]
  
  print("Product:" + title )
  print("Price:" + price )
  print("Rating:" + rating )

  f.write(title.replace(",","|") + ";" +price.replace(",","") + ";" + rating +"\n")


f.close()

