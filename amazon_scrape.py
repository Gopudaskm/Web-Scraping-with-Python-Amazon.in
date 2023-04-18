import requests
import lxml
from bs4 import BeautifulSoup
import json
import csv
import datetime
import time
headers = {
    'authority': 'www.amazon.in',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.6',
    'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

products=[]

def get_data(url):
    response = requests.get(url,headers=headers)
    product_dict={}
    product_soup=BeautifulSoup(response.text,'lxml')
    temp_title=product_soup.find('span',{'id':'productTitle'}).text.strip()
    if "(" in temp_title:
        ind=temp_title.index("(")
        title=temp_title[:ind].strip()
    else:
        title=temp_title
    centercolalign=product_soup.find('div',{'class':'centerColAlign'})
    mrp=centercolalign.find('span',{'class':'a-price a-text-price'})
    savings=centercolalign.find('span',{'class':'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'})
    price=centercolalign.find('span',{'class':'a-price-whole'})
    product_dict['Title']=title
    if mrp:
        product_dict['MRP(Rs.)']=mrp.find_all('span')[0].text.strip().replace(',','').replace('₹','')
    else:
        product_dict['MRP(Rs.)']=mrp
    if savings:
        product_dict['Savings(%)']=savings.text.strip().replace(',','').replace('₹','').replace('-','')
    else:
        product_dict['Savings(%)']=savings
    if price:
        product_dict['Price(Rs.)']=price.text.strip().replace(',','').replace('.','')
    else:
        product_dict['Price(Rs.)']=price
    table=product_soup.find('table',{'id':'productDetails_techSpec_section_1'})
    th=table.find_all('th')
    td=table.find_all('td') 
    if len(th)>=5:
        for i in range(len(th)):
            if str(th[i].text.strip())=='Brand':
                product_dict['Brand']=td[i].text.strip().encode('ascii','ignore').decode('utf-8')
            elif str(th[i].text.strip())=='Model':
                product_dict['Model']=td[i].text.strip().encode('ascii','ignore').decode('utf-8')
            elif str(th[i].text.strip()).replace('Weighted ','')=='Annual Energy Consumption':
                product_dict['Annual Energy Consumption']=td[i].text.strip().replace('Weighted ','').encode('ascii','ignore').decode('utf-8')
            elif str(th[i].text.strip())=='Capacity':
                product_dict['Capacity']=td[i].text.strip().replace('Weighted ','').encode('ascii','ignore').decode('utf-8')
    product_dict['Date']=datetime.datetime.now().strftime("%d-%m-%Y")
    product_dict['Link']=url
    products.append(product_dict)
    time.sleep(10)
    print(product_dict)
    print('\n')



def page(page_url):
    response = requests.get(page_url,headers=headers)
    page_soup=BeautifulSoup(response.text,'html.parser')
    products_results=page_soup.find('div',{'class':'s-main-slot s-result-list s-search-results sg-row'})
    products_url=products_results.find_all('a',{'class':'a-link-normal s-no-outline'})
    for j in range(0,len(products_url)):
        if "/sspa/click?" in (products_url[j]['href']):
            continue
        else:
            url="https://amazon.in"+str(products_url[j]['href'])
            print(url)
            print("----------------------------")
            get_data(url)



def scrape(site_url):
    for k in range(10):
        page(site_url)
        response = requests.get(site_url,headers=headers)
        site_soup=BeautifulSoup(response.text,'lxml')
        next_page=site_soup.find('span',{'class':'s-pagination-strip'})
        next_page_url=next_page.findChild('a',{'class':'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})['href']
        site_url='https://www.amazon.in'+str(next_page_url)
        print("===========NEXT PAGE==============")

home_url='https://www.amazon.in/s?i=kitchen&rh=n%3A3474656031&fs=true&ref=sr_pg_1'
scrape(home_url)
# page(home_url)

# with open('Amazon.json','w',encoding='utf-8') as write_file:
#     json.dump(products,write_file,indent=2,ensure_ascii=False)

with open('Amazone_data1.csv', mode='w', newline='',encoding='utf-8') as write_file:
    writer = csv.DictWriter(write_file, fieldnames=['Title', 'MRP(Rs.)', 'Savings(%)','Price(Rs.)','Brand','Model','Capacity','Annual Energy Consumption','Date','Link'])
    writer.writeheader()
    for row in products:
        writer.writerow(row)