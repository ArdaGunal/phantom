# -*- coding: utf-8 -*-
import discord
from redbot.core import checks,commands,Config 
from redbot.core.data_manager import bundled_data_path
from redbot.core.data_manager import cog_data_path
from deezloader import Login

class Deemix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=7364528762)
        self.config.register_global(token=True
        )
        
        
    
    @commands.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def setbaz(self, ctx, token):
     await self.config.token.set(token)
     await ctx.send("profil ayarlandı!")
        
    @commands.command()
    async def download(self, ctx, artist, song, quality):
       arl = await self.config.token()
       downloa = Login(arl) 
       downloa.download_name(
        artist = artist,
        song = song,
	output_dir = str(bundled_data_path(self)),
	quality_download = quality,
	recursive_quality = False,
	recursive_download = False,
        not_interface = True,
        method_save = 1
        )
       await ctx.send("İndirme tamamlandı,linkten ulaşabilirsiniz.http://phantom2158.ezconnect.to/portal/apis/fileExplorer/share_link.cgi?link=vdi-9ig2aT3ueycISO5KTA")

    @commands.command()
    async def downspo(self, ctx, url, quality):
       arl = await self.config.token()
       downloa = Login(arl) 
       track = downloa.download_trackspo(
        url,
	output_dir = str(bundled_data_path(self)),
	quality_download = quality,
	recursive_quality = False,
	recursive_download = False,
        not_interface = True,
        method_save = 1
        )
       await ctx.send("İndirme tamamlandı,linkten ulaşabilirsiniz.http://phantom2158.ezconnect.to/portal/apis/fileExplorer/share_link.cgi?link=vdi-9ig2aT3ueycISO5KTA")

    @commands.command()
    async def downspoalbum(self, ctx, url, quality):
       arl = await self.config.token()
       downloa = Login(arl) 
       downloa.download_albumspo(
        url,
	output_dir = str(bundled_data_path(self)),
	quality_download = quality,
	recursive_quality = False,
	recursive_download = False,
        not_interface = True,
        method_save = 1
        )
       await ctx.send("İndirme tamamlandı,linkten ulaşabilirsiniz.http://phantom2158.ezconnect.to/portal/apis/fileExplorer/share_link.cgi?link=vdi-9ig2aT3ueycISO5KTA")

    @commands.command()
    async def downspolist(self, ctx, url, quality):
       arl = await self.config.token()
       downloa = Login(arl) 
       track = downloa.download_playlistspo(
        url,
	output_dir = str(bundled_data_path(self)),
	quality_download = quality,
	recursive_quality = False,
	recursive_download = False,
        not_interface = True,
        method_save = 1
        )
       await ctx.send("İndirme tamamlandı,linkten ulaşabilirsiniz.http://phantom2158.ezconnect.to/portal/apis/fileExplorer/share_link.cgi?link=vdi-9ig2aT3ueycISO5KTA")
