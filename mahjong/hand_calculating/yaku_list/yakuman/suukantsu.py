from mahjong.hand_calculating.yaku import Yaku
from mahjong.meld import Meld


class Suukantsu(Yaku):
    """
    The hand with four gang sets
    """

    def __init__(self, yaku_id=None):
        super(Suukantsu, self).__init__(yaku_id)

    def set_attributes(self):
        self.tenhou_id = 51

        self.name = "Suu Kantsu"

        self.han_open = 13
        self.han_closed = 13

        self.is_yakuman = True

    def is_condition_met(self, hand, melds, *args):
        kan_sets = [x for x in melds if x.type == Meld.GANG or x.type == Meld.SHOUMINKAN]
        return len(kan_sets) == 4
