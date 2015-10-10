import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36 QQBrowser/9.1.4060.400')

    response = urllib.request.urlopen(req)
    html = response.read()
    return html
    
def get_page(url):
    
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    print(html[a:b])
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a,a+255)

        if b!= -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a+9
        a = html.find('img src=',b)

    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
def download_mm(folder = 'D:\\Mm',page=30):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://www.jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(page):
        page_num -= 1
        page_url = url+'page-'+str(page_num)+'#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()
'''
proxy_support = urllib.request.ProxyHandler({'http':'118.168.106.233:80'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.69 Safari/537.36 QQBrowser/9.1.4060.400')]
urllib.request.install_opener(opener)

response = opener.open(url)

html = response.read().decode('utf-8')

print(html)
'''
