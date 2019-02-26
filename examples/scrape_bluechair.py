from requests import get
from bs4 import BeautifulSoup

def scrape_bluechair ():
	'''
	Scrape the URL and title of the latest Bluechair web comic.

	Parameters
	----------
	None

	Returns
	-------
	list
		A two-item list where the first is the comic's URL and the second its
		title.
	'''
	target = get("https://www.webtoons.com/en/comedy/bluechair/list?title_no=199")
	soup = BeautifulSoup(target.content, "html5lib")
	# All the comics (of the first page) are located inside a <div> with a class\
	# `detail_lst`
	comics_list = soup.find("div", class_="detail_lst")

	# Both the title and the comic's URL are, in the context of previous <div>,\
	# located inside the first <ul>, then inside the first <li> (since we want the\
	# most recent comic), then inside the first <a>

	# Inside that <a> element, the title is in the <span> with a class `subj`
	comic_title = comics_list.ul.li.a.find("span", class_="subj").span.text.strip()
	# The title is the value of the <a>'s `href` attribute
	comic_url = comics_list.ul.li.a["href"]

	return [comic_url, comic_title]


latest_comic = scrape_bluechair()
print(f'The latest Bluechair web comic is called "{latest_comic[1]}" which can be read at {latest_comic[0]} ')