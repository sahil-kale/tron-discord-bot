import datetime

import discord

from commands import _mongoFunctions, _embedMessage, _dateFunctions


async def set_birthday(ctx: discord.Message, client: discord.Client):
    if not _mongoFunctions.is_user_id_linked_to_verified_user_in_guild(ctx.guild.id, ctx.author.id) and _mongoFunctions.get_settings(ctx.guild.id)['verification_enabled']:
        replyEmbed = _embedMessage.create("SetBirthday Reply", "Invalid Permissions", "red")
        await ctx.channel.send(embed = replyEmbed)
        return

    message_contents = ctx.content.split(" ")

    if len(message_contents) == 4:

        message_contents.pop(0)

        # Expected format is YYYY MM DD
        birth_year = message_contents[0]
        birth_month = message_contents[1]
        birth_day = message_contents[2]

        error_check = _dateFunctions.check_for_errors_in_date(birth_year, birth_month, birth_day)
    else:
        error_check = 1

    if error_check == 1:
        await ctx.channel.send(
            embed = _embedMessage.create("SetBirthday Reply", "The syntax is invalid! Make sure it is in the format YYYY MM DD\nEx: $setbirthday 2002 07 26", "red"))
        return
    if error_check == 2:
        await ctx.channel.send(embed = _embedMessage.create("SetBirthday Reply", "The date is invalid, please ensure that this is a valid date.", "red"))
        return

    birth_date_string = '-'.join(message_contents)

    await ctx.channel.send(embed = _embedMessage.create("SetBirthday Reply", "Your birthday has been set!", "blue"))

    await ctx.delete()

    _mongoFunctions.set_users_birthday(ctx.author.id, datetime.datetime.strptime(birth_date_string, "%Y-%m-%d"))
