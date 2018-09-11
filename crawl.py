# coding:utf-8

import json
import requests


SPLASH_SCRIPT = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
  }
end
"""

ENDPOINT = 'http://localhost:8050' + '/execute'


def crawl(url):
    resp = requests.get(ENDPOINT, params={'url': url, 'lua_source': SPLASH_SCRIPT})
    html = json.loads(resp.text).get('html', '').encode('utf-8').decode('utf-8')
    print(html)


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    crawl(url)
