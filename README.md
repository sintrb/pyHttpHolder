# HttpHolder

用于自动处理Http请求时产生的Cookie，保持HTTP状态（会话）等等，可用于机器人、爬虫。


## 使用举例
代码：
``` Python
headers = {
	# Chrome User-Agent
	'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
	}
# 使用Chrome的User-Agent，设置默认超时为10s
h = HttpHolder(headers=headers, timeout=10)

# 请求豆瓣首页并以便获取相关Cookie，该次请求使用GET方法
h.open_html('http://www.douban.com')


# 登陆表单
form = {
	'email':'abc@def.com',
	'password':'123',
	'app_name':'radio_desktop_win',
	'version':'100'
	}
# 尝试登陆，该次请求使用POST方法，因为data有数据，返回JSON字串
res = h.open_html('http://www.douban.com/j/app/login', 
				headers={'Referer':'http://www.douban.com'}, 
				data=form)
# 解析JSON
reso = json.loads(res)
if 'err' in reso:
	# 有错误，输出
	print reso['err']

# 打印现在的Cookie
print h.get_cookiesdict()
```

输出：

>wrong_password

>{'bid': '"BHg/jlaAdOs"', 'll': '"118348"'}


=

## 怎么获取这些代码？

* 如果你只是想简单的使用这些代码的话你可以把它当作一个压缩包下载到你的电脑上，点击右边的“Download ZIP”:

![image](https://raw.githubusercontent.com/sintrb/forgithub/master/img/screenshots/githubdownloadzip.png)


* 如果你喜欢这些代码，那么你可以加星：

![image](https://raw.githubusercontent.com/sintrb/forgithub/master/img/screenshots/githubstart.png)

* 如果你觉得这些代码还有很多可以改善的地方，那么请先fork一下（欢迎fork）：

![image](https://raw.githubusercontent.com/sintrb/forgithub/master/img/screenshots/githubfork.png)

* fork之后这些代码就变成了你的了，你可以从自己的仓库中把它们clone到你的电脑上，之后的操作就和git一样了：

![image](https://raw.githubusercontent.com/sintrb/forgithub/master/img/screenshots/githubsshclone.png)

**享受开源带来的乐趣吧**
