def str_to_bool(str_bool):
    if str_bool == "True":
        return True
    elif str_bool == "False":
        return False
    raise ValueError(f"{str_bool} to niepoprawna wartość dla typu bool")
