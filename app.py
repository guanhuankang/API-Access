import web
import utils

web.config.debug = False

urls = (
    '/timeapi(.*)', "utils.TimeAPI",
    '/timeapi/(.*)', "utils.TimeAPI",

    '/count(.*)', "utils.Count",
    '/count/(.*)', "utils.Count",
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()