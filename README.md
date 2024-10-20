# YuanKouSuan_iOS

可在iOS平台上自动解决小猿口算比大小pk场

思路也是最基本的模拟

## Preliminaries
确保已经在手机上打开了UI Automation，Mac上安装好了Appium，WebDriverAgent和Xcode.

[WebDriverAgent的安装](https://blog.csdn.net/zhang_jiamin/article/details/138192418)

[Appium的安装](https://blog.csdn.net/zhang_jiamin/article/details/138189033)

请提前使用pip,homebrew安装mitmproxy，并在手机上安装相应证书，确认完全信任。

[mitmproxy的安装](https://blog.csdn.net/2301_78843735/article/details/138803809)

## Usage
用数据线连接手机与Mac, 并在Mac上运行WebDriverAgent与Appium，此时手机上应当出现**Automation Running**字样.
在目录下执行（这里默认的监听端口为8080）
```
mitmdump -s save_body.py --set block_global=false
```
并且在手机上手动设置代理为电脑ip，端口就是8080.

然后运行
```
python3 main.py
```
程序将在检测到获得题目（文件名为response）后等待12秒开始做题。

## PS
代码中的deviceName, udid需要结合自己的设备进行修改，否则无法运行.

此外模拟光标运行轨迹的坐标也应该结合实际情况修改，这里坐标在iPhone 14 Pro Max上运行合理.

如有问题，欢迎提出issues! 

:D