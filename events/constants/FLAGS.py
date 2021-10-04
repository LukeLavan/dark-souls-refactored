from soulstruct.game_types import Flag

class FLAGS(Flag):

    # enabled by default, disabled when Petrus teaches Shrug
    CanLearnShrug = 280

    # enabled by default, disabled when Shiva teaches Look SKyward
    CanLearnLookSkyward = 281

    # enabled by default, disabled when Andre teaches Hurrah!
    CanLearnHurrah = 282

    # enabled by default, disabled when Oswald teaches Well! What is it?
    CanLearnWellWhatIsIt = 283

    # enabled by default, disabled when Dusk teaches Proper Bow
    CanLearnProperBow = 284

    # enabled by default, disabled when Patches teaches Prostration
    CanLearnProstration = 285

    # enabled by default, disabled when player learns Praise the Sun
    CanLearnPraiseTheSun = 286

    # enabled once on first load, becomes disabled if the player class is knight or cleric
    # only used to determine if Rhea can teach you Prayer gesture
    # also disabled if Rhea teaches Prayer
    # (these classes have this gesture available by default)
    CanLearnPrayer = 287

    # enabled once on first load, becomes disabled if player class isn't knight or cleric
    # only used to determine if Domhnall can teach you Joy gesture
    # also disabled if Domhnall teaches Joy
    # (the other classes have this gesture available by default)
    CanLearnJoy = 288

    # flags 289 and 290 are always on and both unused
    # they're enabled in the same event that handles the gesture flags above
