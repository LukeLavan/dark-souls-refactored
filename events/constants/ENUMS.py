from enum import IntEnum


class PlayerStats(IntEnum):
    """ used to reference player status """
    Vitality = 0
    Attunement = 1
    Endurance = 2
    Strength = 3
    Dexterity = 4
    Intelligence = 5
    Faith = 6
    # TODO: Resistance = 7 ?
    Soul = 8
    TotalGetSoul = 9 # TODO: soul memory?
    Humanity = 10
    Covenant = 11
    Gender = 12 # TODO: which is which?
    BossKillAssists = 13
    """ number of hosts assisted through multiplayer, used to offset faith req of sunbro covenant"""
    ForestInvadersKilled = 14
    """ number of hosts killed through forest hunter covenant invasions """
    CurrentCovenantPoints = 15
    """ how many respective covenant items have been offered\n
    a soft betrayal (leaving a covenant amicably) causes this number to be halved (rounded down)\n
    a hard betrayal (getting kicked out) causes this number to be reset to 0 """
    CurrentCovenantLevel = 16
    """ the covenant level that corresponds to the respective CovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    WarriorOfSunlightCovenantPoints = 17
    """ how many sunlight medals have been offered to the Sunlight Altar """
    DarkwraithCovenantPoints = 18
    """ how many humanity have been offered to Kaathe """
    PathOfTheDragonCovenantPoints = 19
    """ how many dragon scales have been offered to the Stone Dragon """
    GravelordServantCovenantPoints = 20
    """ how many eyes of death have been offered to Nito """
    ForestHunterCovenantPoints = 21
    """ how many forest intruders have been defeated """
    DarkmoonBladeCovenantPoints = 22
    """ how many souvenirs of reprisal have been offered to Gwyndolin"""
    ChaosServantCovenantPoints = 23
    """ how many humanity have been offered to the Fair Lady"""
    WarriorOfSunlightCovenantLevel = 24
    """ the covenant level that corresponds to WarriorOfSunlightCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    DarkwraithCovenantLevel = 25
    """ the covenant level that corresponds to DarkwraithCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    PathOfTheDragonCovenantLevel = 26
    """ the covenant level that corresponds to PathOfTheDragonCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    GravelordServantCovenantLevel = 27
    """ the covenant level that corresponds to GravelordServantCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    ForestHunterCovenantLevel = 28
    """ the covenant level that corresponds to ForestHunterCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    DarkmoonBladeCovenantLevel = 29
    """ the covenant level that corresponds to DarkmoonBladeCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    ChaosServantCovenantLevel = 30
    """ the covenant level that corresponds to ChaosServantCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    ReturnResultofHardcodedEventFlag = 31
