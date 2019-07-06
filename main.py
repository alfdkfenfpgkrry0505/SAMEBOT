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
        embed = discord.Embed(title=" ?오늘의시한편 ", description=" 쌔임이 무작위로 시 한편을 읊어줍니다", color=0xff0000)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title=" ?패치노트 ", description=" 쌔임의 패치노트를 불러옵니다 ", color=0xff0000)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("?자기소개"):
        embed = discord.Embed(title="안녕? 난 쌔임[SAME]이야.  ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="내 이름은   ", description="", color=0xffaaaa)
        await message.channel.send(embed=embed)
        embed = discord.Embed(title="SPECIAL GIFT ARE MADE BY EFFORT.  ", description="", color=0xffaaaa)
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
    if message.content.startswith("?배돌이"):
        await message.channel.send("!안녕")
    if message.content.startswith("?오늘의시한편"):
        randomNum = random.randrange(1, 11)
        if randomNum==1:
            await message.channel.send("방문객")
            await message.channel.send("정현종 시인")
            await message.channel.send("============")
            await message.channel.send("사람이 온다는 건")
            await message.channel.send("실로 어마어마한 일이다.")
            await message.channel.send("그는")
            await message.channel.send("그의 과거와")
            await message.channel.send("현재와")
            await message.channel.send("그리고")
            await message.channel.send("그의 미래가 함께 오기 때문이다.")
            await message.channel.send("한 사람의 일생이 오기 때문이다.")
            await message.channel.send("부서지기 쉬운")
            await message.channel.send("그래서 부서지기도 했을")
            await message.channel.send("마음이 오는 것이다 -그 갈피를")
            await message.channel.send("아마 마음은 더듬어볼 수 있을 ")
            await message.channel.send("마음, ")
            await message.channel.send("내 마음이 그런 바람을 흉내낸다면 ")
            await message.channel.send("필경 환대가 될 것이다. ")
        if randomNum==2:
            await message.channel.send("바다")
            await message.channel.send("윤동주 시인")
            await message.channel.send("===========")
            await message.channel.send("실어다 뿌리는 ")
            await message.channel.send("바람조차 시원타.")
            await message.channel.send("===========")
            await message.channel.send("솔나무 가지마다 새촘히 ")
            await message.channel.send("고개를 돌리어 뻐들어지고,")
            await message.channel.send("===========")
            await message.channel.send("밀치고 ")
            await message.channel.send("밀치운다.")
            await message.channel.send("===========")
            await message.channel.send("이랑을 넘은 물결은 ")
            await message.channel.send("폭포처럼 피어오른다.")
            await message.channel.send("===========")
            await message.channel.send("해변에 아이들이 모인다")
            await message.channel.send("찰찰 손을 씻고 구보로,")
            await message.channel.send("바다는 자꾸 설워진다.")
            await message.channel.send("갈매기의 노래에 .....")
            await message.channel.send("===========")
            await message.channel.send("돌아다보고 돌아다보고")
            await message.channel.send("돌아가는 오늘의 바다여!")
        if randomNum==3:
            await message.channel.send("흔들리며 피는 꽃", color=0xfefefe)
            await message.channel.send("도종환 시인", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("흔들리지 않고 피는 꽃이 어디 있으랴", color=0xfefefe)
            await message.channel.send("이 세상 그 어떤 아름다운 꽃들도", color=0xfefefe)
            await message.channel.send("다 흔들리면서 피었나니", color=0xfefefe)
            await message.channel.send("흔들리면서 줄기를 곧게 세웠나니", color=0xfefefe)
            await message.channel.send("흔들리지 않고 가는 사람이 어디 있으랴", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("젖지않고 피는 꽃이 어디 있으랴", color=0xfefefe)
            await message.channel.send("이 세상 그 어떤 빛나는 꽃들도", color=0xfefefe)
            await message.channel.send("다 젖으며 젖으며 피었나니", color=0xfefefe)
            await message.channel.send("바람과 비에 젖으며 꽃잎 따뜻하게 피웠나니", color=0xfefefe)
            await message.channel.send("젖지 않고 가는 삶이 어디 있으랴", color=0xfefefe)
        if randomNum==4:
            await message.channel.send("하늘 냄새", color=0xfefefe)
            await message.channel.send("박희순 시인", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("사람이", color=0xfefefe)
            await message.channel.send("하늘처럼", color=0xfefefe)
            await message.channel.send("맑아 보일 때가 있다.", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("그때 나는 ", color=0xfefefe)
            await message.channel.send("그 사람에게서", color=0xfefefe)
            await message.channel.send("하늘 냄새를 맡는다.", color=0xfefefe)
        if randomNum==5:
            await message.channel.send("호수", color=0xfefefe)
            await message.channel.send("정지용 시인", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("얼굴 하나야", color=0xfefefe)
            await message.channel.send("손바닥 둘로 ", color=0xfefefe)
            await message.channel.send("푹 가리지만", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("보고 싶은 마음 ", color=0xfefefe)
            await message.channel.send("호수만 하니", color=0xfefefe)
            await message.channel.send("눈 감을 수 밖에", color=0xfefefe)
         if randomNum==6:
            await message.channel.send("그 꽃", color=0xfefefe)
            await message.channel.send("고은 시인", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("내려갈 때 보았네", color=0xfefefe)
            await message.channel.send("올라갈 때 못 본 그 꽃", color=0xfefefe)
         if randomNum==7:
            await message.channel.send("행복", color=0xfefefe)
            await message.channel.send("나태주 시인", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("저녁 때", color=0xfefefe)
            await message.channel.send("돌아갈 집이 있다는 것 ", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("힘들 때", color=0xfefefe)
            await message.channel.send("마음 속에 생각나는 사람이 있다는 것 ", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("외로울 때", color=0xfefefe)
            await message.channel.send("혼자서 부를 노래가 있다는 것", color=0xfefefe)
         if randomNum==8:
            await message.channel.send("풀꽃", color=0xfefefe)
            await message.channel.send("나태주 시인", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("자세히 보아야 ", color=0xfefefe)
            await message.channel.send("예쁘다 ", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("오래보아야 ", color=0xfefefe)
            await message.channel.send("사랑스럽다 ", color=0xfefefe)
            await message.channel.send("===========", color=0xfefefe)
            await message.channel.send("너도 그렇다", color=0xfefefe)
         if randomNum==9:
            await message.channel.send("너 외롭구나")
            await message.channel.send("김형태 시인")
            await message.channel.send("===========")
            await message.channel.send("깊이 ")
            await message.channel.send("=========== ")
            await message.channel.send("앓으십시요")
            await message.channel.send("앓음답도록 ")
            await message.channel.send("아름답도록")
        if randomNum==10:
            await message.channel.send("가을")
            await message.channel.send("한민복 시인")
            await message.channel.send("===========")
            await message.channel.send("그대 생각을  ")
            await message.channel.send("켜 놓은 채 ")
            await message.channel.send("잠이 들었습니다")
        

        
        

        


accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
