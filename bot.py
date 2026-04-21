import discord
import os
import random

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("TOKENが設定されていません")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"ログイン成功: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("とと"):
        dice = random.randint(1, 100)
        target = random.randint(1, 100)

        if dice <= target:
            result = "成功" if dice > 5 else "クリティカル"
        else:
            result = "失敗" if dice < 95 else "ファンブル"

        await message.channel.send(
            f"1D100={dice} / 目標値={target} → {result}"
        )

client.run(TOKEN)
