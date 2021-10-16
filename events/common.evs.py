"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *

from constants.COLLISIONS import COLLISIONS
from constants.FLAGS import FLAGS
from constants.GOODS import GOODS
from constants.TEXT import TEXT


def Constructor():
    """ 0: Event 0 """
    EndIfClient()

    DisableFlag(760)
    DisableFlag(762)
    DisableFlag(765)

    Event260(0, 11810000, 10010600, 0.0)
    Event260(1, 257, 10010610, 0.0)
    Event260(2, 710, 10010620, 0.0)

    Event761()

    Event763()

    EnableGestureLearning()

    EnableVagrants()
    ControlOfferLordSoulsPrompt()

    AllowEscapeFromAbyss()
    DisplayTakenByAbyssMessage()

    ControlWarping()

    Event740()

    Event750()

    Event752()

    Event757()
    Event758()
    Event759()

    Event754()

    Event770()

    Event772()

    Event730()
    Event731()

    Event766()

    EnableLordVesselFlag()

    Event711(0, 2500, 711)
    Event711(1, 2501, 712)
    Event711(2, 2502, 713)
    Event711(3, 2504, 714)

    Event715()
    Event716()

    Event8131(0, 202, 203)
    Event8131(1, 204, 205)
    Event8131(2, 206, 207)
    Event8131(3, 208, 209)
    Event8131(4, 210, 211)
    Event8131(5, 212, 213)
    Event8131(6, 214, 215)

    Event819()

    Event970(0, 2, 2500, 9020, 9030)
    Event970(1, 11010901, 0, 9000, 9030)
    Event970(2, 11010902, 2510, 9000, 9030)
    Event970(3, 3, 0, 9020, 0)
    Event970(4, 4, 2520, 9020, 0)
    Event970(5, 11200900, 2530, 9000, 0)
    Event970(6, 5, 2540, 9000, 9030)
    Event970(7, 6, 2550, 9000, 9030)
    Event970(8, 7, 2560, 9000, 0)
    Event970(9, 9, 2570, 9020, 0)
    Event970(10, 11410900, 0, 9000, 9030)
    Event970(11, 11410410, 0, 9000, 0)
    Event970(12, 11410901, 0, 9000, 9030)
    Event970(13, 10, 2580, 9000, 0)
    Event970(14, 11, 2590, 9000, 0)
    Event970(15, 11510900, 2600, 0, 0)
    Event970(16, 11510902, 2610, 9000, 0)
    Event970(17, 11510903, 2620, 9000, 0)
    Event970(18, 13, 2630, 9010, 0)
    Event970(19, 14, 2640, 9000, 0)
    Event970(20, 15, 2650, 0, 0)
    Event970(21, 16, 2660, 9000, 0)
    Event970(22, 11810900, 0, 9000, 9030)
    Event970(23, 11210000, 2680, 9000, 0)
    Event970(24, 11210001, 2690, 0, 0)
    Event970(25, 17, 2700, 9040, 0)
    Event970(26, 11210004, 2710, 0, 0)

    Event250(0, 2600, 250)
    Event250(1, 2601, 251)
    Event250(2, 2602, 252)
    Event250(3, 2603, 253)
    Event250(4, 2604, 254)
    Event250(5, 2605, 255)
    Event250(6, 2606, 256)
    Event250(7, 2607, 257)
    Event250(8, 2608, 258)
    Event250(9, 2609, 259)

    Event350(0, 350, 800)
    Event350(1, 351, 801)
    Event350(2, 352, 802)
    # slots 3, 4, and 5 not used
    Event350(6, 356, 806)
    Event350(7, 357, 807)
    Event350(8, 358, 808)
    Event350(9, 359, 809)
    Event350(10, 360, 810)
    # slot 11 unused
    Event350(12, 362, 812)
    Event350(13, 363, 813)

    Event780(0, 1000, 780)
    Event780(1, 1010, 781)
    Event780(2, 1020, 782)
    Event780(3, 1030, 783)
    Event780(4, 1040, 784)
    Event780(5, 1050, 785)
    Event780(6, 1060, 786)
    Event780(7, 1070, 787)
    Event780(8, 1080, 788)
    Event780(9, 1090, 789)
    Event780(10, 1100, 790)
    Event780(11, 1110, 791)
    Event780(12, 1120, 792)
    Event780(13, 1130, 793)

    Event870(0, 0, 850)
    Event870(1, 1, 851)
    Event870(2, 2, 852)
    Event870(3, 3, 853)
    Event870(4, 4, 854)
    Event870(5, 5, 855)
    Event870(6, 6, 856)
    Event870(7, 7, 857)
    Event870(8, 8, 858)
    Event870(9, 9, 859)

    Event840(0, 840, 7905, 6370, -1)
    Event840(1, 841, 7905, 6072, -1)
    Event840(2, 842, 7905, 6080, -1)
    Event840(3, 843, 7905, 6001, -1)
    Event840(4, 844, 7898, 10000, 7896)
    Event840(5, 845, 7905, 6340, -1)
    Event840(6, 846, 7905, 6341, -1)
    Event840(7, 847, 7913, 10000, 7911)
    Event840(8, 848, 7905, 6380, -1)
    Event840(9, 849, 7905, 1400700, -1)
    Event840(10, 860, 7905, 16969, -1)

    Event690(0, 600, 4, 16, 1175)

    Event719()
    Event720()
    Event721()
    Event722()
    Event723()
    Event724()
    Event725()
    Event726()
    Event727()

    Event745()

    Event818()

    Event810()

    Event812(0, 51400350)
    Event812(1, 51010050)

    Event822()
    Event823()

    Event910(0, 11400591, 1280)

    Event911(0, 11010591, 1000, 1)
    Event911(1, 11510590, 1010, 1)
    Event911(2, 11700591, 1020, 1)
    Event911(3, 11000591, 1030, 1)
    Event911(4, 11400590, 1040, 1)
    Event911(5, 11410594, 1050, 1)
    Event911(6, 11020594, 1060, 1)
    Event911(7, 11020595, 1070, 1)
    Event911(8, 11810590, 1082, 1)
    Event911(9, 11810591, 1080, 1)
    Event911(10, 11510592, 1090, 1)
    Event911(11, 11600592, 1100, 1)
    Event911(12, 11020602, 1110, 1)
    Event911(13, 11010594, 1120, 1)
    Event911(14, 11010595, 1130, 1)
    Event911(15, 11020599, 1140, 1)
    Event911(16, 11020607, 1150, 1)
    Event911(17, 11200592, 1160, 1)
    Event911(18, 11200593, 1170, 1)
    Event911(19, 11200594, 1180, 1)
    Event911(20, 11300590, 1190, 1)
    Event911(21, 11300591, 1200, 1)
    Event911(22, 11310590, 1210, 1)
    Event911(23, 11310592, 1220, 1)
    Event911(24, 11310593, 1230, 1)
    Event911(25, 11310594, 1240, 1)
    Event911(26, 11320590, 1250, 1)
    Event911(27, 11320581, 1260, 1)
    Event911(28, 11320593, 1270, 1)
    Event911(29, 11400592, 1290, 1)
    Event911(30, 11400594, 1300, 1)
    Event911(31, 11400596, 1310, 1)
    Event911(32, 11400597, 1320, 1)
    Event911(33, 11400598, 1330, 1)
    Event911(34, 11400599, 1340, 1)
    Event911(35, 11510595, 1350, 1)
    Event911(36, 11510596, 1360, 1)
    Event911(37, 11510597, 1370, 1)
    Event911(38, 11600594, 1380, 1)
    Event911(39, 11600595, 1390, 1)
    Event911(40, 11600596, 1400, 1)
    Event911(41, 11010598, 1410, 0)
    Event911(42, 11210590, 1500, 1)
    Event911(43, 11210593, 1510, 1)
    Event911(44, 11210594, 1520, 1)
    Event911(45, 11600580, 1401, 1)
    Event911(46, 11600581, 1402, 1)
    Event911(47, 11600582, 1403, 1)
    Event911(48, 11600583, 1404, 1)
    Event911(49, 11020905, 1800, 1)
    Event911(50, 11510905, 1810, 1)
    Event911(51, 11010905, 1820, 1)
    Event911(52, 11600905, 1830, 1)
    Event911(53, 11320905, 1840, 1)
    Event911(54, 11300906, 1850, 1)
    Event911(55, 11200905, 1860, 1)
    Event911(56, 11510906, 1870, 1)
    Event911(57, 11400905, 1880, 1)

    Event890(0, 11310580, 1221, 1)
    Event890(1, 11510580, 1361, 1)
    Event890(2, 11510581, 1371, 1)
    Event890(3, 11320592, 1261, 1)

    Event960(0, 1322, 6190, 6190)
    Event960(1, 1315, 6180, 1100)
    Event960(2, 1402, 6230, 6230)
    Event960(3, 1402, 6230, 6231)

    Event8200(0, 3, 5500, 50000120, 11010594)
    Event8200(1, 3, 5510, 50000130, 11010595)
    Event8200(2, 2, 103, 50000160, 11200592)
    Event8200(3, 3, 240, 50000170, 11200593)
    Event8200(4, 2, 124, 50000180, 11200594)
    Event8200(5, 0, 453000, 50000220, 11310592)
    Event8200(6, 3, 5100, 50000225, 11310580)
    Event8200(7, 3, 5110, 50000230, 11310593)
    Event8200(8, 3, 114, 50000265, 11320581)
    Event8200(9, 3, 377, 50000260, 11320592)
    Event8200(10, 3, 378, 50000270, 11320593)
    Event8200(11, 3, 4500, 50000310, 11400596)
    Event8200(12, 3, 4520, 50000320, 11400597)
    Event8200(13, 3, 4510, 50000330, 11400598)
    Event8200(14, 2, 130, 50000350, 11510595)
    Event8200(15, 3, 113, 50000360, 11510596)
    Event8200(16, 2, 102, 50000365, 11510580)
    Event8200(17, 3, 5910, 50000370, 11510597)
    Event8200(18, 0, 1366000, 50000375, 11510581)
    Event8200(19, 0, 904000, 50000380, 11600594)
    Event8200(20, 3, 102, 50000390, 11600595)
    Event8200(21, 0, 210000, 50000400, 11600596)
    Event8200(22, 1, 40000, 50000410, 11600580)
    Event8200(23, 1, 41000, 50000420, 11600581)
    Event8200(24, 1, 42000, 50000430, 11600582)
    Event8200(25, 1, 43000, 50000440, 11600583)
    Event8200(26, 3, 131, 50000800, 11020905)
    Event8200(27, 3, 132, 50000810, 11510905)
    Event8200(28, 3, 133, 50000820, 11010905)
    Event8200(29, 3, 134, 50000830, 11600905)
    Event8200(30, 3, 135, 50000840, 11320905)
    Event8200(31, 3, 136, 50000850, 11300906)
    Event8200(32, 3, 137, 50000860, 11200905)
    Event8200(33, 3, 138, 50000870, 11510906)
    Event8200(34, 3, 139, 50000880, 11400905)

    Event8300(0, 3, 100, 50000000)
    Event8300(1, 3, 101, 51100330)
    Event8300(2, 3, 102, 50000390)
    Event8300(3, 3, 106, 11017020)
    Event8300(4, 3, 108, 11607020)
    Event8300(5, 3, 112, 11407080)
    Event8300(6, 3, 2508, 11007010)
    Event8300(7, 3, 385, 11017210)

    Event8090(0, 3, 510, 11217010)
    Event8090(1, 3, 511, 11217020)
    Event8090(2, 3, 512, 11217030)
    Event8090(3, 3, 513, 11217040)
    Event8090(4, 3, 514, 11217050)


