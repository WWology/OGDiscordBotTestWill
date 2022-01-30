#imports
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
from discord.utils import get
#from datetime import date
#from datetime import datetime
import datetime
from time import strptime
from googletrans import Translator, LANGUAGES
import asyncio
from itertools import cycle
import asyncio
import requests
import time



def csgomap():
  try:
    #Loading HLTV of OG
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


    #OGpage = Set the HLTV matchbox url for the team you wish to track here e.g - 'https://www.hltv.org/team/10503/og#tab-matchesBox'
    OGpage = 'https://www.hltv.org/team/10503/og#tab-matchesBox'
    r2 = requests.get(OGpage, headers=headers)

    page_soup2 = soup(r2.text, "html.parser")
    dataofpage = page_soup2.findAll("td", {"class":"matchpage-button-cell"})


    linkinfo = []
    #If game found - open the page via the href / link info
    for a in dataofpage[0].findAll('a', href=True):

      linkinfo.append(a['href'])

    matchlink = "https://www.hltv.org" + linkinfo[0]
    #matchlink = "https://www.hltv.org/matches/2351985/heroic-vs-og-blast-premier-fall-showdown-2021"
    


   
    
    r = requests.get(matchlink , headers=headers)
    
    #Load the page of the match
    page_soup = soup(r.text, "html.parser")

    
    #Link to the tournament page
    test2 =  page_soup.find("div", {"class":"flexbox-column"})
    test5 = test2.findAll("div", {"class":"results-teamname text-ellipsis"})
    test4 = test2.findAll("div", {"class":"results-team-score"})
    test3 = test2.findAll("div", {"class":"mapname"})
    i=0
    j=0
    k=0
    z=0
    messagetosend= "The maps for the game: "
    teamnames =[]
    scoresteam1=[]
    scoresteam2=[]
    maps=[]
    #collecting maps
    while(i < len(test3)):
      linkdata = test3[i].text
      maps.append(linkdata)   
      i+=1
    
    if(maps[0] != "TBA"):
      #collecting scores
      while(j < len(test4)):
        scoredata = test4[j].text
        if(j % 2) == 0:
          scoresteam1.append(scoredata)
        else:
          scoresteam2.append(scoredata)
        j=j+1
      
      while(z < 2):
        team = test5[z].text
        teamnames.append(team)
        z=z+1
      print(teamnames)
      print(scoresteam1)
      print(scoresteam2)

      for counter, n in enumerate(scoresteam1):
        if n == "-":
          scoresteam1[counter] = "0"
      for counter, n in enumerate(scoresteam2):
        if n == "-":
          scoresteam2[counter] = "0"

      while(k < len(maps)):
        if k == 0:
          messagetosend =  maps[k] + " (||" + teamnames[0] + " " + scoresteam1[k] + " - " + scoresteam2[k] + " " + teamnames[1] + "||)"
        else:
          messagetosend = messagetosend + ", " + maps[k] + " (||" + teamnames[0] + " " + scoresteam1[k] + " - " + scoresteam2[k] + " " + teamnames[1] + "||)"
        k=k+1
    else:
      i=0
      while i < len(maps):
        if i == 0:
          messagetosend = messagetosend + maps[i]
        else:
          messagetosend = messagetosend + ", " + maps[i]
        i = i+1
      
    



      
    
    


    
    return(messagetosend)



  except:

    
    return("No maps found")