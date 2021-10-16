from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.tools.console.master import ConsoleMaster
from mitmproxy.http import HTTPFlow
from mitmproxy import master, http
import json

# This is default settings
config = {'port': 8088, 'mode': 'dump'}


def run_web(options):
    webserver = WebMaster(options)
    return webserver


def run_dump(options):
    server = DumpMaster(options, with_termlog=False, with_dumper=False)
    return server


def run_console(options):
    server = ConsoleMaster(options)
    return server


class antiAddictionCheater:
    def __init__(self):
        self.entryGame = True

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


addons = [
    antiAddictionCheater()
]

if __name__ == "__main__":
    ops = Options(listen_host='0.0.0.0', listen_port=config['port'],
                  http2=False, ssl_insecure=True)
    if config['mode'].lower() == "web":
        master = run_web(ops)
    elif config['mode'].lower() == "console":
        master = run_console(ops)
    else:  # dump
        master = run_dump(ops)
    master.addons.add(antiAddictionCheater())
    master.run()