def Preconstructor():
    """ 50: Event 50 """

    if FlagDisabled(909):
        SkipLinesIfFlagRangeAnyOn(1, (1000, 1029))
        EnableFlag(1000)
        SkipLinesIfFlagRangeAnyOn(1, (1030, 1059))
        EnableFlag(1030)
        SkipLinesIfFlagRangeAnyOn(1, (1060, 1089))
        EnableFlag(1060)
        SkipLinesIfFlagRangeAnyOn(1, (1090, 1109))
        EnableFlag(1090)
        SkipLinesIfFlagRangeAnyOn(1, (1110, 1119))
        EnableFlag(1110)
        SkipLinesIfFlagRangeAnyOn(1, (1120, 1139))
        EnableFlag(1120)
        SkipLinesIfFlagRangeAnyOn(1, (1140, 1169))
        EnableFlag(1140)
        SkipLinesIfFlagRangeAnyOn(1, (1170, 1189))
        EnableFlag(1170)
        SkipLinesIfFlagRangeAnyOn(1, (1190, 1209))
        EnableFlag(1202)
        SkipLinesIfFlagRangeAnyOn(1, (1210, 1219))
        EnableFlag(1210)
        SkipLinesIfFlagRangeAnyOn(1, (1220, 1229))
        EnableFlag(1220)
        SkipLinesIfFlagRangeAnyOn(1, (1230, 1239))
        EnableFlag(1230)
        SkipLinesIfFlagRangeAnyOn(1, (1240, 1249))
        EnableFlag(1240)
        SkipLinesIfFlagRangeAnyOn(1, (1250, 1259))
        EnableFlag(1250)
        SkipLinesIfFlagRangeAnyOn(1, (1270, 1279))
        EnableFlag(1270)
        SkipLinesIfFlagRangeAnyOn(1, (1280, 1289))
        EnableFlag(1280)
        SkipLinesIfFlagRangeAnyOn(1, (1290, 1309))
        EnableFlag(1290)
        SkipLinesIfFlagRangeAnyOn(1, (1310, 1319))
        EnableFlag(1310)
        SkipLinesIfFlagRangeAnyOn(1, (1320, 1339))
        EnableFlag(1320)
        SkipLinesIfFlagRangeAnyOn(1, (1340, 1359))
        EnableFlag(1340)
        SkipLinesIfFlagRangeAnyOn(1, (1360, 1379))
        EnableFlag(1360)
        SkipLinesIfFlagRangeAnyOn(1, (1380, 1399))
        EnableFlag(1380)
        SkipLinesIfFlagRangeAnyOn(1, (1400, 1409))
        EnableFlag(1400)
        SkipLinesIfFlagRangeAnyOn(1, (1410, 1419))
        EnableFlag(1410)
        SkipLinesIfFlagRangeAnyOn(1, (1420, 1429))
        EnableFlag(1420)
        SkipLinesIfFlagRangeAnyOn(1, (1430, 1459))
        EnableFlag(1430)
        SkipLinesIfFlagRangeAnyOn(1, (1460, 1489))
        EnableFlag(1460)
        SkipLinesIfFlagRangeAnyOn(1, (1490, 1539))
        EnableFlag(1490)
        SkipLinesIfFlagRangeAnyOn(1, (1540, 1569))
        EnableFlag(1540)
        SkipLinesIfFlagRangeAnyOn(1, (1570, 1599))
        EnableFlag(1570)
        SkipLinesIfFlagRangeAnyOn(1, (1600, 1619))
        EnableFlag(1600)
        SkipLinesIfFlagRangeAnyOn(1, (1620, 1639))
        EnableFlag(1620)
        SkipLinesIfFlagRangeAnyOn(1, (1640, 1669))
        EnableFlag(1640)
        SkipLinesIfFlagRangeAnyOn(1, (1670, 1679))
        EnableFlag(1670)
        SkipLinesIfFlagRangeAnyOn(1, (1690, 1699))
        EnableFlag(1690)
        SkipLinesIfFlagRangeAnyOn(1, (1700, 1709))
        EnableFlag(1700)
        SkipLinesIfFlagRangeAnyOn(1, (1710, 1729))
        EnableFlag(1710)
        SkipLinesIfFlagRangeAnyOn(1, (1760, 1769))
        EnableFlag(1760)
        SkipLinesIfFlagRangeAnyOn(1, (1770, 1779))
        EnableFlag(1770)
        SkipLinesIfFlagRangeAnyOn(1, (1780, 1789))
        EnableFlag(1780)

    SkipLinesIfFlagRangeAnyOn(1, (1820, 1839))
    EnableFlag(1820)
    SkipLinesIfFlagRangeAnyOn(1, (1840, 1859))
    EnableFlag(1840)
    SkipLinesIfFlagRangeAnyOn(1, (1860, 1869))
    EnableFlag(1860)
    SkipLinesIfFlagRangeAnyOn(1, (1870, 1889))
    EnableFlag(1870)

    if FlagDisabled(909):
        EnableFlag(11807020)
        EnableFlag(11807030)
        EnableFlag(11807040)
        EnableFlag(11807050)
        EnableFlag(11807060)
        EnableFlag(11807070)
        EnableFlag(11807080)
        EnableFlag(11807090)
        EnableFlag(11807100)
        EnableFlag(11807110)
        EnableFlag(11807120)
        EnableFlag(11807130)
        EnableFlag(11807170)
        EnableFlag(11807180)
        EnableFlag(11807190)
        EnableFlag(11807200)
        EnableFlag(11807210)
        EnableFlag(11807220)
        EnableFlag(11807230)
        EnableFlag(11807240)
        EnableFlag(11217060)
        EnableFlag(11217070)
        EnableFlag(11217080)
        EnableFlag(11217090)

    if FlagDisabled(909):
        EnableFlag(909)
        EnableFlag(814)
        EnableFlag(50006071)
        EnableFlag(50006080)


