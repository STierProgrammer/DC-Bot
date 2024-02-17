import discord
from discord.ext import commands

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join', aliases=['connect'])
    async def join_voice_channel(self, ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You are not connected to a voice channel.")

    @commands.command(name='leave', aliases=['disconnect'])
    async def leave_voice_channel(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("I am not connected to a voice channel.")

    @commands.command(name='play', aliases=['p'])
    async def play_audio(self, ctx, url: str):
        if ctx.voice_client:
            await ctx.send(f"Now playing: {url}")
        else:
            await ctx.send("I am not connected to a voice channel.")

    @commands.command(name='pause')
    async def pause_audio(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Audio paused.")
        else:
            await ctx.send("No audio is currently playing.")

    @commands.command(name='resume')
    async def resume_audio(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("Audio resumed.")
        else:
            await ctx.send("No audio is currently paused.")

    @commands.command(name='stop')
    async def stop_audio(self, ctx):
        if ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused()):
            ctx.voice_client.stop()
            await ctx.send("Audio stopped.")
        else:
            await ctx.send("No audio is currently playing.")

def setup(bot):
    bot.add_cog(Voice(bot))
