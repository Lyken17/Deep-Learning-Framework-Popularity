import requests
from bs4 import BeautifulSoup
import json
import time


class iter_through_query():
    def __init__(self, keywords=("CVPR", "2018")):
        searchkey = "+".join(keywords)

        page = 1
        self.prefix = "https://github.com/search?p=%d"
        self.url = "&q=%s&type=Repositories&utf8=✓" % searchkey

        self.maximum_pages = self.get_maximum_pages()

    def get_maximum_pages(self):
        url = self.prefix % 1 + self.url
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")

        a = soup.select('.pagination')[0]
        # print(type(a))
        # print(a)

        d = a.find_all("a")[-2]
        # print(type(d))
        # print(d)

        return int(d.contents[0])

    def filter_all_repos(self):
        results = []
        for i in range(1, self.maximum_pages + 1):
            res = self.filter_repo_urls(i)
            results += res
            time.sleep(3)
        return results

    def filter_repo_urls(self, page=1):
        url = self.prefix % page + self.url

        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")

        results = []
        for repos in soup.select('.v-align-middle'):
            res = self.extract_single_repo(repos)
            if res is None:
                continue
            results.append(res)
            print(res)
        return results

    def extract_single_repo(self, repo_info):
        try:
            s = repo_info.attrs['data-hydro-click']
            # print(type(s))
            # print(s)

            res = json.loads(s)['payload']['result']['url']
            # print(res)
        except KeyError:
            return None
        return res


if __name__ == "__main__":
    import argparse
    
    d = iter_through_query()
    maxd = d.get_maximum_pages()
    print(maxd)
    res = d.filter_all_repos()

