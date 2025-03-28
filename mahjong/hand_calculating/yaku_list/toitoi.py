from mahjong.hand_calculating.yaku import Yaku
from mahjong.utils import is_pon_or_kan


class Toitoi(Yaku):
    """
    The hand consists of all peng sets (and of course a pair), no sequences.
    """

    def __init__(self, yaku_id=None):
        super(Toitoi, self).__init__(yaku_id)

    def set_attributes(self):
        self.tenhou_id = 28
        self.name = "Toitoi"

        self.han_open = 2
        self.han_closed = 2

        self.is_yakuman = False

    def is_condition_met(self, hand, *args):
        count_of_peng = len([i for i in hand if is_pon_or_kan(i)])
        return count_of_peng == 4
