# -*- coding: utf-8 -*-
"""Scraper4StatareaWebsitePASTDATA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sTaYYpF3-L0lz91QRiag5T1i1i4apXBm

**Scrapping Project:** Getting Data from www.statarea.com for Prediction purpose
**Author :** Oladimeji .O. Awosanya

# **LOADING LIBRARY**
"""

import requests, csv, time
from bs4 import BeautifulSoup

"""# **CRAPPING STATAREA WEBSITE AND GETTING DATA**"""

csv_STATAREAData = [ ]
website = requests.get('http://www.statarea.com/predictions/date/2021-07-05/competition')
time.sleep(3)
soup = BeautifulSoup(website.text, 'html.parser')
dataContainer = soup.find('div', class_='datacotainer')
gameContainer = dataContainer.find_all('div', class_='competition')


for gamelist in gameContainer:

  try :        
      hostTeam = gamelist.find('div', class_='hostteam')
      hostTeamName = hostTeam.select_one('.name > a').get_text()
      hostTeamGoal = int(hostTeam.select_one('.goals').get_text())
      
      
      guestTeam = gamelist.find('div', class_='guestteam')
      guestTeamName = guestTeam.select_one('.name > a').get_text()
      guestTeamGoals = int(guestTeam.select_one('.goals').get_text())
      
      total_Goals = hostTeamGoal + guestTeamGoals

      gameTip4 = str(gamelist.find('div', class_='type4'))[19:21]
      gameTip5 = str(gamelist.find('div', class_='type5'))[19:21]

  except:
      pass
    
  try:
      probabilityRow = gamelist.select_one('.coefrow')
      probabilityBox = probabilityRow.select('.value')
      
      homeWinProbability = int(probabilityBox[0].get_text())
      drawProbability = int(probabilityBox[1].get_text())
      awayWinProbability = int(probabilityBox[2].get_text())

      Diff_b_Team = homeWinProbability - awayWinProbability
      Diff_b_HTeam = homeWinProbability - drawProbability
      Diff_b_ATeam = awayWinProbability - drawProbability

      HT1 = int(probabilityBox[3].get_text())
      HTX = int(probabilityBox[4].get_text())
      HT2 = int(probabilityBox[5].get_text())

      HT_Diff_b_Team = HT1 - HT2
      HT_Diff_b_HTeam = HT1 - HTX
      HT_Diff_b_ATeam = HT2 - HTX

      overOnePointFive = int(probabilityBox[6].get_text())
      overTwoPointFive = int(probabilityBox[7].get_text())
      overThreePointFive = int(probabilityBox[8].get_text())

      Over15_1 = overOnePointFive - overThreePointFive
      Over25_2 = overOnePointFive - overTwoPointFive
      Over35_3 = overThreePointFive - overTwoPointFive

      bootTeamToScore = int(probabilityBox[9].get_text())
      OnlyTeamToScore = int(probabilityBox[10].get_text())

      bootTeamToScore1 = int(probabilityBox[9].get_text())
      OnlyTeamToScore1 = int(probabilityBox[10].get_text())

      if gameTip4 == '1X':
        csv_STATAREAData.append([hostTeamName + " VS " + guestTeamName,hostTeamGoal,guestTeamGoals,total_Goals,'1X',homeWinProbability,drawProbability,awayWinProbability,
                                Diff_b_Team,Diff_b_HTeam,Diff_b_ATeam,HT1,HTX,HT2,HT_Diff_b_Team,HT_Diff_b_HTeam,HT_Diff_b_ATeam,overOnePointFive,
                                overTwoPointFive,overThreePointFive,Over15_1,Over25_2,Over35_3,bootTeamToScore,OnlyTeamToScore])
      if gameTip5 == 'X2':
        csv_STATAREAData.append([hostTeamName + " VS " + guestTeamName,hostTeamGoal,guestTeamGoals,total_Goals,'X2',homeWinProbability,drawProbability,awayWinProbability,
                                Diff_b_Team,Diff_b_HTeam,Diff_b_ATeam,HT1,HTX,HT2,HT_Diff_b_Team,HT_Diff_b_HTeam,HT_Diff_b_ATeam,overOnePointFive,
                                overTwoPointFive,overThreePointFive,Over15_1,Over25_2,Over35_3,bootTeamToScore,OnlyTeamToScore])
  except:
      pass

"""# **SAVING TO CSV FILE**"""

with open('SOCCER_RAW_DATA.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_STATAREAData)