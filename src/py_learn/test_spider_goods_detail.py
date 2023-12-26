import json

category = {
    "C1": "スイーツ・果物",
    "C2": "おかず",
    "C3": "お米・パン・麺",
    "C4": "ドリンク・お酒",
    "C5": "その他食品",
    "C6": "雑貨",
    "C7": "ギフトカタログ",
    "C8": "定期便・頒布会",
    "C9": "マルシェ オリジナル",
    "C101": "スイーツ",
    "C102": "和菓子",
    "C103": "果物",
    "C104": "その他",
    "C201": "肉・肉加工品",
    "C202": "魚介・海産物加工品",
    "C203": "鍋",
    "C204": "おつまみ",
    "C205": "スープ・味噌汁",
    "C206": "野菜・大豆加工品",
    "C207": "漬物・梅干し・珍味・乾物",
    "C208": "チーズ・乳製品",
    "C209": "カレー・洋食",
    "C210": "中華",
    "C211": "その他",
    "C212": "おせち",
    "C213": "野菜・野菜加工品",
    "C301": "お米・雑穀",
    "C302": "パン",
    "C303": "麺類",
    "C304": "その他",
    "C401": "水・ドリンク",
    "C402": "お酒",
    "C501": "調味料・ジャム",
    "C502": "ヘルシーフード",
    "C601": "キッチン用品",
    "C602": "バス＆ボディ",
    "C603": "生花",
    "C801": "定期便",
    "C802": "頒布会",
    "C101AA": "ケーキ・ロールケーキ",
    "C101BB": "バームクーヘン",
    "C101CC": "チョコレート",
    "C101DD": "マカロン",
    "C101EE": "焼き菓子・クッキー・サブレ",
    "C101FF": "マドレーヌ・フィナンシェ・ブッセ",
    "C101GG": "パイ・シュークリーム・スフレ",
    "C101KK": "タルト",
    "C101LL": "栗菓子",
    "C101HH": "プリン・ゼリー・ムース・テリーヌ",
    "C101II": "アイス・ジェラート",
    "C101JJ": "その他",
    "C102AA": "饅頭・どら焼き",
    "C102BB": "カステラ",
    "C102CC": "羊羹・最中・金つば",
    "C102DD": "葛餅・わらび餅",
    "C102EE": "せんべい",
    "C102FF": "おかき・あられ・かりんとう・豆菓子",
    "C102GG": "抹茶",
    "C102HH": "その他",
    "C103AA": "ドライフルーツ",
    "C201AA": "精肉",
    "C201BB": "ハンバーグ",
    "C201CC": "ステーキ・ローストビーフ",
    "C201DD": "ソーセージ・ハム・ベーコン",
    "C201EE": "パテ・テリーヌ",
    "C201GG": "コロッケ",
    "C201HH": "丼もの",
    "C201FF": "その他",
    "C202AA": "干物",
    "C202BB": "漬魚",
    "C202KK": "煮魚",
    "C202CC": "明太子",
    "C202DD": "いくら・うに",
    "C202EE": "カニ・エビ",
    "C202FF": "鰻",
    "C202JJ": "お寿司",
    "C202LL": "鮮魚・刺身",
    "C202GG": "牡蠣・貝類",
    "C202HH": "海産物加工品",
    "C202II": "その他",
    "C203AA": "肉系",
    "C203BB": "魚系",
    "C203CC": "野菜系",
    "C203DD": "その他",
    "C204AA": "肉系",
    "C204BB": "魚系",
    "C204CC": "野菜系",
    "C204DD": "その他",
    "C205AA": "スープ",
    "C205BB": "味噌汁",
    "C205CC": "その他",
    "C206AA": "野菜・野菜加工品",
    "C206BB": "大豆加工品",
    "C209AA": "カレー",
    "C209BB": "洋食",
    "C209CC": "スパイス料理",
    "C210AA": "点心",
    "C210BB": "餃子",
    "C210CC": "その他",
    "C301AA": "白米",
    "C301BB": "無洗米",
    "C301CC": "玄米・雑穀米",
    "C301DD": "お米加工品",
    "C302AA": "ピザ",
    "C303AA": "うどん",
    "C303BB": "そば",
    "C303CC": "そうめん",
    "C303DD": "ラーメン",
    "C303EE": "パスタ・パスタソース",
    "C303FF": "その他",
    "C401AA": "ミネラルウォーター",
    "C401BB": "お茶",
    "C401CC": "コーヒー",
    "C401DD": "ソフトドリンク",
    "C401EE": "野菜・フルーツジュース",
    "C401FF": "ヨーグルト・乳飲料",
    "C401GG": "甘酒",
    "C401HH": "その他",
    "C402AA": "日本酒",
    "C402BB": "ワイン",
    "C402CC": "焼酎",
    "C402DD": "ビール・発泡酒",
    "C402EE": "リキュール",
    "C402GG": "ブランデー",
    "C402FF": "その他",
    "C501AA": "塩",
    "C501BB": "味噌",
    "C501CC": "醤油",
    "C501DD": "酢・ポン酢・ビネガー",
    "C501EE": "砂糖・ジャム",
    "C501FF": "ハーブ・スパイス",
    "C501GG": "だし",
    "C501HH": "ソース",
    "C501II": "オイル",
    "C501JJ": "麹・みりん",
    "C501LL": "ごま・ふりかけ",
    "C501NN": "はちみつ",
    "C501MM": "その他",
    "C502AA": "スーパーフード",
    "C502BB": "健康飲料",
    "C502CC": "サプリメント",
    "C502DD": "その他",
    "C601AA": "洋食器",
    "C601BB": "和食器",
    "C601CC": "グラス・マグ・ポット・酒器",
    "C601DD": "箸・カトラリー",
    "C601EE": "調理器具",
    "C601FF": "その他",
    "C402AA01": "純米",
    "C402AA02": "純米吟醸",
    "C402AA03": "純米大吟醸",
    "C402AA04": "本醸造",
    "C402AA05": "吟醸",
    "C402AA06": "大吟醸",
    "C402AA07": "スパークリング",
    "C402BB01": "赤ワイン",
    "C402BB02": "白ワイン",
    "C402BB03": "ロゼワイン",
    "C402BB04": "スパークリング",
    "C402CC01": "芋焼酎",
    "C402CC02": "麦焼酎",
    "C402CC03": "米焼酎",
    "C402CC04": "黒糖焼酎",
    "C402CC05": "泡盛",
    "C402CC06": "その他",
    "C402EE01": "梅酒",
    "C402EE02": "果実酒",
    "C402EE03": "その他",
    "C601AA01": "プレート小皿(14cm未満)",
    "C601AA02": "プレート中皿(14cm～23cm未満)",
    "C601AA03": "プレート大皿(23cm以上)",
    "C601AA04": "ボウル",
    "C601AA05": "その他",
    "C601BB01": "飯椀・汁椀・丼・鉢",
    "C601BB02": "丸皿",
    "C601BB03": "角皿",
    "C601BB04": "その他",
    "C601CC01": "タンブラー・ジョッキ",
    "C601CC02": "ロック・日本酒・焼酎グラス",
    "C601CC03": "ワイン・シャンパングラス",
    "C601CC04": "マグ・カップ・ソーサー",
    "C601CC05": "ポット・湯呑",
    "C601CC06": "その他",
    "C601DD01": "箸・箸置き",
    "C601DD02": "シルバー",
    "C601DD03": "その他",
    "C601EE01": "鍋・フライパン",
    "C601EE02": "包丁・ナイフ・まな板・カッティングボード",
    "C601EE03": "保存容器・ボトル・弁当箱",
    "C601EE04": "卓上小物",
    "C601EE05": "お玉・トング・フライ返し",
    "C601EE07": "コーヒー用品",
    "C601EE08": "ティー用品",
    "C601EE06": "その他",
}


def find_subcategories(category_code, data):
    subcategories = []

    for key, value in data.items():
        if key.startswith(category_code) and len(key) == len(category_code) + 2:
            subcategories.append(
                {
                    "name": value,
                    "code": key,
                    "subcategories": find_subcategories(key, data),
                }
            )

    return subcategories


def main():
    category_list = list()

    for key, value in category.items():
        if len(key) == 2:  # 一级分类的code长度为2
            result = {
                "name": value,
                "code": key,
                "subcategories": find_subcategories(key, category),
            }
            category_list.append(result)

    print(json.dumps(category_list, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()