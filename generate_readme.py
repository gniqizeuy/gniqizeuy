import sys
import requests
import random

URL = "https://raw.githubusercontent.com/limhenry/earthview/master/earthview.json"

README = """
![{title}]({image_src})

*[{title}]({wiki_link})*
"""


def fetch_image():
    """
    return image url, and image title.
    """
    print("download image...")

    array = requests.get(URL).json()

    info = array[random.randint(0,len(array))]

    country = info['country']
    
    image = info["image"]

    map = info['map']

    return map, country, image



relative_link, title, image_src = fetch_image()

with open("README.md", "r") as old_readme:
    if title in old_readme.read():
        print("Todays featured image not change!")
        sys.exit()

new_readme = README.format(
    title=title,
    image_src=image_src,
    wiki_link=relative_link,
)

print("new readme file generate... save...")
with open("README.md", "w+") as f:
    f.write(new_readme)
