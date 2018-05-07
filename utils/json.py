# coding=utf-8

import json
from datetime import date, datetime
from decimal import Decimal


def __default(obj):
    """
    支持 datetime Decimal 的 json encode
    TypeError: datetime.datetime(2015, 10, 21, 8, 42, 54) is not JSON serializable
    :param obj:
    :return:
    """
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, Decimal):
        return str(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)

if __name__ == '__main__':
    data = {
        'a': datetime.now(),
        'b': Decimal('12.3'),
    }
    print json.dumps(data, indent=4, ensure_ascii=False, default=__default)
