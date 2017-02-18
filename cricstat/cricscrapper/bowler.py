__author__ = 'apatti'

import requests
from lxml import html
import csv

class BowlerScrapper:

    @staticmethod
    def scrap(matchUrl):
        print "Working on {}".format(matchUrl)
        inningData ={}
        for innings in [1,2]:
            url = "http://www.espncricinfo.com{}?innings={};view=commentary".format(matchUrl,innings)
            htmlTree = BowlerScrapper.__gethtmldata(url)
            htmlElements = htmlTree.xpath('//div[@class="end-of-over-info"]')

            fullDetails=[]
            bowlerDetails={}
            for element in htmlElements:
                overDetail={}
                overDetail["over"] = int(filter(str.isdigit, element[0][0].text_content()))
                overDetail["bowler"] = element[1][1][0][0][0].text_content()
                if bowlerDetails.get(overDetail["bowler"]) is None:
                    bowlerDetails[overDetail["bowler"]] = {"runs":0,"wickets":0}

                overDetail["stat"] = element[1][1][0][0][1].text_content()
                runs = int(overDetail["stat"].split('-')[2])
                wickets = int(overDetail["stat"].split('-')[3])
                overDetail["runs"] = runs - bowlerDetails[overDetail["bowler"]]["runs"]
                overDetail["wickets"] = wickets - bowlerDetails[overDetail["bowler"]]["wickets"]
                bowlerDetails[overDetail["bowler"]]["runs"] += overDetail["runs"]
                bowlerDetails[overDetail["bowler"]]["wickets"] += overDetail["wickets"]
                overDetail["url"] = url
                fullDetails.append(overDetail)
            inningData[innings] = fullDetails

        return inningData

    @staticmethod
    def scrapSeries(url):
        htmlTree = BowlerScrapper.__gethtmldata(url)
        htmlElements = htmlTree.xpath('//span[@class="play_team"]/a')
        matches = []
        for element in htmlElements:
            matchData = {}
            matchUrl = element.attrib['href']
            matchData["matchid"] = int(filter(str.isdigit,matchUrl[matchUrl.rindex('/'):]))
            matchData["year"] = int(filter(str.isdigit,matchUrl[:matchUrl.rindex('/')]))
            matchData["innings"] = BowlerScrapper.scrap(matchUrl)
            matches.append(matchData)

        return matches

    @staticmethod
    def __gethtmldata(url):
        page = requests.get(url)
        return html.fromstring(page.content)

    @staticmethod
    def saveToCsv(filename,data):
        with open(filename,'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["matchid", "year", "innings", "bowler", "over", "runs", "wickets", "stat","url"])

            for matchData in matches:
                matchid=matchData["matchid"]
                year = matchData["year"]

                for inning,inningData in matchData["innings"].iteritems():
                    innings = inning
                    for bowlerData in inningData:
                        writer.writerow((matchid,year,innings,
                                        bowlerData["bowler"],bowlerData["over"],bowlerData["runs"],bowlerData["wickets"],bowlerData["stat"],bowlerData["url"]))

if __name__ == '__main__':
    matches=[]
    matches.extend(BowlerScrapper.scrapSeries("http://www.espncricinfo.com/indian-premier-league-2016/content/series/968923.html?template=fixtures"))
    matches.extend(BowlerScrapper.scrapSeries("http://www.espncricinfo.com/indian-premier-league-2015/content/series/791129.html?template=fixtures"))
    matches.extend(BowlerScrapper.scrapSeries("http://www.espncricinfo.com/indian-premier-league-2014/content/series/695871.html?template=fixtures"))
    BowlerScrapper.saveToCsv("../data/ipl_bowler.csv",matches)