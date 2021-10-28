from soulstruct.game_types import Flag


class FLAGS(Flag):

    ObtainedWeaponsmithBox = 250
    """ enabled when the player obtains a Weaponsmith Box\n
    used to determine if bonfires should show the 'Reinforce Weapon' option """

    ObtainedArmorsmithBox = 251
    """ enabled when the player obtains an Armorsmith Box\n
    used to determine if bonfires should show the 'Reinforce Armor' option """

    ObtainedRepairbox = 252
    """ enabled when the player obtains a Repairbox\n
    used to determine if bonfires should show the 'Repair Equipment' option """

    ObtainedRiteOfKindling = 257
    """ enabled when the player obtains the Rite of Kindling\n
    used to determine if bonfires should allow kindling beyond the normal limit """

    ObtainedBottomlessBox = 258
    """ enabled when the player obtains the Bottomless Box\n
    used to determine if bonfires should show the 'Access Bottomless Box' option """

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

    HasGivenLargeEmber = 350
    """ enabled when the user selects 'YES' when Andre asks for the Large Ember """
    HasGivenVeryLargeEmber = 351
    """ enabled when the user selects 'YES' when Andre asks for the Very Large Ember """
    HasGivenCrystalEmber = 352
    """ enabled when the user selects 'YES' when the Giant Blacksmith asks for the Crystal Ember """
    HasGivenLargeMagicEmber = 356
    """ enabled when the user selects 'YES' when Rickert asks for the Large Magic Ember """
    HasGivenEnchantedEmber = 357
    """ enabled when the user selects 'YES' when Rickert asks for the Enchanted Ember """
    HasGivenDivineEmber = 358
    """ enabled when the user selects 'YES' when Andre asks for the Divine Ember """
    HasGivenLargeDivineEmber = 359
    """ enabled when the user selects 'YES' when Andre asks for the Large Divine Ember """
    HasGivenDarkEmber = 360
    """ enabled when the user selects 'YES' when Andre asks for the Dark Ember """
    HasGivenLargeFlameEmber = 362
    """ enabled when the user selects 'YES' when Vamos asks for the Large Flame Ember """
    HasGivenChaosFlameEmber = 363
    """ enabled when the user selects 'YES' when Vamos asks for the Chaos Flame Ember """


    CanOfferLordSouls = 702
    """ enabled when the player is in the Kiln map and hasn't yet offered all four lord souls\n
    for some reason, this flag is kept disabled when the player leaves the Kiln map\n
    disabled when the player offers all four lord souls to the Lordvessel. """

    WarpAllowed = 706
    """ enabled by default; disabled when the player should not be able to warp \n
    specifically, this is enabled when the player is in the Duke's Archives prison cell
    or when they're in the Painted World map\n
    disabled when the above conditions are no longer met\n
    if the player selects the 'Warp' option from a bonfire dialog menu and this flag is disabled,
    the 'Cannot warp' message is displayed """

    GotLordvessel = 710
    """ enabled when the player obtains the Lordvessel """

    CanOfferGwynSoul = 715
    """ enabled when the player is able to offer Gwyn's soul to obtain Sunlight Spear\n
    more specifically, the flag is enabled when: the player has Gwyn's soul, does not already
    have Sunlight Spear, is in the Warriors of Sunlight covenant, and has the Great Lightning Spear
    miracle\n
    note that the Great Lightning Spear is only obtainable by reaching rank 1 of the covenant\n
    disabled by default and when the trade can no longer be made\n
    specifically, it's disabled when the player no longer has Gwyn's soul, if the player\n
    has the sunlight spear miracle already, or if the player is no longer in the covenant """

    ObtainedEstusFlask2 = 716
    """ enabled whenever ObtainedEstusFlask (50000082) is enabled """

    StandingInAbyssWithoutLordvessel = 717
    """ enabled when the player is standing in the abyss and hasn't obtained the Lordvessel\n
    more specifically, the player needs to be in the New Londo map and standing on the collision 
    that is the floor of the Abyss before obtaining the Lordvessel\n
    if enabled, bonfires will have a 'Warp' option; if this flag is forced on when the player does
    have Lordvessel warping, bonfires will have two 'Warp' options\n
    TODO: check if every bonfire has this Abyss warping option (seems so) """

    CanAttuneSpells = 719
    """ enabled when the player obtains any spell (sorcery, pyromancy, or miracle)\n
    when enabled, bonfires will show the 'Attune Magic' option"""

    HasTitaniteShard = 780
    """ enabled when the player has at least one titanite shard; disabled otherwise\n
    not used for anything """
    HasLargeTitaniteShard = 781
    """ enabled when the player has at least one large titanite shard; disabled otherwise\n
    used to determine if Frampt can break down a large titanite shard """
    HasGreenTitaniteShard = 782
    """ enabled when the player has at least one green titanite shard; disabled otherwise\n
    used to determine if Frampt can break down a green titanite shard """
    HasTitaniteChunk = 783
    """ enabled when the player has at least one titanite chunk; disabled otherwise\n
    used to determine if Frampt can break down a titanite chunk """
    HasBlueTitaniteChunk = 784
    """ enabled when the player has at least one blue titanite chunk; disabled otherwise\n
    used to determine if Frampt can break down a blue titanite chunk """
    HasWhiteTitaniteChunk = 785
    """ enabled when the player has at least one white titanite chunk; disabled otherwise\n
    used to determine if Frampt can break down a white titanite chunk """
    HasRedTitaniteChunk = 786
    """ enabled when the player has at least one red titanite chunk; disabled otherwise\n
    used to determine if Frampt can break down a red titanite chunk """
    HasTitaniteSlab = 787
    """ enabled when the player has at least one titanite slab; disabled otherwise\n
    used to determine if Frampt can break down a titanite slab """
    HasBlueTitaniteSlab = 788
    """ enabled when the player has at least one blue titanite slab; disabled otherwise\n
    used to determine if Frampt can break down a blue titanite slab """
    HasWhiteTitaniteSlab = 789
    """ enabled when the player has at least one white titanite slab; disabled otherwise\n
    used to determine if Frampt can break down a white titanite slab """
    HasRedTitaniteSlab = 790
    """ enabled when the player has at least one red titanite slab; disabled otherwise\n
    used to determine if Frampt can break down a red titanite slab """
    HasDragonScale = 791
    """ enabled when the player has at least one dragon scale; disabled otherwise\n
    not used for anything """
    HasDemonTitanite = 792
    """ enabled when the player has at least one demon titanite; disabled otherwise\n
    not used for anything """
    HasTwinklingTitanite = 793
    """ enabled when the player has at least one twinkling titanite; disabled otherwise\n
    not used for anything """

    TakenByAbyss = 8120
    """ enabled when the player gets taken by the abyss, \n
    disabled on next load when the message is displayed to the player """

    ObtainedEstusFlaskPlus1 = 8131
    """ enabled when the player obtains the Estus Flask +1 (full or empty) """
    ObtainedEstusFlaskPlus2 = 8132
    """ enabled when the player obtains the Estus Flask +2 (full or empty) """
    ObtainedEstusFlaskPlus3 = 8133
    """ enabled when the player obtains the Estus Flask +3 (full or empty) """
    ObtainedEstusFlaskPlus4 = 8134
    """ enabled when the player obtains the Estus Flask +4 (full or empty) """
    ObtainedEstusFlaskPlus5 = 8135
    """ enabled when the player obtains the Estus Flask +5 (full or empty) """
    ObtainedEstusFlaskPlus6 = 8136
    """ enabled when the player obtains the Estus Flask +6 (full or empty) """
    ObtainedEstusFlaskPlus7 = 8137
    """ enabled when the player obtains the Estus Flask +7 (full or empty) """

    GotMiracleGreatLightningSpear = 11010595
    """ enabled when the player gets the Great Lightning Spear miracle """

    ObtainedRepairBoxUndeadMerchant = 11017040
    """ enabled when the player buys the repair box from the male undead merchant\n
    also enabled when the repair box is bought from Andre via an event (819 from common) """

    ObtainedRepairBoxAndre = 11017170
    """ enabled when the player buys the repair box from Andre\n
    also enabled when the repair box is bought from the male undead merchant via an event (819 from common) """

    LaurentiusInterestedInSpectacularPyromancy = 11020102
    """ enabled when the player has a pyromancy that Laurentius will find spectacular and will ask about\n
    more specifically, those pyromancies are: Great Fireball, Firestorm, Fire Tempest, Fire Whip,
    Great Combustion, Great Chaos Fireball, Chaos Storm, and Chaos Fire Whip """

    IsInDukesArchivesPrisonCell = 11705170
    """ enabled when the player is inside the prison cell at the Duke's Archives that they
    may not warp from\n
    disabled when the player exits the prison cell (or gets far enough away from the bonfire) \n
    the event that controls this flag restarts itself, so the flag will continue to toggle as you 
    leave and re-enter the region\n
    this flag is a temporary 5XXX flag, so it resets on every map load """

    HasWarpedToFirelinkShrine = 11810000
    """ enabled after the two cutscenes play that warp the player
    from the asylum to Firelink """

    HasOfferedAllLordSouls = 11800210
    """ enabled after all four lord souls have been offered to the lordvessel
    and the door to the kin has been opened """

    EstusFlaskObtained = 50000082
    """ enabled when the item lot that awards the Estus Flask is rolled\n
    also enabled on loading the Asylum for the first time in NG+ and above """
