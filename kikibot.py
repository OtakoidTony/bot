import discord
import asyncio
import random
import openpyxl
import datetime
token="NjYwMzkwNjY2NTM0MjU2NjQw.XiLMnA.R72CUv-JgxURXDYj_lVmIV2xPSA"
client=discord.Client()
@client.event
async def on_ready():
    print('---------------------------------')
    print(f'| Client ID: {client.user.id} |')
    print(f'| Client Name: {client.user.name}           |')
    print('---------------------------------')  
@client.event
async def on_message(message):
    async def makeembed(title, description):
        now=datetime.datetime.now()
        embed=discord.Embed(
            title=title,
            description=description
        )
        embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
        await message.channel.send(embed=embed)
    try:
        if message.author.bot:
            return None
        if message.content.startswith('키키야'):
            if message.content=='키키야': 
                now=datetime.datetime.now()
                msg='안녕하세여^^'
                embed=discord.Embed(
                    title=str(msg),
                    description="챗 기능",
                    colour=discord.Colour.blue()
                )
                embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                await message.channel.send(embed=embed)
            elif message.content.startswith('키키야 한단어커명추가'):
                file = openpyxl.load_workbook("기억.xlsx") #파일 이름은 상관 없어요
                sheet = file.active
                strsss=message.content[12:]
                i = 1
                if strsss=='도움말' or strsss=='도움':
                    now=datetime.datetime.now()
                    msg='커스텀명령어'
                    embed=discord.Embed(
                       title='키키봇 커스텀명령어',
                       description="키키봇 한단어커스텀명령어 사용하는 방법입니다^^",
                       colour=discord.Colour.blue()
                    )
                    embed.add_field(name="형식", value="키키야 커명추가 [입력] [출력]")
                    embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                    await message.channel.send(embed=embed)
                    return None
                q=strsss.split(" ")[0] #A부분
                a=strsss.split(" ")[1] #B부분
                file2=openpyxl.load_workbook('정보.xlsx')
                sheet2=file2.active
                flag=0
                while sheet2["A" + str(i)].value != None:
                    if str(sheet2["A" + str(i)].value) == str(message.author.id):
                        if int(sheet2['D'+str(i)].value)<=0 and message.author.id!=647630912795836437:
                            now=datetime.datetime.now()
                            msg='커스텀명령어'
                            embed=discord.Embed(
                                title="에러 내용: 커스텀명령어 티켓이 부족합니다",
                                description='`키키야 구입 커스텀명령어`를 이용해 커스텀명령어티켓 10개를 사고 다시 해보세여^^',
                                colour=discord.Color.blue()
                            )
                            embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                            await message.channel.send(embed=embed)
                            return None
                        else:
                            ohyeah=int(sheet2['D'+str(i)].value)
                            sheet2['D'+str(i)].value=str(ohyeah-1)
                            flag = 1
                            file2.save('정보.xlsx')  
                            break
                    i += 1
                if flag == 0 : 
                    now=datetime.datetime.now()
                    msg='커스텀명령어'
                    embed=discord.Embed(
                        title="에러 내용: 키키봇 서비스에 가입이 되어있지 않습니다",
                        description='`키키야 가입`를 이용해 가입을 하세여^^',
                        colour=discord.Color.blue()
                    )
                    embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                    await message.channel.send(embed=embed)
                    return None
                i=1
                while sheet["A" + str(i)].value != None:
                    i+=1
                sheet["A" + str(i)].value = str(q[0:]) #A 저장
                sheet["B" + str(i)].value = str(a)     #B 저장
                sheet["C" + str(i)].value = str(message.author.id) #이 말을 가르쳐준 사람 id 저장
                sheet["D" + str(i)].value = str(message.author) #이 말을 가르쳐준 사람 저장
                await makeembed('커스텀명령어 추가 성공!', f'[{str(q[0:])}]라고 말하면 [{str(a)}]라고 말하라고요? 감사합니다')
                file.save("기억.xlsx")
            elif message.content.startswith('키키야 커명추가'):
                file = openpyxl.load_workbook("기억.xlsx") #파일 이름은 상관 없어요
                sheet = file.active
                strsss=message.content[9:]
                i = 1
                if strsss=='도움말' or strsss=='도움':
                    now=datetime.datetime.now()
                    msg='커스텀명령어'
                    embed=discord.Embed(
                       title='키키봇 커스텀명령어',
                       description="키키봇 커스텀명령어 사용하는 방법입니다^^",
                       colour=discord.Colour.blue()
                    )
                    embed.add_field(name="형식", value="키키야 커명추가 [입력]/[출력]")
                    embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                    await message.channel.send(embed=embed)
                    return None
                q=strsss.split("/")[0] #A부분
                a=strsss.split("/")[1] #B부분
                file2=openpyxl.load_workbook('정보.xlsx')
                sheet2=file2.active
                flag=0
                while sheet2["A" + str(i)].value != None:
                    if str(sheet2["A" + str(i)].value) == str(message.author.id):
                        if int(sheet2['D'+str(i)].value)<=0 and message.author.id!=647630912795836437:
                            now=datetime.datetime.now()
                            msg='커스텀명령어'
                            embed=discord.Embed(
                                title="에러 내용: 커스텀명령어 티켓이 부족합니다",
                                description='`키키야 구입 커스텀명령어`를 이용해 커스텀명령어티켓 10개를 사고 다시 해보세여^^',
                                colour=discord.Color.blue()
                            )
                            embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                            await message.channel.send(embed=embed)
                            return None
                        else:
                            ohyeah=int(sheet2['D'+str(i)].value)
                            sheet2['D'+str(i)].value=str(ohyeah-1)
                            flag = 1
                            file2.save('정보.xlsx')  
                            break
                    i += 1
                if flag == 0 : 
                    now=datetime.datetime.now()
                    msg='커스텀명령어'
                    embed=discord.Embed(
                        title="에러 내용: 키키봇 서비스에 가입이 되어있지 않습니다",
                        description='`키키야 가입`를 이용해 가입을 하세여^^',
                        colour=discord.Color.blue()
                    )
                    embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                    await message.channel.send(embed=embed)
                    return None
                i=1
                while sheet["A" + str(i)].value != None:
                    i+=1
                sheet["A" + str(i)].value = str(q[0:]) #A 저장
                sheet["B" + str(i)].value = str(a)     #B 저장
                sheet["C" + str(i)].value = str(message.author.id) #이 말을 가르쳐준 사람 id 저장
                sheet["D" + str(i)].value = str(message.author) #이 말을 가르쳐준 사람 저장
                await makeembed('커스텀명령어 추가 성공!', f'[{str(q[0:])}]라고 말하면 [{str(a)}]라고 말하라고요? 감사합니다')
                file.save("기억.xlsx")
            elif message.content=='키키야 커명확인':
                file = openpyxl.load_workbook("기억.xlsx")
                sheet = file.active
                i=1
                embed=discord.Embed(
                    title='명령어들',
                    description='키키봇의 커스텀명령어들 목록입니다',
                    color=discord.Colour.blue()
                )
                while sheet["A" + str(i)].value != None:
                    embed.add_field(name=str(sheet["A" + str(i)].value), value=str(sheet["B" + str(i)].value), inline=False)
                    i+=1
                await message.channel.send(embed=embed)
            else:
                learn=[]
                file = openpyxl.load_workbook("기억.xlsx")
                sheet = file.active
                q=message.content[4:]
                i = 1
                flag = 0
                j=0
                while sheet["A" + str(i)].value != None:
                    if sheet["A" + str(i)].value == q:
                        learn.append(i)
                        j+=1
                        flag+=1
                    i += 1
                if flag!=0: 
                    if j>1:
                        rand=random.randrange(1, len(learn)+1)
                        now=datetime.datetime.now()
                        msg=str(sheet['B'+str(learn[rand-1])].value)
                        embed=discord.Embed(
                           title=str(msg),
                           description="챗 기능",
                           colour=discord.Colour.blue()
                        )
                        embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                        await message.channel.send(embed=embed)
                    else:
                        now=datetime.datetime.now()
                        msg=str(sheet['B'+str(learn[0])].value)
                        embed=discord.Embed(
                           title=str(msg),
                           description="챗 기능",
                           colour=discord.Colour.blue()
                        )
                        embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                        await message.channel.send(embed=embed)
                else: 
                    now=datetime.datetime.now()
                    embed=discord.Embed(
                        title='키키봇이 모르는 명령어',
                        description="이런건 걍 캡쳐해서 키키님안테 알려주세여",
                        colour=discord.Colour.blue()
                    )
                    embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                    await message.channel.send(embed=embed)
    except ZeroDivisionError:
        print('에러')
    #except Exception as exc:
    #    now=datetime.datetime.now()
    #    embed=discord.Embed(
    #        title=f'에러 내용: {str(exc)}',
    #        description='에러 감지 기능',
    #        colour=discord.Colour.blue()
    #    ) 
    #    embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
    #    await message.channel.send(embed=embed)
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        act=["키키야 도움말을 입력해 명령어 확인", f'{len(client.guilds)}개의 서버에 참여중', f'{len(client.users)}명의 유저들과 소통하는중']
        for i in act:
            game = discord.Game(str(i))
            await client.change_presence(status=discord.Status.online  , activity=game)
            await asyncio.sleep(10)
client.loop.create_task(my_background_task())
client.run(token)  
