import qq
from config import token, appID
import logging

logging.basicConfig(level=logging.DEBUG)
client = qq.Client()

@client.event
async def on_message(message: qq.Message):
    print(message.content)
    if "菜单" in message.content:
        await message.reply("正在开发中")
    if "介绍" in message.content:
        await message.reply("正在开发中...")
@client.event
async def on_ready():
    print("机器人登录成功")


if __name__ == '__main__':
    client.run(token=f"{appID}.{token}")