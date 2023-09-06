# skyland-auto-sign

明日方舟森空岛一键签到脚本，基于python

有三种方法部署
> 1.自己手动在电脑上运行（不想挂载在服务器上的用户推荐这个，因为可以配合MAA一键签到）
>
> 2.在云函数上部署（推荐，省时省力，不用装环境，几乎不用管）
>
> 3.使用Github Actions托管（相比云函数来讲非常推荐，因为有日志会存储，而且也免费）

## 快速导航
- [在自己电脑上运行](#mode1)
  - [配合MAA运行](#maa)
- [在云函数上运行](#mode2)
- [使用Github Actions托管](#mode3)
- [多账号支持](#multiple_account)
- [多端登录问题](#multiple_login)


[视频用法]( https://www.bilibili.com/video/BV1DP411h7s6)

<a id="mode1"></a>
## 方法1

1.先装python（3.6及以上）且安装requests库.cmd 运行`pip install requests`

2.下载脚本`skyland.py`

3.双击本文件（弹出一个黑框框代表你成功了）
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/cd67b87f-75f2-46c4-b55f-82721e97c9bb)

（以上3步可以用我打好的exe文件直接运行，链接见release或者[百度网盘](https://pan.baidu.com/s/1RPi6JyA3iUUv5ubNsoyqIw?pwd=wn4e)（就10m下载很快的））

4.本软件有3种模式：

第一个模式和第二个模式不多说了，填入你的信息即可。

就是注意一下输入的密码是不会显示的，但实际是有的，这点需要注意一下！

如果第一种模式和第二种模式你都没法过人机验证的话，可以使用第三种模式：

登录电脑的森空岛[官网](https://www.skland.com/)
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/641796be-46c9-4bf3-bb8b-12fdc9e663a4)

登录完成后，访问[这个网址](https://web-api.skland.com/account/info/hg)。然后复制这里的所有内容，粘贴进去即可。
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/4176e197-93f4-45fa-b972-1e2737c32a0f)

最后再次启动的时候，脚本就不会再询问你是否添加账号了，而是直接帮你签到了

<a id="maa"></a>
### MAA支持

可以使用MAA自动执行脚本

MAA在连接设置里有运行前脚本，输入`skyland.py`的路径后，每次连接模拟器时会自动帮你签到。

如果你用的exe版本的，请输入`skyland.exe`的路径！
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/36e5583d-a923-4681-a5dd-3ac8370fcd87)

第一次执行的话应该还是会出现这个东西
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/68cdceb5-9596-48d4-9973-8bfbc9fdef84)

设置完毕后直接应该会执行完成，以后都会这样
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/ed4fad78-9e2a-4e2d-93f9-0e363baf817c)

TOKEN和日志应该都会被存储在MAA根路径下
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/b7f61fcf-8b72-4d00-aad3-fee2c80ff38f)



<a id="mode2"></a>
## 方法2

使用华为云挂载服务器签到（华为云有每月免费额度）

在`cloud_functions`文件夹下的代码是华为云的适配好的代码。

1.首先注册登录华为云账号
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/a8466b1e-25cd-4cec-8227-d675defcd5bd)

2.注册且登录完成后，进入[这个网址](https://console.huaweicloud.com/functiongraph)

3.进入后可能要求你实名认证，实名认证一下即可。

4.完成后点击右上角的'创建函数'按钮
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/b6aa83e0-2d54-4366-8b60-b7b3e8fdbc0f)

5.进入选择运行时环境为`Python 3.10`， 并填一下脚本名称（随便填）。其它设置不用动
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/e816158f-e1e3-47e5-959c-148ca2f5f259)

6.进来后是这样的界面，点击右上角上传自zip文件（或者你在左边的编辑器里自己把文件一个个创建好复制粘贴进去也行）
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/fc813308-bd30-4e94-b5b4-0c35f7e62d1d)

7.上传
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/2398932d-09f6-47e2-8694-48570724f6e9)

8.上传完成后应该是这个样子的
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/e357cbb9-47aa-4079-9d0b-b94caf925bbe)

