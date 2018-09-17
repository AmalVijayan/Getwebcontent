import requests
from bs4 import BeautifulSoup as bs
import os


# url to get the images from
url = "https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1317&bih=620&ei=J9afW9KrKsqNvQSixanIDw&q=lions&oq=lions&gs_l=img.3..0l5j0i10k1j0l3j0i10k1.3573.4901.0.5823.7.6.0.1.1.0.194.627.0j4.4.0....0...1ac.1.64.img..2.5.631.0...0.Xo6nV8m1HzA"


# download the webpage in the above url for parsing

page = requests.get(url)
soup = bs(page.text,'html.parser')

# locate all elements with img tag

image_tags = soup.findAll('img')

# create a new directory to download the images from the webpage
if not os.path.exists('image_dir'):
    os.makedirs('image_dir')


# Move to new dir

os.chdir('image_dir')

# image filename variable

x = 0

# writing images

for image in image_tags : 
    try: 
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('image-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x =x+1
    except:
        pass
