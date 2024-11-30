# YoutubeAnalysis

<!--
## 插件开发者详阅

### 开始

此仓库是 QChatGPT 插件模板，您可以直接在 GitHub 仓库中点击右上角的 "Use this template" 以创建你的插件。  
接下来按照以下步骤修改模板代码：

#### 修改模板代码

- 修改此文档顶部插件名称信息
- 将此文档下方的`<插件发布仓库地址>`改为你的插件在 GitHub· 上的地址
- 补充下方的`使用`章节内容
- 修改`main.py`中的`@register`中的插件 名称、描述、版本、作者 等信息
- 修改`main.py`中的`MyPlugin`类名为你的插件类名
- 将插件所需依赖库写到`requirements.txt`中
- 根据[插件开发教程](https://qchatgpt.rockchin.top/develop/plugin-dev.html)编写插件代码
- 删除 README.md 中的注释内容


#### 发布插件

推荐将插件上传到 GitHub 代码仓库，以便用户通过下方方式安装。   
欢迎[提issue](https://github.com/RockChinQ/QChatGPT/issues/new?assignees=&labels=%E7%8B%AC%E7%AB%8B%E6%8F%92%E4%BB%B6&projects=&template=submit-plugin.yml&title=%5BPlugin%5D%3A+%E8%AF%B7%E6%B1%82%E7%99%BB%E8%AE%B0%E6%96%B0%E6%8F%92%E4%BB%B6)，将您的插件提交到[插件列表](https://github.com/stars/RockChinQ/lists/qchatgpt-%E6%8F%92%E4%BB%B6)

下方是给用户看的内容，按需修改
-->

## 安装

配置完成 [LangBot](https://github.com/RockChinQ/LangBot) 主程序后使用管理员账号向机器人发送命令即可安装：

```
!plugin get https://github.com/Garrise/LangBot_Plugin_YoutubeAnalysis
```
或查看详细的[插件安装说明](https://qchatgpt.rockchin.top/develop/plugin-intro.html#%E6%8F%92%E4%BB%B6%E7%94%A8%E6%B3%95)

## 使用
* 参考Google开发者文档，创建一个app并且打开v3 api，记下你的apikey  
  [YouTube Data API Overview  |  Google Developers](https://developers.google.com/youtube/v3/getting-started)

> 
* 将apikey填入config.py中
* 插件将会自动识别群聊里的YouTube视频链接并返回视频预览内容等等，包含以下两种：
  * https://youtu.be/{id}
  * https://www.youtube.com/watch?v={id}
<!-- 插件开发者自行填写插件使用说明 -->
