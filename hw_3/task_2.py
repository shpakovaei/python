# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать
# знаки препинания и регистр символов. За основу возьмите любую статью из википедии

import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """ Капибара[1], или водосвинка[2] (лат. Hydrochoerus hydrochaeris), — полуводное травоядное млекопитающее из 
подсемейства водосвинковых (Hydrochoerinae), один из двух (наряду с малой водосвинкой) ныне существующих видов рода водосвинки. 
Капибара — самый крупный среди современных грызунов.
Название животного берёт начало от слова ka’apiûara, что на мёртвом языке тупи (родственном языку индейцев гуарани) буквально
означает «поедатель тонкой травы» (kaá (трава) + píi (тонкий) + ú (есть) + ara (суффикс, аналогичный русскому суффиксу -тель)).
В наиболее близкой к оригиналу форме capivara оно вошло в португальский язык и широко употребимо в Бразилии. 
Уже в форме capibara через испанский слово вошло в английский, русский, японский и ряд других языков. 
В испаноговорящих странах Латинской Америки также в ходу и другие названия, происходящие из языков местных индейцев: carpincho
(Аргентина, Перу и др.), chigüiro (Венесуэла, Колумбия), jochi (Боливия), ñeque (Колумбия) и др.
Научное название (как родовое, так и видовое) Hydrochoerus hydrochaeris переводится как «водяная свинья» 
(др.-греч. ὕδωρ — вода + χοῖρος — свинья), калька с которого послужила основой как для альтернативного русского наименования 
этого животного — водосвинка, — так и названий его на китайском (水豚), венгерском (Vízidisznó), исландском (Flóðsvín) и 
некоторых других языках, а также для вариантов, употребимых в Аргентине (chancho de agua и puerco de agua)."""

print(top_10_words(text))