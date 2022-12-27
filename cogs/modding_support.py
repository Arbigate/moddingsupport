"""
Copyright notice:

Information for commands partially created and primarily gathered by Geborgen

Copyright (C) 2022-2023 Geborgen
Copyright (C) 2022-2023 Arbigate

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import random
from discord.ext import commands
from common_exceptions import sos_acronym
from common_exceptions import gamepass_gif
from typing import Mapping, List, Optional


class ModdingSupport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='source', description='Bot source code')
    async def source(self, ctx):
        embed = discord.Embed(description='[Source Code](https://github.com/Arbigate/moddingsupport)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='guide', description='Beginners modding guide')
    async def guide(self, ctx):
        embed = discord.Embed(description='[Modding Guide](https://docs.google.com/document/d/1jTXnuuLZQ201rLRFw0TbxDnBDO9DqZDcCqFIJJSXCDU/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='skse', description='SKSE tutorial')
    async def skse(self, ctx):
        embed = discord.Embed(title='SKSE Tutorial', description='Launch your game at least once. Go [here](http://skse.silverlock.org/) and download; **__MAKE SURE YOU GET THE RIGHT VERSION FOR YOUR GAME.__** \nDrag the files from the image below into your game folder, located at \n Steam/steamapps/common/Skyrim Special Edition. \n\nKeep in mind, from now on you will have to launch your game from skse_loader.exe (do not launch through Steam). If you use MO2, it will add an executable there automatically. \n\n[Video Tutorial](https://www.youtube.com/watch?v=tdiFIL_02dI)', color=0x197482)
        embed.set_image(url='https://i.imgur.com/E2HoLOc.png')
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ae', description='Information about AE')
    async def ae(self, ctx):
        embed = discord.Embed(title='AE Info Board', description="The Anniversary Edition *update* was forced for ALL users, while the *upgrade* is a new DLC that includes CC content. Everyone has the AE update, which brings your game version from **1.5.97** to **1.6.640**. \n\nAny mod that uses an SKSE DLL will not work on AE unless it has been updated by the author. At this point, most mods are updated. \n\nMake sure your SKSE mods match your game version. You can check by seeing what file you downloaded, usually they will indicate AE compatibility. \n\n[SKSE Plugin Status](https://modding.wiki/en/skyrim/users/skse-plugins) \n\nIt is possible to downgrade your game (not recommended for average users). \nSee -downgrade for more info.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='downgrade', description='Downgrading game tutorial')
    async def downgrade(self, ctx):
        embed = discord.Embed(title='How to Downgrade', description='It is possible to downgrade your game from 1.6.640 to 1.5.97 for mod compatibility. This is becoming more and more obsolete as more mods get updated, but the option is still available. \n\n[Downgrade Patcher Download](https://www.nexusmods.com/skyrimspecialedition/mods/57618) \n[Instructions](https://www.youtube.com/watch?v=r2XSWUkOKz0)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='version', description='Breaks down versions of the game')
    async def version(self, ctx):
        embed = discord.Embed(title='What version of Skyrim should I get?', description='Legendary Edition (LE): The original version of Skyrim released in 2011, with all DLC. Oldrim refers to the base game without DLC. This version is mostly unsupported. \n\nSpecial Edition (SE): Updated version of the game, released in 2016. Includes all DLC and major graphical/engine updates. Most mods are released here, and you will get the most support for SE.', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='porting', description='Tutorial for porting mods', aliases=['converting', 'port', 'convert'])
    async def porting(self, ctx):
        embed = discord.Embed(description="[TLO's Converting Mods Tutorial](https://docs.google.com/document/d/1V0J-j2mrmEmK0Q7ugVofEyRfa5Ugg1YZl38ikH_6NOg/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='crash', description='What to do in the event of a crash')
    async def crash(self, ctx):
        embed = discord.Embed(title='Crash Resources', description="Use [this](https://www.nexusmods.com/skyrimspecialedition/mods/21294) mod to generate crash logs. \nUse [this](https://www.nexusmods.com/skyrimspecialedition/mods/59596) instead if you're on AE. \nUse [this](https://www.nexusmods.com/skyrimspecialedition/mods/59818) if you're on VR. \n\n[Reading SE Crash Logs Tutorial](https://docs.google.com/document/d/1Gw63VpT_PiiOXaHUeJvrjr3j9H-j-3N17ivxGA-CiTM/edit?usp=sharing) \n[Reading AE Crash Logs Tutorial](https://www.nexusmods.com/skyrimspecialedition/mods/75430) \n[Common Crashes & Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/49130) \n[Troubleshooting Checklist](https://docs.google.com/document/d/1yPob0eHPlE6s_wy-ryCbqp7YuLcQTPdHhXvFOsqchss/edit?usp=sharing) \n[Stability Guide](https://www.youtube.com/watch?v=ucJkYLyRMso)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='modmanager', description='Mod manager comparison')
    async def modmanager(self, ctx):
        embed = discord.Embed(title='What mod manager should I use?', description='[Differences Breakdown](https://docs.google.com/document/d/1tc_upWT4rLZPmShiKR7UIqr1fVq_HsRHUew9xww_5vs/edit?usp=sharing) \n[MO2 Download](https://www.nexusmods.com/skyrimspecialedition/mods/6194) \n[Vortex Download](https://www.nexusmods.com/about/vortex/) \n\nYou may see a lot of references to “Nexus Mod Manager” or NMM. DO NOT USE NMM. Not only is it no longer officially maintained or even supported by modern tools, it is known to directly modify game files and lacks essential features.', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='reinstall', description='How to correctly reinstall the game')
    async def reinstall(self, ctx):
        embed = discord.Embed(description='[Clean Reinstall Tutorial](https://www.youtube.com/watch?v=zQ5uNCKOKmI)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='laws', description='10 commandments of modding')
    async def laws(self, ctx):
        embed = discord.Embed(description="[Arbi's 10 Commandments of Modding](https://docs.google.com/document/d/1MTYjs5ofT0ISXFVfAZWssbWZ8KDcPeOoJ3FBpscTxyY/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='nemesis', description='Tutorial for Nemesis engine')
    async def nemesis(self, ctx):
        embed = discord.Embed(title='Nemesis Unlimited Behavior Engine', description="Nemesis is the modern replacement for FNIS. It is essentially the same thing, you don't need FNIS at all if you use Nemesis. It will even generate an empty FNIS.esp for compatibility. The only thing it doesn't support are creature animations. \n\n[Download](https://www.nexusmods.com/skyrimspecialedition/mods/60033) \n[Instructions](https://www.youtube.com/watch?v=ki2bghy2Mvo) \n[Instructions for Vortex](https://www.youtube.com/watch?v=W9hrvc8ync4) \n*Please keep in mind that these tutorials use Nemesis from GitHub; you can now just download from Nexus and install through your mod manager normally, then pick up from there.* \n\nWhitelist Nemesis in your antivirus/turn off real time protection if you have issues. Also make sure you are installing mods for the correct version of your game.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='dyndolod', description='Tutorial for DynDOLOD')
    async def dyndolod(self, ctx):
        embed = discord.Embed(title='DynDOLOD Guide', description='[Guide by Kiloee & Geborgen](https://docs.google.com/document/d/1n1Bqh1a2kD_Kgg8Hfxc3GZtpYMORP6lYg76kWwP4rOo/edit?usp=sharing) \n[Video Tutorial](https://www.youtube.com/watch?v=encZYHEeQrQ)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='cleaning', description='Tutorial for xEdit plugin cleaning')
    async def cleaning(self, ctx):
        embed = discord.Embed(description='[Cleaning Master Files Tutorial by Arbigate](https://docs.google.com/document/d/1ro3PiBbWimZSwYz1h4DaG_DnpiIFVwNmyqnV_SKdC8Q/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='navmesh', description='Tutorial for fixing deleted navmesh')
    async def navmesh(self, ctx):
        embed = discord.Embed(description='[Fixing Deleted Navmesh Tutorial by Arbigate](https://docs.google.com/document/d/1tTu3N4l5FTs8zb5sNrTvkHFXgrXvQC7WVdT_XJnaXe4/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='eslify', description='Tutorial for ESL flagging plugins')
    async def eslify(self, ctx):
        embed = discord.Embed(description='[ESL Flagging Plugins Tutorial](https://www.nexusmods.com/skyrimspecialedition/mods/21618)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='vanillastart', description='How to fix broken vanilla intro')
    async def vanillastart(self, ctx):
        embed = discord.Embed(title='Broken Vanilla Intro Fix', description='Use [this](https://www.nexusmods.com/skyrimspecialedition/mods/272) mod to make your character, then wait a few minutes and let your scripts load. Then select vanilla start. \n\nAdditionally, try [this](https://www.nexusmods.com/skyrimspecialedition/mods/8004) fix.', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='darkface', description='Dark face bug fix')
    async def name(self, ctx):
        embed = discord.Embed(title="Dark Face Bug Fix", description="[Info Board](https://www.reddit.com/r/skyrimmods/comments/n6gio6/guide_the_dark_face_bug_and_what_causes_it_and/) \n\n[Face Discoloration Fix Download](https://www.nexusmods.com/skyrimspecialedition/mods/42441) \n*Please note that this only fixes the dark tint, and doesn't fix the actual facegen issue.* \n\n[EasyNPC Download](https://www.nexusmods.com/skyrimspecialedition/mods/52313) \n*This tool will merge all of your face data into one plugin.*", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='loadorder', description='Load order resources', aliases=['loot'])
    async def loadorder(self, ctx):
        embed = discord.Embed(title='Load Order Resources', description='[LOOT Download](https://loot.github.io/) \n[LOOT Basic Tutorial](https://www.youtube.com/watch?v=fyvwslyKiog) \n\n[Load Order Basics](https://www.youtube.com/watch?v=Ncv_FWQUw0k)\n[Load Order Structure Info](https://skyrimseblog.wordpress.com/load-order-structure/)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='corrupt', description='Corrupted game save resources', aliases=['fallrim'])
    async def corrupt(self, ctx):
        embed = discord.Embed(title='Save Corruption Resources', description='When playing a modded game, **always** make frequent saves that **are not** quick or autosaves. **Do not** save during heavy script load areas e.g. combat. **Do not** delete old saves. \n\n[FallrimTools](https://www.nexusmods.com/skyrimspecialedition/mods/5031) \nREAD THE MOD PAGE', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='essentials', description='List of essential mods')
    async def essentials(self, ctx):
        embed = discord.Embed(description='[Essential Bugfixes & Tools List](https://github.com/Geborgen/usefulmods)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='script', description='Script info board')
    async def script(self, ctx):
        embed = discord.Embed(description="[Monitor's Script Info Board](https://docs.google.com/document/d/1JdpbjIjIJq_kdr6mC43pVjfyaWngWWBwGRDc-6SkBcc/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='modlimit', description='Mod limit info board')
    async def modlimit(self, ctx):
        embed = discord.Embed(description='[255 Mod Limit for SE/AE Info by Monitor](https://docs.google.com/document/d/1YQFOtjXTqq-0EC0OFPcKZBV5a-ljt1zklXWrfBgXAsc/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='enb', description='ENB info board')
    async def enb(self, ctx):
        embed = discord.Embed(title="ENB Info Board", description="An ENB is, essentially, a complete replacement of the game's lighting and shaders, *in addition* to any weather or lighting mods you might have installed. Two different presets can change the aesthetic of a game drastically; you should choose wisely and find one suited to your weather mod and/or game aesthetic. Do you want fairytale fantasy? Real life? Dark Souls? There’s a preset for every visual persuasion. \n\nEvery ENB has installation instructions on the mod page. You should know the basic steps however; download the most recent ENB binaries [here](http://enbdev.com/download_mod_tesskyrimse.htm) and extract ONLY the two .DLL files in the WrapperVersion folder to your game directory. Then download the preset of your choice and extract to your game directory. \n\n[ENB Settings Breakdown](https://stepmodifications.org/wiki/Guide:ENBSeries_INI)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ini', description='Ini resources')
    async def ini(self, ctx):
        embed = discord.Embed(title='INI Resources', description='[INI Settings Breakdown](https://stepmodifications.org/wiki/Guide:Skyrim_Configuration_Settings#SkyrimPrefs.ini) \n[BethINI Download](https://www.nexusmods.com/skyrimspecialedition/mods/4875) \n*Instructions for BethINI are on the mod page.*', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='modlist', description='Modlist sharing resources')
    async def modlist(self, ctx):
        embed = discord.Embed(title='Tools for Sharing Modlists', description='[Modwat.ch Download](https://modwat.ch/) \n[Modwat.ch for Vortex](https://www.nexusmods.com/site/mods/152) \n[Load Order Library](https://loadorderlibrary.com/)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ussep', description='Link to USSEP')
    async def ussep(self, ctx):
        embed = discord.Embed(title='Unofficial Skyrim Special Edition Patch', description='[USSEP Download](https://www.nexusmods.com/skyrimspecialedition/mods/266) \n[Old Version (1.6.353)](https://www.nexusmods.com/skyrimspecialedition/mods/266?tab=files&file_id=292193) \n[Older Version (1.5.97)](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=209150&game_id=1704) \n[Non-Arthmoor Alternatives](https://www.reddit.com/r/skyrimmods/comments/usamua/unarthmoored_ussep_compendium/)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='tudm', description='Link to TUDM')
    async def tudm(self, ctx):
        embed = discord.Embed(title="The Ultimate Dodge Mod", description="[TUDM Reborn Download](https://www.nexusmods.com/skyrimspecialedition/mods/63000) \n\nCompatible with AE. Please note that your vanilla sneak key will become your dodge key. You can configure the key you use for sneaking in TUDM's MCM.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='synthesis', description='Link to Synthesis patcher')
    async def synthesis(self, ctx):
        embed = discord.Embed(title='Synthesis Patcher', description='[Download](https://github.com/Mutagen-Modding/Synthesis/wiki/Installation) \n[Guide](https://www.youtube.com/watch?v=s7luh0hMMAU)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='xbox', description='Xbox mod recommendations')
    async def xbox(self, ctx):
        embed = discord.Embed(description="[Sovereign's Noteworthy Xbox Mods](https://docs.google.com/document/d/1_wwawgIc2NFe-BYZptcJN9kli92zDkKT4Prg5dVqgpI/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ps4', description='PlayStation mod recommendations')
    async def ps4(self, ctx):
        embed = discord.Embed(description="[Nick's Noteworthy PlayStation Mods](https://docs.google.com/document/d/1NueH5pWdWjgBaH5AVyiJGfy8jaDyNYuhiXgRNfDZsIc/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='sinitar', description='Essay on Sinitar')
    async def sinitar(self, ctx):
        embed = discord.Embed(description='[He had a 29 page essay written about him, should say something.](https://docs.google.com/document/d/1F1-6lF8dI4i2Zz8iT-bv_Ci1VO9MSU4MiSUrT5JqgHA/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='sos', description='Links a random SOS mod')
    async def sos(self, ctx):
        random_sos = random.choice(list(sos_acronym))
        await ctx.send(random_sos)

    @commands.hybrid_command(name='gamepass', description='Sends a random "skse does not work with gamepass" gif')
    async def gamepass(self, ctx):
        gamepass_meme = random.choice(list(gamepass_gif))
        await ctx.send(gamepass_meme)

    @commands.hybrid_command(name='rtfm', description='Sends a "read the manual" image')
    async def rtfm(self, ctx):
        await ctx.send('https://i.imgur.com/k3qSKbl.png')

    @commands.hybrid_command(name='tryitandsee', description='Try it and see')
    async def tryitandsee(self, ctx):
        await ctx.send('https://tryitands.ee/')

    @commands.hybrid_command(name='dontasktoask', description='Sends a message about not asking to ask a question')
    async def dontasktoask(self, ctx):
        await ctx.send('https://dontasktoask.com/')

    @commands.hybrid_command(name='stefan', description="Don't listen to him...")
    async def stefan(self, ctx):
        await ctx.send('ignore him')

    @commands.hybrid_command(name='ping', description='Checks the ping of bot')
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! Bot latency is ``{round(self.bot.latency*1000)} ms``')


class HelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.page_number = 0
        self.help_body = ["-guide (beginner's modding guide) \n-skse (SKSE tutorial) \n-ae (information about AE) \n-downgrade (downgrading game tutorial) \n-version (breaks down the versions of the game) \n-porting / -converting (tutorial for porting mods) \n-crash (what to do in the event of a crash) \n-modmanager (mod manager comparison) \n-reinstall (how to correctly reinstall the game) \n-laws (10 Commandments of Modding™️)", "-nemesis (tutorial for Nemesis engine) \n-dyndolod (tutorial for DynDOLOD) \n-cleaning (xEdit plugin cleaning) \n-navmesh (fixing deleted navmesh) \n-eslify (ESL flagging plugins) \n-vanillastart (broken vanilla intro fix) \n-darkface (dark face bug fix) \n-loadorder / -loot (load order resources) \n-corrupt / -fallrim (corrupted save game resources)", "-essentials (list of essential mods) \n-script (script info board) \n-modlimit (mod limit info board) \n-enb (ENB info board) \n-ini (ini resources) \n-modlist (modlist sharing resources) \n-ussep (link to USSEP) \n-tudm (link to TUDM) \n-synthesis (link to Synthesis patcher) \n-xbox (Xbox mod recommendations) \n-ps4 (PlayStation mod recommendations)", "-sinitar (essay on Sinitar) \n-sos (returns a random 'SOS' mod) \n-gamepass (SKSE does not work with it) \n-rtfm (read the [redacted] manual) \n-tryitandsee (please do this) \n-dontasktoask (seriously, just ask your question) \n-stefan (ignore him) \n-source (links bot source code) \n/link (links mods, separate multiple with commas) \n/suggest-acronym (requests acronym to be added to mod linking"]

    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], List[commands.Command]]):
        view = HelpButtons(HelpCommand())
        ctx = self.context
        embed = discord.Embed(title="Modding Support Help", description=self.help_body[0], color=0x197482)
        embed.set_footer(text="Page 1/4 | Use /ping to return latency")
        view.message = await ctx.send(embed=embed, view=view)


class HelpButtons(discord.ui.View):
    def __init__(self, help_command):
        super().__init__()
        self.help_command = help_command
        self.timeout = 120

    async def on_timeout(self):
        for item in self.children:
            self.remove_item(item)
        await self.message.edit(view=self)

    @discord.ui.button(label="◀ Previous Page", style=discord.ButtonStyle.gray)
    async def help_button_left(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.help_command.page_number > 0:
            self.help_command.page_number -= 1
            embed = discord.Embed(title="Modding Support Help", description=self.help_command.help_body[self.help_command.page_number], color=0x197482)
            embed.set_footer(text=f"Page {self.help_command.page_number + 1}/4 | Use /ping to return latency")
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.defer()

    @discord.ui.button(label="Next Page ▶", style=discord.ButtonStyle.gray)
    async def help_button_right(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.help_command.page_number < 3:
            self.help_command.page_number += 1
            embed = discord.Embed(title="Modding Support Help", description=self.help_command.help_body[self.help_command.page_number], color=0x197482)
            embed.set_footer(text=f"Page {self.help_command.page_number + 1}/4 | Use /ping to return latency")
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.defer()


async def setup(bot):
    await bot.add_cog(ModdingSupport(bot))