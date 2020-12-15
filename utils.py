# -*- coding: UTF-8 -*-
import sys
import time
import web

module_vars = {
    "ok_count": 0,
    "fail_count": 0
}

class TimeAPI:
    def __init__(self):
        pass
    
    def GET(self, name):
        try:
            return self.timeapi()
        except:
            print(sys.exc_info())
            return self.error()

    def POST(self):
        try:
            return self.timeapi()
        except:
            print(sys.exc_info())
            return self.error()
    
    def timeapi(self):
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        global module_vars

        timestamp = time.time()
        # datetime_2 = ("年","月","日","时","分","秒")
        week_name2 = ("星期日","星期一","星期二","星期三","星期四","星期五","星期六")
        week_name3 = ("周日","周一","周二","周三","周四","周五","周六")

        ret = {
            "success":1,
            "result":{
                "timestamp":str(int(timestamp)),
                "datetime_1": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp)),
                "datetime_2": time.strftime(
                    "%Y{0}%m{1}%d{2} %H{3}%M{4}%S{5}", 
                    time.localtime(timestamp)
                    ).format( "年","月","日","时","分","秒" ),
                "week_1": time.strftime("%w", time.localtime(timestamp)),
                "week_2": week_name2[ int( time.strftime("%w", time.localtime(timestamp)) )],
                "week_3": week_name3[ int( time.strftime("%w", time.localtime(timestamp)) )],
                "week_4": time.strftime("%A", time.localtime(timestamp)),
            }
        }

        module_vars["ok_count"] += 1
        return ret
    
    def error(self):
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        global module_vars
        err = {
            "success":0,
            "info":str(sys.exc_info()[0])
        }

        module_vars["fail_count"] += 1
        return err

class Count:
    def __init__(self):
        pass
    
    def GET(self, name):
        try:
            return self.count()
        except:
            print(sys.exc_info())
            return self.error()

    def POST(self):
        try:
            return self.count()
        except:
            print(sys.exc_info())
            return self.error()

    def count(self):
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        global module_vars
        ok_count = module_vars["ok_count"]
        fail_count = module_vars["fail_count"]
        tot_count = ok_count + fail_count

        ret = {
            "success":1,
            "result":{
                "count": tot_count,
                "ok_count":ok_count,
                "fail_count": fail_count
            }
        }
        return ret
    
    def error(self):
        web.header('Content-Type','application/json; charset=utf-8', unique=True)
        err = {
            "success":0,
            "info":str(sys.exc_info()[0])
        }
        return err