def EnableGestureLearning():
    """ 290: Enables flags that allow learning gestures from NPCs """
    # these flags are disabled once the respective gestures are learned

    EndIfThisEventOn()

    EnableFlagRange((280, 290))
    # see entries in FLAGS

    if PlayerIsClass(ClassType.Knight) or PlayerIsClass(ClassType.Cleric):
        DisableFlag(FLAGS.CanLearnPrayer)
    else:
        DisableFlag(FLAGS.CanLearnJoy)


def EnableVagrants():
    """ 701: Enables vagrant spawning after leaving the asylum """
    EndIfThisEventOn()

    EnableVagrantSpawning()

    Await(InsideMap(UNDEAD_ASYLUM))
    DisableVagrantSpawning()

    Await(FlagEnabled(FLAGS.HasWarpedToFirelinkShrine))
    EnableVagrantSpawning()


def ControlOfferLordSoulsPrompt():
    """ 702: handles the event flag responsible for displaying the 'Offer Lord Souls' prompt at the Lordvessel """
    DisableFlag(FLAGS.CanOfferLordSouls)

    Await(FlagDisabled(FLAGS.HasOfferedAllLordSouls)
          and InsideMap(KILN_OF_THE_FIRST_FLAME))
    EnableFlag(FLAGS.CanOfferLordSouls)

    Await(OutsideMap(KILN_OF_THE_FIRST_FLAME)
          or FlagEnabled(FLAGS.HasOfferedAllLordSouls))
    DisableFlag(FLAGS.CanOfferLordSouls)

    Restart()


