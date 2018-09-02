# import libraries
import urllib2
from bs4 import BeautifulSoup
from building import Building


def checkBuilding(Building):

        page = urllib2.urlopen(Building.url)
        soup = BeautifulSoup(page, "html.parser")

        data = []
        table = soup.find("table", attrs={"class":"table"})
        table_body = table.find("tbody")

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]

            if cols[-1] == "bWOLNE":
                rowWithMeters = str(cols[2]).replace("m2", "")
                if(float(rowWithMeters) >= 40.00 and float(rowWithMeters) <= 50.00):
                    data.append([ele for ele in cols if ele]) # Get rid of empty values
        print(len(data))


if __name__ == "__main__":
    building1 = Building("http://centralparkapartments.pl/cpa2/znajdz-mieszkanie/budynek-b/#lista-mieszkn",'building_b.txt','building_b.txt')
    building2 = Building("http://centralparkapartments.pl/cpa2/znajdz-mieszkanie/budynek-b1/#lista-mieszkn",'building_b1.txt','building_b1.txt')
    building3 = Building("http://centralparkapartments.pl/cpa3/budynek-d1/#lista-mieszkan",'building_d1.txt','building_d1.txt')

    checkBuilding(building1)
    checkBuilding(building2)
    checkBuilding(building3)
