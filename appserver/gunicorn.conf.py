import multiprocessing

bind = ['0.0.0.0:5000']
workers = multiprocessing.cpu_count() * 2 + 1
threads = 25
loglevel = 'debug'
timeout = 10
# capture_output = True
# accesslog = '/home/pizza/gunicorn-accesslog.log'
# errorlog = '/home/pizza/gunicorn-errorlog.log'