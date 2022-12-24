from functions import *

engine = create_engine("sqlite:///:memory:", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

BOT_TOKEN = '5621497652:AAF-F3Xbkj0Sj7f9EN6VpzP-4nlPQPdsVag'
bot = AsyncTeleBot(BOT_TOKEN)


async def main():
    user = classes.User(**def_classes.default_user)
    loc0 = classes.Location(**def_classes.default_loc0)
    loc1 = classes.Location(**def_classes.default_loc1)
    classes.Base.metadata.create_all(engine)
    session.add(user)
    session.add(loc0)
    session.add(loc1)

    session.commit()

    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == '__main__':
    asyncio.run(main())
