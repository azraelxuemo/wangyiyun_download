from json import loads
from httpx import Client
from os import system
client = Client(http2=True, verify=False)
print("这个只能用来获取非vip的歌曲（vip歌曲的接口暂时没有找到)")
print("#####################")
song_name = input("请输入想要下载的歌:")
print("#####################")
number = input("请输入想要看几个搜索结果:")
print("#####################")
url = 'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s=' + \
    song_name+'&type=1&offset=0&total=true&limit='+number
response = client.get(url)
result = []
i = 1
for song in loads(response.content)['result']['songs']:
    json = {}
    json['id'] = song['id']
    json['name'] = song['name']
    json['artist'] = song['artists'][0]['name']
    result.append(json)
    print("第"+str(i)+"首 歌曲名为:"+song["name"]+"歌手为:"+json['artist'])
    print("#####################")
    i += 1
i = int(input("请输入想要下载第几首歌:"))-1
print("#####################")
url = "https://music.163.com/song/media/outer/url?id=" + \
    str(result[i]['id'])+".mp3"

response = client.get(url)
url = response.headers['location']
if url == "http://music.163.com/404":
    print("这个歌暂时无法下载哦嘻嘻")
    system("pause")
    exit(0)
response = client.get(url)
file = open(result[i]['name']+'---'+result[i]['artist']+'.mp3', 'wb')
file.write(response.content)
file.close()
print("下载成功啦，文件名为"+result[i]['name']+'---'+result[i]['artist']+'.mp3')
system("pause")
exit(0)
