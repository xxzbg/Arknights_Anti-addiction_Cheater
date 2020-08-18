# Arknights_Anti-addiction_Crack 

明日方舟防沉迷破解 / Arknights_Anti-addiction_Crack 

利用 [mitmproxy](https://www.mitmproxy.org/) 来实现对明日方舟数据的中间人攻击，从而实现防沉迷的破解。
通过设置PAC代理的方式可以支持任意设备、模拟器使用，支持多个用户同时使用。

**仅供学习使用，被封号我不管，禁止违法用途。**~~我已经爽够了（划掉~~

## 使用说明

1. 下载mitmdump.exe，放入脚本同级目录。

2. 执行 明日方舟防沉迷破解.bat。

3. 按照bat配置手机代理。

4. 按照bat在手机或模拟器中信任mitmproxy证书(进入网站 http://mitm.it/ 下载)。

5. 在bat按任意键继续。

6. 信任Windows防火墙。

7. 进入游戏~~享受没有防沉迷的快乐。~~

#### 注：
- 按下ctrl+c关闭破解
- 有时候mitmdump.exe会卡住，这时候按下ctrl+c可以让其恢复(此时要按下两次ctrl+c关闭破解)。
- 此方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:<br/>解决方法1：~~使用安卓7.0以下版本的手机。~~<br/>解决方式2：root手机，安装 Xposed + JustTrustMe。<br/>解决方式3：不root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。

## 修改端口
明日方舟防沉迷破解.bat 第二行
```
set porxy=12450
```
"porxy="后为端口，修改即可。
