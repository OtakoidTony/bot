import asyncio
import discord
import random
import logging
app=discord.Client()
token = "NjU3OTQ5ODk2MjYzMDczODEx.Xgcv1g.JPleX2JshGl_0pCQmm7fP28cods"
@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(activity=discord.Game(name="키키야 도움말", type=1))
@app.event
async def on_message(message):
    if(message.content.startswith('키키야')):
        if message.author.bot:
             return None
        if message.content == "키키야": await message.channel.send("안녕하세요 키키봇입니다^^")
        elif message.content == "키키야 테스트": await message.channel.send("성공")
        elif message.content == "키키야 일본": await message.channel.send(":flag_jp::left_facing_fist:")
        elif message.content == "키키야 한국":  await message.channel.send(":flag_kr::thumbsup:")   
        elif message.content == "키키야 대한민국": await message.channel.send( ":flag_kr::thumbsup:")
        elif message.content == "키키야 북한": await message.channel.send( ":flag_kp:")
        elif message.content == '키키야 뒤져': await message.channel.send( '그럼 님은 앞져요(아재키키)')
        elif message.content == '키키야 바보': await message.channel.send( '제가 바다의 보물이죠(수중생활)')
        elif message.content == '키키야 천재': await message.channel.send( '저는 천하의 재수있는놈(?) 입니다')
        elif message.content == '키키야 메롱': await message.channel.send( '메롱x무한')
        elif message.content == '키키야 아무말': await message.channel.send( '아니, 아무말 말고 다른 말을 써야져')
        elif message.content == '키키야 안녕': await message.channel.send( '안녕하세요')
        elif message.content == '키키야 키키는': await message.channel.send( '이 봇을 만드셨죠')
        elif message.content == '키키야 키키': await message.channel.send( '이 봇을 만드셨죠')
        elif message.content == '키키야 디토': await message.channel.send( '엄청난 슷칼러(?)에요')
        elif message.content == '키키야 디토는': await message.channel.send( '엄청난 슷칼러(?)에요')
        elif message.content == '키키야 꿀벌': await message.channel.send( '꿀벌꿀벌~')
        elif message.content == '키키야 꿀벌은': await message.channel.send( '꿀벌꿀벌~')
        elif message.content == '키키야 mswgen':  await message.channel.send('엄청난 천재죠')
        elif message.content == '키키야 mswgen은': await message.channel.send( '엄청난 천재죠')
        elif message.content == '키키야 미안해':  await message.channel.send('미안해미안해하지마')
        elif message.content == '키키야 도움': await message.channel.send( 'ㄴㄴ 도움말')
        elif message.content == '키키야 생일':  await message.channel.send('몸은 12월 11일에 만들어졌지만 뇌는 디토봇과 같은 12월 22일에 만들어졌어요^^')
        elif message.content == '키키야 멍청이': await message.channel.send( '저 멍청이로 삼행시 지으면 님 멍청이에요')
        elif message.content == '키키야 멍청이삼행시': await message.channel.send( '멍: 멍청한 님\n청: (포기)\n이: 이름은?\n(키키봇 인성논란)')
        elif message.content == '키키야 죽어': await message.channel.send( '형님 먼저~')
        elif message.content == '이 망할 키키봇': await message.channel.send( '망-함')
        elif message.content == '키키야 인성':await message.channel.send(  '아, 참 생각해볼 문제군')
        elif message.content == '키키야 ㅎ2': await message.channel.send( 'ㅎ3')
        elif message.content == '키키야 애교': await message.channel.send( '1+1은?:left_facing_fist::left_facing_fist::left_facing_fist:\n토나오겠다')
        elif message.content == '키키야 팀크레센도': await message.channel.send( '아 저기 안에 들어갈수만 있다면...')
        elif message.content == '키키야 슷칼봇': await message.channel.send( '저안테는 워렌 버펫같은 대단한 투자가이자 존경하는 분이죠')
        elif message.content == '키키야 배추봇': await message.channel.send( '아 인성 안좋은 선배죠')
        elif message.content == '키키야 배그': await message.channel.send( '아 그 설치 오래걸리는 게임')
        elif message.content == '키키야 클로': await message.channel.send( '제가 그거 1달만에 아레나 3에서 10까지 간 사연 아나요?')
        elif message.content == '키키야 클오클': await message.channel.send( '아 그거 저 하다가 탈탈 털림요')
        elif message.content == '키키야 언더테일':  await message.channel.send('그 해골나오는거요?')
        elif message.content == '키키야 행복한서버는': await message.channel.send( '제 집이죠')
        elif message.content=='키키야 도배': await message.channel.send('키키야 도배')
        elif message.content == '키키야 서버초대': await message.channel.send( 'https://discord.gg/m2zNAS3')
        elif message.content == '키키야 봇초대': await message.channel.send( 'https://discordapp.com/oauth2/authorize?client_id=657949896263073811&scope=bot')
        elif message.content=='키키야 심심해':  await message.channel.send('키키야 개논리를 입력해 즐거운 개논리를 보세요^^')
        elif message.content=='키키야 개논리':
            r=random.randrange(1, 2)
            if r==1:
                embed=discord.Embed(
                    title= '개논리',
                    description= '저는 개입니다\n제가 논리를 펼쳤습니다\n그래서 그 논리는 개논리입니다',
                    footer= '제작자: 키키',
                    colour= discord.Colour.blue()
                )
            await message.channel.send(embed=embed)
        elif message.content=='키키야 이모지':
            emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                " ( •́ ̯•̀ ) ",
                " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "                                                                          " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] 
            randomNum = random.randrange(0, len(emoji)) 
            print(emoji[randomNum])
            await message.channel.send(embed=discord.Embed(description=emoji[randomNum])) 
        elif message.content=="키키야 도움말":
            embed = discord.Embed(
                title = '키키봇 명령어',
                author = '키키',
                colour = discord.Colour.blue()
            )
            embed.add_field(name = '키키야 아무말', value = '아무말에 키키안테 하고싶은 말을 써주세요(다는 대답 못해요)',inline = False)
            embed.add_field(name = '키키야 개논리', value = '개-논-리',inline = False)
            await message.channel.send(embed=embed)
        else: await message.channel.send('키키봇의 프로그램에는 없는 명령어에요!')
@app.event
async def on_member_join(member):
    channel = app.get_channel(660775449449988107)
    message ='{}, 환영합니다^^'.format(member.mention)
    await channel.send(message)
@app.event
async def on_member_remove(member):
    channel = app.get_channel(660775449449988107)
    message ='{}, 가지마요ㅠㅠ'.format(member.mention)
    await channel.send(message)
app.run(token)  
