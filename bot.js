const Discord = require('discord.js');
const client = new Discord.Client();
var xp=0;
client.on('ready', () => {
  console.log('키키봇 준비 완료');  
});
function makeembed(str1, str2){
  const embed=new Discord.RichEmbed()
    .setTitle(str1)
    .setDescription(str2)
    .setColor('#f50057')
    .setAuthor('키키', 'https://cdn.discordapp.com/avatars/647630912795836437/03b3ba91907c8bc88e1cbaa4a81f43a6.png');
  return(embed);
}
client.on('message', message => {
  function dsend(str1, str2, str3){
    if(str1 === str2){
      message.channel.send(str3);
    }
  }
  dsend(message.content, '키키야 뒤져', '그럼 님은 앞져요(아재키키)');
  dsend(message.content, '키키야 바보', '제가 바다의 보물이죠');
  dsend(message.content, '키키야 천재', '저는 천하의 재수있는놈(?) 입니다');
  dsend(message.content, '키키야 메롱', '메롱x무한');
  dsend(message.content, '키키야 디토님어떡해', 'ㅠㅠ');
  dsend(message.content, '키키야', '키키봇입니다^^');
  dsend(message.content, '키키야 개논리1', '개논리-키키\n저는 개 입니다\n방금 논리를 펼쳤습니다\n그러므로 이 논리는 개논리 입니다');
  dsend(message.content, '키키야 embed', makeembed('제목', '내용'));
  dsend(message.content, '키키야 embed', makeembed('제목', '내용'));
  if(message.content === '키키야 가지마'){
  message.channel.send('```키키봇 xp-1```');
  xp--;
}
 else if(message.content === '키키야 가'){
   message.channel.send('```키키봇 xp+1```');
   xp++;  
 }
 else if(message.content === '키키야 레벨'){
   message.channel.send('```키키봇 레벨: ' + xp + '```');
 }
else if (message.content === '키키야 햄스터봇') {
  message.channel.send('커져라');
}
  else if (message.content === '키키야 키키는'){
    message.channel.send('천재이자 바보에요');
  }
else if (message.content === '키키야 도움'){
  message.channel.send(makeembed('키키봇 도움말','1. 키키야 아무말: 키키와 대화하기\n2. 키키야 랜덤게임: 랜덤게임 하는 방법을 알려줘요\n3. 키키야 가: 키키 레벨를 늘려줘요'));
  }
else if (message.content === '키키야 행복한서버는'){
  message.channel.send('키키님이 만드신 서버에요');
  }
else if (message.content === '키키야 초대'){
  message.channel.send('https://discordapp.com/oauth2/authorize?client_id=657949896263073811&scope=bot');
  }
else if (message.content === '키키야 서포트'){
  message.channel.send('https://discord.gg/8mSYc9D');
  }
else if (message.content === '키키야 랜덤'){
  message.channel.send('랜덤번호 1부터 100중 하나를 불러드릴게요');
    message.reply(Math.floor(Math.random() * (100 - 1)) + 1);
  }
else if (message.content === '키키야 랜덤게임'){	
  message.channel.send('렌덤게임 하는 방법\n1. 키키야 랜덤을 입력한다\n2. 가장 높은 번호를 받으면 이겨요^^');
  }
else if (message.content === '키키야 안녕'){
  message.channel.send('ㅎ2');
  }
if (message.content.startsWith('키키야 차단')) {
    const user = message.mentions.users.first();
    if (user) {
      const member = message.guild.member(user);
      if (member) {
        member.ban({
          reason: '누가 시켰어요',
        }).then(() => {
          message.reply(`${user.tag}, 다신 내 앞에 오지마!!!`);
        }).catch(err => {
          message.reply('악 키키야 에러좀 고치라');
          console.error(err);
        });
      } else {
        message.reply('이 사람이 누구길레 차단하지?');
      }
    } else {
      message.reply('누구를 차단할건데요?!');
    }
  }
else if (message.content.startsWith('키키야 추방')) {
    const user = message.mentions.users.first();
    if (user) {
      const member = message.guild.member(user);
      if (member) {
        member.kick(`${message.author}님이 추방시킴`).then(() => {
          message.reply(`${user.tag}, 뭐를 했길레 추방당했을까?`);
        }).catch(err => {
          message.reply('아 헛발짓을 했네요');
          console.error(err);
        });
      } else {
        message.reply('이분이 누구죠');
      }
    } else {
      message.reply('누구를 차여?');
    }
  }
else if (message.content === '키키야 디토는'){
  message.channel.send('과연 누구일까여?');
  }
else if(message.content === '키키야 테스트'){
  message.channel.send('테스트');
}
else if (message.content === '키키야 내아바타') {
message.channel.send('멋진 아바타네요');
message.channel.send(message.author.avatarURL);
  }
else if(message.content === '키키야 도배'){
var i=0;
for(i=0;i<25;i++){
  message.channel.send('도배는 좋아');
}
}
else if(message.content === '키키야 핑'){
message.reply('퐁, '+Math.floor(client.ping) + ' ms');
}
});
client.on('guildMemberAdd', member => {
  // Send the message to a designated channel on a server:
  const channel = member.guild.channels.find(ch => ch.name ==='키키봇');
  if (!channel) return;
  // Send the message, mentioning the member
  channel.send(`ㅎ2, ${member}`);
return;
});
client.login('NjU3OTQ5ODk2MjYzMDczODEx.XgsNmQ.oV4n9SK276t7W53cgCk-bk36ieA');
