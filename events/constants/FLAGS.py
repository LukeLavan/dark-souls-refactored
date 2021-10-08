from soulstruct.game_types import Flag


class FLAGS(Flag):

    CanLearnShrug = 280
    """ enabled by default, disabled when Petrus teaches Shrug """

    CanLearnLookSkyward = 281
    """ enabled by default, disabled when Shiva teaches Look SKyward """

    CanLearnHurrah = 282
    """ enabled by default, disabled when Andre teaches Hurrah! """

    CanLearnWellWhatIsIt = 283
    """ enabled by default, disabled when Oswald teaches Well! What is it? """

    CanLearnProperBow = 284
    """ enabled by default, disabled when Dusk teaches Proper Bow """

    CanLearnProstration = 285
    """ enabled by default, disabled when Patches teaches Prostration """

    CanLearnPraiseTheSun = 286
    """ enabled by default, disabled when player learns Praise the Sun """

    CanLearnPrayer = 287
    """ enabled once on first load, disabled if the player class is knight or cleric\n
    becomes disabled once Rhea teaches Prayer\n
    (these classes have this gesture available by default) """

    CanLearnJoy = 288
    """ enabled once on first load, disabled if player class isn't knight or cleric\n
    becomes disabled once Domhnall teaches Joy\n
    (the other classes have this gesture available by default) """

    # flags 289 and 290 are always on and both unused
    # they're enabled in the same event that handles the gesture flags above

    CanOfferLordSouls = 702
    """ Enabled when the player is in the Kiln map and hasn't yet offered all four lord souls.\n
    For some reason, this flag is kept disabled when the player leaves the Kiln map.\n
    Disabled when the player offers all four lord souls to the Lordvessel. """

    HasWarpedToFirelinkShrine = 11810000
    """ enabled after the two cutscenes play that warp the player
    from the asylum to Firelink """

    HasOfferedAllLordSouls = 11800210
    """ enabled after all four lord souls have been offered to the lordvessel
    and the door to the kin has been opened """
