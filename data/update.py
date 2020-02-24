#!/usr/bin/env python
# -*-coding:Latin-1 -*

import json
seasons = []

class team(object):
   def __init__(self,name,country):
       self.name = name
       self.country = country

# Teams Countries & Names

RM=team("Real Madrid","Spain")
Barca=team("FC Barcelona","Spain")
OM=team("Olymique de Marseille","France")
Juve=team("Juventus","Italy")
Valencia=team("Valencia","Spain")
ACM=team("AC Milan","Italy")
Ajax=team("Ajax Amsterdam","Netherlands")
BVB=team("Borussia Dortmund","Germany")
FCBayern=team("Bayern Munich","Germany")
DLC=team("Deportiva La Corûna","Spain")
RZ=team("Real Zaragoza","Spain")
RCD=team("RCD Espanyol","Spain")
FCP=team("FC Porto","Portugal")
Chelsea=team("Chelsea FC","England")
Inter=team("Inter Milan","Italy")
Reds=team("Liverpool","England")
MU=team("Manchester United","England")
RMajorqa=team("Real Majorqua","Spain")
Sevilla=team("FC Sevilla","Spain")
AM=team("Atletico Madrid","Spain")
Betis=team("Real Betis","Spain")
SW=team("Shieffield Wednesday","England")
A=team("Arsenal","England")
Ev=team("Everton","England")
Portsmouth=team("Portsmouth","England")
MC=team("Manchester City","England")
WA=team("Wigan Athletic","England")
Roovers=team("Blackburn Rovers","England")
Leicester=team("Leicester City","England")
Lazio=team("Lazio","Italy")
Napoli=team("Napoli","Italy")
Parme=team("Parme FC","Italy")
Fiorentina=team("ACF Fiorentina","Italy")
Vicence=team("Vicence","Italy")
Sampdoria=team("UC Sampdoria","Italy")
Torino=team("Torino FC","Italy")
Roma=team("AS Roma","Italy")
WB=team("Werder Bremen","Germany")
Stuttgart=team("Vfb Stuttgart","Germany")
Kaiserslautern=team("FC Kaiserslauten","Germany")
Wolfsburg=team("Vfl Wolfsburg","Germany")
Bilbao=team("Atletico Bilbao","Spain")
Bennefica=team("Benefica Lisbonne","Portugal")
Celtic=team("Celtic Glasgow","Scotland")
Feynoord=team("Feyenoord Rotterdam","Netherlands")
NF=team("Nottingham Forest","England")
Hambourg=team("Hambourg SV","Germany")
Steaua=team("Steaua Bucarest","Romania")
PSV=team("PSV Eindhoven","Netherlands")
ERB=team("Red Star Belgrade","Belgrade")
AV=team("Aston Villa","England")
Sociedad=team("Real Sociedad","Spain")
Spurs=team("Tottenham Hotspur","England")


# UEFA Trophies 
UEFA_CUP = {
    "1956":RM.name,"1957":RM.name,"1958":RM.name,
    "1959":RM.name,"1960":RM.name,"1961":Bennefica.name,
    "1962":Bennefica.name,"1963":ACM.name,"1964":Inter.name,
    "1965":Inter.name,"1966":RM.name,"1967":Celtic.name,
    "1968":MU.name,"1969":ACM.name,"1970":Feynoord.name,
    "1971":Ajax.name,"1972":Ajax.name,"1973":Ajax.name,
    "1974":FCBayern.name,"1975":FCBayern.name,"1976":FCBayern.name,
    "1977":Reds.name,"1978":Reds.name,"1979":NF.name,
    "1980":NF.name,"1981":Reds.name,"1982":AV.name,
    "1983":Hambourg.name,"1984":Reds.name,"1985":Juve.name,
    "1986":Steaua.name,"1987":FCP.name,"1988":PSV.name,
    "1989":ACM.name,"1990":ACM.name,"1991":ERB.name,
    "1992":Barca.name,
    "1993":OM.name,"1994":ACM.name,"1995":Ajax.name,
    "1996":Juve.name,"1997":BVB.name,"1998":RM.name,
    "1999":MU.name,"2000":RM.name,"2001":FCBayern.name,
    "2002":RM.name,"2003":ACM.name,"2004":FCP.name,
    "2005":Reds.name,"2006":Barca.name,"2007":ACM.name,
    "2008":MU.name,"2009":Barca.name,"2010":Inter.name,
    "2011":Barca.name,"2012":Chelsea.name,"2013":FCBayern.name,
    "2014":RM.name,"2015":Barca.name,"2016":RM.name,
    "2017":RM.name,"2018":RM.name,"2019":Reds.name,
}

