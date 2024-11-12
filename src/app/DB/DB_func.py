import peewee


from src.app.DB.models import *

# with db:
#     db.create_tables([Soluble, Insoluble, Device, Type_water, Characteristic])
#     Soluble(name = "Фенол", quantity = 0.0).save()
#
#     water = [
#         {'name_type': "Водоемы хозяйственно-питьевого водопользования", 'suspended_PDK': 1.5},
#         {'name_type': "Водоемы культурно-бытового водопользования", 'suspended_PDK': 2.0},
#         {'name_type': "Водоемы рыбохозяйственного водопользования: Высшая и первая категория", 'suspended_PDK': 10.0},
#         {'name_type': "Водоемы рыбохозяйственного водопользования: Вторая категория", 'suspended_PDK': 20.0},
#         {'name_type': "Озера", 'suspended_PDK': 10.0},
#         {'name_type': "Реки", 'suspended_PDK': 12.0},
#         {'name_type': "Морские воды(от 8 метров глубины)", 'suspended_PDK': 10.0},
#         {'name_type': "Подземные воды", 'suspended_PDK': 20.0},
#         {'name_type': "Нейтральные воды", 'suspended_PDK': 0.0},
#         {'name_type': "Болотные воды", 'suspended_PDK': 20.0},
#     ]
#     Type_water.insert_many(water).execute()
#     device = [
#         {'name_device': "Аэрируемая песколовка", 'expenditure': 10000, 'start': 900,
#          'effectiveness': 60, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 1, 'use': True, 'cost' : 273600.0},
#         {'name_device': "Тангенсальная песколовка", 'expenditure': 50000, 'start': 300,
#          'effectiveness': 85, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 1, 'use': True, 'cost' : 296865.0},
#         {'name_device': "Горизонтальная песколовка", 'expenditure': 10000, 'start': 200,
#          'effectiveness': 85, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 1, 'use': True, 'cost' : 308460.0},
#         {'name_device': "Радиальный отстойник", 'expenditure': 20000, 'start': 500,
#          'effectiveness': 60, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 2, 'use': True, 'cost' : 268402.0},
#         {'name_device': "Отстойник с аэрацией", 'expenditure': 9000, 'start': 400,
#          'effectiveness': 70, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 2, 'use': True, 'cost' : 454714.0},
#         {'name_device': "Вертикальный отстойник", 'expenditure': 20000, 'start': 350,
#          'effectiveness': 60, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 2, 'use': True, 'cost' : 797713.0 },
#         {'name_device': "Горизонтальный отстойник", 'expenditure': 15000, 'start': 300,
#          'effectiveness': 90, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 2, 'use': True, 'cost' : 459855.0},
#         {'name_device': "Напорный флотатор", 'expenditure': 10000, 'start': 1000,
#          'effectiveness': 90, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 3, 'use': True, 'cost' : 311182.0},
#         {'name_device': "Гидроциклон", 'expenditure': 35000, 'start': 300,
#          'effectiveness': 70, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 3, 'use': True, 'cost' : 311182.0},
#         {'name_device': "Коагуляция", 'expenditure': 12000, 'start': 100,
#          'effectiveness': 30, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 4, 'use': True, 'cost' : 504100.0},
#         {'name_device': "Барабанные сеточные фильтры", 'expenditure': 48000, 'start': 250,
#          'effectiveness': 44, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 4, 'use': True, 'cost' : 597731.0},
#         {'name_device': "Фильтры патронные", 'expenditure': 300, 'start': 900,
#          'effectiveness': 98, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 5, 'use': True, 'cost' : 379174.0},
#         {'name_device': "Барабанные фильтры со сходящим полотном", 'expenditure': 20000, 'start': 250,
#          'effectiveness': 20, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 5, 'use': True, 'cost' : 469892.0},
#         {'name_device': "Фильтры с зернистым слоем", 'expenditure': 15000, 'start': 100,
#          'effectiveness': 98, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 5, 'use': True, 'cost' : 290156.0},
#         {'name_device': "Тонкослойный отстойник", 'expenditure': 20000, 'start': 12,
#          'effectiveness': 80, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 6, 'use': True, 'cost' : 730644.0},
#         {'name_device': "Жидкостные центробежные сепараторы", 'expenditure': 20000, 'start': 152,
#          'effectiveness': 98, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 7, 'use': True, 'cost' : 265819.0},
#         {'name_device': "Листовые фильтры", 'expenditure': 6000, 'start': 3,
#          'effectiveness': 90, 'temperature': 1.5, 'oxygen': 1.5, 'BPK': 1.5, 'XPK': 1.5,
#          'pH': 1.5, 'radioactivity': 1.5, 'color': "--", 'coloration': 1.5, 'smell': 1.5, 'rigidity': 1.5,
#          'level': 8, 'use': True, 'cost' : 390101.0},
#     ]
#     Device.insert_many(device).execute()
#
#
#     char = Characteristic(temperature = 0.0, KRK = 0.0, BPK = 0.0, HPK = 0.0, alkalinity = 0.0, smell = 0.0,
#                           chroma = 0.0, radioactivity = 0.0, color = "Цвет", rigidity = 0.0).save()
#     Insoluble(name="Взвешанные", quantity=0.0).save()



