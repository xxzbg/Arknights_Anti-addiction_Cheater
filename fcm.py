import mitmproxy.http

from mitmproxy import ctx, http
import json
entryGame=True

class fcm:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "ak-gs-localhost.hypergryph.com":
            flow.request.host = "ak-gs.hypergryph.com"
            flow.request.port = 8443
        elif flow.request.host == "ak-as-localhost.hypergryph.com":
            flow.request.host = "ak-as.hypergryph.com"
            flow.request.port = 9443
    
    def response(self, flow: mitmproxy.http.HTTPFlow):
        global entryGame
        if flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/Android/preannouncement.meta.json") or flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/IOS/preannouncement.meta.json"):
            entryGame=True #进入游戏开始唤醒界面都会调用这个
        if flow.request.url.startswith("https://as.hypergryph.com/online/v1/ping"):
            j=json.loads(flow.response.get_text())
            if entryGame:
                flow.response.set_text('{"result":0,"message":"OK","interval":5400,"timeLeft":-1,"alertTime":600}')
                entryGame=False
            else:
                flow.response = http.HTTPResponse.make(404)
            if j['message'][:6]=='您已达到本日':
                print('明日方舟防沉迷破解: 您已达到本日在线时长上限或不在可游戏时间范围内，破解后仍可以继续游戏，但请合理安排游戏时间。')
            else:
                s = j['timeLeft']
                h = int(s/3600)
                m = int((s-h*3600)/60)
                ss = int(s-h*3600-m*60)
                print('明日方舟防沉迷破解: 游戏剩余时间 '+str(h)+'小时'+str(m)+'分钟' + str(ss)+'秒 修改为 不限制，但请合理安排游戏时间。')

addons = [
    fcm()
]
