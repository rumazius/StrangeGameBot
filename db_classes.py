import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, select, insert
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    UserID = Column(Integer, primary_key=True)
    Nickname = Column(String,)
    Level = Column(Integer,)
    HP = Column(Integer,)
    CurHP = Column(Integer,)
    Money = Column(Integer,)
    Attack = Column(Integer,)
    MagicAttack = Column(Integer,)
    XP = Column(Integer,)
    Armour = Column(Integer,)
    MagicArmour = Column(Integer,)
    LocationID = Column(Integer,)
    State = Column(String,)


class Mob(Base):
    __tablename__ = "mobs"

    MobID = Column(Integer, primary_key=True)
    HP = Column(Integer)
    XP = Column(Integer)
    ReqLevel = Column(Integer)
    AttackType = Column(String)
    Attack = Column(Integer)
    Armour = Column(Integer)
    MagicArmour = Column(Integer)


class Location(Base):
    __tablename__ = 'locations'

    LocationID = Column(Integer, primary_key=True)
    XCoord = Column(Integer)
    YCoord = Column(Integer)
    LocationType = Column(String)


class Item(Base):
    __tablename__ = 'items'

    ItemID = Column(Integer, primary_key=True)
    Cost = Column(Integer)
    CostToSale = Column(Integer)
    ItemType = Column(String)
    HP = Column(Integer)
    Mana = Column(Integer)
    Attack = Column(Integer)
    MagicAttack = Column(Integer)
    Armour = Column(Integer)
    MagicArmour = Column(Integer)
    ReqLevel = Column(Integer)
