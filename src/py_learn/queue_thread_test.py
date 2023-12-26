from concurrent.futures import ThreadPoolExecutor


def task(num):
    return num * 2


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(task, range(10))
        executor.shutdown()
        for result in results:
            print(result)
