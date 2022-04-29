import discord
import datetime
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('==================================')
    print(client.user.name)
    print(client.user.id)
    print('육군본부 BOT의 구동이 완료되었지 말입니다.')
    print('==================================')
    game = discord.Game("살아 방패 , 죽어 충성")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    id = message.author.id
    if message.content.startswith("!ㅊ"):
        embed = discord.Embed(title="출근", description="<@{0}>님 출근기록이 완료됐지 말입니다!".format(id), color=0x3CB371, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="\n육군본부", value="살아 방패 죽어 충성 , 시민을 보호하고 치안을 유지하자\n", inline=True)
        embed.set_footer(text="출근 시간")
        await message.channel.send(embed=embed)
        await message.delete()
        role = discord.utils.get(message.guild.roles, name="🔫 = = 출근 수방사 인원 = = 🔫")
        await message.author.add_roles(role)
        role2 = discord.utils.get(message.guild.roles, name="🔫 = = 퇴근 수방사 인원 = = 🔫")
        await message.author.remove_roles(role2)
        
    if message.content.startswith("!ㅌ"):
        embed = discord.Embed(title="퇴근", description="<@{0}>님 퇴근기록이 완료됐지 말입니다!".format(id), color=0x3CB371, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="\n육군본부", value="살아 방패 죽어 충성 , 시민을 보호하고 치안을 유지하자\n", inline=True)
        embed.set_footer(text="퇴근 시간")
        await message.channel.send(embed=embed)
        await message.delete()
        role = discord.utils.get(message.guild.roles, name="🔫 = = 퇴근 수방사 인원 = = 🔫")
        await message.author.add_roles(role)
        role2 = discord.utils.get(message.guild.roles, name="🔫 = = 출근 수방사 인원 = = 🔫")
        await message.author.remove_roles(role2)


client.run("토큰")