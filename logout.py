import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print('준비 완료')

@bot.command()
async def 명령어(ctx):
 embed = discord.Embed(colour = 222100)
 embed.add_field(name='명령어', value='규칙, 감도, 파오, 어진, 로그인, 매니저', inline=False)
 embed.set_footer(text="도배를 하시면 뮤트를 드실 수 있으니 조심하세요.")
 await ctx.send(embed=embed)

@bot.command()
async def 규칙(ctx):
 embed = discord.Embed(colour = 222100)
 embed.add_field(name='1.', value='욕설, 성단어, 비속어 금지', inline=False)
 embed.add_field(name='2.', value='타스트리머 비교 발언 금지', inline=False)
 embed.add_field(name='3.', value='분쟁유발 단어, 싸움 금지', inline=False)
 embed.add_field(name='4.', value='도배, 섭파배포 금지', inline=False)
 embed.set_footer(text="- 매니저의 판단하에 바로 벤 처리가 될 수도 있습니다.")
 await ctx.send(embed=embed)

@bot.command()
async def 감도(ctx):
 embed = discord.Embed(colour = 222100)
 embed.add_field(name='감도', value='DPI 1000, 인게임 7', inline=False)
 embed.set_footer(text="공지를 자주 확인해주세요")
 await ctx.send(embed=embed)

@bot.command()
async def 파오(ctx):
 embed = discord.Embed(colour = 222100)
 embed.add_field(name='파오', value='바보같지만 귀여운 스트리머', inline=False)
 embed.set_footer(text="공지를 자주 확인해주세요")
 await ctx.send(embed=embed)

@bot.command()
async def 어진(ctx):
 embed = discord.Embed(colour = 222100)
 embed.add_field(name='어진', value='로그아웃 봇 주인', inline=False)
 embed.set_footer(text="공지를 자주 확인해주세요")
 await ctx.send(embed=embed)

@bot.command()
async def 로그인(ctx):
 embed = discord.Embed(colour = 222100)
 embed.add_field(name='로그인', value='총괄매니저', inline=False)
 embed.set_footer(text="공지를 자주 확인해주세요")
 await ctx.send(embed=embed)

@bot.command()
async def 매니저(ctx):
  embed = discord.Embed(colour = 222100)
  embed.add_field(name='총괄매니저', value='로그인#6380', inline=True)
  embed.add_field(name='매니저', value='어진#0276', inline=True)
  embed.set_footer(text="매니저 추가 모집중")
  await ctx.send(embed=embed)
  
access_token = os.environ["BOT_TOKEN"]
bot.run('access_token')
