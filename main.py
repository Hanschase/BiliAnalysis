from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import re
import requests
from pkg.platform.types import *
from plugins.LangBot_Plugin_YoutubeAnalysis.config import Config

'''
当收到B站视频链接时，对B站链接进行分析并发送封面，标题，作者，等内容
'''

#注册插件
@register(name='YoutubeAnalysis', description='当收到油管视频链接时，对该链接进行分析并发送封面，标题，作者，等内容', version='0.1', author="Garrise")
class BiliAnalysisPlugin(BasePlugin):
    #插件加载时触发
    def __init__(self, host: APIHost):
        pass
    @handler(PersonMessageReceived)
    @handler(GroupMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = str(ctx.event.message_chain).strip()
        # 如果msg含有youtube.com或https://youtu.be则截取视频id
        match = re.search(r'www.youtube.com/watch\?v=([\w-]{11})', msg) or re.search(r'youtu.be/([\w-]{11})', msg)
        if match:
            yt_id = match.group(1)
            print(f"Analyzing Youtube id: {yt_id}")
            # 发送封面，标题，作者等信息
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
            response = requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={yt_id}&key={Config.key}&part=snippet", headers=headers)
            data = response.json()
            if data['pageInfo']['totalResults'] != 0:
                snippet = data['items'][0]['snippet']
                title = snippet['title']
                description = snippet['description']
                channelTitle = snippet['channelTitle']
                thumbnails = snippet['thumbnails']
                publishedAt = snippet['publishedAt']
                tagString = ""
                tags = snippet['tags']
                if tags:
                    tagString = ", ".join(tags)
                else:
                    tagString = "无"
                thumbnailUrl = thumbnails['maxres']['url'] if thumbnails['maxres'] else thumbnails['high']['url'] 
                await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id),MessageChain([
                                                                                                        Image(url=thumbnailUrl),
                                                                                                        f"频道：{channelTitle}\n",
                                                                                                        f"标题：{title}\n",
                                                                                                        f"时间：{publishedAt}\n",
                                                                                                        f"链接：http://youtu.be/{yt_id}\n\n",
                                                                                                        f"标签：{tagString}"
                                                                                                        ]))
                ctx.prevent_default()
                ctx.prevent_postorder()
            else:
                await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id),["视频解析失败"])
                ctx.prevent_default()
                ctx.prevent_postorder()
