---
dg-publish: false
author: 王垠
created: 2016-01-10
source: https://www.yinwang.org
---
> 以下内容是《[Tesla Model S的设计失误](http://www.yinwang.org/blog-cn/2015/12/12/tesla-model-s)》一文中新加入的小节。由于写作时间相距太远，而且由于它的[时效性](http://www.reuters.com/article/us-tesla-autopilot-idUSKCN0UO0NM20160110)，现在也把它单独提出来，独立成文。

两个月前，Tesla 通过“软件更新”，使 Model S 具有了初级的“自动驾驶”（autopilot）功能。这个功能可以让 Model S 自动地，沿着有“清晰边界线”的车道行驶，根据前后车辆的速度相应的加速和减速。

这貌似一个很新很酷的功能，咋一看跟 Google 的自动车有的一拼（其实差得天远）。然而在推出后不久，YouTube 上出现了一些视频（[视频1](https://www.youtube.com/watch?v=MrwxEX8qOxA)，[视频2](https://www.youtube.com/watch?v=Lx3-epk_ztQ)，[视频3](https://www.youtube.com/watch?v=LJnYCEQwtHs)，[视频4](https://www.youtube.com/watch?v=rkZ-jhLxrVc)，[视频5](https://www.youtube.com/watch?v=mLOG1bw3vSM)）。它们显示，autopilot 在某些情况下有可能进行错误的判断和操作，有些险些造成严重的迎面车祸。

![model-s-autopilot-frontal.png](/images/Tesla Autopilot/model-s-autopilot-frontal.png)

特别是[视频1](https://www.youtube.com/watch?v=MrwxEX8qOxA)显示，在路面线条清晰，天气很好的路上，autopilot 忽然向左，试图转向反方向的车道，差点导致严重的对撞车祸。仔细观察 autopilot 转向之前的情况，是由于路面上有阳光投下来的树影。Autopilot 误以为那是一个障碍物，所以试图把车转上反方向的车道！

从这个简单的视频我们可以看出：

1. Autopilot 没有对图像进行基本的“阴影消除”，它不能区分阴影和障碍物。阳光强烈，阴影明显的时候，autopilot 可能把阴影当成障碍物。阴影消除在计算机视觉已经研究挺多了，这说明 Tesla 有可能没有进行基础的计算机视觉研究。缺乏分辨阴影和障碍物的能力，这样的自动驾驶系统是完全不可接受的。
    
2. 道路中间有明显的，表示“禁止超车”的双黄线，对面有来车。Autopilot 为了避开“障碍”，冒着对撞的危险，左转跨越双黄线。这表示 autopilot 连基本的交通规则，紧急情况下的正确操作方式都搞不清楚。或者也许这软件里面连双黄线都没有识别，甚至连这个概念都没有。
    
    对于一个有经验的驾驶员来说，如果发现前方有障碍物，正确的作法不应该是猛烈地转弯避开，而应该是紧急刹车。从视频上我们看出，车子没有刹车减速（保持在 37~38），而是猛烈地左转。而且是等树影到了面前，才忽然进行操作，没有计算提前量。这说明设计 autopilot 的人，连基本的开车常识都不明白。
    
让我感到悲哀的是，这些视频的很多评论，大部分都在谩骂车主是傻逼：“这是车主自己的责任！”，“Autopilot 只能在高速公路上使用”，“只能在车道上有明确的边界线的时候使用！”，“不能在有很多弯道的地方“，“只能在能够看见前方 300 米道路的地方使用”，“谁叫你不看说明书的！”…… Elon Musk 也在一次[采访](https://www.youtube.com/watch?v=60-b09XsyqU)中明确的告诉记者：“如果用户因为使用 autopilot 而导致了车祸，是用户自己的责任！” 他反复地声明：“autopilot 还处于 beta 版本……” 意思是，你们小心着用！

我对这些说法持不同的观点。首先，Tesla 根本就不应该把一个处于”beta 状态”的功能，自动推送到所有 Model S 的系统里面。实际上，像 autopilot 这种功能，关系到人的生命安全，根本就不应该有”beta 版本”或者“测试版本”之说。Tesla 把这样不成熟的系统，强制推送给用户，然后又说如果出了事故，用户负所有责任，这是一种推卸责任的做法。要知道，没有任何人愿意拿自己的生命给 Tesla 做“beta 测试”。

另外，就算是用户没有仔细阅读 autopilot 的使用说明，在“不该”用它的地方（比如路面线条不清晰的地方）使用了 autopilot，如果出了车祸，Tesla 也应该负完全的责任。理由如下：

1. 作为用户，他们没有义务阅读并且深刻的理解 autopilot 的局限性。在软件行业，存在一种习惯性的“责备用户”的不良风气。如果软件的设计有问题，用户没记住它的毛病，没能有效地绕过，那么如果出了问题，一般被认为是用户的错。Tesla 想把软件行业的这种不正之风，引入到人命关天的汽车行业，那显然是行不通的。
    
2. Tesla 的 autopilot 实现方式幼稚，局限性实在太多。天气不好的时候不行，路面上的边界线不清晰也不行，光线不好或者有阴影不行，路上有施工的路桩不行，高速出口不行，…… 实际上，在如此苛刻的限定条件下，任何一个汽车厂商都可以做出 Tesla 那种 autopilot。
    
    我自己的便宜 Honda 车，就有偏离车道时发出警告的功能（Lane Drift Warning，LDW）。装个摄像头，来点最简单的图像处理就搞定。在 Indiana 大学的时候，我们有一门本科级别的课程，就是写代码控制一辆高尔夫球车（也是电动车呢），沿着路面上的线条自动行驶。这根本没什么难度，因为它能正确行驶的条件，实在是太苛刻了。
    
    其它汽车厂商很清楚这种功能的局限性，所以他们没有大肆吹嘘这种“线检测”的技术，或者把它做成 autopilot。他们只是把它作为辅助的，提示性的功能。这些汽车厂商理解，作为一个用户，他们不可能，也不应该记住 autopilot 能正确工作的种种前提条件。
    
3. 用户没有足够的能力来“判断”autopilot 正常工作的条件是否满足。比如，路上的线还在，但是被磨损了，颜色很浅，那么 autopilot 到底能不能用呢？谁也不知道。把判断这些条件是否满足的任务推给用户，就像是在要求用户帮 Tesla 的工程师 debug 代码。这显然是不可行的。如果 autopilot 能够在检测到道路条件不满足的情况下，自动警告用户，并且退出自动驾驶模式，那还稍微合理一些。
    
4. 用户也许没有足够的时间来响应条件的改变。Autopilot 自动驾驶的时候，车子有可能最初行驶在较好的条件下（天气好，路面线条清晰），然而随着高速行驶，路面条件有可能急速的变化。有可能上一秒还好好的，下一秒路面线条就不再清晰（[视频5](https://www.youtube.com/watch?v=mLOG1bw3vSM)貌似这种情况）。路面条件的变化突如其来，驾驶员没有料到。等他们反应过来，想关闭 autopilot 的时候，车祸已经发生了。这种情况如果上诉到法庭，稍微明理一点的法官，都应该判 Tesla 败诉。
    
5. Autopilot 显摆出的“高科技”形象，容易使人产生盲目的信任，以至于疏忽而出现车祸。既然叫做“autopilot”，这意味着它能够不需要人干预，自动驾驶一段时间。既然用户觉得它能自动驾驶，那么他们完全有理由在到达高速路口之前（比如 GPS 显示还有一个小时才到出口），做一些自己的事情：比如看看手机啊，看看书啊，甚至刷刷牙…… 不然，谁让你叫它是“autopilot”的呢？我坐飞机时，就见过飞行员打开 autopilot，上厕所去了。如果启用了 autopilot 还得一秒钟不停地集中注意力，那恐怕比自己开车还累。自己开车只需要看路，现在有了 autopilot，不但要看路，还要盯着方向盘，防止 autopilot 犯傻出错……
    
6. Tesla 把“beta 版”的 autopilot 推送给所有的 Model S，是对社会安全不负责任的做法。你要明白 Murphy’s Law：如果一个东西可能出问题，那么就一定会有人让它出问题。Autopilot 的功能不成熟，限制条件很多，不容易被正确使用，这不但对 Model S 的车主自己，而且对其他人也是一种威胁。汽车不是玩具，随便做个新功能，beta 版，让人来试用，是会玩出人命的。我觉得 Tesla 的 autopilot，跟无照驾驶的人一样，应该被法律禁止。由于 autopilot 的复杂性和潜在的危险性，使用 autopilot 的用户，应该经过 DMV 考核，在驾照上注明“能正确使用 Tesla autopilot”，才准上路。
    
7. 关系到人的生命安全的“免责声明”和“用户协议”，在法律上是无效的。在美国，到处都存在“免责声明”之说。比如你去参加学校组织的春游活动，都要叫你签一个“waiver”，说如果出了安全事故或者意外，你不能把学校告上法庭。这种免责声明，一般在法律上都是无效的。如果由于学校的过错而致使你的身体受了损伤，就算你签了这种 waiver，照样可以把学校告上法庭。我估计 Tesla 的 autopilot 在启动时，也有这样的免责声明，说如果使用 autopolit 而出现车祸，Tesla 不负责任。由于 autopilot 直接操控了你的车子，如果真的出了车祸，这跟其它的 waiver 一样，都是无效的。你照样可以上法庭告他们。
    
由于意识到这个问题，知道出了问题自己是逃不掉责任的，Tesla 最近又通过强制的软件更新，对 autopilot 的功能进行了一些[限制](http://www.reuters.com/article/us-tesla-autopilot-idUSKCN0UO0NM20160110)，说是为了防止用户“滥用”autopilot 做一些“疯狂”的事情。Tesla 很疯狂，反倒指责用户“滥用”和“疯狂”。这让人很愤慨。

对 autopilot 进行限制的同时，Tesla 又推出了 beta 版的“[自动趴车](http://www.cnet.com/news/tesla-cars-can-now-self-park-at-your-command)”和“召唤”（summon）功能。这些功能貌似很酷，然而它们也附带了许多的限制条件。你只能在某些地方，满足某种特定条件，才能用这些功能。如果你违反这些条件，出了事故，Tesla 声称不负责。

这些能够让车子自己移动的功能，跟 autopilot 一样，同样会给社会带来安全隐患。比如，有人在不该使用自动趴车和 summon 功能的地方用了它，就可能会导致车祸。这不是用户的问题，而是 Tesla 根本不应该发布这些不成熟的技术来哗众取巧。

![kimi](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAA6YSURBVHgB7Z09bBTbFcev1wYkA4mLB4lepLBOkwgKL4pIFYl10mEp2OLDUGGnxFJsCihjOyUubAq7jE2FYluyKewu8bqFgk2B9VJ5XTwKoNj3EJbAZsn5z5u7unP3zsyd3Znd+bg/abS7s7s8vz3/e+455351sRSysbGR//z5cyGXy+Xp5YWurq6+r1+/5nHhfXqdV32P3q/Qe1V6WqXnVXpeoecHdJXx+vbt22WWMrpYwoGxj46OimSsAXqJRxi6j0UAxEH/NkRQrtVquydPniyPjIxUWIJJnADI4H3Hx8cFenqdjDHs1prbSJn+BniIp7du3SqxhJEYAaytraF136Onw1G18Faxu4/NL1++PB8dHd1kCSDWAlhdXS3Qj3qdrqkgRv/48SOrVCrs3bt31iNe4zku/j4umfPnz7Pe3l52+vRp68rn89ZrPOLCPV3s+KHU3d09G+duIpYCQGunh2m6ijqff/36tWXovb096/Ht27csCs6dO8f6+/vZxYsXLUFcunRJ96slumbj2EXESgC6hkfrLZVK7OXLl/UW3gngESCCK1euWKKAB/ECXoGCx1nKJlZYTIiFAHQMLxodLT6OQAzFYtFXDHESQkcFgBSOIvpl5mF4GJsbvlMtvRkgBFxe3QTFNZsnTpx40MkYoSMCsFO5SXo64/YZGJ48Q2xbuy6IFYaGhiwxeDDT09PzhIRQZW2m7QKw07llXpWTgcEXFxfrEXtaQABJLt9VCOgW6DcZb3eg2DYB2K0e/fyU6v20tHg/IISJiQmvrmGBRPCAtYm2CAB9PRVHdlStHinb0tJS6g0vA09AhlYGi/AGVD8YbEdsELkA1tfXUb1bUBVytra2rFafpOAuTJBGIj6AEBRUqdHM3rlzZ4FFSKQCIOPOM4XLz2qrdwPdwszMjFvqOEMCmWUREYkA0N+TehHoDcvvZb3VuwFvgCDx2rVrDe/Z6eJ4FFlC6AKwc/sNeloQ78PgMDwEYHAHXcLY2FjD/ajiglAF4BbsweXPzc1ZZVuDP25dQhQiCE0AbsaH0R8/fpy6vD5q2iWCUATgZnyUb1HUMf19cyAuQM0Ag00iYYqgZQG4GR/1exjf0DoQgVxBDEsELQnAjvZfGeNHj0oERJnGEAZbyQ5yrAXsVC8v3jPGjwb8pvhtJQpHR0fLrAWaFgCldNNyns/7fEM04LfFbyxCXcGwXXBriqYEQOXdhqFcpHrG+NGD31iRTk/ZJffABBYAgj6mMD5SFhPtRw9+Y6TV8rxH8sYLtm0CEVgAdsTvGNiB8U2e3z7wW6Owdnh4KN5GQL6DwJwFIJAA0NfIQd/KyooxfgdAN7C6uuq4B9vYcy600RaAPXHTMbKHur6p7XcO/Pbb29vy7SnbVlpoCQBuBdO4xHvogzC4Y+gs8AJyPABb6XYFWgLABE7Z9ZugLx7ABphbIWJ3BVM63/cVgCrqR8s3/X58wMQaRVcwrZMV+AqAIktHkQHuxvT78UPVFdhrLjzJ+fyjY3K1z8zmiSeqroAo+gWEngLI5XKOlIKv0jHEE9hHMc/SMy10FYDd+vPiPVPqjT+KzMzTC/S4vYHWTwKov0bLN4FfcH72qyLr+81fWF//dXbqbN669+H7Xfb+u6fsw5td9unHCgsT7gWkhSfwAiXV55XzAWzF7Ij37t+/bwQQkF//cZ79YuBvru9/+lBhlX//lf1IgggTTCdTxAODqmVnbh7A0W+0s/UXCgXW1+dfw6hWq6xcjm7TLr4rSLN/h5/xATzCb4f/w/63+adQRQBb6XqBBg9gT+veF+89fPiwbTN6xW7HC4hycHCQRcX+/r6WADAWMj4+7rj3ze/usf4//5PpAk/w+l+/Z18+hTftH8ZHsU6EftvL8lZ3DUEg5f0NkX/WpnNjXr6O8cHsbOOinW//8HcWBHiCXw5MsjBRZQSYPCJ/TpUFFMUXWUz7pqf1BtTw28iN4ywFfTzYC8LZb6+ysFHYrkFlDgGsr68Pi6kfKktZE0Crrf/U2QusGXq/GWBhg+lj8pwBOSWUPcB18QV23coauq0fLT/MxtF9KvytD/m+SiL2Xot1ZAE4+gjT+t1Rtf5WOHz/XxYFL168cLxGaV8cKq4LAK5BnOoF95+15dv37unNq0TrR/QfJofvo0lpYUO5G7C32rWoC0B2DVlz/3xXLx3Cbv3gzct/sKiQPbk4wJcTbjqWc8uuI+10svW/eTkbeklYRLYllfnrsZ4lAHvigEMAWfIA6PdVa/JVPH36lIUJxgS+fxFd6wdyqopMj08WsQRAxR+H8dFvZGnMXzfyB2G1/s9U/duncQBcUQNbyvFcrVYr4pGPBRTFN7NU+QvS+mF8v98GI31+RkXAF1XU78bBwYFjbIA3eksA5BIcVYgsRf9BWr9O8Ie6/qfvKixuwKbS/kNW6dHqAigDcHQBWfEAYbf+OIPBLRF+0kqOgoGCmP/zwxWygG7kD6JI/doJbCrXAxAI5qgo4KhBZqX1Y86BbutXDfokEdkLWCerMSn9y4oAhoeHO1b27RSyZ8exejn51C3JTaQW3eBvc3MzNWMiqnoAPIBj/FJ2E2lEd9AHP9iDB23buDty5NoOeYCf5+S1/lnwADqtH8bHlLM0dYlyF8A9gEMAaa8A+rV+TPJEn3/58uXUxUOKVcT5HngAelK/mRQPgNnDOzs7TX3PDRgfRr969ap1qd7b3d21ZgGnRRxda2trjmm4LnvXtw3dWcGdBoUheIokCQE7j8pjGS3tE5hl0JW8evWKTU1pLcOPBaru3QigBVBMmp+fDzSeEDeMADRA/+8FFmAEKSvHCSMADVAM8mNhYUFrSVvcaBBAkBOyswIifz9g/CTFAxwUgiriDSMAJ0Ei/cnJyVh7AawaFsGW86YL8AD5vrzA0gsY36vO0GnOnDnjeF2r1aoYDKqIN2WVZBVM/mxm9XGcBdDb2+t4TbavwgMciDe9jj1PO4j2+bJz5Pl+0b+KgYHw1/iFhdy9U/f/Qw9UIFbfZJXEFRhKXpffKmmfC6EYA6n0yEGg7iSJOJC1fQtaRfYAVhBoYoDscOFCw9L1cu7o6MixKjFJHsAQjP7+fsdr8v7V3N27dyuIA/hNuIksB4JpBTaV4rsq9guy6gByHKBwFYaEo/DslufnC0MctU5pezFDCpBtSo3eWptmCYAqQiYOSDmyVycBlPDIVweXxDehFjMmkB5gS9kD8EZvCQCBYJLrAQZvFO6/DJvjeX0wKJfLPRc/JJ9YbUgusi3J1vUuX9wixjHrQXe/HEP8UXiA+jYndQH09PSU5XqAyQaSD2woVXer4q7hdQHgCHJShukGUobsyamROzy9PCFkRf6yyQaSjezFKeNzNHKHAOAa5G7AeIHkggYsun9keqOjo54eAB96Iv8jhmQi246i/5L8GZUAHAqBCzHBYPLAyJ9sNxr5bdjpokEA9okSJfFep9cLGoIj7QgGSrz4I+I2K9ihFCjJDBEnB9hK0XUr97lRCsDOE0viPZwaZkgGssdG8Kc6MQx4rQto8AImFog/QVo/cBWAyguYWCD+yJ4arZ/iuhW3z7ueHGoD5RT5C+4FotxKVndLtnbOCMYKId2/K8qzDP1Ay1d4ac8/vIv5sLa2hn1Yivw1NhrCOYLmBPF4gaLd3NycXPjZpNY/4vU937WBx8fHjtUX+A+YriB+IO2Tp/RT2dd3jztfAdi5o8ONDA0NmYAwRiDwo5Yu355V5f0yWquDaah4QZ4xNDExYQaKYgBsoDgitgKb6XxfSwAYKqZBItMVxBDYQLHufxw20/m+9v4A9kihY6AIXYGi5GhoE/j9cYlgMM+t6KMi0AYR3d3dM3JXgL7HTCBtP+j35e3u7Zw/0D41gQQAt0KR5aA8Z+DRo0dmrKCN4LdW7Fxi2YYFJPAWMYgsa7WaI71AH4TagAkKo4cHfYpV3FpRv0xTewShtCjHA+gGzIBR9CD7Uhmf+n2tqF/GtxLoxfr6+oZ4DCnAzh2Li4vMED5oYPK+RZjkefPmzRHWJC3tEkZBIVJDR/Eb9Wio1BAuKuMj6LNt0DQtCQBBIZWKR+TMwIggXNyMj6BPN993o6UugPPs2bM8KXFHPn8IhxYvLS2ZgaMmQcCHhiTPzObGbybokwlFAMBNBBg9RNQqn1Zh8AapHjIrucYSpvFBaAIARgThAKOjtiJH+2EbH4QqAOAmArC8vMy2t7eZwR2UdlFdVezXWEa8FabxQegCABsbG32k1GU5RQRbW1uYZGLiAgn09xjYkWv7AKkeov1WAz4VkQiAQ4aeoYeG4zRMl+AEcytcCjzW4E7Q+n4QIhUAIBFMkYKn5fMJwerqqtUlZNUbeLV6oprL5R7cuHFjhUVI5AIAXnEBvAGEkJbjWXXxafWhB3tutEUAHCodY2bRpOo9zDRGzSDt3QIMj1bvNqUOLv/EiRMzUfT3KtoqAEBdQpH+J5dV3gDAEyBITJsQkNejoudheOzYOh5kMkcYtF0AAFkCpTQIbFzPW4MQkDEkfUdwvxZvM4s5fO1q9SIdEQAHsQG5u3lVushB1wAxJClG4BtruCzUEClh2n07+no3OioADgWBY/Qw7dYtAASLXAxRrkxqBRgbhsfAjc/BGyX20xh+iXWYWAiAoyMEwMWAwaa9vb2OpZFo6SjbahodlFhMDM+JlQA4CBTZT/FBUefzEANiBTweHBxEFkAikMOeu2jpMHyAxTElFjPDc2IpAA5iBAqOMBP5qp9XEDk8PGT7+/uWKPhzPMJT4FElELRmPqcRuTku3sLxHFuuBDxPCQHdE3t9XudWjPoQawGIUA1h2A4Wr9MV19MZsYBmEztxxrG1q0iMAETsLmKMLpzR1tGD+uzZUM9heOy22olUrhUSKQARO5Us1Gq1IhmBCyIqDwHjYmd1HLBRpv9uiQxeYQkm8QJQQdlEgcQAERTIWHkaVLlgD0b14dEtnuBzG3GSGi4S1Q/8OY1llJNubBX/B9Di4rYoX+f6AAAAAElFTkSuQmCC)
