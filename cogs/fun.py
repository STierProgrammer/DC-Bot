import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='compliment')
    async def compliment(self, ctx):
        compliments = [
            "You have a great sense of humor!",
            "You're incredibly smart!",
            "You're a fantastic friend!",
            "Your positivity is infectious!",
            "You're really good at what you do!",
            "You have a beautiful smile!",
            "You're a great listener!",
            "You always know how to make people feel special!"
        ]
        compliment = random.choice(compliments)
        await ctx.send(compliment)

    @commands.command(name='fortune')
    async def fortune(self, ctx):
        fortunes = [
            "A beautiful, smart, and loving person will be coming into your life.",
            "Your life will be happy and peaceful.",
            "You will always be surrounded by true friends.",
            "An exciting opportunity lies ahead for you.",
            "You will find joy in the simple things in life.",
            "You will achieve great things.",
            "Your hard work will pay off soon.",
            "Good things are coming your way!"
        ]
        fortune = random.choice(fortunes)
        await ctx.send(f"Your fortune: {fortune}")

    @commands.command(name='joke')
    async def joke(self, ctx):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What did one ocean say to the other ocean? Nothing, they just waved!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "What do you call a cheese that isn't yours? Nacho cheese!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]
        joke = random.choice(jokes)
        await ctx.send(joke)

def setup(bot):
    bot.add_cog(Fun(bot))
