#Script to scrape 'http://coreyms.com' \'s articles' titles, summaries and youtube links, then write them to a csv file

#Import the necessary modules
from bs4 import BeautifulSoup
import requests, csv

#Get a text version of the requested website source code
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('bs4_tutorial.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

article = soup.find('article')
# print(article.prettify())

#Single article (the first/most recent one)
'''
#get the tile of an article
headline = article.h2.a.text
print(headline,'\n')

#get the summary/description of an article
summary = article.find('div', class_ ='entry-content').p.text
print(summary,'\n')

#get the video id of a video of an article
#get the embeded video url from the source code
vid_src = article.find('iframe', class_='youtube-player')['src']
# print(vid_src, '\n')
#then obtain just the video id
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

#now form the complete youtuble link for the video
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
'''

for article in soup.find_all('article'):
    try:
        #Get the tile of an article
        headline = article.h2.a.text
        # print(f'Headline:\n{headline}')

        #Get the summary/description of an article
        summary = article.find('div', class_ ='entry-content').p.text
        # print(f'Summary:\n{summary}')

        #Get the video id of a video of an article
        #Get the embeded video url from the source code
        vid_src = article.find('iframe', class_='youtube-player')['src']
        #Then obtain just the video id
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        #Now form the complete youtuble link for the video
        yt_link = f'https://youtube.com/watch?v={vid_id}'
        # print(f'Video link:\n{yt_link}')
    
    except expression as identifier:
        pass
        #We could, for example, still print out the error or do something else with it, but for this /
        #specific case we'll just pass if an exception is raised
        #e.g. let's say we knew some articles won't have a youtube link embeded. then we could do this:
        '''
        yt_link = 'No video link available'
        #then it would print the above string as 'yt_link'
        '''

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()