#########################
### Запросы
#########################


# Работа с веществами

# Получение всех веществ
def get_insoluble_value():
    insoluble = Insoluble.select()
    return insoluble
def get_soluble_value():
    soluble = Soluble.select()
    return soluble

# Изменение в БД значенией
def chance_insoluble(name_sub, qua, measure):
    add_in = Insoluble.get(Insoluble.name == name_sub)
    #if measure
    add_in.quantity = qua
    add_in.save()

def chance_soluble(name_sub, qua, measure):
    add = Soluble.get(Soluble.name == name_sub)
    add.quantity = qua
    add.save()

# Добавление в БД
def add_soluble(name_sub):
    try:
        Soluble(name = str(name_sub), quantity = 0.0).save()
        return "ok"
    except peewee.IntegrityError:
        return None
def add_insoluble(name_sub):
    try:
        Insoluble(name = str(name_sub), quantity = 0.0).save()
        return "ok"
    except peewee.IntegrityError:
        return None
# Удаление из БД
def del_soluble(name_sub):
    try:
        obj = Soluble.get(Soluble.name == name_sub)
        obj.delete_instance()
        return "ok"
    except peewee.DoesNotExist:
        return None
def del_insoluble(name_sub):
    try:
        obj = Insoluble.get(Insoluble.name == name_sub)
        obj.delete_instance()
        return "ok"
    except peewee.DoesNotExist:
        return None

# Тип воды
# Получение всех типов воды
def type_water_DB():
    vs = Type_water.select()
    return vs
# Получение конечной концентрции от типа воды
def end_concent_water(name):
    try:
        obj = Type_water.get(Type_water.name_type == name)
        return obj.suspended_PDK
    except peewee.DoesNotExist:
        return None

# Устройства
# Получение всех устройств
def all_device():
    vs = Device.select()
    return vs
# Изменение статуса устроства
def chance_device_status(name, status):
    st = Device.get(Device.name_device == name)
    st.use = status
    st.save()


# Свойства
# Изменение в бд
def chance_temperature(temperature):
    add = Characteristic.get()
    add.temperature = temperature
    add.save()
def chance_KRK(KRK):
    add = Characteristic.get()
    add.KRK = KRK
    add.save()
def chance_BPK(BPK):
    add = Characteristic.get()
    add.BPK = BPK
    add.save()
def chance_HPK(HPK):
    add = Characteristic.get()
    add.HPK = HPK
    add.save()
def chance_alkalinity(alkalinity):
    add = Characteristic.get()
    add.alkalinity = alkalinity
    add.save()
def chance_smell(smell):
    add = Characteristic.get()
    add.smell = smell
    add.save()
def chance_chroma(chroma):
    add = Characteristic.get()
    add.chroma = chroma
    add.save()
def chance_radioactivity(radioactivity):
    add = Characteristic.get()
    add.radioactivity = radioactivity
    add.save()
def chance_rigidity(rigidity):
    add = Characteristic.get()
    add.rigidity = rigidity
    add.save()

def device_open_char(name):
    device = Device.get(Device.name_device == name)
    return (device.expenditure, device.start, device.effectiveness, device.temperature, device.oxygen, device.BPK,
            device.XPK, device.pH, device.radioactivity, device.color, device.coloration, device.smell,
            device.rigidity, device.level, device.cost)
