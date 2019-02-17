from bs4 import BeautifulSoup as soup
import requests
import os

inp= "c"
while inp!="exit":
  if inp == "c":
    url = "https://r6.tracker.network/profile/pc/"
    #inp = 'PNIS.lele394'
    name = input("name of da dude?\n> ")
    url = url + name

  
  page_response = requests.get(url, timeout=5)

  content = soup(page_response.content, "html.parser")
  os.system("clear")
  print("---------------------")
  print(name)
  print("---------------------")





  # rank ----------------------------
  r = content.find("div", class_="trn-text--dimmed")
  print("rank     : ", r.string.string)


  #MMR------------------
  MMR = content.find("div", class_="trn-text--dimmed",style="font-size: 2rem;")
  print("MMR      : ", MMR.string)


  #lv----------------------------
  lv = content.find("div", class_="trn-defstat__value")
  lv =lv.string.string
  lv = lv.replace("\n","")
  print("lv       : ", lv)


  #data-stat list --------------------
  dataStat = []
  for i in content.find_all("div", class_="trn-defstat__value"):
    dataStat.append(i)


  #win------------------------
  stat = dataStat[6]
  stat =stat.string.string
  win = stat.replace("\n","")
  print("win      : ", win)


  #kill------------------------
  stat = dataStat[8]
  stat =stat.string.string
  kill = stat.replace("\n","")
  print("kill     : ", kill)


  #ratio------------------------
  stat = dataStat[9]
  stat =stat.string.string
  ratio = stat.replace("\n","")
  print("ratio    : ", ratio)


  #match------------------------
  stat = dataStat[25]
  stat =stat.string.string
  match = stat.replace("\n","")
  print("match    : ", match)


  #time------------------------
  stat = dataStat[24]
  stat =stat.string.string
  time = stat.replace("\n","")
  print("time     : ", time)



  #xp------------------------
  stat = dataStat[26]
  stat =stat.string.string
  xp = stat.replace("\n","")
  print("XP       : ", xp)


  #melee------------------------
  stat = dataStat[27]
  stat =stat.string.string
  melee = stat.replace("\n","")
  print("melee    : ", melee)


  #blind-----------------------
  stat = dataStat[28]
  stat =stat.string.string
  blind = stat.replace("\n","")
  print("blind    : ", blind)


  #headshot-----------------------
  stat = dataStat[20]
  stat =stat.string.string
  headshot = stat.replace("\n","")
  print("headshot : ", headshot)

  inp = input("\nchange da dude (c) or refresh (r) or exit (exit)\n> ")

  #print(dataStat)

  #print(content.get_text())




