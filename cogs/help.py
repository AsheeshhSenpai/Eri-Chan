import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def help(self, ctx):
        kana = self.client.get_user(self.kana_id)
        try:
            h = discord.Embed(
            title="HELP HAS COME!",
            description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
            color=0x2e69f2,
            )
            h.add_field(
            name="🔑 **PREFIX**", 
            value=f"Send `kana prefix`", 
            inline=True
            )
            h.add_field(
            name="📃 **COMMANDS**",
            value=f"Send `kana cmds`",
            inline=True
            )
            h.add_field(
            name="⚙ **SOURCE**",
            value=f"Send `kana source`",
            inline=True
            )
            h.add_field(
            name="🎐 **INVITE ME**",
            value=f"[Click here](https://discord.com/api/oauth2/authorize?client_id=857835279259664403&permissions=318528&scope=bot)",
            inline=True
            )
            h.add_field(
            name="❓ **ABOUT**",
            value=f"[Click here](https://github.com/AsheeshhSenpai/Kanna-Chan/blob/main/README.md#about)",
            inline=True
            )
            h.add_field(
            name="⭐ **UPVOTE ME**",
            value=f"[Click here](https://discordbotlist.com/bots/kanna-chan/upvote)",
            inline=True
            )
            h.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=h)
        except Exception as e:
            print(e)

    @commands.command()
    async def source(ctx):
        await ctx.send("https://github.com/AsheeshhSenpai/Kanna-Chan")
        
    @commands.command()
    async def vote(self, ctx):
        emb = discord.Embed(title="UPVOTE KANNA CHAN!!", description="Vote for Kanna uwu\n[Click here](https://discordbotlist.com/bots/kanna-chan/upvote)", color=0x2e69f2)
        kana = self.client.get_user(self.kana_id)
        emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def prefix(ctx):
        await ctx.send("Prefixes for kanna are `k.`, `kana ` and `kanna `.")

    @commands.command()
    async def cmds(self, ctx):
        kana = self.client.get_user(self.kana_id)
        try:
            h = discord.Embed(
            title="COMMANDS",
            description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
            color=0x2e69f2,
            )
            h.add_field(
            name="🤪 **FUN**", 
            value=f"Send `kana fun` to see list of commands available.", 
            inline=False
            )
            h.add_field(
            name="💳 **CUSTOM CARDS**",
            value=f"`simpcard (person you simp for)` Kana makes a simpcard for you with your name and pfp on it.\n`gaycard` Kana makes a gaycard for you with your name and pfp.\n`uwucard` (mention someone) Kana makes a card to show your love for another person uwu.",
            inline=False
            )
            h.add_field(
            name="🎴 **AVATAR**",
            value=f"`av`, `avatar` or `pfp` Kana sends pfp of a user or shared pfp.",
            inline=False
            )
            h.add_field(
            name="🧩 **GAMES**",
            value=f"Send `kana games` to see list of games available and how to play them.",
            inline=False
            )
            h.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=h)
        except Exception as e:
            print(e)

    @commands.command()
    async def fun(self, ctx):
        kana = self.client.get_user(self.kana_id)
        try:
            h = discord.Embed(
            title="FUN COMMANDS",
            description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
            color=0x2e69f2,
            )
            h.add_field(
            name="❤ **Love**", 
            value=f"Kanna sends love to the person.", 
            inline=True
            )
            h.add_field(
            name="🤚 **Pat**",
            value=f"pat any person.",
            inline=True
            )
            h.add_field(
            name="🙇‍♀️ **Thank**",
            value=f"Kanna thanks the person.",
            inline=True
            )
            h.add_field(
            name="🤔 **Think**",
            value=f"Kanna thinks hmmm..",
            inline=True
            )
            h.add_field(
            name="😮 **Amazed**",
            value=f"Kanna is amazed woah..",
            inline=True
            )
            h.add_field(
            name="🫂 **Hug**",
            value=f"Kanna hugs the person.",
            inline=True
            )
            h.add_field(
            name="💃 **Dance**",
            value=f"Kanna dances with the person.",
            inline=True
            )
            h.add_field(
            name="🔪 **Kill**",
            value=f"Kanna kills the person.",
            inline=True
            )
            h.add_field(
            name="🤝 **Befriend**",
            value=f"Kanna befriends the person.",
            inline=True
            )
            h.add_field(
            name="👅 **Lick**",
            value=f"lickie lickie..",
            inline=True
            )
            h.add_field(
            name="😈 **Attack**",
            value=f"Kanna attacks",
            inline=True
            )
            h.add_field(
            name="🗣 **Say**",
            value=f"Kanna says what you want her to say.",
            inline=True
            )
            h.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=h)
        except Exception as e:
            print(e)

    @commands.command()
    async def games(self, ctx):
        kana = self.client.get_user(self.kana_id)
        emb = discord.Embed(title="GAMES", color=0x2e69f2)
        emb.add_field(
            name="🌚 **TRUTH OR DARE**",
            value="Start a game of truth or dare using eri! For truth send `kanna truth` and for dare send `kanna dare`.",
            inline="False"
        )
        emb.add_field(
            name="🎰 **LOTTERY**",
            value="Start a game of lattery using eri. You will have to send three random numbers between 0 to 5 with space in between like `kanna lottery 1 3 4`.",
            inline="False"
        )
        emb.add_field(
            name="📄 **DEFINE**",
            value="`kana df (your query here)` Kana sends the definition of your query.",
            inline="False"
        )
        emb.add_field(
            name="❤ **MARRY**",
            value="Marry any person. Send `kana marry` to know more.",
            inline="False"
        )
        emb.add_field(
            name="🥰 **SHIP**",
            value="Ship two people, cus why not? Command: `kanna ship`",
            inline="False"
        )
        emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Help(client))
    print(">> Help loaded")