def device_change_char(name, expenditure, start, effectiveness, temperature, oxygen, BPK, XPK, pH, radioactivity, color,
                       coloration, smell, rigidity, level, cost):
    device = Device.get(Device.name_device == name)
    device.expenditure = expenditure
    device.start = start
    device.effectiveness = effectiveness
    device.temperature = temperature
    device.oxygen = oxygen
    device.BPK = BPK
    device.XPK = XPK
    device.pH = pH
    device.radioactivity = radioactivity
    device.color = color
    device.coloration = coloration
    device.smell = smell
    device.rigidity = rigidity
    device.level = level
    device.cost = cost
    device.save()

#Очистить все введенные данные
def clean_DB():
    query_soluble = Soluble.update(quantity=0).where(Soluble.quantity > 0)
    query_soluble.execute()
    query_insoluble = Insoluble.update(quantity=0).where(Insoluble.quantity > 0)
    query_insoluble.execute()
    query_temperature = Characteristic.update(temperature=0).where(Characteristic.temperature > 0)
    query_temperature.execute()
    query_KRK = Characteristic.update(KRK=0).where(Characteristic.KRK > 0)
    query_KRK.execute()
    query_BPK = Characteristic.update(BPK=0).where(Characteristic.BPK > 0)
    query_BPK.execute()
    query_HPK = Characteristic.update(HPK=0).where(Characteristic.HPK > 0)
    query_HPK.execute()
    query_alkalinity = Characteristic.update(alkalinity=0).where(Characteristic.alkalinity > 0)
    query_alkalinity.execute()
    query_smell = Characteristic.update(smell=0).where(Characteristic.smell > 0)
    query_smell.execute()
    query_chroma = Characteristic.update(chroma=0).where(Characteristic.chroma > 0)
    query_chroma.execute()
    query_radioactivity = Characteristic.update(radioactivity=0).where(Characteristic.radioactivity > 0)
    query_radioactivity.execute()
    query_rigidity = Characteristic.update(rigidity=0).where(Characteristic.rigidity > 0)
    query_rigidity.execute()
    query_color = Characteristic.update(color="Color").where(Characteristic.color != "Color")
    query_color.execute()
    query_device = Device.update(use=1).where(Device.use == 0)
    query_device.execute()

#Получить все значение
def get_all():
    characteristic_list = {}
    soluble_list = {}
    insoluble_list = {}
    device_list = []
    array_values_device = []
    index = 1
    help_list_device = []
    soluble = Soluble.select().where(Soluble.quantity > 0).order_by(Soluble.quantity.asc())
    for soluble_value in soluble:
        soluble_list.update({soluble_value.name: soluble_value.quantity})
    insoluble = Insoluble.select().where(Insoluble.quantity > 0).order_by(Insoluble.quantity.asc())
    for insoluble_value in insoluble:
        insoluble_list.update({insoluble_value.name: insoluble_value.quantity})
    device = Device.select().where(Device.use == 1)
    for device_value in device:
        if device_value.level == index:
            help_list_device.append(device_value.name_device)
            array_values_device.append({
                'name_device': device_value.name_device, 'expenditure': device_value.expenditure,
                'start': device_value.start, 'effectiveness': device_value.effectiveness,
                'temperature': device_value.temperature, 'oxygen': device_value.oxygen, 'BPK': device_value.BPK,
                'XPK': device_value.XPK, 'pH': device_value.pH, 'radioactivity': device_value.radioactivity,
                'color': device_value.color, 'coloration': device_value.coloration, 'smell': device_value.smell,
                'rigidity': device_value.rigidity, 'cost': device_value.cost
            })
        else:
            device_list.append(help_list_device.copy())
            array_values_device.append({
                'name_device': device_value.name_device, 'expenditure': device_value.expenditure,
                'start': device_value.start, 'effectiveness': device_value.effectiveness,
                'temperature': device_value.temperature, 'oxygen': device_value.oxygen, 'BPK': device_value.BPK,
                'XPK': device_value.XPK, 'pH': device_value.pH, 'radioactivity': device_value.radioactivity,
                'color': device_value.color, 'coloration': device_value.coloration, 'smell': device_value.smell,
                'rigidity': device_value.rigidity, 'cost': device_value.cost
            })
            index += 1
            help_list_device.clear()
            help_list_device.append(device_value.name_device)
    device_list.append(help_list_device)
    return device_list, array_values_device, insoluble_list
