import os
import sys
import csv
import yaml
import time
from rich.console import Console
from rich.table import Column, Table
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import core.rprint as rprint

lst = []
result = []
domain = open('logs/domain.txt', 'w')

console = Console()

with open('./config.yaml','r', encoding='utf-8') as f:
    config = yaml.load(f, Loader=yaml.CLoader)

def subfinder(date):
    rprint.info(date, '正在调用subfinder进行子域名探测任务！')
    time.sleep(1)
    if config['system'] == 1:
        os.system('./core/plus/mac/subfinder -list domain.txt -t 100 -all -o ./logs/subfinder/%s -silent'%(date + '_subfinder.txt'))
        rprint.success(date, '已完成subfinder子域名探测任务！')
        time.sleep(1)
    if config['system'] == 2:
        os.system('./core/plus/linux/subfinder -list domain.txt -t 100 -all -o ./logs/subfinder/%s -silent'%(date + '_subfinder.txt'))
        rprint.success(date, '已完成subfinder子域名探测任务！')
        time.sleep(1)

def ksubdomain(date):
    rprint.info(date, '正在调用ksubdomain进行子域名探测任务！')
    time.sleep(1)
    if config['wild'] == True:
        if config['system'] == 1:
            a = os.system('./core/plus/mac/ksubdomain enum --band 1G -dl domain.txt --skip-wild --silent --only-domain --level %s --retry 1 --output logs/ksubdomain/%s'%(config['level'], date + '_ksubdomain.txt'))
            rprint.success(date, '已完成ksubdomain子域名探测任务！')
            time.sleep(1)
        if config['system'] == 2:
            os.system('./core/plus/linux/ksubdomain enum --band 1G -dl domain.txt --skip-wild --silent --only-domain --level %s --retry 1 --output logs/ksubdomain/%s'%(config['level'], date + '_ksubdomain.txt'))
            rprint.success(date, '已完成ksubdomain子域名探测任务！')
            time.sleep(1)
    elif config['wild'] == False:
        if config['system'] == 1:
            a = os.system('./core/plus/mac/ksubdomain enum --band 1G -dl domain.txt --silent --only-domain --level %s --retry 1 --output logs/ksubdomain/%s'%(config['level'], date + '_ksubdomain.txt'))
            rprint.success(date, '已完成ksubdomain子域名探测任务！')
            time.sleep(1)
        if config['system'] == 2:
            os.system('./core/plus/linux/ksubdomain enum --band 1G -dl domain.txt --silent --only-domain --level %s --retry 1 --output logs/ksubdomain/%s'%(config['level'], date + '_ksubdomain.txt'))
            rprint.success(date, '已完成ksubdomain子域名探测任务！')
            time.sleep(1)
def merge(date):
    rprint.info(date, '正在进行域名合并任务！')
    time.sleep(1)
    exists = os.path.exists('logs/ksubdomain/%s_ksubdomain.txt'%(date))
    if exists == True:
        with open('logs/ksubdomain/%s_ksubdomain.txt'%(date), 'r') as f:
            for line in f:
                lst.append(line.strip('\n'))
        f.close()
    else:
        rprint.error(date, 'ksubdomain结果为空！')

    exists = os.path.exists('logs/subfinder/%s_subfinder.txt'%(date))
    if exists == True:
        with open('logs/subfinder/%s_subfinder.txt'%(date), 'r') as f:
            for line in f:
                lst.append(line.strip('\n'))
        f.close()
    else:
        rprint.error(date, 'subfinder结果为空！')
    if len(lst) > 0:
        for item in lst:
            if not item in result:
                result.append(item.strip('\n'))
        for line in result:
            print(line)
            domain.write(line+'\n')
        domain.close()
    rprint.success (date, '已完成域名合并任务！')

def httpx(date):
    merge(date)
    rprint.info(date, '正在调用Httpx进行子域名验证任务！')
    if config['system'] == 1:
        os.system('./core/plus/mac/httpx -l logs/domain.txt -cdn -ec -content-length -title -tech-detect -status-code -match-code 200,301,302,304,403 -threads 500 -silent -csv -o logs/httpx/%s.csv'%(date + '_domain'))
        table = Table(show_header=True)
        table.add_column("ID", style="dim")
        table.add_column("IP")
        table.add_column('CDN')
        table.add_column("Url")
        table.add_column("Port")
        table.add_column("Title")
        table.add_column("Code")
        table.add_column("Length")
        table.add_column("Technologies")
        csv_reader = csv.reader(open("logs/httpx/%s_domain.csv".encode('latin-1').decode('utf-8')%(date)))
        ii = 0
        Output = open('result/domain.txt',mode='w', encoding="utf-8")
        for line in csv_reader:
            Url = line[10]
            if 'http' in Url:
                ID = ii
                IP = line[19]
                Port = line[4]
                Url = line[10]
                Title = line[13]
                Length = line[20]
                Code = line[22]
                CDN = line[29]
                Technologies = line[31]
                Output.write('%s\n'%(Url))
                table.add_row(
                    str(ii),
                    str(IP),
                    str(CDN),
                    str(Url),
                    str(Port),
                    str(Title),
                    str(Code),
                    str(Length),
                    str(Technologies.strip('[').strip(']'))
                    )
                ii += 1
        Output.close()
        console.print(table)
        rprint.success(date, '已完成httpx域名验证任务！')
    if config['system'] == 2:
        os.system('./core/plus/linux/httpx -l logs/domain.txt -cdn -ec -content-length -title -tech-detect -status-code -match-code 200,301,302,304,403 -threads 500 -silent -csv -o logs/httpx/%s.csv'%(date + '_domain'))
        table = Table(show_header=True)
        table.add_column("ID", style="dim")
        table.add_column("IP")
        table.add_column('CDN')
        table.add_column("Url")
        table.add_column("Port")
        table.add_column("Title")
        table.add_column("Code")
        table.add_column("Length")
        table.add_column("Technologies")
        csv_reader = csv.reader(open("logs/httpx/%s_domain.csv".encode('latin-1').decode('utf-8')%(date)))
        ii = 0
        Output = open('result/domain.txt',mode='w', encoding="utf-8")
        for line in csv_reader:
            Url = line[10]
            if 'http' in Url:
                ID = ii
                IP = line[19]
                Port = line[4]
                Url = line[10]
                Title = line[13]
                Length = line[20]
                Code = line[22]
                CDN = line[29]
                Technologies = line[31]
                Output.write('%s\n'%(Url))
                table.add_row(
                    str(ii),
                    str(IP),
                    str(CDN),
                    str(Url),
                    str(Port),
                    str(Title),
                    str(Code),
                    str(Length),
                    str(Technologies.strip('[').strip(']'))
                    )
                ii += 1
            else:
                continue
        Output.close()
        console.print(table)
        rprint.success(date, '已完成httpx域名验证任务！')