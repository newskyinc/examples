import httplib, urllib
import locale
import sys
import os
import time
import subprocess
import socks
import socket
import random
import hashlib
import pprint
import random

urllib.URLopener.version = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

#Initiate Tor
"""
print "[i] Initializing tor"
os.system("killall -9 tor")
time.sleep(2)
cmd = "tor"
p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
time.sleep(20)

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
"""

"""
match("<b>aaa</b><p><b>bbb</b></p>", "<b>", "</b>") => ["aaa", "bbb"]
"""
def match(data, left, right):
	result = []
	while (data.find(left) != -1 and data.find(right) != -1):
		if data.find(right) < data.find(left):
			data = data[data.find(right) + len(right):]
			continue
		myContent = data[data[0 : data.find(right)].rfind(left) + len(left) : data.find(right)]
		result += [myContent]
		data = data[data.find(right) + len(right):]
	return result

"""
Send out a HTTP request
"""
def readUrl(domain, url, params, cookie = None, ref = None, https = False):
	if (params):
		params = urllib.urlencode(params)
	#print "GET", url
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "User-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
	if cookie != None:
		headers["Cookie"] = cookie
	if ref != None:
		headers["Referer"] = ref
	if not https:
		conn = httplib.HTTPConnection(domain, 80)
	else:
		conn = httplib.HTTPSConnection(domain, 443)

	if params == None:
		conn.request("GET", url, params, headers)
	else:
		conn.request("POST", url, params, headers)
	response = conn.getresponse()

	if response.status != 200:
		print "HTTP Error:", response.status, response.reason
		return "err"
	data = response.read()
	return data

"""
Request a new IP using tor
"""
def changeIP():
	print "\n[i] Changing IP\n"

	os.system("killall -9 tor")
	time.sleep(2)

	cmd = "tor"
	p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	time.sleep(5)

def getDownloadURL(name):
	#https://apkpure.com/p/com.facebook.katana
	cookie = "hl=en"
	result = readUrl("apkpure.com", ("/p/%s" % (name)), None, cookie, "https://apkpure.com/", True)
	try:
		raw = match(result, "<a rel=\"nofollow\" class=\"ga down\"", "</a></p>")
		link = []
		for i in raw:
			link.append(match(i, "https://download.apkpure.com", "\">Download")[0])
		return link
	except:
		print "[i] %s: Parse Err\n" % (name)
		print "error"
		return None



startTime = time.time()
total = 0

#Package name here
name = "net.wappie.spyster"

try:
	#changeIP()
	result = getDownloadURL(name)
	print result
	for i in result:
		total += 1
		urllib.urlretrieve ("https://download.apkpure.com" + i.strip(), "./sample/%s_%d" % (name, total))
		print "[i] https://download.apkpure.com" + i.strip()
except:
	print "[i] Time used: %d" % (time.time() - startTime)
	print "[i] Total: %d" % (total)
	raise
	#sys.exit(1)
print "[i] Time used: %d" % (time.time() - startTime)
print "[i] Total: %d" % (total)