# Spain Trophies
Spain_CUP = {
    "1956":Bilbao.name,"1957":Barca.name,"1958":Bilbao.name,
    "1959":Barca.name,"1960":AM.name,"1961":AM.name,
    "1962":RM.name,"1963":Barca.name,"1964":RZ.name,
    "1965":AM.name,"1966":RZ.name,"1967":Valencia.name,
    "1968":Barca.name,"1969":Bilbao.name,"1970":RM.name,
    "1971":Barca.name,"1972":AM.name,"1973":Bilbao.name,
    "1974":RM.name,"1975":RM.name,"1976":AM.name,
    "1977":Betis.name,"1978":Barca.name,"1979":Valencia.name,
    "1980":RM.name,"1981":Barca.name,"1982":RM.name,
    "1983":Barca.name,"1984":Bilbao.name,"1985":AM.name,
    "1986":RZ.name,"1987":Sociedad.name,"1988":Barca.name,
    "1989":RM.name,"1990":Barca.name,"1991":AM.name,
    "1992":AM.name,
    "1993":RM.name,"1994":RZ.name,"1995":DLC.name,
    "1996":AM.name,"1997":Barca.name,"1998":Barca.name,
    "1999":Valencia.name,"2000":RCD.name,"2001":RZ.name,
    "2002":DLC.name,"2003":RMajorqa.name,"2004":RZ.name,
    "2005":Betis.name,"2006":RCD.name,"2007":Sevilla.name,
    "2008":Valencia.name,"2009":Barca.name,"2010":Sevilla.name,
    "2011":RM.name,"2012":Barca.name,"2013":AM.name,
    "2014":RM.name,"2015":Barca.name,"2016":Barca.name,
    "2017":Barca.name,"2018":Barca.name,"2019":Valencia.name
}
Spain_League = {
    "1956":Bilbao.name,"1957":RM.name,"1958":RM.name,
    "1959":Barca.name,"1960":Barca.name,"1961":RM.name,
    "1962":RM.name,"1963":RM.name,"1964":RM.name,
    "1965":RM.name,"1966":AM.name,"1967":RM.name,
    "1968":RM.name,"1969":RM.name,"1970":AM.name,
    "1971":Valencia.name,"1972":RM.name,"1973":AM.name,
    "1974":Barca.name,"1975":RM.name,"1976":RM.name,
    "1977":AM.name,"1978":RM.name,"1979":RM.name,
    "1980":RM.name,"1981":Sociedad.name,"1982":Sociedad.name,
    "1983":Bilbao.name,"1984":Bilbao.name,"1985":Barca.name,
    "1986":RM.name,"1987":RM.name,"1988":RM.name,
    "1989":RM.name,"1990":RM.name,"1991":Barca.name,
    "1992":Barca.name,
    "1993":Barca.name,"1994":Barca.name,"1995":RM.name,
    "1996":AM.name,"1997":RM.name,"1998":Barca.name,
    "1999":Barca.name,"2000":DLC.name,"2001":RM.name,
    "2002":Valencia.name,"2003":RM.name,"2004":Valencia.name,
    "2005":Barca.name,"2006":Barca.name,"2007":RM.name,
    "2008":RM.name,"2009":Barca.name,"2010":Barca.name,
    "2011":Barca.name,"2012":RM.name,"2013":Barca.name,
    "2014":AM.name,"2015":Barca.name,"2016":Barca.name,
    "2017":RM.name,"2018":Barca.name,"2019":Barca.name,
}

