from mahjong.constants import SOUTH
from mahjong.hand_calculating.yaku import Yaku
from mahjong.utils import is_pon_or_kan


class YakuhaiSouth(Yaku):
    """
    Peng of south winds
    """

    def __init__(self, yaku_id=None):
        super(YakuhaiSouth, self).__init__(yaku_id)

    def set_attributes(self):
        self.tenhou_id = 10

        self.name = "Yakuhai (south)"

        self.han_open = 1
        self.han_closed = 1

        self.is_yakuman = False

    def is_condition_met(self, hand, player_wind, round_wind, *args):
        if len([x for x in hand if is_pon_or_kan(x) and x[0] == player_wind]) == 1 and player_wind == SOUTH:
            return True

        if len([x for x in hand if is_pon_or_kan(x) and x[0] == round_wind]) == 1 and round_wind == SOUTH:
            return True

        return False
