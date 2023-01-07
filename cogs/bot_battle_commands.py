"""
Copyright notice:
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
from discord.ext import tasks, commands

attack_counter = 0
attack_info = {}


async def sort_leaderboard():
    sorted_leaderboard = sorted(attack_info.items(), key=lambda x: x[1], reverse=True)
    return sorted_leaderboard


class BotBattles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.attack_track.start()

    @commands.hybrid_command(name='attack', description='Attacks the Augur of Dunlain bot!')
    async def attack(self, ctx):
        global attack_counter
        global attack_info

        attack_counter += 1
        attack_info[ctx.author.id] = attack_info.get(ctx.author.id, 0) + 1
        embed = discord.Embed(description=f"\U0001f5e1 Augur of Dunlain took 1 point of damage!", color=0x197482)
        embed.set_footer(text=f'Total Damage Inflicted: {attack_counter}')
        await ctx.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(name='check-attack', description='Checks how much damage has been inflicted on Augur of Dunlain.')
    async def check_attack(self, ctx):
        embed = discord.Embed(description=f"{attack_counter} damage done to Augur of Dunlain so far!", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='attack-leaderboard', description='Returns the leaderboard for attacks against Augur of Dunlain.')
    async def attack_leaderboard(self, ctx):
        description = f'A total of {attack_counter} damage has been dealt to <@1042491973635944479>!\n \n'
        sorted_leaderboard = await sort_leaderboard()
        top_ten_places = 0
        all_places = 0
        for i in sorted_leaderboard[:10]:
            top_ten_places += 1
            description = description + f'{top_ten_places}. <@{i[0]}> - {i[1]} damage dealt\n'
        embed = discord.Embed(title=f"\U0001f3c6 Damage Leaderboard", description=description, color=0x197482)
        embed.set_footer(text=f'Total Contributors: {len(attack_info)} ㅣ Your % Contribution: 0%')
        for i in sorted_leaderboard:
            all_places += 1
            if ctx.author.id == i[0]:
                embed.set_footer(text=f'Your rank: {all_places}/{len(sorted_leaderboard)} ㅣ Your % Contribution: {round((attack_info[ctx.author.id]/attack_counter)*100, 1)}%')
                break
        await ctx.send(embed=embed)

    @tasks.loop(hours=8)
    async def attack_track(self):
        tracking_channel = self.bot.get_channel(1061109702248910898) or await self.bot.fetch_channel(1061109702248910898)
        await tracking_channel.send(f'**----------Total attacks: {attack_counter}----------**')
        await tracking_channel.send(attack_info)


async def setup(bot):
    await bot.add_cog(BotBattles(bot))
