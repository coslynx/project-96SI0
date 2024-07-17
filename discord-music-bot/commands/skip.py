import discord

async def skip_song(ctx):
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)

    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Skipping the current song.")
    else:
        await ctx.send("No music is currently playing to skip.")