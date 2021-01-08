from hoshino.modules.hoshino_training.util.module import *
from hoshino.typing import MessageSegment

async def new_spider_work(spider, bot, gid, sv, TAG):
    if not spider.item_cache[gid]:
        await spider.get_update(gid)
        # sv.logger.info(f'群{gid}的{TAG}缓存为空，已加载至最新')
        return
    updates = await spider.get_update(gid)
    if not updates:
        # sv.logger.info(f'群{gid}的{TAG}未检索到新视频')
        return
    # sv.logger.info(f'群{gid}的{TAG}检索到{len(updates)}个新视频！')
    msg_list = spider.format_items(updates)
    for i in range(len(updates)):
        pic = MessageSegment.image('http:'+updates[i].pic)
        msg = f'{msg_list[0]}{pic}{msg_list[i+1]}'
        await bot.send_group_msg(group_id=int(gid), message=msg)

module_replace('hoshino.modules.GWYOG-Hoshino-plugins.bilisearchspider','spider_work',new_spider_work)