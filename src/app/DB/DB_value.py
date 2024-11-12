from src.app.DB import *

def value():
    list_of_soluble = list()
    list_of_insoluble = list()
    list_of_water = list()
    list_of_device = list()
    var = get_insoluble_value()
    for l in var:
        list_of_insoluble.append(l.name)
        print(l.name)
    sl = get_soluble_value()
    for r in sl:
        print(r.name)
        list_of_soluble.append(r.name)
    tw = type_water_DB()
    for t in tw:
        list_of_water.append(t.name_type)
    dw = all_device()
    for d in dw:
        list_of_device.append(d.name_device)
    return list_of_soluble, list_of_insoluble, list_of_water, list_of_device