def AllowEscapeFromAbyss():
    """ 717: Responsible for the flag that enables warping from the Abyss bonfire without the Lordvessel """
    DisableFlag(FLAGS.StandingInAbyssWithoutLordvessel)

    Await(FlagDisabled(FLAGS.GotLordvessel) and InsideMap(NEW_LONDO_RUINS)
          and PlayerStandingOnCollision(COLLISIONS.abyss))

    EnableFlag(FLAGS.StandingInAbyssWithoutLordvessel)

    Await(PlayerStandingOnCollision(COLLISIONS.abyss))

    DisableFlag(FLAGS.StandingInAbyssWithoutLordvessel)
    Restart()


def DisplayTakenByAbyssMessage():
    """ 718: Displays the 'You were taken by the abyss' message, if applicable """
    EndIfFlagOff(FLAGS.TakenByAbyss)

    DisplayStatus(TEXT.TakenByAbyss, pad_enabled=True)
    DisableFlag(FLAGS.TakenByAbyss)


def ControlWarping():
    """ 706: Controls whether warping from bonfires is allowed """
    Await(FlagEnabled(FLAGS.GotLordvessel))

    EnableFlag(FLAGS.WarpAllowed)

    Await(FlagEnabled(FLAGS.IsInDukesArchivesPrisonCell)
          or InsideMap(PAINTED_WORLD))

    DisableFlag(FLAGS.WarpAllowed)

    Await(FlagDisabled(FLAGS.IsInDukesArchivesPrisonCell)
          and OutsideMap(PAINTED_WORLD))

    Restart()


def EnableLordVesselFlag():
    """ 710: enables a flag when the player obtains the Lordvessel """
    EndIfThisEventOn()

    Await(HasGood(GOODS.Lordvessel))

    EnableFlag(FLAGS.GotLordvessel)


def Event711(_, arg_0_3: int, arg_4_7: int):
    """ 711: Event 711 """
    EndIfThisEventSlotOn()

    IfPlayerHasGood(0, arg_0_3, including_box=False)
    EnableFlag(arg_4_7)


def Event715():
    """ 715: Event 715 """
    DisableFlag(715)

    # condition group 1 consists of the following joined by AND:
    IfPlayerHasGood(1, 702, including_box=False)
    IfPlayerDoesNotHaveGood(1, 5520, including_box=True)
    IfPlayerCovenant(1, Covenant.WarriorOfSunlight)

    # condition group 2 consists of condition group 1, plus a flag check joined by AND:
    IfFlagOn(2, 11010595)
    IfConditionTrue(2, 1)

    AwaitConditionTrue(2)

    EnableFlag(715)

    AwaitConditionFalse(1)

    Restart()


def Event716():
    """ 716: Event 716 """
    EndIfThisEventOn()

    Await(FlagEnabled(50000082))
    EnableFlag(716)


def Event8131(_, arg_0_3: int, arg_4_7: int):
    """ 8131: Event 8131 """
    EndIfThisEventSlotOn()

    Await(HasGood(arg_0_3) or HasGood(arg_4_7))

    if arg_0_3 == 202:
        EnableFlag(8131)
    if arg_0_3 == 204:
        EnableFlagRange((8131, 8132))
    if arg_0_3 == 206:
        EnableFlagRange((8131, 8133))
    if arg_0_3 == 208:
        EnableFlagRange((8131, 8134))
    if arg_0_3 == 210:
        EnableFlagRange((8131, 8135))
    if arg_0_3 == 212:
        EnableFlagRange((8131, 8136))
    if arg_0_3 == 214:
        EnableFlagRange((8131, 8137))


