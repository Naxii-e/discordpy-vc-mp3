import discord
import secret, os, time
from discord.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.command()
async def play(ctx):
    if ctx.author.voice is None:
        await ctx.send("ボイスチャンネルに接続してください")
        return
    else:
        await ctx.author.voice.channel.connect()
        voice_client = ctx.message.guild.voice_client
        if not voice_client:
            await ctx.send("ボイスチャンネルへの接続に失敗しました。")
            return
        if ctx.message.attachments:
            await ctx.send("再生します。")
            await ctx.message.attachments[0].save("temp.mp3")
            music = "temp.mp3"
            ffmpeg_audio_source = discord.FFmpegPCMAudio(music)
            voice_client.play(ffmpeg_audio_source)
            return
    return

@bot.command()
async def dis(ctx):
    await ctx.guild.voice_client.disconnect()
    await ctx.send("切断しました。")
    time.sleep(5)
    os.remove("temp.mp3")
    return


if __name__ == "__main__":
    bot.run(secret.TOKEN)
    print("起動")