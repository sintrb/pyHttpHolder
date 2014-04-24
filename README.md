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