9.选中`INPUT_HYPERGRYPH_TOKEN.txt`，在右边添加你的鹰角通行证.支持多个，换行添加下一个即可。
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/e6e92eb8-fc00-4a50-be72-7d8cb571930d)

10.保存完毕后，可以点击测试测试一下脚本。创建测试这里直接点击创建即可
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/61d2f18e-cf68-4a07-b4c4-c82ddf63022c)
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/648a0035-e1c1-40eb-ae94-9614605c9379)

11.正常结束后是这个样子的（记得保存和部署）：
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/9e93ed91-7527-4edc-830b-f4cd45aeb3ef)

12.为了让脚本每天执行，我们需要创建一个触发器
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/dcccce9c-d6f6-4fc7-a2e3-f8565d5a2d71)

触发器类型请选择`定时触发器`
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/4e60bf81-8ec2-4423-b68b-444435dd0edc)

触发器类型选择`Cron表达式`
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/25ae6a8d-247f-489b-b924-d4f8b26f559c)

然后填入这串东西`0 1 1 * * ?`
它指的是每天凌晨1点01分会执行一次
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/815335fc-b810-4321-b25a-2052e23e06f1)

然后确定保存即可

最后大功告成，等着每天发奖励即可！

注意：如果森空岛登录失效，则可能需要重新配置cred！


<a id="mode3"></a>
## 方法3

使用Github Action自动运行脚本

首先确认自己的github处于登录状态，然后点击本项目右上角的fork按钮，选择create fork将项目搬到自己的仓库

![1693722642573](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/8494f183-dd42-4138-b200-8308b147ee8d)

进入自己仓库的项目主页后，在上方的菜单中进入Settings > Secrets and variables > Actions

![1693722945708](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/8f757d1f-e89d-4e45-b186-c98c9effce14)

![1693723079068](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/194c6919-c7ac-43ae-ba1d-947841067e46)

点击 New repository secret

![1693723278777](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/fd163c62-90f9-426a-948a-f364d7950e52)

创建名为`TOKEN`的变量（注意变量名全大写），并填入你的鹰角网络通行证，如果要管理多个账号，换行即可
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/0faef7e4-9763-48a3-8481-d0f830382374)

完成后应该是这样的

![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/f30e584f-5117-4e0d-8c06-afda7f65eb71)

如果是第一次使用GitHub Action的话，还需要手动打开这个功能 在你仓库上方菜单中进入Actions

![image](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/e3f178fe-0a3c-47b6-bee8-45eb4dc73400)

点击 I understand... enable them > Enable workflow

![屏幕截图 2023-09-03 152800](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/5fdd673a-eaaa-42cb-b3b8-db71b812fe6f)

![屏幕截图 2023-09-03 153402](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/95fd2ad2-ce21-446d-9291-1a7750d4f0a2)

之后就可以自动运行签到了, 想要手动测试的话，选择左侧的Auto Sign > Run workflow, 刷新页面就能看到结果了

![image](https://github.com/LogicDX342/skyland-auto-sign/assets/52480482/2038dd9c-ac90-4ccf-8bf2-e2bf0e8958bd)

多个账号的运行结果（图里有重复token，虽然说读到4个但所以实际只有两个）：
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/0ae92ef9-1b4a-4613-ab2f-9363edfbb166)

<a id="multiple_account"></a>

## 多账号支持

软件支持多个账号添加，在文件里换行即可

//todo

### 使用浏览器登录多个账号获得TOKEN时要注意的问题

**不要去登出账号，否则鹰角网络通行证会失效！**

如果要添加多个账号，请删除浏览器缓存。或者使用浏览器自带的隐私浏览模式，拿到Token后，关闭隐私窗口，再登录一次即可！

![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/bc9f9ab5-fc90-4724-b877-d470b3494180)
![图片](https://github.com/xxyz30/skyland-auto-sign/assets/81208875/5889969c-3b25-4f6e-b4a2-0d5b923771d0)

<a id="multiple_account"></a>

## 多端登录的问题

同一账号多端登录是没问题的，但是要注意一点就是电脑在用密码登录后，手机客户端有可能会被挤掉

最后就是别手贱去点客户端里的清理会话，因为那样子会把所有的登录状态清空