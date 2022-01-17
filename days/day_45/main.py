from bs4 import BeautifulSoup
import requests

# with open(file="website.html", mode="r") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# all_a = soup.find_all(name="a")
#
# for tag in all_a:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading, heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading, section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
#
# name = soup.select_one(selector="#name")
# print(name.getText())
#
# headings = soup.select(selector=".heading")
# print(headings)

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")
story_texts = []
story_links = []

stories = soup.find_all(name="a", class_="titlelink")
for story in stories:
    story_text = story.getText()
    story_texts.append(story_text)
    story_link = story.get("href")
    story_links.append(story_link)

story_upvotes = [int(upvote.getText().split(" ")[0]) for upvote in soup.find_all(name="span", class_="score")]

print(len(story_texts), len(story_links), len(story_upvotes))

print(story_texts)
print(story_links)
print(story_upvotes)

max_index = story_upvotes.index(max(story_upvotes))
print(story_texts[max_index], story_links[max_index])