def Event819():
    """ 819: Event 819 """
    EndIfThisEventOn()

    Await(FlagEnabled(11017040) or FlagEnabled(11017170))

    EnableFlag(11017040)
    EnableFlag(11017170)


def Event719():
    """ 719: Event 719 """
    EndIfThisEventOn()

    Await(HasGood(3000) or
          HasGood(3010) or
          HasGood(3020) or
          HasGood(3030) or
          HasGood(3040) or
          HasGood(3050) or
          HasGood(3060) or
          HasGood(3070) or
          HasGood(3100) or
          HasGood(3110) or
          HasGood(3120) or
          HasGood(3300) or
          HasGood(3400) or
          HasGood(3410) or
          HasGood(3500) or
          HasGood(3510) or
          HasGood(3520) or
          HasGood(3530) or
          HasGood(3540) or
          HasGood(3550) or
          HasGood(3600) or
          HasGood(3610) or
          HasGood(3700) or
          HasGood(4000) or
          HasGood(4010) or
          HasGood(4020) or
          HasGood(4030) or
          HasGood(4040) or
          HasGood(4050) or
          HasGood(4060) or
          HasGood(4100) or
          HasGood(4110) or
          HasGood(4200) or
          HasGood(4210) or
          HasGood(4220) or
          HasGood(4300) or
          HasGood(4310) or
          HasGood(4360) or
          HasGood(4400) or
          HasGood(4500) or
          HasGood(4510) or
          HasGood(4520) or
          HasGood(5000) or
          HasGood(5010) or
          HasGood(5020) or
          HasGood(5030) or
          HasGood(5040) or
          HasGood(5050) or
          HasGood(5100) or
          HasGood(5110) or
          HasGood(5200) or
          HasGood(5210) or
          HasGood(5300) or
          HasGood(5310) or
          HasGood(5320) or
          HasGood(5400) or
          HasGood(5500) or
          HasGood(5510) or
          HasGood(5520) or
          HasGood(5600) or
          HasGood(5610) or
          HasGood(5700) or
          HasGood(5710) or
          HasGood(5800) or
          HasGood(5810) or
          HasGood(5900) or
          HasGood(5910) or
          HasGood(3710) or
          HasGood(3720) or
          HasGood(3730) or
          HasGood(3740) or
          HasGood(4530))

    EnableFlag(719)


def Event720():
    """ 720: Event 720 """
    EndIfThisEventOn()

    Await(HasGood(4020) or
          HasGood(4030) or
          HasGood(4040) or
          HasGood(4060) or
          HasGood(4110) or
          HasGood(4500) or
          HasGood(4510) or
          HasGood(4520))

    EnableFlag(11020102)


def Event730():
    """ 730: Event 730 """
    Await(FlagDisabled(732) and FlagEnabled(8000))

    EnableFlag(732)
    EnableFlag(735)

    Restart()


def Event731():
    """ 731: Event 731 """
    AwaitFlagOff(8000)

    DisableFlag(732)
    DisableFlag(735)

    AwaitFlagOn(8000)

    Restart()


def Event250(_, arg_0_3: int, arg_4_7: int):
    """ 250: Event 250 """
    EndIfThisEventSlotOn()

    Await(HasGood(arg_0_3))

    EnableFlag(arg_4_7)


def Event350(_, arg_0_3: int, arg_4_7: int):
    """ 350: Event 350 """
    if THIS_SLOT_FLAG and not HasGood(arg_4_7):
        End()

    AwaitFlagOn(arg_0_3)

    RemoveGoodFromPlayer(arg_4_7, quantity=1)


def Event780(_, arg_0_3: int, arg_4_7: int):
    """ 780: Event 780 """
    DisableFlag(arg_4_7)

    Await(HasGood(arg_0_3))

    EnableFlag(arg_4_7)

    Await(not HasGood(arg_0_3))

    Restart()


def Event870(_, arg_0_0: uchar, arg_4_7: int):
    """ 870: Event 870 """
    IfPlayerCovenant(1, arg_0_0)

    AwaitConditionTrue(1)

    EnableFlag(arg_4_7)

    AwaitConditionFalse(1)

    DisableFlag(arg_4_7)
    Restart()


