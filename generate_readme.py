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

    # content = requests.get(URL).content
    # print(content)
    # html = lxml.html.fromstring(content)
    # presentation_table = html.xpath("//table[@role='presentation']")[0]
    # a_tag = presentation_table.xpath(".//a[@class='image']")[0]
    # relative_link = a_tag.get("href")
    # title = a_tag.get("title")
    # image_src = a_tag.xpath("./img/@srcset")[0]
    # best_image = image_src.split(" ")[0]
    # print(f"{relative_link} {title}, image srcset:{image_src}")
    # print(f"best image: {best_image}")
    # return relative_link, title, "https://" + best_image[2:]
    return map, country, image



relative_link, title, image_src = fetch_image()

with open("readme.md", "r") as old_readme:
    if title in old_readme.read():
        print("Todays featured image not change!")
        sys.exit()

new_readme = README.format(
    title=title,
    image_src=image_src,
    wiki_link=relative_link,
)

print("new readme file generate... save...")
with open("readme.md", "w+") as f:
    f.write(new_readme)
