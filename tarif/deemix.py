# -*- coding: utf-8 -*-
import discord
from redbot.core import checks,commands,Config 
from redbot.core.data_manager import cog_data_path
import pydeezloader

class Deemix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=7364528762)
        self.config.register_guild(email=None, 
         password=None
         )
        
        
    
    @commands.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def setbaz(self, ctx, arl):
     await self.config.guild(ctx.guild).arl.set(arl)
     await ctx.send("profil ayarlandı!")
        
    @commands.command()
    async def download(self, ctx, url,quality):
       arl = await self.config.guild(ctx.guild).arl()
       download = pydeezloader.Login(arl) 
       download.download_trackspo(url,
	output = str(cog_data_path(self) / url.quality),
	quality = quality,
	recursive_quality = False,
	recursive_download = False,
        not_interface = False
        )
