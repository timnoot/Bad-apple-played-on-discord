# Bad-apple-played-in-discord
This is the code I made to play Bad apple in discord. Inspired by https://youtu.be/TfS1GIr4kW4


# How to use?

| Modules | 

First you should start by installing all the required modules:
- moviepy.editor | pip install moviepy | https://pypi.org/project/moviepy/
- asyncio | pip install asyncio | https://pypi.org/project/asyncio/
- discord.py | pip install discord.py | https://pypi.org/project/discord.py/
- pygame | pip install pygame | https://pypi.org/project/pygame/
- a ffmpeg https://community.chocolatey.org/packages/ffmpeg to play the audio not a module

| Running code |

- Create a folder called "frames"
- Put the mp4 and mp3 file of badapple inside of it. Leave the python files in the root.
- Run the file "badapple video to frames.py"
- Once done run the file "playing vid with pygame.py"
- Once thats done get 15 Discord bot tokens and edit those in to "badapple discord.py"
- Change the channel id to the one you want on line 114
- Next run the file "badapple discord.py"
- Join a vc and do the command !start
- It should start

This IS api abuse, as 15 bots were used to circumvent the rate limit, so I do not recommend doing this! However, only 2,191 messages were sent totalling about 12MB, which were later deleted, so I think the impact on Discord's infrastructure was negligible, especially considering that Discord constantly processes thousands of messages per second (if not tens or hundreds of thousands). No relevant spikes were visible on the API response time graph.
