def all_thing_is_obj(object: any) -> int:

    obj = type(object)

    if (obj == list):
        print("List : ", obj)
    elif (obj == tuple):
        print("Tuple : ", obj)
    elif (obj == set):
        print("Set : ", obj)
    elif (obj == dict):
        print("Dict : ", obj)
    elif (obj == str):
        print(object, "is in the kitchen : ", obj)
    else:
        print("Type not found")
    return 42
