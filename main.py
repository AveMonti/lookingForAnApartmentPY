# import libraries
import urllib2
from bs4 import BeautifulSoup
from building import Building
import filecmp


def checkIfThereAreChanges(Building):
    if filecmp.cmp(Building.input, Building.output):
        print("Don't worry. Nothing has changed in "+str(Building.input))
    else:
        print("O.o Something has not changed in "+str(Building.input))


def saveToTxtFile(nameFile, array):

    with open(nameFile, "w") as f:
        for item in array:
            f.write("%s\n" % item)
        f.write("%s\n" % len(array))


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
        saveToTxtFile(Building.output, data)




if __name__ == "__main__":
    building1 = Building("http://centralparkapartments.pl/cpa2/znajdz-mieszkanie/budynek-b/#lista-mieszkn",'building_b.txt','newBuilding_b.txt')
    building2 = Building("http://centralparkapartments.pl/cpa2/znajdz-mieszkanie/budynek-b1/#lista-mieszkn",'building_b1.txt','newBuilding_b1.txt')
    building3 = Building("http://centralparkapartments.pl/cpa3/budynek-d1/#lista-mieszkan",'building_d1.txt','newBuilding_d1.txt')

    checkBuilding(building1)
    checkBuilding(building2)
    checkBuilding(building3)
    checkIfThereAreChanges(building1)
    checkIfThereAreChanges(building2)
    checkIfThereAreChanges(building3)
