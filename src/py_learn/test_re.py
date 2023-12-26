import re
from datetime import datetime

# 定义要匹配的字符串
text = "販売開始予定：2023/04/15 10:00～"

# 定义日期正则表达式
date_regex = r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}"

# 使用正则表达式匹配日期字符串

match = re.search(date_regex, text)

# 如果匹配成功，将匹配到的字符串转换为 datetime 对象
if match:
    date_str = match.group()
    datetime(year=2023, month=1, day=10)

    # date_obj = datetime.strptime(date_str, "%Y/%m/%d %H:%M")
    # print(date_obj)
