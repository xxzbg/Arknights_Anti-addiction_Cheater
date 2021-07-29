# Arknights_Anti-addiction_Cheater 

明日方舟防沉迷破解 / Arknights_Anti-addiction_Cheater  

利用 [mitmproxy](https://www.mitmproxy.org/) 来实现对明日方舟数据的中间人攻击，从而实现防沉迷的破解。
通过设置PAC代理的方式可以支持任意设备、模拟器使用，支持多个用户同时使用。

**仅供学习使用，被封号我不管，禁止违法用途。** ~~我已经爽够了（划掉~~

## 配置mitmproxy
此破解方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:
- 解决方法1：~~使用安卓7.0以下版本的手机。~~
- 解决方式2：Root手机，安装 Xposed + JustTrustMe。
- 解决方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。

请在手机或模拟器中完成以下配置：
1. 确保手机或模拟器和电脑在同一局域网下。

2. 进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。<br>安卓：修改网络--高级选项--代理--手动<br>iOS：HTTP代理--配置代理--手动<br>将服务器和端口设置为mitmproxy所监听的端口和主机ip。<br>保存/储存

 _例如此时我的电脑和手机处于同一局域网下，电脑的ip为192.168.1.48，端口在12450上开放。_![](https://i0.hdslb.com/bfs/article/318e9a0abec227de118d118144271d7611032704.jpg)
 _安卓操作_![](https://i0.hdslb.com/bfs/article/ec7e3ed3fb3b1bb3df5cf24a33922cd39e6c04a7.jpg)
 _iOS操作_

3. 进入网站 http://mitm.it 下载证书(iOS为描述文件)并安装。<br>iOS多一步：设置--通用--关于本机--证书信任设置--mitmproxy--打开<br>_(此步必须在上一步完成后且电脑端开启着mitmproxy或运行着脚本时候进行)_
![](https://i0.hdslb.com/bfs/article/3c6435bb30b234adfd323673e590dd8c10909bc0.jpg)
_安卓操作_
![](https://i0.hdslb.com/bfs/article/e478d1bc37a358899d670a6bb2f9744dcff51abe.jpg)
_iOS操作_

#### 注：
- 按下ctrl+c关闭破解
- 有时候mitmdump.exe会卡住，这时候按下ctrl+c可以让其恢复(此时要按下两次ctrl+c关闭破解)。

## 修改端口和模式
config.ini 中
```
[default]
port = 12450
mode = "dump"
```
"port = "后为端口，修改即可。
"mode = "后为模式，共有web、dump、console三种模式
