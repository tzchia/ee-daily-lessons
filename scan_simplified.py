import sys, re

# Curated simplified-only chars (traditional uses a different glyph).
chars = ('个们这个为从产关线机设过还进级织组给绝护报误灵间业别头样张带墙处备够宽贵资员图会举义乐乱传储关'
 '养阀阅难静页顶顺须预频题风飞马鱼鸟鸡鸣麦齐齿电问队阳阴随阶驻驾验证驶跃践赵购财负责贤败货质贩贪贫贬贮贯贰贱贝贞贡'
 '话说请谢谱语误该详询咙叹叶参双压厢厂厅历厉卫单卖华协医击势动励劳则刚决况净农军写册偿优价仪仓仅亲买长开无显晓暂术让认'
 '续类体专转轮辑号尽离夹将响忆虚总态弹复声张区环际时当后'
 '构讯记论议让训准敏'  # 敏/训 remove below
 '强归录寻虽汉沟洁济浓温满触办汇举'
 '应档达许评较载违标纪统')
chars = chars.replace('敏','').replace('训','').replace('议','')
# shared glyphs that must NOT be flagged
chars = ''.join(sorted(set(chars) - set('敏训议')))

path = sys.argv[1]
text = open(path, encoding='utf-8').read()
total = 0
for i, line in enumerate(text.splitlines(), 1):
    for c in sorted(set(ch for ch in line if ch in chars)):
        for m in re.finditer(re.escape(c), line):
            a = max(0, m.start()-10); b = min(len(line), m.end()+10)
            print(f'{i:4d} [{c}] ...{line[a:b]}...')
            total += 1
print('=== total hits:', total)
