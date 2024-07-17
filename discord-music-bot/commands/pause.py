# discord-music-bot/commands/pause.py

import discord

async def pause(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    
    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send("Music paused.")
    else:
        await ctx.send("No music is currently playing to pause.")