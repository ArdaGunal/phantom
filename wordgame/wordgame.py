import json
import random
import os
from redbot.core.commands import Cog
import discord
from redbot.core import Config, checks, commands

class Wordgame(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.word_list = self.load_word_list()
        self.scores = self.load_scores()
        self.current_word = None
    
    def load_word_list(self):
        with open("wordlist.txt") as f:
            return [line.strip() for line in f]
    
    def load_scores(self):
        if os.path.exists("scores.json"):
            with open("scores.json") as f:
                return json.load(f)
        return {}
    
    def save_scores(self):
        with open("scores.json", "w") as f:
            json.dump(self.scores, f)
    
    @commands.command()
    async def wordgame_start(self, ctx):
        self.current_word = random.choice(self.word_list)
        await ctx.send(f"The word game has started! The first word is: {self.current_word}")
    
    @commands.command()
    async def wordgame_submit(self, ctx, *, word: str):
        if self.current_word is None:
            await ctx.send("The word game has not started yet. Use the `wordgame_start` command to start a new game.")
            return
        
        if not word.lower().startswith(self.current_word[-1]):
            await ctx.send("The word must start with the last character of the previous word.")
            return
        
        if word.lower() not in self.word_list:
            await ctx.send("The word is not in the word list.")
            return
        
        # Update scores
        self.scores[str(ctx.author.id)] = self.scores.get(str(ctx.author.id), 0) + len(word)
        self.save_scores()
        
        self.current_word = word
        await ctx.send(f"{ctx.author.mention} has submitted a valid word! The new word is: {self.current_word}")
    
    @commands.command()
    async def wordgame_leaderboard(self, ctx):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        leaderboard_message = "Word Game Leaderboard:\n"
        for i, (user_id, score) in enumerate(sorted_scores):
            user = self.bot.get_user(int(user_id))
            leaderboard_message += f"{i+1}. {user}: {score}\n"
        await ctx.send(leaderboard_message)