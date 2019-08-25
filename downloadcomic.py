#coding:utf-8

import requests,os,bs4
url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    print('downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text)
    comicelem =soup.select('#comic img')
    if comicelem == []:
        print('could not find comic image.')
    else:
        comicurl = comicelem[0].get('src')
        print('downloading image %s'%(comicurl))
        res = requests.get("http:"+comicurl)
        res.raise_for_status()
        imagefile = open(os.path.join('xkcd',os.path.basename(comicurl)),'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()

    prevlink = soup.select('a[rel= "prev"]')[0]
    url = 'http://xkcd.com' +prevlink.get('href')
print('done')
