class SPECIALEFFECTS(int):
    
    IngwardBreakCurse = 4600
    """ applied when Ingward breaks your curse for a soft humanity (humanity price not included in effect)\n
    uses special state 118, does not include visual effect\n
    TODO: how does this use the registCurse field, which is also -99999? """

    IngwardRemoveCurseBuildup = 4601
    """ applied when Ingward breaks your curse for a soft humanity (humanity price not included in effect)\n
    uses special state 116, removes 99999 curse buildup """

    EggHead = 5213
    """ 50% soul gain multiplier\n
    egg head not yet fully grown """
    EggHeadFinal = 5214
    """ 50% soul gain multipler\n
    egg head fully grown """
