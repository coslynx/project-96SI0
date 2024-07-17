import discord
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, song_name):
        voice_channel = ctx.author.voice.channel
        if voice_channel:
            voice = await voice_channel.connect()
            voice.play(discord.FFmpegPCMAudio(song_name))
        else:
            await ctx.send("You need to be in a voice channel to use this command.")

    @commands.command()
    async def pause(self, ctx):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client.is_playing():
            voice_client.pause()

    @commands.command()
    async def skip(self, ctx):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client.is_playing():
            voice_client.stop()

    @commands.command()
    async def volume(self, ctx, volume: int):
        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice_client:
            voice_client.source.volume = volume / 100

def setup(client):
    client.add_cog(Music(client))