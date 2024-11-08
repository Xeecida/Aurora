import json
from Aurora.logger import *
from Aurora.system import *
from Aurora.discord import *
import nextcord
from nextcord.ext import commands
from datetime import datetime
from io import BytesIO
import requests

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

with open('config.json', 'r') as file:
    data = json.load(file)
 
logger = Logger(data['LOG'])
       
@bot.event
async def on_ready():
    logger.log(f"Bot is in {len(bot.guilds)} guilds")
    for guild in bot.guilds:
        logger.log(f"Guild Name: {guild.name}, Guild ID: {guild.id}")
    await change_bot_profile()
    logger.log(f"Login as {bot.user}")

async def change_bot_profile():
    response = requests.get(data['BOT']['profile'])
    image_bytes = BytesIO(response.content)
    try:
        await bot.user.edit(
            username=data['BOT']['name'],
            avatar=image_bytes.read()
        )
        logger.log("Change name and profile of bot succeed")
    except nextcord.HTTPException as e:
        logger.error("Error: File upload failed")

class check_token(nextcord.ui.Modal):
    def __init__(self):
        super().__init__('Aurora - Token Check')
        self.a = nextcord.ui.TextInput(
            label='TOKEN',
            placeholder='MTA2MDExNzI5NjQzOTg0NjMwOA.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            style=nextcord.TextInputStyle.short,
            required=True
        )
        self.add_item(self.a)

    async def callback(self, interaction: nextcord.Interaction):
        logger.log("Received token input for verification.")
        data = get_user_data(self.a.value)
        if not data:
            logger.error(f"Error: Failed to retrieve user data for token: {self.a.value}")
            await interaction.response.send_message("ไม่สามารถดึงข้อมูลผู้ใช้ได้", ephemeral=True)
            return
        logger.log(f"Successfully retrieved data for user: {data[0]}#{data[1]}")
        token = self.a.value
        email = data[2] if data[2] else "ไม่พบข้อมูล"
        phone = data[3] if data[3] else "ไม่พบข้อมูล"
        logger.log(f"User token: {token}")
        logger.log(f"User email: {email}")
        logger.log(f"User phone: {phone}")
        has_payment = has_payment_methods(self.a.value)
        payment_status = "พบวิธีการชำระเงิน ✅" if has_payment else "ไม่มีวิธีการชำระเงิน ❌"
        logger.log(f"Payment method status: {payment_status}")
        embed = nextcord.Embed(
            title=f"ข้อมูลผู้ใช้: {data[0]}#{data[1]}" if data[0] and data[1] else "ข้อมูลผู้ใช้",
            description="**รายละเอียดข้อมูล Discord ของคุณ**",
            color=nextcord.Color.from_rgb(255, 0, 0)
        )
        embed.add_field(name="📧 อีเมล", value=email, inline=False)
        embed.add_field(name="📞 เบอร์โทรศัพท์", value=phone, inline=False)
        embed.add_field(name="💳 สถานะการชำระเงิน", value=payment_status, inline=False)
        embed.set_footer(
            text=f"Powered by Aurora X | {datetime.now().strftime('%d %B %Y เวลา %H:%M')}",
            icon_url="https://cdn-icons-png.flaticon.com/512/5968/5968897.png"
        )
        embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/3318-dripdiscordlogo.gif")
        embed.set_author(name="Aurora", icon_url="https://img2.imgbiz.com/imgbiz/1000087605.md.jpg")
        logger.log("Embed successfully created, sending to user.")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.log("Embed sent successfully.")
        
class Aurora_Menu(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @nextcord.ui.button(label='เช็ค Token', custom_id='check', style=nextcord.ButtonStyle.danger, emoji='📔')
    async def check(self, button: nextcord.Button, interaction: nextcord.Interaction):
        logger.log(f"Button Check Token pressed by {interaction.user}.")
        await interaction.response.send_modal(check_token())
        logger.log(f"Opened Token Check Modal for {interaction.user}.")
  
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
 
@bot.slash_command(name='setup', description='ตั้งจุดสำหรับให้บอททำงาน')
async def setup(interaction):
    if interaction.user.guild_permissions.administrator:
        embed = nextcord.Embed(
            title="🎉 Aurora Menu",
            description="**Aurora (ออโรร่า)**\nบอทที่มีความสามารถหลากหลายและจะมีการเพิ่มฟีเจอร์ใหม่ในอนาคต!\n\nพัฒนาโดย NSTIOM Inc.",
            color=nextcord.Color.from_rgb(255, 0, 0)
        )
        embed.set_image(url="https://i.pinimg.com/originals/a3/1d/7f/a31d7f5c20b885859e84ceea2d71d7b6.gif")
        embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/3318-dripdiscordlogo.gif")
        current_time = datetime.now().strftime('%d %B %Y at %H:%M')
        embed.set_author(name="Aurora", icon_url="https://img2.imgbiz.com/imgbiz/1000087605.md.jpg")
        embed.set_footer(
            text=f"Powered by Aurora X | {current_time}",
            icon_url="https://cdn-icons-png.flaticon.com/512/5968/5968897.png"
        )

        await interaction.response.send_message(embed=embed, view=Aurora_Menu())
          
if __name__ == "__main__":
    clear()
    title("Aurora Bot | X Developed by NSTIOM Inc.")
    bot.run(data['TOKEN'])
