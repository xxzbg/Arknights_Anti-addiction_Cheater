# Arknights_Anti-addiction_Cheater

基于 [mitmproxy](https://www.mitmproxy.org/) 实现中间人攻击绕开明日方舟防沉迷限制

通过设置 HTTP/PAC 代理的方式可以支持任意数量的设备、模拟器等多个用户使用。
*网络负载的承受范围之内*

## 配置 mitmproxy

### 修改端口和模式(可选)

端口及模式在`config.ini` 中

```ini
[default]
port = 12450 // 可修改1024~65535, 无特殊情况无需修改
mode = "dump" // 共有web、dump、console三种模式
```

### 安装依赖并运行

1. 下载好此仓库文件 / git clone
2. MacOS请打开终端, Windows请打开PowerShell或者CMD
3. 用`cd`命令进入到仓库目录
4. 安装依赖

```bash
pip install -r requirments.txt #pip无效可尝试pip3
```

或者

```bash
pip install mitmproxy
```

5. 运行脚本

```bash
python fcm.py
```

或者

```bash
mitmdump -s fcm-nobilibili.py --listen-host 0.0.0.0 --listen-port 12450
```

6. 进行手机端的操作

### 安装证书

请在手机或模拟器中完成以下配置：

1. 确保手机或模拟器和电脑在同一局域网下。

#### IOS 苹果

适用范围: iOS通过安装描述文件后全版本均可使用。

2. 进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。

iOS：HTTP代理--配置代理--手动
![](https://i0.hdslb.com/bfs/article/ec7e3ed3fb3b1bb3df5cf24a33922cd39e6c04a7.jpg)

3. 进入网站 http://mitm.it 下载描述文件并安装。

4. 设置--通用--关于本机--证书信任设置--mitmproxy--打开

> :warning: 此步必须在上一步完成后且电脑端开启着mitmproxy或运行着脚本时候进行)

![](https://i0.hdslb.com/bfs/article/e478d1bc37a358899d670a6bb2f9744dcff51abe.jpg)

#### Android 安卓

对于 Https 的中间人攻击需要自签 SSL 证书,然后 Android 从 7.0 开始系统不再信任用户 CA 证书。

*（应用targetSdkVersion >= 24时生效，如果targetSdkVersion < 24即使系统是7.0+依然会信任）*

对于大部分模拟器来说, 版本均在 Android 7 以下, 可直接使用。

**Android 7.0及以上**

- 解决方式1：Root手机，安装 Xposed + JustTrustMe。
- 解决方式2：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。


2. 进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。

安卓：修改网络--高级选项--代理--手动
![](https://i0.hdslb.com/bfs/article/318e9a0abec227de118d118144271d7611032704.jpg)
> 将服务器和端口设置为mitmproxy所监听的端口和主机ip。 例如此时我的电脑和手机处于同一局域网下，电脑的ip为192.168.1.48，端口在12450上开放。

3. 进入网站 http://mitm.it 下载证书并安装。
   ![](https://i0.hdslb.com/bfs/article/3c6435bb30b234adfd323673e590dd8c10909bc0.jpg)

#### 注意事项

- 按下 Ctrl+C 关闭电脑端程序
- 有时候 mitmdump.exe 会卡住，这时候按下 Ctrl+C 可以让其恢复 (此时要按下两次Ctrl+C关闭程序)

## 免责声明

本程序仅供学习使用，请在当地法律法规下使用。

不承担对于用户就使用本程序所提供的功能所引致的任何直接、间接、附带、从属等损失。
