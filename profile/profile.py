# -*- coding: utf-8 -*-
import discord
from redbot.core import commands
from redbot.core import Config

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=7895645342)
        self.config.register_member(
            name=None, 
            age=None, 
            gender=None,
            city=None, 
            occupation=None, 
            favorite_tv_shows=None, 
            favorite_movies=None,
            hobbies=None,
            about=None
        )

    @commands.group()
    async def profil(self, ctx: commands.Context) -> None:
        """Profilinizi oluşturun veya başka birinin profilini görüntüleyin """
        pass

    @profil.command(name="oluştur")
    async def _oluştur(self, ctx):
        await ctx.author.send("Merhaba, profilinizi oluşturmak için birkaç soru sormak istiyoruz. Lütfen adınızı söyler misiniz?")
        name = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        
        await ctx.author.send("Yaşınız kaç?")
        age = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        
        await ctx.author.send("Cinsiyetiniz nedir?")
        gender = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        
        await ctx.author.send("Hangi şehirde yaşıyorsunuz?")
        city = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        
        await ctx.author.send("Mesleğiniz nedir?")
        occupation = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        
        await ctx.author.send("Hangi dizileri izlemeyi seversiniz?")
        favorite_tv_shows = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
        
        await ctx.author.send("Hangi filmleri izlemeyi seversiniz?")
        favorite_movies = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        await ctx.author.send("Hangi hobileriniz var?")
        hobbies = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        await ctx.author.send("Kısaca kendinizden bahseder misiniz?")
        about = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)

        await self.config.member(ctx.author).name.set(name.content)
        await self.config.member(ctx.author).age.set(age.content)
        await self.config.member(ctx.author).gender.set(gender.content)
        await self.config.member(ctx.author).city.set(city.content)
        await self.config.member(ctx.author).occupation.set(occupation.content)
        await self.config.member(ctx.author).favorite_tv_shows.set(favorite_tv_shows.content)
        await self.config.member(ctx.author).favorite_movies.set(favorite_movies.content)
        await self.config.member(ctx.author).hobbies.set(hobbies.content)
        await self.config.member(ctx.author).about.set(about.content)
        
        await ctx.send("Profiliniz başarıyla oluşturuldu!")
        
    @profil.command(name="değiştir")
    async def _değiştir(self, ctx, field: str):
     fields = {
        "isim": "name",
        "yaş": "age",
        "cinsiyet": "gender",
        "şehir": "city",
        "meslek": "occupation",
        "en sevdiğiniz tv programı": "favorite_tv_shows",
        "en sevdiğiniz film": "favorite_movies",
        "hobiler": "hobbies",
        "hakkımda": "about_me"
    }
    field = fields.get(field.lower())
    if not field:
        return await ctx.send("Geçersiz alan adı!")
    await ctx.author.send(f"Lütfen yeni {field} değerini girin.")
    value = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author)
    await self.config.member(ctx.author).set_raw(field, value=value.content)
    await ctx.send(f"{field} değeri başarıyla güncellendi!")

@profil.command(name="göster")
async def _göster(self, ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    name = await self.config.member(member).name()
    age = await self.config.member(member).age()
    gender = await self.config.member(member).gender()
    city = await self.config.member(member).city()
    occupation = await self.config.member(member).occupation()
    favorite_tv_shows = await self.config.member(member).favorite_tv_shows()
    favorite_movies = await self.config.member(member).favorite_movies()
    hobbies = await self.config.member(member).hobbies()
    about_me = await self.config.member(member).about_me()

    embed = discord.Embed(title=f"{member.display_name}'s Profile", color=0x00ff00)
    embed.set_thumbnail(url=member.avatar_url)
    fields = [
        ("İsim", name or "Bilinmiyor", True),
        ("Yaş", age or "Bilinmiyor", True),
        ("Cinsiyet", gender or "Bilinmiyor", True),
        ("Şehir", city or "Bilinmiyor", False),
        ("Meslek", occupation or "Bilinmiyor", False),
        ("En Sevdiğiniz TV Programları", favorite_tv_shows or "Bilinmiyor", False),
        ("En Sevdiğiniz Filmler", favorite_movies or "Bilinmiyor", False),
        ("Hobiler", hobbies or "Bilinmiyor", False),
        ("Hakkımda", about_me or "Bilinmiyor", False),
    ]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    embed.set_image(url=member.avatar_url_as(size=1024))
    await ctx.send(embed=embed)

    
    
