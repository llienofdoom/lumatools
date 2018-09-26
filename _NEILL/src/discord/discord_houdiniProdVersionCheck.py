import os, feedparser
from discord_hooks import Webhook

ver_file = os.environ['LA_ROOT'] + os.sep + '_' +  os.environ['LA_BRANCH'] + os.sep + 'etc' + os.sep + 'hou_latest_production_build'

# Get current version
current = open(ver_file, 'r').read()
c_maj = int(current.split('.')[0])
c_min = int(current.split('.')[1])
c_pnt = int(current.split('.')[2])
c_ver = c_maj + c_min + c_pnt
print 'Current version is %s - %d.' % (current, c_ver)

# Check rss for latest version
url_rss = 'https://www.sidefx.com/forum/feeds/forum/2/'
url_wh  = 'https://discordapp.com/api/webhooks/482545052963569679/vgKoDu7G-HsN9o51MC1mp4_PIhs3ODX9gXRN2Hfkzz4mXyc_dCVxPWPqvnJrR2fy41I7'

feed = feedparser.parse(url_rss)
builds = []
for i in feed['entries']:
    title = str(i['title'])
    if 'Production Build updated' in title:
        builds.append(title)

latest = builds[0].split(' ')[-1]
l_maj = int(latest.split('.')[0])
l_min = int(latest.split('.')[1])
l_pnt = int(latest.split('.')[2])
l_ver = l_maj + l_min + l_pnt
print 'Latest version is %s - %d.' % (latest, l_ver)

if l_ver > c_ver:
    print 'Latest is newer!'
    ver_file_write = open(ver_file, 'w')
    ver_file_write.write(latest)
    ver_file_write.close()
    msg = Webhook(url_wh, msg=builds[0])
    msg.post()
else:
    print 'Current version is latest.'
