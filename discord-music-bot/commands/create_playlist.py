import discord
from discord.ext import commands

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

class CreatePlaylist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.playlists = {}

    @commands.command(name='createplaylist')
    async def create_playlist(self, ctx, playlist_name):
        if playlist_name in self.playlists:
            await ctx.send(f'Playlist "{playlist_name}" already exists.')
        else:
            new_playlist = Playlist(playlist_name)
            self.playlists[playlist_name] = new_playlist
            await ctx.send(f'Playlist "{playlist_name}" created successfully.')

def setup(bot):
    bot.add_cog(CreatePlaylist(bot))