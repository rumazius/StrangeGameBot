import asyncio
import aioschedule
from telebot.async_telebot import AsyncTeleBot

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db_classes as classes
import default_classes as def_classes
import random

engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

BOT_TOKEN = '5621497652:AAF-F3Xbkj0Sj7f9EN6VpzP-4nlPQPdsVag'
bot = AsyncTeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
async def start_game(message):
    ar = message.text.split()
    if len(ar) > 1:
        await bot.reply_to(message, "You've successfully started game!")
    else:
        await bot.reply_to(message, 'cringe man')


@bot.message_handler(commands=['finish'])
async def finish(message):
    await bot.reply_to(message, 'Ты большая умничка, можешь пойти поспать наконец,,,')


@bot.message_handler(commands=['restore_hp'])
async def restore_hp(message):
    usr = session.query(classes.User).first()
    usr.HP += 5
    session.add(usr)
    session.commit()


@bot.message_handler(commands=['restore_arm'])
async def heal(message):
    usr = session.query(classes.User).first()
    usr.MagicArmour += 5
    usr.Armour += 5
    session.add(usr)
    session.commit()


@bot.message_handler(commands=['move'])
async def move(message):
    usr = session.query(classes.User).first()
    if usr.State == "Fight":
        await bot.reply_to(message, 'Not now, you must beat him!')
    elif usr.LocationID == 0:
        usr.LocationID = 1
        usr.HP = 100
        usr.Armour = 100
        usr.MagicArmour = 100
        session.add(usr)
        session.commit()
        await bot.reply_to(message, 'Hanging out with your friends in the town!')
    else:
        usr.LocationID = 0
        if random.randint(0, 2) == 0:
            hmob = classes.Mob(**def_classes.heavy_mob)
            session.add(hmob)
            usr.State = "Fight"
        else:
            mmob = classes.Mob(**def_classes.magic_mob)
            session.add(mmob)
            usr.State = "Fight"

        session.add(usr)
        session.commit()
        await bot.reply_to(message, 'Fighting starts!')


@bot.message_handler(commands=['beat'])
async def beat(message):
    usr = session.query(classes.User).first()
    if usr.State != "Fight":
        await bot.reply_to(message, 'You have nobody bad to beat!')
    else:
        mob = session.query(classes.Mob).first()
        mob.HP -= usr.Attack
        if mob.HP <= 0:
            usr.XP += mob.XP
            usr.Money += 100
            usr.State = "chill"
            session.delete(mob)
            session.add(usr)
            session.commit()
        else:
            usr.HP -= mob.Attack
            session.add(usr)
            session.commit()


@bot.message_handler(commands=['stat'])
async def stat(message):
    usr = session.query(classes.User).first()
    await bot.reply_to(message,
                       "Name: {}, HP: {}, Armour: {}, Money: {}, State: {}".format(
                           usr.Nickname,
                           usr.HP,
                           usr.Armour,
                           usr.Money,
                           usr.State,
                           "Town" if usr.State != "Fight" else "HSE"
                       ))


@bot.message_handler(commands=['change_name'])
async def change_name(message):
    new_name = message.text.split()[1]
    usr = session.query(classes.User).first()
    usr.Nickname = new_name
    session.add(usr)
    session.commit()
    await bot.reply_to(message, "Your name was successfully changed!")


async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
