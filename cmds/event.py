import json
import discord
from discord.ext import commands
from core.classes import Cog_Extantion


class event(Cog_Extantion): 
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content=='hi':
            await msg.channel.send('hi三小噁男')




def setup(bot):
    bot.add_cog(event(bot))