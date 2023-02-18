import requests , bs4 , os 

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print(f"downloading page {url}")
    res = res.get(url)
    res.raise_for_status()

    soup  = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("there is no commic image anymore")

    else:
        commicUrl = comicElem[0].get('src')
        print(f'downloading image {commicUrl}')
        res.get(commicUrl)
        res.raise_for_status()
    file  = open((os.path.join('xkcd',os.path.basename(commicUrl)),'wb'))
    for chunk in res.iter_content(1000):
        file.write(chunk)
    file.close()


    prev = soup.select('a[rel="prev"]=')[0]
    url  = 'http://xkcd.com'+prev.get('href')
    

print('done')