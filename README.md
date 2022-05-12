# FuYao - 扶摇直上九万里 - 转Go 不再维护Python项目

## **[加入Discord](https://discord.gg/GCZzJmzW3G)** | **[WanLi](https://github.com/ExpLangcn/WanLi)** ｜[LICENSE](LICENSE)| **[问题解决](https://github.com/ExpLangcn/FuYao/wiki/help)**｜**[FuYao - Go](https://github.com/ExpLangcn/FuYao-Go)**

**自动化进行资产探测及漏洞扫描｜适用黑客进行赏金活动、SRC活动、大规模攻击使用**

## 法律免责声明
本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。 在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。 如果发现上述禁止行为，我们将保留追究您法律责任的权利。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任. 您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。

# 更新日志

* V1.3
    - 修复编码问题（应该是修复了...还是报错的话看一下终端编码是不是有问题）
    - 修复Ksu不运行问题（原因是会跳过泛解析问题，现在可以在config文件内判断是否跳过）
    - 修复httpx结果为空问题
    - 优化子域名枚举速度
    - 优化漏洞扫描速度
* V1.2
    - 新增Docker一键部署 感谢群成员 [@l0ners](https://github.com/l0ners) 支持!
* V1.1
    - 修复报错logs问题
* V1.0
    - 脚本发布

# docker使用教程

`domain.txt` 存放目标一级域名（主域名）

```
docker pull explang/fuyaov:v1.3
docker run -d -it --name fuyao explang/fuyao:v1.3
docker exec -it -w /FuYao fuyao bash
```

在domain.txt文件中添加主域名后执行下方命令即可开始自动化扫描（主域名 = xxx.com 这种的！www.xxx.com 属于二级域名！）

```
vim domain.txt
python3 FuYao.py
```

# 源代码使用教程

`domain.txt` 存放目标一级域名（主域名）

`config.yaml` 配置扫描器

```
git clone https://github.com/ExpLangcn/FuYao.git
cd FuYao & pip3 install -r requirements.txt & mkdir logs result logs/subfinder logs/ksubdomain logs/httpx
vim config.yaml
```

在domain.txt文件中添加主域名后执行下方命令即可开始自动化扫描（主域名 = xxx.com 这种的！www.xxx.com 属于二级域名！）

```
vim domain.txt
python3 FuYao.py
```

**注：目前工具仅限支持Mac系统及Linux系统，建议使用Linux系统！扫描速度与网络有关，建议VPS最少5MB宽带。**

# BiLiBiLi

**[RedCodeTm](https://www.bilibili.com/)**

# Twitter

**[@ExpLang_Cn](https://twitter.com/ExpLang_Cn)**

# 微信群

<img width="400" height="550" src="img/WechatIMG455.jpeg"/>

# 作者微信

<img width="400" height="550" src="img/WechatIMG408.jpeg"/>

# 知识星球介绍：

【**一次付费 永久免费**，到期联系运营即可免费加入】 

星球面向群体：主要面向信息安全研究人员. 

更新周期：最晚每两天更新一次. 

内容方向：`原创安全工具`｜`安全开发`｜`WEB安全`｜`内网渗透`｜`Bypass`｜`代码审计`｜`CTF`｜`免杀`｜`思路技巧`｜`实战分享`｜`最新漏洞`｜`安全资讯`

<img width="400" height="550" src="https://mmbiz.qpic.cn/mmbiz_jpg/9wVk7PSWIjJQzLyRNhDuxwPovLKzY8xqOqAZnicV5ud9Xbic88kerYd3Iyq50wr2kESufRYYR9b9VPCgDc10cdLQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1"/>

# Info

* **[ksubdomain](https://github.com/knownsec/ksubdomain)**
* **[subfinder](https://github.com/projectdiscovery/subfinder)**
* **[httpx](https://github.com/projectdiscovery/httpx)**
* **[nuclei](https://github.com/projectdiscovery/nuclei)**
