
def foo(a: str, b: str, c: str) -> int:
    if a:
        if b:
            if c:
                return 1
                if a:
                    if b:
                        if c:
                            return 1
                        if a:
                            if b:
                                if c:
                                    return 1
                                    if a:
                                        if b:
                                            if c:
                                                return 1
                                        else:
                                            return 2
                                    else:
                                        return 3
                                else:
                                    return 4
                            else:
                                return 2
                        else:
                            return 3
                    else:
                        return 4
                else:
                    return 4
            else:
                return 2
        else:
            return 3
    else:
        return 4

from enum import Enum, StrEnum

class T(StrEnum):
    a = "a"
    b = "b"
    c = "c"