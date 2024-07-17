import discord
import asyncio
import json
from commands import play, pause, skip, queue, volume, create_playlist, manage_playlist, search, user_permissions, customization_options

# Load bot token from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    token = config['token']

# Initialize Discord bot
client = discord.Client()

# Event handler for bot initialization
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event handler for incoming messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Process commands
    if message.content.startswith('!play'):
        await play.handle_play_command(message)
    elif message.content.startswith('!pause'):
        await pause.handle_pause_command(message)
    elif message.content.startswith('!skip'):
        await skip.handle_skip_command(message)
    elif message.content.startswith('!queue'):
        await queue.handle_queue_command(message)
    elif message.content.startswith('!volume'):
        await volume.handle_volume_command(message)
    elif message.content.startswith('!createplaylist'):
        await create_playlist.handle_create_playlist_command(message)
    elif message.content.startswith('!add'):
        await manage_playlist.handle_add_command(message)
    elif message.content.startswith('!remove'):
        await manage_playlist.handle_remove_command(message)
    elif message.content.startswith('!reorder'):
        await manage_playlist.handle_reorder_command(message)
    elif message.content.startswith('!search'):
        await search.handle_search_command(message)
    elif message.content.startswith('!userpermissions'):
        await user_permissions.handle_user_permissions_command(message)
    elif message.content.startswith('!customizationoptions'):
        await customization_options.handle_customization_options_command(message)

# Run the bot
client.run(token)