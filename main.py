# import libraries
import urllib2
from bs4 import BeautifulSoup
from building import Building
import filecmp
import config
import time
import datetime
from sendMail import send_mail

def checkIfThereAreChanges(Building):
    if filecmp.cmp(Building.input, Building.output):
        print("Don't worry. Nothing has changed in "+str(Building.input))
    else:
        print("O.o Something has not changed in "+str(Building.input))

        if (send_mail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS_TO_SEND, config.SUBJECT, config.MESSAGE, files=[Building.input, Building.output], server="smtp.gmail.com", port=587, username=config.EMAIL_ADDRESS, password=config.PASSWORD)):
            with open(Building.output) as f:
                with open(Building.input, "w") as f1:
                    for line in f:
                        f1.write(line)
            print("ok")
        else:
            print("nie ok")
            return


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

        saveToTxtFile(Building.output, data)


if __name__ == "__main__":

    for building in config.arrayBuildings:
        checkBuilding(building)
        checkIfThereAreChanges(building)
    print(datetime.datetime.now())
    
