import random, time
def app(environ, start_response):
        wait_time = random.randrange(1,10)
        #wait_time = 0
        time.sleep(wait_time)
        #for i in range(100000000):
        #    continue
        payload = ("Hello, World! after waiting "+str(wait_time)+"\n").encode('ascii')
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(payload)))
        ])
        return iter([payload])
