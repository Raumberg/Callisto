
import openai
import discord
from discord.ext import commands

openai.api_key = str(###)
bot_token = str(###)
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.command(name='ask')
async def on_message(context):
    message = context.message
    if message.author == client.user:
        return
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    if message.channel.name == 'test':
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=3000,
            temperature=0.5,
        )

    output = response["choices"][0]["text"]
    await message.channel.send(output, reference=message)


if __name__ == '__main__':
    client.run(bot_token)
