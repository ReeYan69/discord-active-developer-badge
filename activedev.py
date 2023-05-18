import discord 
from discord import *
intents = discord.Intents.default()




class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        selfsynced = False

    async def on_ready(self):
        await tree.sync()

        self.synced = True

        

                           

client = abot()
tree = app_commands.CommandTree(client)




@tree.command(name="badge",description="hello")
async def self(interaction: discord.Interaction):
            question=discord.Embed(title="Congratulations", description= f"You'll now be able to redeem the active developer badge. Just check up on the discord active developer portal later and an option to redeem it should show up", color=discord.Color.red())


            await interaction.response.send_message(embed=question)



client.run("ENTER_BOT_TOKEN_HERE")