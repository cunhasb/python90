def logger(msg):

    def log_message():
        print('log:', msg)

    return log_message


log_hi = logger('Hi!')
log_hi()
