import discord

async def set_volume(ctx, volume):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return

    voice_channel = ctx.message.author.voice.channel
    voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)

    if not voice_client:
        await voice_channel.connect()
        voice_client = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)

    if not voice_client.is_playing():
        await ctx.send("No audio is currently playing.")
        return

    try:
        volume = int(volume)
        if volume < 0 or volume > 100:
            await ctx.send("Volume must be between 0 and 100.")
            return
        voice_client.source.volume = volume / 100
        await ctx.send(f"Volume set to {volume}%")
    except ValueError:
        await ctx.send("Volume must be a valid number.")

# Command registration
@client.command(name='volume')
async def volume(ctx, volume: str):
    await set_volume(ctx, volume)