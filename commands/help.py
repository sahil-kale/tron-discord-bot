import discord

from commands import _embedMessage, _mongoFunctions, _checkrole, _util

commandPrefix2 = "$"


async def help_command(ctx: discord.Message, client: discord.Client):
    help_embed = _embedMessage.create("General Commands", "Commands that can be run with BediBot. Each word represents an argument.", "green")
    _embedMessage.add_field(help_embed, commandPrefix2 + "help", "Allows you to view commands!", False)
    _embedMessage.add_field(help_embed, commandPrefix2 + "ping", "Returns Pong", False)

    _embedMessage.add_field(help_embed, commandPrefix2 + "addquote \"quote with spaces\" Name",
                            "Adds a quote from the individual of your choice\nEx: " + commandPrefix2 + "addQuote \"Life is Good\", Bedi", False)
    _embedMessage.add_field(help_embed, commandPrefix2 + "getQuotes person pagenumber",
                            "Gets a persons quotes with a page number, with each page in 5 days\nEx: " + commandPrefix2 + "getQuote Bedi 2", False)

    await ctx.channel.send(embed = help_embed)

    if _mongoFunctions.get_settings(ctx.guild.id)['verification_enabled']:
        verification_embed = _embedMessage.create("Verification Commands", "Commands related to verification.", "green")
        _embedMessage.add_field(verification_embed, commandPrefix2 + "verify userID@uwaterloo.ca",
                                "Allows you to verify yourself as a UWaterloo Student and access the server\nEx: " + commandPrefix2 + "$verify g0ose@uwaterloo.ca", False)
        _embedMessage.add_field(verification_embed, commandPrefix2 + "unverify",
                                "Unverifies you from the server. Note that this does NOT remove the associated email address from your discord user ID", False)
        _embedMessage.add_field(verification_embed, commandPrefix2 + "confirm code",
                                "Allows you to enter in your 2FA verification code after you run the verify command\nEx: " + commandPrefix2 + "confirm 123456789", False)
        await ctx.channel.send(embed = verification_embed)

    if _mongoFunctions.get_settings(ctx.guild.id)['birthday_announcements_enabled']:
        birthday_embed = _embedMessage.create("Birthday Commands", "Commands related to birthdays.", "green")
        _embedMessage.add_field(birthday_embed, commandPrefix2 + "getbirthdays monthnumber",
                                "Gets all birthdays for the specified month\nEx: " + commandPrefix2 + "getbirthdays 5", False)
        _embedMessage.add_field(birthday_embed, commandPrefix2 + "setbirthday YYYY MM DD",
                                "Allows you to set your birthday and let the server know when to embarrass you :D\nEx: " + commandPrefix2 + "setbirthday 2001 01 01", False)
        await ctx.channel.send(embed = birthday_embed)

    if _mongoFunctions.get_settings(ctx.guild.id)['due_dates_enabled']:
        due_date_embed = _embedMessage.create("Due Date Commands", "Commands related to due dates.", "green")
        _embedMessage.add_field(due_date_embed, commandPrefix2 + "addduedate",
                                "Add's an assignment's due date to be counted down to\nEx: " + commandPrefix2 + "addduedate", False)
        await ctx.channel.send(embed = due_date_embed)

    if _checkrole.author_has_role(ctx, _mongoFunctions.get_settings(ctx.guild.id)['admin_role']) or _util.author_is_bot_owner(ctx):
        admin_embed = _embedMessage.create("Admin Commands", "Commands that can only be run by those with the admin role.", "green")
        _embedMessage.add_field(admin_embed, commandPrefix2 + "removequote \"quote with spaces\" Name",
                                "Removes a quote from the individual of your choice\nEx: " + commandPrefix2 + "addQuote \"Life is Good\", Bedi", False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "adminverify @Mention",
                                "Manually verifies a user. Note that this does NOT add in a role and simply adds them to the database\nEx: " + commandPrefix2 + "adminverify " + client.user.mention,
                                False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "removeduedate", "Remove's a due date\nEx: " + commandPrefix2 + "removeduedate", False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "lockdown role",
                                "Sets send message permissions to false for specified role\nEx: " + commandPrefix2 + "lockdown " + "Tron", False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "unlock role",
                                "Sets send message permissions to True for specified role\nEx: " + commandPrefix2 + "unlock " + "Tron",
                                False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "say title content channel",
                                "Sends a message inside an embed to the specified channel\nEx: " + commandPrefix2 + "say Hello world " + ctx.channel.mention, False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "setbedibotchannel",
                                "Sets the channel which will be used for announcements\nWARNING: This clears the channel's history. Use with caution.", False)
        _embedMessage.add_field(admin_embed, commandPrefix2 + "settings", "Displays the guild's settings", False)
        await ctx.channel.send(embed = admin_embed)
