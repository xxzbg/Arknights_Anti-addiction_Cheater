from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.tools.console.master import ConsoleMaster
from mitmproxy.http import HTTPFlow
from mitmproxy import master, http
from configparser import ConfigParser
import json, socket

# This is default settings
config = {'port': 12450, 'mode': 'dump'}


def run_web(options):
    webserver = WebMaster(options)
    return webserver


def run_dump(options):
    server = DumpMaster(options, with_termlog=False, with_dumper=False)
    return server


def run_console(options):
    server = ConsoleMaster(options)
    return server


def get_config():
    global config
    parser = ConfigParser()
    try:
        parser.read(r'config.ini', encoding='utf-8')
        config['port'] = int(parser.get("default", "port"))
        config['mode'] = parser.get("default", "mode")
        return True
    except Exception as e:
        print(repr(e))
        return False


def get_host_ip():
    try:
        session = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        session.connect(('8.8.8.8', 80))
        ip = session.getsockname()[0]
    finally:
        session.close()
    return ip


class antiAddictionCheater:
    def __init__(self):
        print(f"明日方舟防沉迷破解已在端口{config['port']}开启")
        self.fklist = ["line1-sdk-center-login-sh.biligame.net",
                       "line2-sdk-center-login-sh.biligame.net",
                       "line3-sdk-center-login-sh.biligame.net",
                       "line3-sdkcenter-login.bilibiligame.net",
                       "p.biligame.com",
                       "line1-log.biligame.net",
                       "line2-log.biligame.net",
                       "line3-log.biligame.net",
                       "line1-login.biligame.net",
                       "line2-login.biligame.net",
                       "line3-login.biligame.net"]
        self.entryGame = True

    def http_connect(self, flow: HTTPFlow):
        if flow.request.host in self.fklist or not self.entryGame:
            flow.request.host = "127.0.0.1"

    def response(self, flow: HTTPFlow):
        if flow.request.url.startswith(
            "https://ak-conf.hypergryph.com/config/prod/announce_meta/Android/preannouncement.meta.json") or flow.request.url.startswith(
            "https://ak-conf.hypergryph.com/config/prod/announce_meta/IOS/preannouncement.meta.json"):
            self.entryGame = True  # 进入游戏开始唤醒界面都会调用这个
        if flow.request.url.startswith(
            "https://as.hypergryph.com/online/v1/ping"):
            j = json.loads(flow.response.get_text())
            if self.entryGame:
                flow.response.set_text(
                    '{"result":0,"message":"OK","interval":5400,"timeLeft":-1,"alertTime":600}')
                self.entryGame = False
            if j['message'][:6] == '您已达到本日':
                print('您已达到本日在线时长上限或不在可游戏时间范围内，破解后仍可以继续游戏，但请合理安排游戏时间。')
            else:
                s = j['timeLeft']
                h = int(s / 3600)
                m = int((s - h * 3600) / 60)
                ss = int(s - h * 3600 - m * 60)
                print(f'游戏剩余时间{h}小时{m}分钟{ss}秒,已绕过限制,请合理安排游戏时间。')


addons = [
    antiAddictionCheater()
]

if __name__ == "__main__":
    if not get_config():
        ops = Options(listen_host='0.0.0.0', listen_port=config['port'],
                      http2=False, ssl_insecure=True)
        if config['mode'].lower() == "web":
            master = run_web(ops)
        elif config['mode'].lower() == "console":
            master = run_console(ops)
        else:  # dump
            master = run_dump(ops)
    else:
        ops = Options(listen_host='0.0.0.0', listen_port=config['port'],
                      http2=False, ssl_insecure=True)
        master = run_dump(ops)
    print(f"""
请在手机或模拟器中完成以下配置：
1.确保手机或模拟器和电脑在同一局域网下。
2.在游戏开始唤醒时进行以下操作，防止拦截游戏更新。
3.进入手机或模拟器 WLAN(Wi-Fi) 设置配置手机代理。
    安卓：修改网络--高级选项--代理--手动
    iOS：HTTP 代理--配置代理--手动
        服务器(存在多个本机ip时，请输入和手机同一局域网的 ip)：{get_host_ip()}
        端口：{config['port']}
    保存/储存
4.进入网站 http://mitm.it 下载证书(iOS为描述文件)并安装。
    iOS 多一步：设置--通用--关于本机--证书信任设置--mitmproxy--打开
5.重新进入游戏。
如果手机为安卓7.0及以上，请参考:
    方法1：使用安卓7.0以下版本的手机。
    方式2：Root 手机，安装 Xposed + JustTrustMe。
    方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或将游戏安装到安卓内模拟器 如: VMOS 等。
""")
    input('按[回车]继续...')
    master.addons.add(antiAddictionCheater())
    master.run()
