@echo off
set porxy=12450
:run
cls
echo.
echo.此破解方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:
echo.    解决方法1：使用安卓7.0以下版本的手机。
echo.    解决方式2：Root手机，安装 Xposed + JustTrustMe。
echo.    解决方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。
echo.
echo.请在手机或模拟器中完成以下配置：
echo.1.确保手机或模拟器和电脑在同一局域网下。
echo.2.建议在游戏开始唤醒时进行以下操作，防止拦截游戏更新。
echo.3.进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。
echo.    安卓：修改网络--高级选项--代理--手动
echo.    iOS：HTTP代理--配置代理--手动
echo.        服务器(存在多个本机ip时，请输入和手机同一局域网的ip)：
for /f "delims=: tokens=2" %%i in ('ipconfig ^| find /i "IPv4"') do echo.        %%i 
echo.        端口：%porxy%
echo.    保存/储存
echo.4.进入网站http://mitm.it下载证书(iOS为描述文件)并安装。
echo.    iOS多一步：设置--通用--关于本机--证书信任设置--mitmproxy--打开
echo.5.重新进入游戏。
echo.
pause
echo.
echo.按下ctrl+c关闭破解
echo.有时候mitmdump.exe会卡住，这时候按下ctrl+c可以让其恢复(此时要按下两次ctrl+c关闭破解)。
echo.
mitmdump.exe -s .\fcm.py --ssl-insecure -p %porxy% --no-http2 -q