#England Trophies

England_CUP = {
    "1956":MC.name,"1957":AV.name,"1958":"Bolton Wanderers",
    "1959":"Wolverhamption Wanderers","1960":Spurs.name,
    "1961":Spurs.name,"1962":MU.name,"1963":MU.name,
    "1964":"West Ham United","1965":Reds.name,"1966":Ev.name,
    "1967":Spurs.name,"1968":"West Bromwich Albion","1969":MC.name,
    "1970":Chelsea.name,"1971":A.name,"1972":"Leeds United",
    "1973":"Sunderland","1974":Reds.name,"1975":"West Ham United",
    "1976":"Southampton","1977":MU.name,"1978":"Ipswich Town",
    "1979":A.name,"1980":"West Ham United","1981":Spurs.name,
    "1982":Spurs.name,"1983":MU.name,"1984":Ev.name,
    "1985":MU.name,"1986":Reds.name,"1987":"Coventry City",
    "1988":"Wimbledon","1989":Reds.name,"1990":MU.name,
    "1991":Spurs.name,"1992":Reds.name,
    "1993":A.name,"1994":MU.name,"1995":Ev.name,
    "1996":MU.name,"1997":Chelsea.name,"1998":A.name,
    "1999":MU.name,"2000":Chelsea.name,"2001":Reds.name,
    "2002":A.name,"2003":A.name,"2004":MU.name,
    "2005":A.name,"2006":Reds.name,"2007":Chelsea.name,
    "2008":Portsmouth.name,"2009":Chelsea.name,"2010":Chelsea.name,
    "2011":MC.name,"2012":Chelsea.name,"2013":WA.name,
    "2014":A.name,"2015":A.name,"2016":Leicester.name,
    "2017":A.name,"2018":Chelsea.name,"2019":MC.name
}
England_League = {
    "1956":MU.name,"1957":MU.name,"1958":"BWolverhampton Wanderers",
    "1959":"Wolverhamption Wanderers","1960":"Burnley",
    "1961":Spurs.name,"1962":"Ipswich Town","1963":Ev.name,
    "1964":Reds.name,"1965":MU.name,"1966":Reds.name,
    "1967":MU.name,"1968":MC.name,"1969":"Leeds United",
    "1970":Ev.name,"1971":A.name,"1972":"Derby County",
    "1973":Reds.name,"1974":"Leeds United","1975":"Derby County",
    "1976":Reds.name,"1977":Reds.name,"1978":NF.name,
    "1979":Reds.name,"1980":Reds.name,"1981":AV.name,
    "1982":Reds.name,"1983":Reds.name,"1984":Reds.name,
    "1985":Ev.name,"1986":Reds.name,"1987":Ev.name,
    "1988":Reds.name,"1989":A.name,"1990":Reds.name,
    "1991":A.name,"1992":"Leeds United",
    "1993":MU.name,"1994":MU.name,"1995":Roovers.name,
    "1996":MU.name,"1997":MU.name,"1998":A.name,
    "1999":MU.name,"2000":MU.name,"2001":MU.name,
    "2002":A.name,"2003":MU.name,"2004":A.name,
    "2005":Chelsea.name,"2006":Chelsea.name,"2007":MU.name,
    "2008":MU.name,"2009":MU.name,"2010":Chelsea.name,
    "2011":MU.name,"2012":MC.name,"2013":MU.name,
    "2014":MC.name,"2015":Chelsea.name,"2016":MU.name,
    "2017":Chelsea.name,"2018":MC.name,"2019":MC.name
}

