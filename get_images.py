import requests
from bs4 import BeautifulSoup as bs
import os


# url to get the images from
url = "https://www.google.com/search?q=multi+line+comment+in+python&client=ubuntu&hs=Njw&channel=fs&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj5o7vn7b_dAhXVbisKHXxVADEQ_AUIDigB&biw=1317&bih=616"


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
