from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import re
import requests
from pkg.platform.types import *

'''
当收到B站视频链接时，对B站链接进行分析并发送封面，标题，作者，等内容
'''
#注册插件
@register(name='BiliAnalysis', description='当收到B站视频链接时，对B站链接进行分析并发送封面，标题，作者，等内容', version='0.2', author="Hanschase")
class BiliAnalysisPlugin(BasePlugin):
    #插件加载时触发
    def __init__(self, host: APIHost):
        pass
    @handler(PersonMessageReceived)
    @handler(GroupMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        msg = str(ctx.event.message_chain).strip()
        # 如果msg含有https://www.bilibili.com/video/字段则截取BV号
        bv_match = re.search(r'www.bilibili.com/video/(BV\w+)', msg) or re.search(r'b23.tv/(BV\w+)', msg)
        if bv_match: 
            id = bv_match.group(1)
            req = f"bvid={id}"
        av_match = re.search(r'www.bilibili.com/video/av(\w+)', msg) or re.search(r'b23.tv/av(\w+)', msg)
        if av_match:
            id = av_match.group(1)
            req = f"aid={id}"
            id = "av" + id
        if bv_match or av_match:
            # 发送封面，标题，作者等信息
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
            }
            response = requests.get(f"https://api.bilibili.com/x/web-interface/view?{req}", headers=headers)
            data = response.json()
            if data['code'] == 0:
                video_data = data['data']
                cover_url = video_data['pic']
                author_name = video_data['owner']['name']
                video_url = "https://www.bilibili.com/video/" + id
                title = video_data['title']
                await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id),MessageChain([
                                                                                                        Image(url=cover_url),
                                                                                                        f"视频标题：{title}\n",
                                                                                                        f"UP主：{author_name}\n",
                                                                                                        f"视频链接：{video_url}"
                                                                                                        ]))
                ctx.prevent_default()
                ctx.prevent_postorder()
            else:
                await ctx.send_message(ctx.event.launcher_type, str(ctx.event.launcher_id),["视频解析失败"])
                ctx.prevent_default()
                ctx.prevent_postorder()
