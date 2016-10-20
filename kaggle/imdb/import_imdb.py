from bs4 import BeautifulSoup 
import urllib2
import re
import csv
import os.path

if not os.path.isfile("imdb_indian_ta.csv"):
    imdb_indian_file = open("imdb_indian_ta.csv","ab+")
    writer = csv.writer(imdb_indian_file)
    writer.writerow(["id","name","duration","genre","titleYear","releaseDate","director","language","budget","cast","link"])
else:
    imdb_indian_file = open("imdb_indian_ta.csv","ab+")
    writer = csv.writer(imdb_indian_file)

imdb_indian_file.flush()
movieDurationRegex = re.compile('[0-9]+')
movieLinkHead = "http://www.imdb.com"
#movieData = []

def getMovieDetails(movieLink):
    try:
        movieSoup = BeautifulSoup(urllib2.urlopen(movieLinkHead+movieLink).read())
        titleYear = movieSoup.find(id="titleYear").contents[1].contents[0]
    
        releaseDate = movieSoup.find(title="See more release dates")
        if releaseDate is None:
            releaseDate = None
        else:
            releaseDate = releaseDate.contents[1]['content']
    
        try:
            director = movieSoup.find(itemprop="director").contents[1].contents[0].contents[0]
        except:
            director = ""

        titleDetails = movieSoup.find(id="titleDetails")
        languageItem = titleDetails.find("h4",text="Language:")
        
        if languageItem is None:
            language=''
        else:
            
            language = languageItem.next_sibling.next_sibling.contents[0]
        #print language
        budget = 0
    
        budgetItem = titleDetails.find("h4",text="Budget:")
        if budgetItem is not None:
            budget = re.sub('[a-zA-Z, ]','',budgetItem.next_sibling).strip()
    
        cast = []
        castItems = movieSoup.find("table","cast_list")
        if castItems is not None:
            for castItem in castItems.find_all("span",itemprop="name"):
                cast.append(castItem.contents[0])
    
        return {"titleYear":titleYear,"releaseDate":releaseDate,"director":director.strip(),"budget":budget,"language":language.strip(),"cast":cast}
    except:
        return None

def cleanValue(value):
    return re.sub('\n','',value).strip()

def getMoviesPage():
    #pageUrl = 'http://www.imdb.com/search/title?countries=in&countries=IN&title_type=feature&explore=countries&sort=alpha,asc&view=advanced&page=201'
    pageUrl = 'http://www.imdb.com/search/title?title_type=feature&languages=ta&sort=alpha,asc&page=1&ref_=adv_nxt'
    id = 1
    pageId=1
    while True:
        movieData = []
        print "Processing page:"+str(pageId)
        page = urllib2.urlopen(pageUrl)
        soup = BeautifulSoup(page.read())
        for movieItem in soup.find_all('div','lister-item-content'):
            nameLink = movieItem.find('a')
            name = nameLink.contents[0]
            print str(id)+":"+name
            duration = movieItem.find('span','runtime')
            if duration is None:
                duration = 0
            else:
                duration = re.search(movieDurationRegex,duration.contents[0]).group(0)
    
            genre = movieItem.find('span','genre')
            if genre is None:
                genre = ""
            else:
                genre = cleanValue(genre.contents[0])
            
            link = nameLink['href'] 
        
            movieDetails = getMovieDetails(link)
            if movieDetails is None:
                continue
            movieFull ={'id':id,'name':name,'duration':duration,'link':movieLinkHead+link,'genre':genre}
            movieFull.update(movieDetails)
        
            movieData.append(movieFull)
            id +=1
        
        writeCsv(movieData)
        #break
        
        pageItem = soup.find('a','lister-page-next next-page')
        if pageItem is None:
            break
        else:
            pageUrl = 'http://www.imdb.com/search/title'+pageItem['href']
        pageId += 1
        

def writeCsv(movieData):
    
    for movie in movieData:
        try:
            cast = ",".join(movie["cast"])
            writer.writerow([movie["id"],movie["name"],movie["duration"],movie["genre"],movie["titleYear"],movie["releaseDate"],movie["director"],movie["language"],movie["budget"],cast,movie["link"]])
        except:
            continue
    imdb_indian_file.flush()
    return

if __name__=='__main__':
    getMoviesPage()
    imdb_indian_file.close()
    #print movieData
    
