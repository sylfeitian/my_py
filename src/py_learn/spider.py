import requests
from parsel import Selector


def get_goods_list():
    # 定义要爬取的网页链接
    url = "https://marche.onward.co.jp/shop/goods/search.aspx?isstock=0&isgift=0&ps=60&search=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B&s_div_not=1"

    # 发送 HTTP GET 请求获取网页内容
    response = requests.get(url)

    # 使用 Selector 解析 HTML 内容
    selector = Selector(text=response.text)

    product_ul = selector.xpath("//ul[@class='block-thumbnail-t']")

    if product_ul:
        url_list = product_ul.xpath("./li/a/@href").getall()
        for idx, url in enumerate(url_list):
            # 打印结果
            goods_url = "https://marche.onward.co.jp/" + url
            print(f"fetch_shop_goods_list: goods_url={goods_url}, idx={idx}")


def get_goods_detail():
    # 定义要爬取的网页链接
    url = "https://marche.onward.co.jp/shop/g/gOWM0047030/"

    # 发送 HTTP GET 请求获取网页内容
    response = requests.get(url)

    # 使用 Selector 解析 HTML 内容
    selector = Selector(text=response.text)

    tablses = selector.xpath(".//table[@class='block-goods-detail-spec-tables--table']")
    table = tablses[0]

    ths = table.xpath(".//th").getall()
    tds = table.xpath(".//td").getall()

    for th, td in zip(ths, tds):
        if th == "賞味期限または消費期限":
            print(td)


get_goods_detail()
