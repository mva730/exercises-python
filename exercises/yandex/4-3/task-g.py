# https://new.contest.yandex.ru/41244/problem?id=149944/2022_11_06/0hIPECwYRI

def same_type(f):
    def decorated(*args):
        current_type = type(args[0])
        for arg in args[1:]:
            if type(arg) is not current_type:
                print("Обнаружены различные типы данных")
                return
            current_type = type(arg)
        return f(*args)

    return decorated
