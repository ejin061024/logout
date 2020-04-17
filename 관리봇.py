import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

client = discord.Client()

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
  print('준비 완료')

@bot.command()
async def 회탈(ctx):
 embed = discord.Embed(colour = 766666)
 embed.add_field(name='회원탈퇴', value='관리봇입니다.', inline=False)
 embed.set_footer(text="명령어는 아직 추가중")
 await ctx.send(embed=embed)

bot.run('NzAwNTI4MDMwNjYxMDgzMTM4.XpkPmA.Pbkx1mFHl6hhuspLAnZxEQr__q0')
