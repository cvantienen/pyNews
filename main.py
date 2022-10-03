# Cody Vantienen

# importing modules 

from tracemalloc import start
from turtle import done, end_fill
import requests
import bs4
import lxml
from xlsxwriter import Workbook
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')

# ny times

nyTimes = "https://www.nytimes.com/" 
result = requests.get(nyTimes)
soup = bs4.BeautifulSoup(result.text,'html.parser')
soup.prettify()

nyarticle = soup.find_all(["section",'p'])
nystorys = []
    
for nystory in nyarticle:
    cleantext = nystory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    nystorys.append(cleantoken)
    ny_list = []
    for sublist in nystorys:
        for item in sublist:
            ny_list.append(item) 
    done
 
 
    
# Guardian


theGuardian = "https://www.theguardian.com/us" 
gresult = requests.get(theGuardian)
gsoup = bs4.BeautifulSoup(gresult.text,'html.parser')
gsoup.prettify()

guardianArticle = gsoup.find_all(['a','p'])
guardianStorys = []
    
for guardianStory in guardianArticle:
    cleantext = guardianStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    guardianStorys.append(cleantoken)
    g_list = []
    for sublist in guardianStorys:
        for item in sublist:
            g_list.append(item) 
    
    done
    
   
   
    
# huffington post
# <h3 class_="card__headline__text">Racism Seen As Root Of Water Crisis In Mississippi Capital</h3>
# <div class="card__description">The rapper has doubled down on his claims about reading and yet opened a school that runs on a few classes and vibes.</div>

apnews = "https://www.huffpost.com/" 
aresult = requests.get(apnews)
asoup = bs4.BeautifulSoup(aresult.text,'html.parser')
asoup.prettify()

aarticle = asoup.find_all(['h3', 'div'])
astorys = []
    
for astory in aarticle:
    cleantext = astory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    astorys.append(cleantoken)
    hf_list = []
    for sublist in astorys:
        for item in sublist:
            hf_list.append(item)
    done


# the washington post 
reuters = "https://www.washingtonpost.com/" 
rresult = requests.get(reuters)
rsoup = bs4.BeautifulSoup(rresult.text,'html.parser')
rsoup.prettify()

rArticle = rsoup.find_all('span')
rStorys = []
    
for rStory in rArticle:
    cleantext = rStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    rStorys.append(cleantoken)
    r_list = []
    for sublist in rStorys:
        for item in sublist:
            r_list.append(item)
    done


# foxnews 
fox = "https://www.foxnews.com/" 
fresult = requests.get(fox)
fsoup = bs4.BeautifulSoup(fresult.text,'html.parser')
fsoup.prettify()

fArticle = fsoup.find_all('a')
fStorys = []
    
for fStory in fArticle:
    cleantext = fStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    fStorys.append(cleantoken)
    f_list = []
    for sublist in fStorys:
        for item in sublist:
            f_list.append(item)
    done
    

# nbc
# <a href="https://www.nbcnews.com/news/world/ukraine-volodymyr-zelenskyy-izyum-rcna47634" class="related-content__headline-link">Russia launches cruise missiles at Ukraine after Zelenskyy visits recently retaken city</a>
nbc = "https://www.nbcnews.com/" 
nresult = requests.get(nbc)
nsoup = bs4.BeautifulSoup(nresult.text,'html.parser')
nsoup.prettify()

nArticle = nsoup.find_all(['a','span'])
nStorys = []
    
for nStory in nArticle:
    cleantext = nStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    nStorys.append(cleantoken)
    n_list = []
    for sublist in nStorys:
        for item in sublist:
            n_list.append(item)
    done


# abc
# <a href="https://www.nbcnews.com/news/world/ukraine-volodymyr-zelenskyy-izyum-rcna47634" class="related-content__headline-link">Russia launches cruise missiles at Ukraine after Zelenskyy visits recently retaken city</a>
abc = "https://abcnews.go.com/" 
abcresult = requests.get(abc)
abcsoup = bs4.BeautifulSoup(abcresult.text,'html.parser')
abcsoup.prettify()

abcArticle = abcsoup.find_all(['span','a'])
abcStorys = []
    
for abcStory in abcArticle:
    cleantext = abcStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    abcStorys.append(cleantoken)
    abc_list = []
    for sublist in abcStorys:
        for item in sublist:
            abc_list.append(item)
    done
    
    
# npr
# <a href="https://www.npr.org/2022/09/14/1122958027/amazon-union-election-vote-albany" data-metrics="{&quot;action&quot;:&quot;Click Story Title&quot;,&quot;category&quot;:&quot;Story List&quot;}">Amazon warehouse workers in Albany will vote on unionization in October</a>
npr = "https://www.npr.org/" 
nprresult = requests.get(npr)
nprsoup = bs4.BeautifulSoup(nprresult.text,'html.parser')
nprsoup.prettify()

nprArticle = nprsoup.find_all(['a','p'])
nprStorys = []
    
for nprStory in nprArticle:
    cleantext = nprStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    nprStorys.append(cleantoken)
    npr_list = []
    for sublist in nprStorys:
        for item in sublist:
            npr_list.append(item)
    done
    
    
    
#cbs
#<span <p class="item__dek">

usnews = "https://www.cbsnews.com/" 
usresult = requests.get(usnews)
ussoup = bs4.BeautifulSoup(usresult.text,'html.parser')
ussoup.prettify()

usArticle = ussoup.find_all('p')
usStorys = []
    
