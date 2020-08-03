import threading
import urllib.error
import urllib.request
import concurrent.futures
import datetime
from database import db, Url, Base, session

from config import INTERVAL, CONCURRENCY, TIMEOUT, URLS

Base.metadata.create_all(db)


def request_url(url, timeout):
    date = datetime.datetime.now()

    try:
        # what about redirects?
        code = urllib.request.urlopen(url=url, timeout=timeout).getcode()
    except urllib.error.HTTPError as e:
        code = e.code
    except urllib.error.URLError as e:
        code = e.errno

    if code is None:
        code = 0

    duration = datetime.datetime.now() - date

    return url, date, duration.seconds, code


def get_urls_data(urls, concurrency, timeout):
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        tasks = {executor.submit(request_url, url, timeout): url for url in urls}
        for task in concurrent.futures.as_completed(tasks):
            data = task.result()
            yield data


def check_urls(interval, urls, concurrency, timeout):
    threading.Timer(interval=interval,
                    function=check_urls,
                    args=(interval, urls, concurrency, timeout)
                    ).start()

    for url_data in get_urls_data(urls, concurrency, timeout):
        session.add(Url(*url_data))
    session.commit()


check_urls(INTERVAL, URLS, CONCURRENCY, TIMEOUT)

