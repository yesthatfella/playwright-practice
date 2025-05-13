
def dict_to_dataclass(data: dict, cls):
    """
    Recursively converts a dictionary to a dataclass instance
    """
    field_types = {field.name: field.type for field in cls.__dataclass_fields__.values()}
    kwargs = {}
    for key, typ in field_types.items():
        if key in data:
            value = data[key]
            # Recurse dataclass fields type
            origin_type = getattr(typ, '__origin__', None)
            if hasattr(typ, '__dataclass_fields__'):
                kwargs[key] = dict_to_dataclass(value, typ)
            elif origin_type is list and not any(isinstance(item, str) for item in value):
                # Handle list of dataclasses if needed
                kwargs[key] = [dict_to_dataclass(item, typ.__args__[0]) for item in value]
            else:
                kwargs[key] = value
        else:
            kwargs[key] = None

    return cls(**kwargs)