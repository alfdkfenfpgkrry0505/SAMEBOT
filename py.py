#Work with Python 3.7.3
import asyncio, discord, datetime, logging, random, traceback, time, os
from discord.ext import commands

app = discord.Client()


@app.event
async def on_ready():
    print('로그인 중 입니다 ..!')
    print(app.user.name)
    print(app.user.id)
    print('===============')
    game = discord.Game("쌔임에게 ?도와줘라고 도움을 요청해봐!")
    await app.change_presence(status=discord.Status.online, activity=game)
    

        
@app.event
async def on_message(message):

    if message.content.startswith("?도와줘"):
        embed = discord.Embed(title="  ", description=" 안녕? 난 쌔임이야. 아래는 명령어 목록이야.", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" 명령어 목록 ", description=" ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ?안녕 ", description=" 쌔임이 인사를 해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ?자기소개 ", description=" 쌔임이 자기소개를 해줍니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ?패치노트 ", description=" 쌔임의 패치노트를 불러옵니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("?자기소개"):
        embed = discord.Embed(title="안녕? 난 쌔임이야.  ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="내 이름은   ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="[Special gift are made by effort.]  ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="[특별한 재능은 노력으로 만들어진다.] 라는 의미를 가진 약자야.   ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="뭐 도움받고 싶은 것이 있다면 ?도와줘를 대화창에다 입력해봐.   ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        
     if message.content.startswith("?안녕"):
        msg = "{0.author.mention} 안녕? 반갑다.".format(message)
        await message.channel.send( msg)
        
     if message.content.startswith("?패치노트"):
        embed = discord.Embed(title="2019.07.06.토요일  ", description="1.0.0 개발 시작!", color=0xffaaaa)
        await message.channel.send(embed=embed)
        
        

        





accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
