# import urllib2, re
#
# rs_url = urllib2.urlopen('https://www.redshift3d.com/forums/viewforum/39/')
# html   = rs_url.read()
#
# regex = r"Version \d*\.\d*\.\d* is now available"
#
#
# matches = re.findall(regex, html, re.MULTILINE)
#
# print html
# print matches

import requests

r = requests.get('https://www.redshift3d.com/forums/viewforum/39/', auth=('neill@luma.co.za', 'P@ssw0rd1'))
print r.text