import discord, logging, datetime, os
from discord.ext import commands, tasks
from discord import app_commands

print("> Beginning bot setup")

dirpath = os.path.dirname(os.path.realpath(__file__))
os.chdir(dirpath)

print(f"> Changed working directory to {os.getcwd()}")

import autochannels
from self_secrets import SECRETS
from holidays import HOLIDAYS

print("> Imported custom modules")

CST = datetime.timezone(-datetime.timedelta(hours=5))
active_tasks = {}

intents = discord.Intents()

class HolidayClient(discord.Client):
	
	async def on_ready(self):
		
		print(f"> Client running as {self.user}")
		
		for channel in autochannels.AUTOCHANNELS:
			add_task(channel, autochannels.AUTOCHANNELS[channel])
		print(f"> Set up autochannel tasks from records")
		
		synced = await self.tree.sync()
		print(f"> Synced {len(synced)} commands")
		
		print(f"> Init finished!")

client = HolidayClient(intents=intents)
client.tree = app_commands.CommandTree(client)

def add_task(channel: str, hour: int) -> None:
	
	channel = str(channel)
	
	remove_task(channel)
	
	@tasks.loop(time=datetime.time(hour=int(hour), minute=0, tzinfo=CST))
	async def new_task():
		c_obj = (client.get_channel(int(channel)) or await client.fetch_channel(int(channel)))
		if c_obj != None:
			print(f"* Sending daily message to id={channel} at {hour}:00")
			await c_obj.send(embed=make_today_embed())
		else:
			print(f"* Tried to send to id={channel} at {hour}:00, but failed")
	
	active_tasks[channel] = new_task
	
	new_task.start()

def remove_task(channel: str) -> None:
	channel = str(channel)
	if channel in active_tasks:
		active_tasks[channel].cancel()
		active_tasks.pop(channel, None)

def make_today_embed():
	
	today = datetime.date.today()
	m = today.month
	d = today.day
	y = today.year
	days = HOLIDAYS[m][d]
	
	embed = discord.Embed(
		color=discord.Color.random()
	).set_author(name=f"{m}/{d}/{y}")
	
	if len(days) == 0:
		
		embed.title = "There's no record of any holidays today..."
		embed.description = "That can't be right. Yell at me to fix it!"
		
	else:
		
		main_day = days[0]
		
		embed.title = "Today is **" + main_day["name"] + "**!"
		embed.description = main_day["desc"]
		img = main_day["img"]
		
		if len(days) > 1:
			embed.description += "\n\nToday is also..."
			for day in days[1:4]:
				embed.add_field(name=day["name"], value=day["desc"])
				if img == None:
					img = day["img"]
		
		if img != None:
			embed.set_thumbnail(url=img)
	
	return embed

# -------- #
# COMMANDS #
# -------- #

@client.tree.command(name="holidays", description="Sends a public message with a list of today's holidays")
async def holidays(interaction: discord.Interaction) -> None:
	await interaction.response.send_message(embed=make_today_embed())
    
@client.tree.command(name="autochannel", description="Run to have this channel receive a daily list of holidays")
@app_commands.describe(hour="The hour at which to send the message in CST (Give a number 0-23)")
async def autochannel(interaction: discord.Interaction, hour: int) -> None:
	
	if hour < 0 or hour > 23:
		
		embed = discord.Embed(
			title="Error: Hour out of range",
			description="Make sure the hour is an integer between `0` and `23`!",
			color=discord.Color.random()
		)
		
		await interaction.response.send_message(embed=embed, ephemeral=True)
		
	else:
		
		autochannels.add_autochannel(interaction.channel_id, hour)
		add_task(interaction.channel_id, hour)
		
		embed = discord.Embed(
			title="Channel added!",
			description=f"A daily message will be sent to this channel at {hour}:00 CST!",
			color=discord.Color.random()
		)
		
		await interaction.response.send_message(embed=embed, ephemeral=True)

@client.tree.command(name="remove_autochannel", description="Remove this channel from receiving daily messages")
async def remove_autochannel(interaction: discord.Interaction) -> None:
	autochannels.remove_autochannel(interaction.channel_id)
	remove_task(interaction.channel_id)
	await interaction.response.send_message(f"Daily messages will no longer be sent here", ephemeral=True)
    
# -------- #

print("> Setup finished, calling client run")
client.run(SECRETS['token'], log_level=logging.WARN)
