import discord
from discord.ext import commands
import os
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
import sqlite3
import datetime
import asyncpg
import re
from ast import literal_eval
import botinfo
from cogs.premium import check_upgraded
import topgg
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import asyncio
import aiohttp
import logging
from database import *
import subprocess 
# logging.basicConfig(level=logging.DEBUG)
# log = logging.getLogger(__name__)

# async def on_request_end(
#     session: aiohttp.ClientSession,
#     trace_config_ctx,
#     params: aiohttp.TraceRequestEndParams,
# ) -> None:
#     if params.response.status >= 400:
#         log.warning(
#             'Request to %s failed with status code %s with method %s',
#             params.url,
#             params.response.status,
#             params.method,
#         )

# trace = aiohttp.TraceConfig()
# trace.on_request_end.append(on_request_end)

botinfo.starttime = datetime.datetime.utcnow()
check = False

async def by_cmd(ctx, user: discord.Member, cmd):
    c = await check_upgraded(ctx.guild.id)
    if not c:
        return False
    query = "SELECT * FROM  bypass WHERE guild_id = ?"
    val = (ctx.guild.id,)
    with sqlite3.connect('database.sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute(query, val)
        ig_db = cursor.fetchone()
    if ig_db is None:
        return False
    xd = literal_eval(ig_db['bypass_users'])
    xdd = literal_eval(ig_db['bypass_roles'])
    xddd = literal_eval(ig_db['bypass_channels'])
    if user.id not in xd:
        pass
    else:
        ls = xd[user.id]
        if 'cmd' in ls:
          lss = ls['cmd']
          if lss == "all":
              return True
          elif cmd in lss:
              return True
          else:
              pass
    for i in user.roles:
        if i.id in xdd:
            ls = xdd[i.id]
            if 'cmd' in ls:
              lss = ls['cmd']
              if lss == "all":
                  return True
              elif cmd in lss:
                  return True
              else:
                  pass
    if ctx.channel.id not in xddd:
      pass
    else:
        ls = xddd[ctx.channel.id]
        if 'cmd' in ls:
          lss = ls['cmd']
          if lss == "all":
              return True
          elif cmd in lss:
              return True
          else:
              pass
    return False

async def by_module(ctx, user: discord.Member, module):
    c = await check_upgraded(ctx.guild.id)
    if not c:
        return False
    query = "SELECT * FROM  bypass WHERE guild_id = ?"
    val = (ctx.guild.id,)
    with sqlite3.connect('database.sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute(query, val)
        ig_db = cursor.fetchone()
    if ig_db is None:
        return False
    xd = literal_eval(ig_db['bypass_users'])
    xdd = literal_eval(ig_db['bypass_roles'])
    xddd = literal_eval(ig_db['bypass_channels'])
    if user.id not in xd:
        pass
    else:
        ls = xd[user.id]
        if 'module' in ls:
          lss = ls['module']
          if lss == "all":
              return True
          elif module in lss:
              return True
          else:
              pass
    for i in user.roles:
        if i.id in xdd:
            ls = xdd[i.id]
            if 'module' in ls:
              lss = ls['module']
              if lss == "all":
                  return True
              elif module in lss:
                  return True
              else:
                  pass
    if ctx.channel.id not in xddd:
      pass
    else:
        ls = xddd[ctx.channel.id]
        if 'module' in ls:
          lss = ls['module']
          if lss == "all":
              return True
          elif module in lss:
              return True
          else:
              pass
    return False

async def by_channel(ctx, user: discord.Member, channel: discord.TextChannel):
    c = await check_upgraded(ctx.guild.id)
    if not c:
        return False
    query = "SELECT * FROM  bypass WHERE guild_id = ?"
    val = (ctx.guild.id,)
    with sqlite3.connect('database.sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute(query, val)
        ig_db = cursor.fetchone()
    if ig_db is None:
        return False
    xd = literal_eval(ig_db['bypass_users'])
    xdd = literal_eval(ig_db['bypass_roles'])
    if user.id not in xd:
        pass
    else:
        ls = xd[user.id]
        if 'channel' in ls:
          lss = ls['channel']
          if lss == "all":
              return True
          elif channel.id in lss:
              return True
          else:
              pass
    try:
        for i in user.roles:
            if i.id in xdd:
                ls = xdd[i.id]
                if 'channel' in ls:
                    lss = ls['channel']
                    if lss == "all":
                        return True
                    elif channel.id in lss:
                        return True
                    else:
                        pass
    except:
        pass
    return False

async def by_role(ctx, user: discord.Member, role: discord.Role):
    c = await check_upgraded(ctx.guild.id)
    if not c:
        return False
    query = "SELECT * FROM  bypass WHERE guild_id = ?"
    val = (ctx.guild.id,)
    with sqlite3.connect('database.sqlite3') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute(query, val)
        ig_db = cursor.fetchone()
    if ig_db is None:
        return False
    xd = literal_eval(ig_db['bypass_users'])
    xdd = literal_eval(ig_db['bypass_roles'])
    xddd = literal_eval(ig_db['bypass_channels'])
    if user.id not in xd:
        pass
    else:
        ls = xd[user.id]
        if 'role' in ls:
          lss = ls['role']
          if lss == "all":
              return True
          elif role.id in lss:
              return True
          else:
              pass
    for i in user.roles:
        if i.id in xdd:
            ls = xdd[i.id]
            if 'role' in ls:
              lss = ls['role']
              if lss == "all":
                  return True
              elif role.id in lss:
                  return True
              else:
                  pass
    if ctx.channel.id not in xddd:
      pass
    else:
        ls = xddd[ctx.channel.id]
        if 'role' in ls:
          lss = ls['role']
          if role.id in lss:
              return True
          elif lss == "all":
              return True
          else:
              pass
    return False

async def add_count(ctx, user, guild, cmd_name):
    query = "SELECT * FROM  count WHERE xd = ?"
    val = (1,)
    with sqlite3.connect('./database.sqlite3') as db:
      db.row_factory = sqlite3.Row
      cursor = db.cursor()
      cursor.execute(query, val)
      user_columns = cursor.fetchone()
    if user_columns is None:
        c = {}
        c[user.id] = 1
        cc = {}
        cc[guild.id] = 1
        ccc = {}
        ccc[cmd_name] = 1
        sql = (f"INSERT INTO count(xd, 'user_count', 'guild_count', 'cmd_count') VALUES(?, ?, ?, ?)")
        val = (1, f"{c}", f"{cc}", f"{ccc}",)
        cursor.execute(sql, val)
    else:
        c = literal_eval(user_columns['user_count'])
        if user.id in c:
            c[user.id] = c[user.id] + 1
        else:
            c[user.id] = 1
        c = {k: v for k, v in reversed(sorted(c.items(), key=lambda item: item[1]))}
        sql = "UPDATE count SET 'user_count' = ? WHERE xd = ?"
        val = (f"{c}", 1,)
        cursor.execute(sql, val)
        cc = literal_eval(user_columns['guild_count'])
        if guild.id in cc:
            cc[guild.id] = cc[guild.id] + 1
        else:
            cc[guild.id] = 1
        cc = {k: v for k, v in reversed(sorted(cc.items(), key=lambda item: item[1]))}
        sql = "UPDATE count SET 'guild_count' = ? WHERE xd = ?"
        val = (f"{cc}", 1,)
        cursor.execute(sql, val)
        ccc = literal_eval(user_columns['cmd_count'])
        if cmd_name in ccc:
            ccc[cmd_name] = ccc[cmd_name] + 1
        else:
            ccc[cmd_name] = 1
        ccc = {k: v for k, v in reversed(sorted(ccc.items(), key=lambda item: item[1]))}
        sql = "UPDATE count SET 'cmd_count' = ? WHERE xd = ?"
        val = (f"{ccc}", 1,)
        cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()

async def get_prefix(message: discord.Message):
    with sqlite3.connect('database.sqlite3') as db:
      db.row_factory = sqlite3.Row
      cursor = db.cursor()
      cursor.execute(f'SELECT prefix FROM prefixes WHERE guild_id = {message.guild.id}')
      res = cursor.fetchone()
    if res:
      prefix = str(res[0])
    if not res:
      prefix = '?'
    try:
        cursor.execute(f'SELECT * FROM noprefix WHERE user_id = {message.author.id}')
        res1 = cursor.fetchone()
        if res1 is not None:
            if res1['servers'] is not None:
                no_prefix = literal_eval(res1['servers'])
                if message.guild.id in no_prefix:
                    return [f"<@{message.guild.me.id}>", prefix, ""]
            if res1['main'] is not None:
                if res1['main'] == 1:
                    return [f"<@{message.guild.me.id}>", prefix, ""]
    except:
        pass
    db.commit()
    cursor.close()
    db.close()
    return [f"<@{message.guild.me.id}>", prefix]

async def get_pre(bot, ctx):
    if ctx.guild is None:
        return commands.when_mentioned_or(f"-")(bot, ctx)
    with sqlite3.connect('database.sqlite3') as db:
      db.row_factory = sqlite3.Row
      cursor = db.cursor()
      cursor.execute(f'SELECT prefix FROM prefixes WHERE guild_id = {ctx.guild.id}')
      res = cursor.fetchone()
    if res:
      prefix = str(res[0])
    if not res:
      prefix = '-'
    try:
        cursor.execute(f'SELECT * FROM noprefix WHERE user_id = {ctx.author.id}')
        res1 = cursor.fetchone()
        if res1 is not None:
            if res1['servers'] is not None:
                no_prefix = literal_eval(res1['servers'])
                if ctx.guild.id in no_prefix:
                    return commands.when_mentioned_or(f"{prefix}", "")(bot, ctx)
            if res1['main'] is not None:
                if res1['main'] == 1:
                    return commands.when_mentioned_or(f"{prefix}", "")(bot, ctx)
    except:
        pass
    db.commit()
    cursor.close()
    db.close()
    return commands.when_mentioned_or(prefix)(bot,ctx)

async def node_connect():
    await bot.wait_until_ready()
    bot.wavelink = await wavelink.NodePool.create_node(bot=bot,host="54.38.198.24", port=88, password="stonemusicgay")



bot.run("teri amma bhen pe aajaunga")