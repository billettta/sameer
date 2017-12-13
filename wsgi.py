#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
import nflgame
from decimal import *
from collections import defaultdict

def application(environ, start_response):

    games = nflgame.games(2016, week=15)
    if games:
        players = nflgame.combine_game_stats(games)
    else:
        players = []
    rossTotal = 0
    kyleTotal = 0
    rossWeek1 = 0.00
    rossWeek2 = 0.00
    kyleWeek1 = 0.00
    kyleWeek2 = 0.00
    rossQB1 = 'D.Carr'
    rossWR1 = 'D.Jackson'
    rossWR2 = 'D.Adams'
    rossRB1 = 'F.Gore'
    rossRB2 = 'R.Mathews'
    rossTE1 = 'K.Rudolph'
    rossFLX = 'B.Marshall'
    rossK = 'M.Bryant'
    kyleQB1 = 'D.Brees'
    kyleWR1 = 'E.Sanders'
    kyleWR2 = 'T.Pryor'
    kyleRB1 = 'B.Powell'
    kyleRB2 = 'S.Ware'
    kyleTE1 = 'C.Brate'
    kyleFLX = 'A.Robinson'
    kyleK = 'D.Bailey'

    kyleQB1Points = '0.00'
    kyleQB1Stats = ''
    kyleWR1Points = '0.00'
    kyleWR1Stats = ''
    kyleWR2Points = '0.00'
    kyleWR2Stats = ''
    kyleRB1Points = '0.00'
    kyleRB1Stats = ''
    kyleRB2Points = '0.00'
    kyleRB2Stats = ''
    kyleFLXPoints = '0.00'
    kyleFLXStats = ''
    kyleTE1Points = '0.00'
    kyleTE1Stats = ''
    kyleKPoints = '0.00'
    kyleKStats = ''
    rossQB1Points = '0.00'
    rossQB1Stats = ''
    rossWR1Points = '0.00'
    rossWR1Stats = ''
    rossWR2Points = '0.00'
    rossWR2Stats = ''
    rossRB1Points = '0.00'
    rossRB1Stats = ''
    rossRB2Points = '0.00'
    rossRB2Stats = ''
    rossFLXPoints = '0.00'
    rossFLXStats = ''
    rossTE1Points = '0.00'
    rossTE1Stats = ''
    rossKPoints = '0.00'
    rossKStats = ''
    ctype = 'text/plain'

    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        for p in players:
            if(p.name == kyleQB1):
	            kyleQB1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleQB1Points = round(kyleQB1Points,2)
	            kyleQB1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleWR1):
	            kyleWR1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleWR1Points = round(kyleWR1Points,2)
	            kyleWR1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleWR2):
        	    kyleWR2Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleWR2Points = round(kyleWR2Points,2)
	            kyleWR2Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleRB1):
	            kyleRB1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleRB1Points = round(kyleRB1Points,2)
	            kyleRB1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleRB2):
	            kyleRB2Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleRB2Points = round(kyleRB2Points,2)
	            kyleRB2Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleTE1):
	            kyleTE1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleTE1Points = round(kyleTE1Points,2)
	            kyleTE1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleFLX):
	            kyleFLXPoints = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            kyleFLXPoints = round(kyleFLXPoints,2)
	            kyleFLXStats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == kyleK):
	            kyleKPoints = Decimal(kyleKPoints) + (Decimal(p.kicking_xpmade) + Decimal(p.kicking_fgm) * Decimal(3))
	            kyleKPoints = round(kyleKPoints,2)
	            kyleKStats = str(p.kicking_xpmade) + " XP " + str(p.kicking_fgm) + " FG "
            if(p.name == rossQB1):
	            rossQB1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossQB1Points = round(rossQB1Points,2)
	            rossQB1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossWR1):
	            rossWR1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossWR1Points = round(rossWR1Points,2)
	            rossWR1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossWR2):
	            rossWR2Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossWR2Points = round(rossWR2Points,2)
	            rossWR2Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossRB1):
	            rossRB1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossRB1Points = round(rossRB1Points,2)
	            rossRB1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossRB2):
	            rossRB2Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossRB2Points = round(rossRB2Points,2)
	            rossRB2Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossTE1):
	            rossTE1Points = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossTE1Points = round(rossTE1Points,2)
	            rossTE1Stats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossFLX):
	            rossFLXPoints = (Decimal(p.rushing_yds)*Decimal(0.1) + Decimal(p.rushing_tds) * Decimal(6.) + Decimal(p.receiving_yds) * Decimal(0.1) + Decimal(p.receiving_tds) * Decimal(6.) + Decimal(p.passing_yds) * Decimal(.04) + Decimal(p.passing_tds) * Decimal(6.) + Decimal(p.rushing_twoptm) * Decimal(2.) + Decimal(p.receiving_twoptm) * Decimal(2.)  + Decimal(p.passing_twoptm) * Decimal(2.) + Decimal(p.passing_ints) * Decimal(-2.) + Decimal(p.fumbles_lost) * Decimal(-2.))
	            rossFLXPoints = round(rossFLXPoints,2)
	            rossFLXStats = str(p.rushing_yds + p.receiving_yds) + " Yds " + str(p.rushing_tds + p.receiving_tds) + " TDs " + str(p.passing_yds) + " PassYd " + str(p.passing_tds) + " PassTD " + str(p.fumbles_lost + p.passing_ints) + " TO " + str(p.passing_twoptm + p.rushing_twoptm + p.receiving_twoptm) + " 2pt"
            if(p.name == rossK):
	            rossKPoints = Decimal(rossKPoints) + (Decimal(p.kicking_xpmade) + Decimal(p.kicking_fgm) * Decimal(3))
	            rossKPoints = round(rossKPoints,2)
	            rossKStats = str(p.kicking_xpmade) + " XP " + str(p.kicking_fgm) + " FG "

    kyleWeek2 = Decimal(kyleWeek2) + Decimal(kyleQB1Points) + Decimal(kyleWR1Points) + Decimal(kyleWR2Points) + Decimal(kyleRB1Points) + Decimal(kyleRB2Points) + Decimal(kyleTE1Points) + Decimal(kyleFLXPoints) + Decimal(kyleKPoints)
    kyleWeek2 = round(kyleWeek2,2)
    rossWeek2 = Decimal(rossWeek2) + Decimal(rossQB1Points) + Decimal(rossWR1Points) + Decimal(rossWR2Points) + Decimal(rossRB1Points) + Decimal(rossRB2Points) + Decimal(rossTE1Points) + Decimal(rossFLXPoints) + Decimal(rossKPoints)
    rossWeek2 = round(rossWeek2,2)
    kyleTotal = Decimal(kyleWeek1) + Decimal(kyleWeek2)
    kyleTotal = round(kyleTotal,2)
    rossTotal = Decimal(rossWeek1) + Decimal(rossWeek2)
    rossTotal = round(rossTotal,2)

    response_body = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>Welcome to The Sameer</title>
