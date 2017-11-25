import discord
from discord.ext import commands
import os
import json
import inspect
import io
import textwrap
import traceback
from contextlib import redirect_stdout

bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'))
bot.remove_command('help')
@bot.event
async def on_connect():
    print("print('connected')")
    bot._last_result = None

@commands.check(lambda ctx: ctx.author.id == 180314310298304512)
async def role(self, ctx, member:discord.Member):
    #await member.add_roles
    pass

@commands.check(lambda ctx: discord.utils.get(discord.utils.get(bot.guilds, id=345787308282478592).roles, id=383188931384180737) in ctx.author.roles)
@bot.command(name='eval')
async def _eval(ctx, *, body):
    """Evaluates python code"""
    blocked_words = ['.delete()', 'os']
    if body in blocked_words:
        return await ctx.send('Your code contains certain blocked words.')
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        '_': bot._last_result,
        'source': inspect.getsource
    }

    env.update(globals())

    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:
                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = ctx.paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = ctx.paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')

def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    # remove `foo`
    return content.strip('` \n')

def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'


try:
    with open('config.json') as f:
        token = json.load(f).get('token') or os.environ.get('token')
    bot.run(token, reconnect=True)
except Exception as e:
    print(e)
