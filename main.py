import discord
from discord import app_commands
import random
import string
import json
import os


TOKEN = "MTM0Njg1MzEzNDc4MTI1NTc0Mg.GWFy1n.58JsEJ5g3UU44roN1UVjdib8Yc2l1RaGoMA_IQ"
GUILD_ID = 1278743108464541796  # Sunucu ID'sini buraya girin
ADMIN_ROLE_ID = 1289891789775306763  # Admin rol ID'sini buraya girin
CODES_FILE = "codes.json"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Kodları yükleme
if os.path.exists(CODES_FILE):
    with open(CODES_FILE, "r") as f:
        codes = json.load(f)
else:
    codes = []

def save_codes():
    with open(CODES_FILE, "w") as f:
        json.dump(codes, f, indent=4)

def generate_code():
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))

@tree.command(name="kodüret", description="Kod Üret.", guild=discord.Object(id=GUILD_ID))
async def koduret(interaction: discord.Interaction):
    if ADMIN_ROLE_ID not in [role.id for role in interaction.user.roles]:
        await interaction.response.send_message("Bu komutu kullanma yetkiniz yok!", ephemeral=True)
        return
    
    new_code = generate_code()
    while new_code in codes:
        new_code = generate_code()
    
    codes.append(new_code)
    save_codes()
    await interaction.response.send_message(f"Yeni kod oluşturuldu: `{new_code}`", ephemeral=True)

@tree.command(name="kodgöster", description="Kayıtlı tüm kodları gösterir.", guild=discord.Object(id=GUILD_ID))
async def kodgoster(interaction: discord.Interaction):
    if ADMIN_ROLE_ID not in [role.id for role in interaction.user.roles]:
        await interaction.response.send_message("Bu komutu kullanma yetkiniz yok!", ephemeral=True)
        return
    
    if not codes:
        await interaction.response.send_message("Kayıtlı kod bulunamadı.", ephemeral=True)
        return
    
    await interaction.response.send_message("Kayıtlı kodlar:\n" + "\n".join(codes), ephemeral=True)

@tree.command(name="assettocorsa", description="Assetto Corsa Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Assetto Corsa\nKullanıcı Adı: cybermachine040\nŞifre: Bwahid512040"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="raft", description="Raft Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Raft\nKullanıcı Adı: qq1070414930\nŞifre: mhEklDDkjP"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)



@tree.command(name="bannerlord", description="Bannerlord Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Bannerlord\nKullanıcı Adı: thb112676\nŞifre: steamok456789"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="tombraider", description="Tomb Raider Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Tomb Raider\nKullanıcı Adı: dynacraft\nŞifre: raposafox3i"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)



@tree.command(name="gta5", description="Gta 5 Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Gta 5\nKullanıcı Adı: aocab2555\nŞifre: fajok1993"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"{client.user} olarak giriş yapıldı!")





@tree.command(name="forzahorizon5", description="Forza Horizon 5 Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Forza Horizon 5\nKullanıcı Adı: aocab2555\nŞifre: fajok1993"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="streamerlifesimulator2", description="Streamer Life Simulator 2 Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Streamer Life Simulator 2\nKullanıcı Adı: carmechanic21_396174\nŞifre: Xaviz_Remax_Evren_285645"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="hitman2", description="Hitman 2 Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Hitman 2\nKullanıcı Adı: lolopasha\nŞifre: mozgovoi65"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="pes2021", description="Pes 2021 Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Pes 2021\nKullanıcı Adı: dimkoxd\nŞifre: Dimko1995"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="godofwar", description="God Of War Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"God Of War\nKullanıcı Adı: Xavizgodofwar_1\nŞifre: Xavizgodofwar_835856"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="callofduty", description="Call of Duty® Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Call of Duty®\nKullanıcı Adı: cybermachine040\nŞifre: Bwahid512040"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)




@tree.command(name="callofdutymodernwarfare2_2009", description="Call of Duty®: Modern Warfare® 2 (2009) Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Call of Duty®: Modern Warfare® 2 (2009)\nKullanıcı Adı: dimkoxd\nŞifre: Dimko1995"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)



@tree.command(name="marvelsspidermanremastered", description="Marvels Spiderman Remastered Oyunu.", guild=discord.Object(id=GUILD_ID))
async def assettocorsa(interaction: discord.Interaction, kod: str):
    if kod not in codes:
        await interaction.response.send_message("Geçersiz kod girdiniz!", ephemeral=True)
        return
    
    codes.remove(kod)
    save_codes()
    
    dm_message = f"Marvels Spiderman Remastered\nKullanıcı Adı: wbtq1087800\nŞifre: steamok456456"
    try:
        await interaction.user.send(dm_message)
        await interaction.response.send_message("Kod doğrulandı! Bilgiler DM olarak gönderildi.", ephemeral=True)
    except:
        await interaction.response.send_message("Özel mesaj kutunuz kapalı olduğu için bilgiler gönderilemedi.", ephemeral=True)





@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"{client.user} olarak giriş yapıldı!")





















client.run(TOKEN)