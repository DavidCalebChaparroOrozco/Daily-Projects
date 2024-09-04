# Import necessary libraries
import discord
from discord.ext import commands
import yt_dlp
import asyncio
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the Discord bot token from the environment variables
DISCORD_TOKEN = os.getenv("DISCORD_KEY")

# Set up intents for the bot to listen to specific events
intents = discord.Intents.default()
# Allow bot to read message content
intents.message_content = True  
# Allow bot to handle voice state updates
intents.voice_states = True  

# Options for YouTube-DL to fetch the best audio format
YDL_OPTIONS = {"format": "bestaudio", "noplaylist": True, "quiet": True}
# Options for FFMPEG to handle the audio streaming
FFMPEG_OPTIONS = {
    # Reconnect options for streaming
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",  
    # Ignore the video stream
    "options": "-vn",  
}

# Define a class for the music bot using discord.py commands.Cog
class MusicBot(commands.Cog):
    def __init__(self, client):
        # Store the bot client
        self.client = client  
        # Initialize an empty queue for songs
        self.queue = []  

    # Command to play a song based on a search query
    @commands.command()
    async def play(self, ctx, *, search):
        # Check if the user is in a voice channel
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            # Inform the user if they aren't in a voice channel
            return await ctx.send("You're not in a voice channel!")  
        if not ctx.voice_client:
            # Connect the bot to the voice channel if it's not already connected
            await voice_channel.connect()  

        # Indicate that the bot is processing the search query
        async with ctx.typing():
            try:
                # Use YouTube-DL to search and get the first result's URL and title
                with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(f"ytsearch:{search}", download=False)
                    url = info['entries'][0]['url']
                    title = info['entries'][0]['title']
                    # Add the song to the queue
                    self.queue.append((url, title))  
                    # Inform the user that the song was added to the queue
                    await ctx.send(f"Added to queue: **{title}**")  
            except Exception as e:
                # Handle any errors that occur during the search
                return await ctx.send(f"An error occurred: {str(e)}")  

        # If nothing is playing, start playing the next song in the queue
        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)

    # Function to play the next song in the queue
    async def play_next(self, ctx):
        if self.queue:
            # Get the next song in the queue
            url, title = self.queue.pop(0)  
            # Stop any currently playing song
            ctx.voice_client.stop()  
            # Create an audio source for the next song
            source = discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)  
            # Play the song and set up the after function to play the next one when this one ends
            ctx.voice_client.play(source, after=lambda e: self.client.loop.create_task(self.play_next(ctx)))
            # Inform the user which song is currently playing
            await ctx.send(f"Now playing **{title}**")  
        else:
            # Inform the user if the queue is empty
            await ctx.send("Queue is empty")

    # Command to skip the currently playing song
    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            # Stop the current song
            ctx.voice_client.stop()  
            # Inform the user that the song was skipped
            await ctx.send("Skipped")  

# Create the bot client with a specific command prefix and intents
client = commands.Bot(command_prefix="!", intents=intents)

# Main function to add the music bot cog and start the bot
async def main():
    # Add the music bot cog to the client
    await client.add_cog(MusicBot(client))  
    # Start the bot with the provided token
    await client.start(DISCORD_TOKEN)  

# Run the main function asynchronously
asyncio.run(main())
