import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick_member(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f'{member.display_name} has been kicked from the server.')
        else:
            await ctx.send("You don't have permission to kick members.")

    @commands.command(name='ban')
    async def ban_member(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            await ctx.send(f'{member.display_name} has been banned from the server.')
        else:
            await ctx.send("You don't have permission to ban members.")

    @commands.command(name='unban')
    async def unban_member(self, ctx, *, member):
        if ctx.author.guild_permissions.ban_members:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'{user.name}#{user.discriminator} has been unbanned from the server.')
                    return
            await ctx.send(f'{member} was not found in the ban list.')
        else:
            await ctx.send("You don't have permission to unban members.")

def setup(bot):
    bot.add_cog(Admin(bot))
