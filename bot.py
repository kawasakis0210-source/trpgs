import discord
import random
import os

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("TOKENが設定されていません")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} としてログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('とと'):
        dice = random.randint(1, 100)
        target = random.randint(1, 100)

        if dice <= target:
            if dice <= 5:
                result = "クリティカル"
            else:
                result = "成功"
        else:
            if dice >= 95:
                result = "ファンブル"
            else:
                result = "失敗"

        await message.channel.send(f"1D100={dice} / 目標値={target} → {result}")

Thread(target=run_web).start()
client.run(TOKEN)