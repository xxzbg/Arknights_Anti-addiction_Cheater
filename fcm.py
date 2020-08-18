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
        if flow.request.url.startswith("https://ak-as.hypergryph.com:9443/online/v1/ping"):
            j=json.loads(flow.response.get_text())
            print('明日方舟防沉迷破解: 禁用 防沉迷-游戏剩余时间')
            if entryGame:
                flow.response.set_text('{"result": 0, "message": "OK", "interval": 60, "timeLeft": 5400, "alertTime": 600}')
                entryGame=False
            else:
                flow.response = http.HTTPResponse.make(404)
            if j['result']==3:
                print('明日方舟防沉迷破解: 您已达到本日在线时长上限或不在可游戏时间范围内，破解后仍可以继续游戏，但请合理安排游戏时间。')
            else:
                s = 5400-j['timeLeft']
                h = int(s/3600)
                m = int((s-h*3600)/60)
                ss = int(s-h*3600-m*60)
                print ('明日方舟防沉迷破解: 您已在线'+str(h)+'小时'+str(m)+'分钟' + str(ss)+'秒，请合理安排游戏时间。')

addons = [
    fcm()
]
