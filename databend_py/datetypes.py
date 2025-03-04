import ast
from datetime import datetime

INTType = "int"
FLOATTYPE = "float"
DOUBLETYPE = "double"
BOOLEANTYPE = "bool"
ARRAYTYPE = "array"
MAPTYPE = "map"
JSONTYPE = "json"
NULLTYPE = "null"
DATETYPE = "date"
TIMESTAMPTYPE = "timestamp"


class DatabendDataType:
    def __init__(self):
        pass

    @staticmethod
    def type_convert_fn(type_str: str, native_datetime: bool):
        if INTType in type_str.lower():
            return int
        elif FLOATTYPE in type_str.lower():
            return float
        elif DOUBLETYPE in type_str.lower():
            return float
        elif BOOLEANTYPE in type_str.lower():
            return bool
        elif MAPTYPE in type_str.lower():
            return ast.literal_eval
        elif ARRAYTYPE in type_str.lower():
            return ast.literal_eval
        elif JSONTYPE in type_str.lower():
            return ast.literal_eval
        elif DATETYPE in type_str.lower() and native_datetime:
            return lambda x: datetime.strptime(x, "%Y-%m-%d")
        elif TIMESTAMPTYPE in type_str.lower() and native_datetime:
            return lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f")
        else:
            return str


if __name__ == '__main__':
    d = DatabendDataType()
    print(d.type_convert_fn("Uint64")('0'))
