Fork of [Python Riichi `mahjong` library](https://github.com/MahjongRepository/mahjong/), extended to include Chinese scoring rules.

# Ruleset Grammar

I'm working on creating a grammar for a file where you can define custom scoring rules. In Chinese Mahjong you get points known as fans or faans (ZH: 番). Generally, in order to win, you need a minimum number of fans.

The file format will probably be YAML, with something like the following:

```yaml
---
SETTINGS:
    minimumfan: 3
    startingchips: 2000
    fanstochips:
        3: 16
        4: 32
        5: 64
        6: 128
pinghu:
    fan: 1
    desc: All runs, no 1s or 9s
    rule:
        exclusion: [ any peng, any 1, any 9]
halfhalf:
    fan: 4
    desc: Half 5 or above, half 5 or below, 5 eyes
    rule:
        inclusion:
            - eyes 5
            - 2 mianzi all <= 5
            - 2 mianzi all >= 5
```