def Event260(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 260: Event 260 """
    EndIfFlagOn(arg_0_3)

    AwaitFlagOn(arg_0_3)

    if FlagDisabled(9121):
        Wait(arg_8_11)
        DisplayStatus(arg_4_7, pad_enabled=True)


def Event970(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 970: Event 970 """
    EndIfFlagOn(arg_0_3)

    AwaitFlagOn(arg_0_3)

    if arg_4_7 != 0:
        AwardItemLot(arg_4_7, host_only=True)

    DisableNetworkSync()
    Wait(5.0)

    if arg_8_11 != 0:
        AwardItemLot(arg_8_11, host_only=True)
    if arg_12_15 != 0:
        AwardItemLot(arg_12_15, host_only=True)


def Event911(_, award_allowed: int, item_lot: int, repeatable: uchar):
    """ 911: Event 911 """
    EndIfFlagOn(award_allowed)

    AwaitFlagOn(award_allowed)

    AwardItemLot(item_lot, host_only=True)

    SetFlagState(award_allowed, state=repeatable)
    EndIfFlagOn(award_allowed)

    Restart()


def Event890(_, award_allowed: int, item_lot: int, repeatable: uchar):
    """ 890: Event 890 """
    EndIfFlagOn(award_allowed)

    AwaitFlagOn(award_allowed)

    AwardItemLot(item_lot, host_only=True)

    SetFlagState(award_allowed, state=repeatable)
    EndIfFlagOn(award_allowed)

    Restart()


def Event960(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 960: Event 960 """
    EndIfThisEventSlotOn()

    Await(FlagEnabled(arg_0_3) and IsDead(arg_4_7))

    AwardItemLot(arg_8_11, host_only=True)


def Event8200(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 8200: Event 8200 """
    EndIfFlagOn(arg_8_11)

    if NEW_GAME_CYCLE < 1:
        End()
    if not OwnsItem(arg_4_7, item_type=arg_0_0):
        End()

    EnableFlag(arg_8_11)
    EnableFlag(arg_12_15)


def Event8300(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """ 8300: Event 8300 """
    EndIfFlagOn(arg_8_11)

    if NEW_GAME_CYCLE < 1:
        End()
    if not OwnsItem(arg_4_7, item_type=arg_0_0):
        End()

    EnableFlag(arg_8_11)


def Event8090(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """ 8090: Event 8090 """
    EndIfFlagOn(arg_8_11)

    if NEW_GAME_CYCLE < 1:
        End()
    if not OwnsItem(arg_4_7, item_type=arg_0_0):
        End()

    EnableFlag(arg_8_11)


def Event910(_, arg_0_3: int, arg_4_7: int):
    """ 910: Event 910 """
    if FlagDisabled(arg_0_3):
        AwaitFlagOn(arg_0_3)
        AwardItemLot(arg_4_7, host_only=True)

    AwaitFlagOff(arg_0_3)
    Restart()


def Event690(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint, arg_12_15: int):
    """ 690: Event 690 """
    SkipLinesIfThisEventSlotOn(1)

    AwaitFlagOn(arg_12_15)

    # here we conditionally add to the -1 condition group:
    # if the flag is disabled at this point, it's added to the group,
    # and afterwards we check to see when any of these become enabled
    if FlagDisabled(2):
        IfFlagOn(-1, 2)
    if FlagDisabled(3):
        IfFlagOn(-1, 3)
    if FlagDisabled(4):
        IfFlagOn(-1, 4)
    if FlagDisabled(5):
        IfFlagOn(-1, 5)
    if FlagDisabled(6):
        IfFlagOn(-1, 6)
    if FlagDisabled(7):
        IfFlagOn(-1, 7)
    if FlagDisabled(8):
        IfFlagOn(-1, 8)
    if FlagDisabled(9):
        IfFlagOn(-1, 9)
    if FlagDisabled(10):
        IfFlagOn(-1, 10)
    if FlagDisabled(11):
        IfFlagOn(-1, 11)
    if FlagDisabled(12):
        IfFlagOn(-1, 12)
    if FlagDisabled(13):
        IfFlagOn(-1, 13)
    if FlagDisabled(14):
        IfFlagOn(-1, 14)
    if FlagDisabled(15):
        IfFlagOn(-1, 15)

    AwaitConditionTrue(-1)

    IncrementEventValue(arg_0_3, bit_count=arg_4_7, max_value=arg_8_11)
    Restart()


def Event721():
    """ 721: Event 721 """
    EndIfFlagOn(728)

    Await(FlagEnabled(11707000) and
          FlagEnabled(11707010) and
          FlagEnabled(11707020) and
          FlagEnabled(11707030) and
          FlagEnabled(11707040) and
          FlagEnabled(11707050) and
          FlagEnabled(11707060) and
          FlagEnabled(11707070))
    AwaitConditionTrue(1)

    EnableFlag(721)

    Await(FlagEnabled(11707090) and FlagEnabled(
        11707100) and FlagEnabled(11707110))

    EnableFlag(728)


def Event722():
    """ 722: Event 722 """
    EndIfThisEventOn()

    Await(FlagEnabled(11407120) and
          FlagEnabled(11407130) and
          FlagEnabled(11407150) and
          FlagEnabled(11407160) and
          FlagEnabled(11407170) and
          # yes this was ordered like this in vanilla
          FlagEnabled(11407140) and
          FlagEnabled(11407180) and
          FlagEnabled(11407190) and
          FlagEnabled(10) and
          HasWeapon(1332500))

    EnableFlag(722)


def Event723():
    """ 723: Event 723 """
    EndIfThisEventOn()

    Await(FlagEnabled(11027130) and
          FlagEnabled(11027140) and
          FlagEnabled(11027150) and
          FlagEnabled(11027160) and
          FlagEnabled(11027170) and
          FlagEnabled(11027180) and
          FlagEnabled(11027190) and
          FlagEnabled(11027200) and
          FlagEnabled(11027210) and
          FlagEnabled(11027220) and
          FlagEnabled(11027230) and
          FlagEnabled(11027240))

    EnableFlag(723)


def Event724():
    """ 724: Event 724 """
    EndIfThisEventOn()

    Await(FlagEnabled(11017050) and
          FlagEnabled(11017060) and
          FlagEnabled(11017070) and
          FlagEnabled(11017080) and
          FlagEnabled(11017090) and
          FlagEnabled(11017100) and
          FlagEnabled(11017110) and
          FlagEnabled(11017120) and
          FlagEnabled(11017130))

    EnableFlag(724)


def Event725():
    """ 725: Event 725 """
    EndIfThisEventOn()
    Await(TrueFlagCount((11707100, 11707190)) >= 2)
    EnableFlag(725)


def Event726():
    """ 726: Event 726 """
    EndIfThisEventOn()
    Await(TrueFlagCount((11607000, 11607090)) >= 2)
    EnableFlag(726)


def Event727():
    """ 727: Event 727 """
    EndIfThisEventOn()

    Await(FlagEnabled(11327000) and
          FlagEnabled(11327010) and
          FlagEnabled(11327020) and
          FlagEnabled(11327030) and
          FlagEnabled(11327040) and
          FlagEnabled(11327050) and
          FlagEnabled(11327060) and
          FlagEnabled(11327070) and
          FlagEnabled(11327080) and
          FlagEnabled(11327090))

    EnableFlag(727)


def Event740():
    """ 740: Event 740 """
    Await(PlayerIsClass(ClassType.Pyromancer))
    EnableFlag(740)


def Event745():
    """ 745: Event 745 """
    if FlagEnabled(1604) and FlagEnabled(1764):
        Await(FlagEnabled(703))

    # wait until one of these flags become enabled, but only if they were disabled to begin with
    if FlagDisabled(1604):
        IfFlagOn(-1, 1604)
    if FlagDisabled(1764):
        IfFlagOn(-1, 1764)
    AwaitConditionTrue(-1)
    End()


def Event754():
    """ 754: Event 754 """
    DisableFlag(754)

    AwaitFlagOn(754)

    DisableFlag(754)
    AddSpecialEffect(PLAYER, 4600)
    AddSpecialEffect(PLAYER, 4601)
    CreateTemporaryVFX(22715, anchor_entity=PLAYER,
                       anchor_type=CoordEntityType.Character, model_point=7)
    Restart()


def Event770():
    """ 770: Event 770 """
    AwaitFlagOn(755)

    DisableFlag(755)
    DisableFlag(742)
    DisableFlag(743)
    DisableFlag(744)
    DisableFlag(745)
    DisableFlag(746)
    DisableFlagRange((11000501, 11000519))
    DisableFlagRange((11010501, 11010519))
    DisableFlagRange((11020501, 11020529))
    DisableFlagRange((11100501, 11100519))
    DisableFlagRange((11200501, 11200519))
    DisableFlagRange((11300501, 11300519))
    DisableFlagRange((11310501, 11310519))
    DisableFlagRange((11320501, 11320519))
    DisableFlagRange((11400501, 11400519))
    DisableFlagRange((11410501, 11410519))
    DisableFlagRange((11500501, 11500519))
    DisableFlagRange((11510501, 11510519))
    DisableFlagRange((11600501, 11600519))
    DisableFlagRange((11700501, 11700519))
    DisableFlagRange((11800501, 11800519))
    DisableFlagRange((11810501, 11810519))
    DisableFlagRange((11210501, 11210519))
    DisableFlag(1004)
    DisableFlag(1033)
    DisableFlag(1096)
    DisableFlag(1114)
    DisableFlag(1176)
    DisableFlag(1179)
    DisableFlag(1195)
    DisableFlag(1197)
    DisableFlag(1213)
    DisableFlag(1223)
    DisableFlag(1241)
    DisableFlag(1253)
    DisableFlag(1282)
    DisableFlag(1283)
    DisableFlag(1287)
    DisableFlag(1294)
    DisableFlag(1314)
    DisableFlag(1321)
    DisableFlag(1341)
    DisableFlag(1361)
    DisableFlag(1381)
    DisableFlag(1401)
    DisableFlag(1411)
    DisableFlag(1421)
    DisableFlag(1434)
    DisableFlag(1461)
    DisableFlag(1512)
    DisableFlag(1547)
    DisableFlag(1574)
    DisableFlag(1603)
    DisableFlag(1627)
    DisableFlag(1646)
    DisableFlag(1675)
    DisableFlag(1691)
    EnableFlag(1710)  # one of these is not like the others
    DisableFlag(1711)
    DisableFlag(1712)
    DisableFlag(11200596)
    DisableFlag(71200035)
    DisableFlag(71200042)
    DisableFlag(1763)
    DisableFlag(1822)
    DisableFlag(1841)
    DisableFlag(1863)
    DisableFlag(1871)
    SetTeamType(6001, TeamType.Ally)
    SetTeamType(6040, TeamType.Ally)
    SetTeamType(6072, TeamType.Ally)
    SetTeamType(6190, TeamType.Ally)
    SetTeamType(6230, TeamType.Ally)
    SetTeamType(6300, TeamType.Ally)
    Restart()


def Event772():
    """ 772: Event 772 """
    AwaitFlagOff(744)

    Await(FlagEnabled(1004) or
          FlagEnabled(1033) or
          FlagEnabled(1096) or
          FlagEnabled(1114) or
          FlagEnabled(1176) or
          FlagEnabled(1179) or
          FlagEnabled(1195) or
          FlagEnabled(1197) or
          FlagEnabled(1213) or
          FlagEnabled(1223) or
          FlagEnabled(1241) or
          FlagEnabled(1253) or
          FlagEnabled(1282) or
          FlagEnabled(1283) or
          FlagEnabled(1287) or
          FlagEnabled(1294) or
          FlagEnabled(1314) or
          FlagEnabled(1321) or
          FlagEnabled(1341) or
          FlagEnabled(1361) or
          FlagEnabled(1381) or
          FlagEnabled(1401) or
          FlagEnabled(1411) or
          FlagEnabled(1421) or
          FlagEnabled(1434) or
          FlagEnabled(1461) or
          FlagEnabled(1512) or
          FlagEnabled(1547) or
          FlagEnabled(1574) or
          FlagEnabled(1603) or
          FlagEnabled(1627) or
          FlagEnabled(1646) or
          FlagEnabled(1675) or
          FlagEnabled(1691) or
          FlagEnabled(1711) or
          FlagEnabled(1712) or
          FlagEnabled(71200035) or
          FlagEnabled(71200042) or
          FlagEnabled(1763) or
          FlagEnabled(1822) or
          FlagEnabled(1841) or
          FlagEnabled(1863) or
          FlagEnabled(1871))

    EnableFlag(744)
    AwaitFlagOff(744)

    Restart()


def Event761():
    """ 761: Event 761 """
    DisableNetworkSync()

    AwaitFlagOn(760)

    WaitFrames(200)
    DisableFlag(760)
    Restart()


def Event763():
    """ 763: Event 763 """
    DisableNetworkSync()

    AwaitFlagOn(762)

    ForceAnimation(PLAYER, 7697)
    Wait(3.5)
    DisableFlag(762)
    Wait(2.799999952316284)
    DisableFlag(764)
    ForceAnimation(PLAYER, 7701, loop=True)
    Restart()


def Event750():
    """ 750: Event 750 """
    DisableNetworkSync()

    Await(HasSpecialEffect(PLAYER, 71) or
          HasSpecialEffect(PLAYER, 72) or
          HasSpecialEffect(PLAYER, 73) or
          HasSpecialEffect(PLAYER, 74) or
          FlagEnabled(751))

    EnableFlag(751)

    Await(not HasSpecialEffect(PLAYER, 71) and
          not HasSpecialEffect(PLAYER, 72) and
          not HasSpecialEffect(PLAYER, 73) and
          not HasSpecialEffect(PLAYER, 74))

    DisableFlag(751)
    Restart()


def Event752():
    """ 752: Event 752 """
    DisableNetworkSync()

    Await(HasSpecialEffect(PLAYER, 5213) or
          HasSpecialEffect(PLAYER, 5214) or
          FlagEnabled(753))

    EnableFlag(753)

    Await(not HasSpecialEffect(PLAYER, 5213) and
          not HasSpecialEffect(PLAYER, 5214))

    DisableFlag(753)
    DisableFlag(11400591)
    Restart()


def Event757():
    """ 757: Event 757 """
    if FlagEnabled(757):
        DisplayStatus(10010660, pad_enabled=True)

    DisableFlag(757)

    Await(HOST and
          HasSpecialEffect(PLAYER, 71) and
          HasSpecialEffect(PLAYER, 72) and
          HasSpecialEffect(PLAYER, 73) and
          HasSpecialEffect(PLAYER, 74) and
          (
              HasSpecialEffect(PLAYER, 33) or
              HasSpecialEffect(PLAYER, 34)
          )
          )

    End()


def Event758():
    """ 758: Event 758 """
    if THIS_FLAG:
        DisplayStatus(10010670, pad_enabled=True)

    DisableFlag(758)

    Await(HOST and
          HealthValue(PLAYER) <= 0 and
          HasSpecialEffect(PLAYER, 2130))

    Await(HOST and
          IsDead(PLAYER) and
          HasSpecialEffect(PLAYER, 2130))

    End()


def Event759():
    """ 759: Event 759 """
    if THIS_FLAG:
        DisplayStatus(10010680, pad_enabled=True)

    DisableFlag(759)

    Await(HOST and
          HealthValue(PLAYER) <= 0 and
          HasSpecialEffect(PLAYER, 2131))

    Await(HOST and
          IsDead(PLAYER) and
          HasSpecialEffect(PLAYER, 2131))

    End()


def Event818():
    """ 818: Event 818 """
    if FlagDisabled(11510150):
        AwaitFlagOn(11510150)
        DisplayStatus(10010690, pad_enabled=True)

    Await(FlagEnabled(11510150) and
          OutsideMap(ANOR_LONDO))

    DisableFlag(11510150)
    Restart()


def Event810():
    """ 810: Event 810 """
    EndIfThisEventOn()

    AwaitFlagOn(50001031)

    EnableFlag(810)


def Event812(_, arg_0_3: int):
    """ 812: Event 812 """
    EndIfThisEventSlotOn()

    AwaitFlagOn(arg_0_3)

    End()


def Event822():
    """ 822: Event 822 """
    AwaitFlagOn(830)

    Await(SecondsElapsed(0.5) and
          OutsideMap(KILN_OF_THE_FIRST_FLAME))

    DisableFlag(830)
    Restart()


def Event823():
    """ 823: Event 823 """
    AwaitFlagOn(831)

    Await(SecondsElapsed(0.5) and
          OutsideMap(KILN_OF_THE_FIRST_FLAME))

    DisableFlag(831)
    Restart()


def Event840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 840: Event 840 """
    DisableFlag(arg_0_3)

    AwaitFlagOn(arg_0_3)

    if FlagDisabled(844) and FlagDisabled(847):
        RotateToFaceEntity(PLAYER, arg_8_11)
        ForceAnimation(PLAYER, arg_4_7)

    if (FlagDisabled(840) and
        FlagDisabled(841) and
        FlagDisabled(842) and
        FlagDisabled(843) and
        FlagDisabled(845) and  # note 844 is skipped
        FlagDisabled(846) and
        FlagDisabled(848) and
        FlagDisabled(849) and
            FlagDisabled(860)):  # not 850

        ForceAnimation(PLAYER, arg_4_7, skip_transition=True)

    Wait(1.0)
    PlaySoundEffect(anchor_entity=PLAYER,
                    sound_type=SoundType.s_SFX, sound_id=123456789)
    Wait(4.0)

    if arg_12_15 != -1:
        ForceAnimation(PLAYER, arg_12_15, loop=True)

    Restart()


def Event766():
    """ 766: Event 766 """
    if ONLINE:
        End()
    EnableFlag(765)