for usStory in usArticle:
    cleantext = usStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    usStorys.append(cleantoken)
    us_list = []
    for sublist in usStorys:
        for item in sublist:
            us_list.append(item)
    done
    
    
    
#pbs
#<span>

pbsnews = "https://www.pbs.org/newshour/" 
pbsresult = requests.get(pbsnews)
pbssoup = bs4.BeautifulSoup(pbsresult.text,'html.parser')
pbssoup.prettify()

pbsArticle = pbssoup.find_all(['span','p'])
pbsStorys = []
    
for pbsStory in pbsArticle:
    cleantext = pbsStory.text.strip()
    cleantext = cleantext.lower()
    cleantoken = nltk.word_tokenize(cleantext)
    pbsStorys.append(cleantoken)
    flat_list = []
    for sublist in pbsStorys:
        for item in sublist:
            flat_list.append(item)
    done
    

#print(ny_list)
#print()
#print(g_list)
#print()
#print(a_list)
#print()
#print(r_list)
#print(f_list)
#print(n_list)
#print(abc_list)
#print(npr_list)
#print(us_list)
#print(flat_list)
masterList = ny_list + g_list + hf_list + r_list + f_list + n_list + abc_list + npr_list + us_list + flat_list


#Creating WordCloud
mergedList = ' '.join(masterList)

stopwords = set(STOPWORDS)
stopwords.add('news')
stopwords.add('read')
stopwords.add('book')
stopwords.add('world')
stopwords.add('trending')
stopwords.add('sports')
stopwords.add('S')
stopwords.add('new')
stopwords.add('s')
stopwords.add('u')
stopwords.add('U')
stopwords.add('politics')
stopwords.add('school')
stopwords.add('min')
stopwords.add('make')
stopwords.add('images')
stopwords.add('live')
stopwords.add('entertainment')
stopwords.add('life')
stopwords.add('lifestyle')
stopwords.add('health')
stopwords.add('us')
stopwords.add('monday')
stopwords.add('tuesday')
stopwords.add('wednesday')
stopwords.add('thursday')
stopwords.add('friday')
stopwords.add('saturday')
stopwords.add('sunday')
stopwords.add('home')
stopwords.add('day')
stopwords.add('nbc')
stopwords.add('fox')
stopwords.add('say')
stopwords.add('said')
stopwords.add('view')
stopwords.add('show')
stopwords.add('think')
stopwords.add('search')
stopwords.add('case')
stopwords.add('week')
stopwords.add('people')
stopwords.add('review')
stopwords.add('now')
stopwords.add('first')
stopwords.add('caption')
stopwords.add('latest')
stopwords.add('photo')
stopwords.add('cbs')
stopwords.add('house')
stopwords.add('share')

news_wc = WordCloud(
    background_color='white',
    max_words=100000,
    stopwords=stopwords,
    min_font_size=10)
news_wc.generate(mergedList)

fig = plt.figure()
fig.set_figwidth(16) # set width
fig.set_figheight(20) # set height

# display the word cloud
plt.imshow(news_wc, interpolation='bilinear')
plt.axis('off')
plt.savefig('news.png')

workbook = Workbook('newsAll.xlsx')
Report_Sheet = workbook.add_worksheet()

# Write the column headers if required.
Report_Sheet.write(0, 0, 'NY TIMES')
Report_Sheet.write(0, 1, 'THE GUARDIAN')
Report_Sheet.write(0, 2, 'HUFFINGTON POST')
Report_Sheet.write(0, 3, 'WASHINGTON POST')
Report_Sheet.write(0, 4, 'FOX NEWS')
Report_Sheet.write(0, 5, 'NBC')
Report_Sheet.write(0, 6, 'ABC')
Report_Sheet.write(0, 7, 'NPR')
Report_Sheet.write(0, 8, 'US NEWS')
Report_Sheet.write(0, 9, 'PBS')

## Write the column data.
Report_Sheet.write_column(1, 0, ny_list)
Report_Sheet.write_column(1, 1, g_list)
Report_Sheet.write_column(1, 2, hf_list)
Report_Sheet.write_column(1, 3, r_list)
Report_Sheet.write_column(1, 4, f_list)
Report_Sheet.write_column(1, 5, n_list)
Report_Sheet.write_column(1, 6, abc_list)
Report_Sheet.write_column(1, 7, npr_list)
Report_Sheet.write_column(1, 8, us_list)
Report_Sheet.write_column(1, 9, flat_list)
workbook.close()
print("News Headline File Was Created!")

#ny_list, g_list, hf_list, r_list, f_list, n_list, abc_list, npr_list, us_list, flat_list, 'NY TIMES', 'THE GUARDIAN', 'HUFFINGTON POST', 'WASHINGTON POST', 'FOX NEWS', 'NBC', 'ABC', 'NPR', 'US NEWS', 'PBS'

df = pd.DataFrame(list(zip(ny_list, g_list, hf_list, r_list, f_list, n_list, abc_list, npr_list, us_list, flat_list)), columns =['NY TIMES', 'THE GUARDIAN', 'HUFFINGTON POST', 'WASHINGTON POST', 'FOX NEWS', 'NBC', 'ABC', 'NPR', 'US NEWS', 'PBS'])
print('printing DataFrame')
print(df)

df.to_csv('newsEqual.csv', encoding='utf-8', index=False)
print(df.nunique())

#print(mergedList)
#
#
#
#with open('my_file.csv', 'w') as #my_file:
#    for (moveName, moveStartUp, #totalFrames, landingLag) in #all_move_data:
#        my_file.write("{0},{1}\n".format#(moveName, moveStartUp, #totalFrames, landingLag))
#print('File created')
#
