from Boomslang import Parser , Grabber
form Queue import Queue

num_threads = 4
max_size = 1000
url_queue = Queue()
content_queue = Queue(maxsize=max_size)

parsers = [Parser.Thread(content_url, url_queue) for i in xrange(num_threads)]
grabbers = [Grabber.Thread(url_queue,content_queue) for i in xrange(num_threads)]

for thread in parsers+grabbers:
    thread.daemon = True
    thread.start()

url_queue.put('http://codeguage.com')
