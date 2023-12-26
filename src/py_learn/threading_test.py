from queue import Queue
from threading import Thread, get_ident


def upload(input):
    print(f"upload: {get_ident()}--{input}")
    return input


def download(input):
    if input[0] == 2:
        raise
    print(f"download: {get_ident()}--{input}---{input[0]}: {input[1]}")
    return input


def resize(item):
    print(f"resize: {get_ident()}--{item}")
    return item


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return  # Cause the thread to exit
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


class QueueProcessor:
    def __init__(self):
        self.threads = []

    def start_threads(self, count, *args):
        self.threads = [StoppableWorker(*args) for _ in range(count)]
        for thread in self.threads:
            thread.start()

    def stop_threads(self, closable_queue):
        i = 1
        for thread in self.threads:
            if not thread.is_alive():
                continue

            i += 1
            closable_queue.close()
            print(f"{i}--===========")

        closable_queue.join()

        for thread in self.threads:
            if not thread.is_alive():
                continue

            thread.join()


if __name__ == "__main__":
    download_queue = ClosableQueue()
    resize_queue = ClosableQueue()
    upload_queue = ClosableQueue()
    done_queue = ClosableQueue()

    down_queue_processor = QueueProcessor()
    resize_queue_processor = QueueProcessor()
    upload_queue_processor = QueueProcessor()

    down_queue_processor.start_threads(3, download, download_queue, resize_queue)
    resize_queue_processor.start_threads(4, resize, resize_queue, upload_queue)
    upload_queue_processor.start_threads(5, upload, upload_queue, done_queue)

    for i in range(15):
        print(f"{i}......")
        download_queue.put((i, object()))

    down_queue_processor.stop_threads(download_queue)
    resize_queue_processor.stop_threads(resize_queue)
    upload_queue_processor.stop_threads(upload_queue)

    print(done_queue.qsize(), "items finished")
