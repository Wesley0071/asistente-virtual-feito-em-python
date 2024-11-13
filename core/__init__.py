import datetime
# 2015 5 6 8 53 40


class SystemInfo:
    def __init__(self):
        pass
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'São{} horas e {} minutos'.format(now.hour, now.minute)
        return answer