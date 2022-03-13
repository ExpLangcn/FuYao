import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import datetime as d
import core.domain as domain
import core.Vulnerability as vul

date = str(d.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

domain.subfinder(date)
domain.ksubdomain(date)
domain.httpx(date)
vul.vulscan(date)