#Germany Trophies
Germany_CUP = {
    "1956":"Karlsruher","1957":FCBayern.name,"1958":Stuttgart.name,
    "1959":"Schwarz-Weiss","1960":"Monchengladbach","1961":WB.name,
    "1962":"Nuremberg","1963":Hambourg.name,"1964":"TSV",
    "1965":BVB.name,"1966":FCBayern.name,"1967":FCBayern.name,
    "1968":"Cologne","1969":FCBayern.name,"1970":"Kickers Offenbach",
    "1971":FCBayern.name,"1972":"Shalke","1973":"Monchengladbach",
    "1974":"Eintracht Francfort","1975":"Eintracht Francfort","1976":"Eintracht Francfort",
    "1977":"Cologne","1978":"Cologne","1979":"Dusseldorf",
    "1980":"Dusseldorf","1981":"Eintracht Francfort","1982":FCBayern.name,
    "1983":"Cologne","1984":FCBayern.name,"1985":"Uerdingen",
    "1986":FCBayern.name,"1987":Hambourg.name,"1988":"Eintracht Francfort",
    "1989":BVB.name,"1990":Kaiserslautern.name,"1991":WB.name,
    "1992":"Hanovre 96",
    "1993":WB.name,"1994":FCBayern.name,"1995":BVB.name,
    "1996":BVB.name,"1997":FCBayern.name,"1998":Kaiserslautern.name,
    "1999":FCBayern.name,"2000":FCBayern.name,"2001":FCBayern.name,
    "2002":BVB.name,"2003":FCBayern.name,"2004":WB.name,
    "2005":FCBayern.name,"2006":FCBayern.name,"2007":Stuttgart.name,
    "2008":FCBayern.name,"2009":Wolfsburg.name,"2010":FCBayern.name,
    "2011":BVB.name,"2012":BVB.name,"2013":FCBayern.name,
    "2014":FCBayern.name,"2015":FCBayern.name,"2016":FCBayern.name,
    "2017":FCBayern.name,"2018":FCBayern.name,"2019":FCBayern.name,
}
Germany_League = {
    "1956":BVB.name,"1957":BVB.name,"1958":"Shalke",
    "1959":"Eintracht Francfurt","1960":Hambourg.name,"1961":"Nurnberg",
    "1962":"FC Koln","1963":BVB.name,"1964":"FC Koln",
    "1965":WB.name,"1966":"TSV 1860","1967":"Eintracht Braunschweig",
    "1968":"FC Nurnberg","1969":FCBayern.name,"1970":"Monchengladbach",
    "1971":"Monchengladbach","1972":FCBayern.name,"1973":FCBayern.name,
    "1974":FCBayern.name,"1975":"Monchengladbach","1976":"Monchengladbach",
    "1977":"Monchengladbach","1978":"FC Koln","1979":Hambourg.name,
    "1980":FCBayern.name,"1981":FCBayern.name,"1982":Hambourg.name,
    "1983":Hambourg.name,"1984":Stuttgart.name,"1985":FCBayern.name,
    "1986":FCBayern.name,"1987":FCBayern.name,"1988":WB.name,
    "1989":FCBayern.name,"1990":FCBayern.name,"1991":Kaiserslautern.name,
    "1992":Stuttgart.name,
    "1993":WB.name,"1994":FCBayern.name,"1995":BVB.name,
    "1996":BVB.name,"1997":FCBayern.name,"1998":Kaiserslautern.name,
    "1999":FCBayern.name,"2000":FCBayern.name,"2001":FCBayern.name,
    "2002":BVB.name,"2003":FCBayern.name,"2004":WB.name,
    "2005":FCBayern.name,"2006":FCBayern.name,"2007":Stuttgart.name,
    "2008":FCBayern.name,"2009":Wolfsburg.name,"2010":FCBayern.name,
    "2011":BVB.name,"2012":BVB.name,"2013":FCBayern.name,
    "2014":FCBayern.name,"2015":FCBayern.name,"2016":FCBayern.name,
    "2017":FCBayern.name,"2018":FCBayern.name,"2019":FCBayern.name,
}
#Italy Trophies
Italy_CUP = {
    "1993":Torino.name,"1994":Sampdoria.name,"1995":Juve.name,
    "1996":Fiorentina.name,"1997":Vicence.name,"1998":Lazio.name,
    "1999":Parme.name,"2000":Lazio.name,"2001":Fiorentina.name,
    "2002":Parme.name,"2003":ACM.name,"2004":Lazio.name,
    "2005":Inter.name,"2006":Inter.name,"2007":Roma.name,
    "2008":Roma.name,"2009":Lazio.name,"2010":Inter.name,
    "2011":Inter.name,"2012":Napoli.name,"2013":Lazio.name,
    "2014":Napoli.name,"2015":Juve.name,"2016":Juve.name,
    "2017":Juve.name,"2018":Juve.name,"2019":Lazio.name,
}
Italy_League = {
    "1993":ACM.name,"1994":ACM.name,"1995":Juve.name,
    "1996":ACM.name,"1997":Juve.name,"1998":Juve.name,
    "1999":ACM.name,"2000":DLC.name,"2001":RM.name,
    "2002":Valencia.name,"2003":Lazio.name,"2004":ACM.name,
    "2005":"Not_Awarded","2006":Inter.name,"2007":Inter.name,
    "2008":Inter.name,"2009":Inter.name,"2010":Inter.name,
    "2011":ACM.name,"2012":Juve.name,"2013":Juve.name,
    "2014":Juve.name,"2015":Juve.name,"2016":Juve.name,
    "2017":Juve.name,"2018":Juve.name,"2019":Juve.name,
}


