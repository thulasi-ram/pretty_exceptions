import inspect
import linecache
import os
import sys
import time
from cgitb import scanvars

from html import HTML


class PrettyException(object):
    color_dict = {
        'blue': '#ffccee',
        'green': '#ffccee',
        'red': '#ffccee',
        'yellow': '#ffccee',
    }

    def __init__(self, exc_info, **kwargs):
        self.exception_info = exc_info
        self.color_scheme = kwargs.get('color_scheme', 'blue')
        self.no_of_tb_steps = 5

    def get_hex_color_code(self, color, shade=1):
        hex_code = self.color_dict[color]

    def format_exception(self):
        etype, evalue, etb = self.exception_info
        python_version = 'Python ' + sys.version.split()[0] + ': ' + sys.executable
        date = time.ctime(time.time())
        html_page = HTML()
        frames =[]
        records = inspect.getinnerframes(etb, self.no_of_tb_steps)
        for frame, file, lnum, func_name, lines, index in records:
            file_name = ''
            if file:
                file_name = os.path.abspath(file)
            args, varargs, varkw, locals = inspect.getargvalues(frame)
            function_args = inspect.formatargvalues(args, varargs, varkw, locals)

            def reader(line_num=lnum):
                try: return linecache.getline(file, line_num)
                finally: line_num += 1

            vars = scanvars(reader, frame, locals)
            if index:
                i = lnum - index
                for line in lines:
                    if i==lnum: continue
                    i += 1
            frames.append({'file_name': file_name, 'function_args': function_args, 'locals': vars})




