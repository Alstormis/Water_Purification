from peewee import *
db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db
class Soluble(BaseModel):
    id_soluble = PrimaryKeyField(unique=True)
    name = CharField(unique=True)
    quantity = FloatField()
    class Meta:
        order_by = 'id_soluble'
        db_table = 'solubles'

class Insoluble(BaseModel):
    id_insoluble = PrimaryKeyField(unique=True)
    name = CharField(unique=True)
    quantity = FloatField()
    class Meta:
        order_by = 'id_insoluble'
        db_table = 'insolubles'
class Characteristic(BaseModel):
    id_characteristic = PrimaryKeyField(unique=True)
    temperature = FloatField()
    KRK = FloatField()
    BPK = FloatField()
    HPK = FloatField()
    alkalinity = FloatField()
    smell = FloatField()
    chroma = FloatField()
    radioactivity = FloatField()
    color = CharField()
    rigidity = FloatField()
    class Meta:
        db_table = 'сharacteristic'
class Device(BaseModel):
    id_device = PrimaryKeyField(unique=True)
    name_device = CharField(unique=True)
    expenditure = FloatField()
    start = FloatField()
    effectiveness = FloatField()
    temperature = FloatField()
    oxygen = FloatField()
    BPK = FloatField()
    XPK = FloatField()
    pH = FloatField()
    radioactivity = FloatField()
    color = CharField()
    coloration = FloatField()
    smell = FloatField()
    rigidity = FloatField()
    level = IntegerField()
    use = IntegerField()
    cost = FloatField()
    class Meta:
        order_by = 'level'
        db_table = 'devices'
class Type_water(BaseModel):
    id_type_water = PrimaryKeyField(unique=True)
    name_type = CharField(unique=True)
    suspended_PDK = FloatField()
    class Meta:
        order_by = 'id'
        db_table = 'waters'