<style>
.penishead {{
	background-color:#AC6F6C
}}
td.penisbody {{
	background-color:#D3AF8E
}}
td.balls {{
	background-color:#D5A28E;
	text-align:center
}}
</style>
</head>
<body style="text-align:center">
<h1>Welcome to the Sameer Bowl</h1>
<table style="width:80%" align="center"><thead><tr><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:27.27%" class="penishead" colspan=3>Current Scores</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th></tr>
<tr><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:27.27%" class="penishead" colspan=3>Kyle Week 1</th><th style="width:18.18%" class="penishead" colspan=2>{d[kyleWeek1]}</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th></tr>
<tr><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:27.27%" class="penishead" colspan=3>Kyle Week 2</th><th style="width:18.18%" class="penishead" colspan=2>{d[kyleWeek2]}</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th></tr>
<tr><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:27.27%" class="penishead" colspan=3>Ross Week 1</th><th style="width:18.18%" class="penishead" colspan=2>{d[rossWeek1]}</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th></tr>
<tr><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:27.27%" class="penishead" colspan=3>Ross Week 2</th><th style="width:18.18%" class="penishead" colspan=2>{d[rossWeek2]}</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th><th style="width:9.09%">&nbsp;</th></tr>
<tr><th style="width:100%;text-align:center" colspan=11><div style="width:70%;display:inline-block" class="penishead">Note, FG yardage bonuses and DST points are NOT INCLUDED.</div></th></tr>
<tr><th style="width:9.09%">&nbsp;</th><th style="width:18.18%" class="penishead" colspan=2><h2>Kyle Total:</h2></th><th style="width:18.18%" class="penishead" colspan=2><h2>{d[kyleTotal]}</h2></th><th style="width:9.09%" class="penishead">&nbsp;</th><th style="width:18.18%" class="penishead" colspan=2><h2>Ross Total:</h2></th><th style="width:18.18%" class="penishead" colspan=2><h2>{d[rossTotal]}</h2></th><th style="width:9.09%">&nbsp;</th></tr>
</thead>
<tbody>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleQB1]}</td><td class="penisbody">{d[kyleQB1Points]}</td><td class="penisbody">QB1</td><td class="penisbody">{d[rossQB1]}</td><td class="penisbody">{d[rossQB1Points]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleQB1Stats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossQB1Stats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleWR1]}</td><td class="penisbody">{d[kyleWR1Points]}</td><td class="penisbody">WR1</td><td class="penisbody">{d[rossWR1]}</td><td class="penisbody">{d[rossWR1Points]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleWR1Stats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossWR1Stats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleWR2]}</td><td class="penisbody">{d[kyleWR2Points]}</td><td class="penisbody">WR2</td><td class="penisbody">{d[rossWR2]}</td><td class="penisbody">{d[rossWR2Points]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleWR2Stats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossWR2Stats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleRB1]}</td><td class="penisbody">{d[kyleRB1Points]}</td><td class="penisbody">RB1</td><td class="penisbody">{d[rossRB1]}</td><td class="penisbody">{d[rossRB1Points]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleRB1Stats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossRB1Stats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleRB2]}</td><td class="penisbody">{d[kyleRB2Points]}</td><td class="penisbody">RB2</td><td class="penisbody">{d[rossRB2]}</td><td class="penisbody">{d[rossRB2Points]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleRB2Stats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossRB2Stats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleTE1]}</td><td class="penisbody">{d[kyleTE1Points]}</td><td class="penisbody">TE1</td><td class="penisbody">{d[rossTE1]}</td><td class="penisbody">{d[rossTE1Points]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleTE1Stats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossTE1Stats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleFLX]}</td><td class="penisbody">{d[kyleFLXPoints]}</td><td class="penisbody">FLX</td><td class="penisbody">{d[rossFLX]}</td><td class="penisbody">{d[rossFLXPoints]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleFLXStats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossFLXStats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">{d[kyleK]}</td><td class="penisbody">{d[kyleKPoints]}</td><td class="penisbody">K</td><td class="penisbody">{d[rossK]}</td><td class="penisbody">{d[rossKPoints]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody" colspan=2>{d[kyleKStats]}</td><td class="penisbody">&nbsp;</td><td class="penisbody" colspan=2>{d[rossKStats]}</td><td></td><td></td><td></td><tr>
<tr><td></td><td></td><td></td><td class="penisbody">KC</td><td class="penisbody">0.00</td><td class="penisbody">D/ST</td><td class="penisbody">Arizona</td><td class="penisbody">0.00</td><td></td><td></td><td></td><tr>
<tr style="height:60px"><td class="balls" colspan=5><img src="http://lawmagazine.pepperdine.edu/wp-content/uploads/2012/06/DCprogram07-183x275.jpg" width="100%"></td><td></td><td class="balls" colspan=5><img src="http://i.imgur.com/oATzXFS.png" width="100%"></td></tr>
<tbody>
</table>
</body>
</html>
'''

    response_body = response_body.format( d=defaultdict(str, kyleQB1=kyleQB1, kyleQB1Points=kyleQB1Points, kyleQB1Stats=kyleQB1Stats
,kyleWR1=kyleWR1, kyleWR1Points=kyleWR1Points, kyleWR1Stats=kyleWR1Stats
,kyleWR2=kyleWR2, kyleWR2Points=kyleWR2Points, kyleWR2Stats=kyleWR2Stats
,kyleRB1=kyleRB1, kyleRB1Points=kyleRB1Points, kyleRB1Stats=kyleRB1Stats
,kyleRB2=kyleRB2, kyleRB2Points=kyleRB2Points, kyleRB2Stats=kyleRB2Stats
,kyleTE1=kyleTE1, kyleTE1Points=kyleTE1Points, kyleTE1Stats=kyleTE1Stats
,kyleFLX=kyleFLX, kyleFLXPoints=kyleFLXPoints, kyleFLXStats=kyleFLXStats
,kyleK=kyleK, kyleKPoints=kyleKPoints, kyleKStats=kyleKStats
,kyleWeek1=kyleWeek1, kyleWeek2=kyleWeek2, kyleTotal=kyleTotal
,rossQB1=rossQB1, rossQB1Points=rossQB1Points, rossQB1Stats=rossQB1Stats
,rossWR1=rossWR1, rossWR1Points=rossWR1Points, rossWR1Stats=rossWR1Stats
,rossWR2=rossWR2, rossWR2Points=rossWR2Points, rossWR2Stats=rossWR2Stats
,rossRB1=rossRB1, rossRB1Points=rossRB1Points, rossRB1Stats=rossRB1Stats
,rossRB2=rossRB2, rossRB2Points=rossRB2Points, rossRB2Stats=rossRB2Stats
,rossTE1=rossTE1, rossTE1Points=rossTE1Points, rossTE1Stats=rossTE1Stats
,rossFLX=rossFLX, rossFLXPoints=rossFLXPoints, rossFLXStats=rossFLXStats
,rossK=rossK, rossKPoints=rossKPoints, rossKStats=rossKStats
,rossWeek1=rossWeek1, rossWeek2=rossWeek2, rossTotal=rossTotal
))
    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