teams={
    RM:[],
    Barca:[],
    MU:[],
    Reds:[],
    Chelsea:[],
    MC:[],
    BVB:[],
    FCBayern:[],

}
leagues=[Germany_League,Spain_League,Italy_League,England_League]
local_cups=[Germany_CUP,Spain_CUP,Italy_CUP,England_CUP]

def TypeOf(Dict_Compet):
    if (Dict_Compet in leagues):
        return "League"
    elif (Dict_Compet in local_cups):
        return "CUP"
    else:
        return "UEFA_CUP"


# --------------- Initiate the seasons list --------------- #

seasons_list=list()

for key,value in UEFA_CUP.items():
    seasons_list.append(key)


l = len(UEFA_CUP)

#Initiating the dictionnaries of the teams and their trophies 

for team,value in teams.items():
    for year in seasons_list:
        value.append({
        "Team":team.name,
        "Country":team.country,
        "UEFA_CUP":0,
        "League":0,
        "CUP":0,
    })

#Updating the trophies function

def Update_Compet(Compet_winners):
    k=0
    for year,winner in Compet_winners.items():
        for team,value in teams.items():
            if winner==team.name:
                for j in range(k, len(seasons_list)):
                   value[j][TypeOf(Compet_winners)]+=1
        k=k+1

#-------------- UEFA trophies update --------------- #
print("------- UEFA --------")
Update_Compet(UEFA_CUP)

# -------------- CUP trophies update ------------- #
print("------- Spain_CUP --------")
Update_Compet(Spain_CUP)
print("-------- England Cup --------")
Update_Compet(England_CUP)
Update_Compet(Italy_CUP)
Update_Compet(Germany_CUP)

# -------------- League trophies update ------------- #
print("--------- Spain League ---------- ")
Update_Compet(Spain_League)
print("---------- England League -------- ")
Update_Compet(England_League)
Update_Compet(Italy_League)
Update_Compet(Germany_League)



# ----------- Final Step : Storing the data ---------- #
data =[]
year_index=0
for year in seasons_list:
    d={}
    d["season"]=year
    d["teams"]=[]
    for team,value in teams.items():
        d["teams"].append(value[year_index])
    year_index+=1
    data.append(d)

        
# ------------ JSON file creation --------------- #

with open('data.json', 'w') as outfile:  
   json.dump(data, outfile)
