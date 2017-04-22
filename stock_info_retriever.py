import urllib3
import re


http = urllib3.PoolManager()
pattern = re.compile("\"([^\"]*)\"")


def gen_url(file_name):
    code_list = []
    with open(file_name, 'r') as fs:
        for i in fs.readlines():
            code_list.append("http://hq.sinajs.cn/list=%s" % (i.strip('\n')))
    return code_list


def get_stock_info(url):
    response = http.request('POST', url)
    raw_info = response.data.decode('gb2312')
    info = pattern.findall(raw_info)
    result = re.split(r',', info[0])
    return result


url_list = gen_url('stock_code.txt')

example_url = url_list[0]
print(get_stock_info(example_url))
# with open('result.txt', mode='w', encoding='utf-8') as fd:
#     fd.write("%s" % get_stock_info(example_url))
