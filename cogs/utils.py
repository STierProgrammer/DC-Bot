import discord
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def get_member(ctx, member_id: int):
        guild = ctx.guild
        member = guild.get_member(member_id)
        if member is None:
            try:
                member = await guild.fetch_member(member_id)
            except discord.NotFound:
                member = None
        return member

    @staticmethod
    async def get_channel(ctx, channel_id: int):
        guild = ctx.guild
        channel = guild.get_channel(channel_id)
        if channel is None:
            channel = discord.utils.get(guild.text_channels, id=channel_id)
        return channel

    @staticmethod
    async def get_role(ctx, role_id: int):
        guild = ctx.guild
        role = guild.get_role(role_id)
        if role is None:
            role = discord.utils.get(guild.roles, id=role_id)
        return role

    @staticmethod
    async def get_message(ctx, channel_id: int, message_id: int):
        channel = await Utils.get_channel(ctx, channel_id)
        if channel:
            try:
                message = await channel.fetch_message(message_id)
                return message
            except discord.NotFound:
                return None

def setup(bot):
    bot.add_cog(Utils(bot))
