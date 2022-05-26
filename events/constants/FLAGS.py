from soulstruct.game_types import Flag

class FLAGS(Flag):

    KilledGapingDragon = 2
    """ enabled when the gaping dragon boss dies """

    KilledBellGargoyles = 3
    """ enabled when both bell gargoyle bosses die """

    KilledPriscilla = 4
    """ enabled when priscilla dies """

    KilledSif = 5
    """ enabled when sif dies """

    KilledPinwheel = 6
    """ enabled when the pinwheel boss dies """

    KilledNito = 7
    """ enabled when Nito dies """

    KilledQuelaag = 9
    """ enabled when Quelaag dies """

    KilledBedOfChaos = 10
    """ enabled when bed of chaos dies """

    KilledIronGolem = 11
    """ enabled when iron golem dies """

    KilledOandS = 12
    """ enabled when O & S die (either order) """

    KilledFourKings = 13
    """ enabled when the four kings fight is over """

    KilledSeath = 14
    """ enabled when seath dies """

    KilledGwyn = 15
    """ enabled when gwyn dies """

    KilledAsylumDemon = 16
    """ enabled when asylum demon dies """

    KilledManus = 17
    """ enabled when manus dies """

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

    RheaBossCount = 600
    """ a 4-bit number used to keep track of how many bosses have been killed since 
    Rhea moved to the Parish\n
    see flags 1-16 for which bosses count, since not all do """

    RheaBossCountBit1 = 601
    RheaBossCountBit2 = 602
    RheaBossCountBit3 = 603

    CanOfferLordSouls = 702
    """ enabled when the player is in the Kiln map and hasn't yet offered all four lord souls\n
    for some reason, this flag is kept disabled when the player leaves the Kiln map\n
    disabled when the player offers all four lord souls to the Lordvessel. """

    NGPlusOrBeyond = 705
    """ enabled at the beginning of a cycle that's in NG+ or beyond\n
    if disabled, the game is still in NG; if enabled, the game is in NG+ or beyond """

    WarpAllowed = 706
    """ enabled by default; disabled when the player should not be able to warp \n
    specifically, this is enabled when the player is in the Duke's Archives prison cell
    or when they're in the Painted World map\n
    disabled when the above conditions are no longer met\n
    if the player selects the 'Warp' option from a bonfire dialog menu and this flag is disabled,
    the 'Cannot warp' message is displayed """

    ObtainedLordvessel = 710
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

    LoganPurchasedAllSpellsFirelink = 721
    """ enabled when the player purchased all of Logans spells that are available at Firelink """

    QuelanaDone = 722
    """ enabled when all of Quelana's pyromancies have been purchased, 
    the Bed of Chaos is dead, and teh ascended Pyro glove+5 has been obtained 
    (ie, there's nothing left that Quelana can do for you, and she leaves permanently) """

    GriggsDone = 723
    """ enabled when all of Grigg's spells and rings are purchased, triggering him
    to go hollow and move to sen's fortress """

    RheaPurchasedAll = 724
    """ enabled when all of Rhea's miracles and her divine blessing are purchased """

    LoganPurchasedAllSpellsArchives = 728
    """ enabled when the player purchases all of Logan's spells, including the three exclusive to the Archives"""

    PlayerIsPyromancerClass = 740
    """ used for Laurentius dialog """

    CovenantHardBetrayal = 742
    """ enabled when a covenant is hard-betrayed; namely:\n
        - forest hunters: TODO: flag 11205051 in m12_00 and event 11400504 in m14_00\n
        - chaos servants: killing fair lady while in covenant\n
        - darkmoon blade: challenging Gwyndolin while in covenant\n
        - princess guard: destroying Gwynevere illusion while in covenant\n
    disabled on absolution """

    GwyndolinAngry = 743
    """ enabled when killing Gwynevere or entering Gwyndolin's boss fog\n
    when enabled, Gwyndolin's 'Kneel' prompt will not appear\n
    disabled on absolution, but does not count towards having sin
    (another valid sin must be active to receive absolution) """

    HasPvESin = 744
    """ enabled if the player has PvE sin (excluding covenant hard betrayals), meaning an NPC has been aggro'd\n
    see common event 772 for full list of triggers\n
    disabled on absolution """

    ShivaOrBodyguardDead = 745
    """ enabled when either Shiva or his bodyguard dies\n
    causes a hard betrayal of the Forest Hunters covenant\n
    disabled on absolution """

    ForestHuntersBetrayed = 746
    """ TODO: investigate Event11205056 in m12_00 for exact triggers\n
    disabled on absolution """

    EggHeadActive = 753
    """ enabled when the player has egg head status active (ie, 50% soul gain multiplier, can't 
    equip helmet, visuals), fully grown or not"""

    BreakCurse = 754
    """ when enabled, the player has their curse broken and the flag is automatically disabled\n
    enabled when Ingward breaks your curse - purging stones do not use this """

    ReceiveAbsolution = 755
    """ enabled when oswald grants absolution after giving soul level * 500 souls\n
    when enabled, the absolution event re-disables this flag and disables a whole bunch
    of other flags - see event 770 in common """

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

    InNoCovenant = 850
    """ enabled when the player is in no covenant; disabled otherwise\n
    not used for anything """
    InWayOfWhiteCovenant = 851
    """ enabled when the player is in Way of White covenant; disabled otherwise\n
    not used for anything """
    InPrincessGuardCovenant = 852
    """ enabled when the player is in Princess Guard covenant; disabled otherwise\n
    not used for anything """
    InWarriorOfSunlightCovenant = 853
    """ enabled when the player is in Warrior of Sunlight covenant; disabled otherwise\n
    used to determine if the player can interact with Altar of Sunlight, bypassing normal requirements """
    InDarkwraithCovenant = 854
    """ enabled when the player is in Darkwraith covenant; disabled otherwise\n
    used to determine if the player may ask for covenant item from and offer humanity to Kaathe """
    InPathOfTheDragonCovenant = 855
    """ enabled when the player is in Path of the Dragon covenant; disabled otherwise\n
    used to determine if the player may offer dragon scales to the stone dragon """
    InGravelordServantCovenant = 856
    """ enabled when the player is in Gravelord covenant; disabled otherwise\n
    used to determine if the player may offer eyes of death to Nito """
    InForestHunterCovenant = 857
    """ enabled when the player is in Forest Hunter covenant; disabled otherwise\n
    not used for anything """
    InDarkmoonBladeCovenant = 858
    """ enabled when the player is in Darkmoon Blade covenant; disabled otherwise\n
    used to determine if the player may offer souvenirs of reprisal to Gwyndolin """
    InChaosServantCovenant = 859
    """ enabled when the player is in Chaos Servant covenant; disabled otherwise\n
    used to determine if the player may offer humanity to the Fair Lady """

    # NPC QUESTLINES

    SolaireHostile = 1004

    DarkmoonKnightessHostile = 1033

    LoganHostile = 1096

    GriggsHostile = 1114

    RheaParish = 1175
    """ when enabled, Rhea will appear at the Parish """

    RheaHostileFisticuffs = 1176
    """ if Rhea is made hostile before Vince and Niko are killed in ToTG
    then Rhea will fight the player with her fists """

    RheaHostileNothing = 1179
    """ if Rhea is made hostile after Vince and Niko are killed in ToTG
    then Rhea will just stand around and do nothing """

    PetrusHostileGuilty = 1195
    """" if Petrus is made hostile after buying Lautrec's tip, this is the hostility flag enabled\n
    specifically, his quest state needs to be at 1194 TODO: Petrus questline """

    PetrusHostileInnocent = 1197
    """ if Petrus is made hostile at any other point than after buying Lautrec's tip, this is the
    hostility flag enabled """

    VinceHostile = 1213

    NicoHostile = 1223

    GwyndolinHostile = 1241
    GwyndolinDead = 1242

    LaurentiusHostile = 1253

    FairLadyDead = 1272

    EingyiHostileFairLady = 1282
    """ enabled when the fair lady is dead, driving Eingyi to attack """
    EingyiHostileAttackedUnproven = 1283
    """ enabled when Eingyi aggros normally, ie attacking him to < 90% HP,
    except if the player has egg head Eingyi is not blocking the path to the bonfire """

    EingyiHostileAttackedProven = 1287
    """ enabled when Eingyi aggros normally while the player has egg head and 
    Eingyi is in his spot next to the bonfire\n
    TODO: specifically, when Eingyi is in quest state 1286 - do more thorough testing to
    find all conditions """

    QuelanaHostile = 1294

    IngwardHostile = 1314
    IngwardDead = 1315
    """ enabled when Ingward's health is <= 0 """

    AndreHostile = 1321
    AndreDead = 1322
    """ enabled when Andre's health is <= 0 """

    VamosHostile = 1341

    GiantBlacksmithHostile = 1361

    RickertHostile = 1381
    RickertDead = 1382

    MaleUndeadMerchantHostile = 1401
    MaleUndeadMerchantDead = 1402
    """ enabled when the male undead merchant's health is <= 0 """

    FemaleUndeadMerchantHostile = 1411
    """ not enabled until she makes it to her flee point behind the bars """

    CrestfallenMerchantHostile = 1421
    CrestfallenMerchantDead = 1422

    DomhnallHostile = 1434

    CrestfallenWarriorHostile = 1461

    SiegmeyerStart = 1490
    """ enabled by default, becomes disabled when Siegmeyer's quest progresses in some way """

    SiegmeyerInSensAlreadyMet = 1491
    """ enabled when the Sen's Fortress gate opens and Siegmeyer's first conversation has been exhausted\n
    players do not need to interact with him here for him to move to Anor Londo """

    SiegmeyerInSensNotMet = 1492
    """ enabled when the Sen's Fortress gate opens and Siegmeyer's first conversation has not been exhausted\n
    players need to interact with him here for him to move to Anor Londo """

    SiegmeyerAnorLondo = 1493
    """ enabled when Siegmeyer should appear at Anor Londo """

    SiegmeyerAnorLondoRescued = 1494
    """ enabled when the three silver knights past Siegward are slain, but only
    if Siegward is there to witness it (ie, 1493 is enabled and 1512 is disabled) """

    SiegmeyerFirelink = 1497
    """ enabled when Siegmeyer appears at Firelink (1494 is enabled and the tiny being's 
    ring has been awarded) """

    SiegmeyerBlighttown = 1501
    """" enabled when the player enters the Blighttown map after exhausting Siegmeyer's Firelink dialog\n
    when enabled, Siegmeyer appears in his Blighttown spot asking for purple moss clumps """

    SiegmeyerTravelToLostIzalith = 1502
    """ enabled when the pierce shield is awarded for giving Siegmeyer purple moss clumps\n
    when enabled, Siegmeyer will appear in his Lost Izalith spot """

    SiegmeyerAtLostIzalth = 1503
    """ enabled when the player enters the Lost Izalth map while 1502 is enabled\n
    when enabled, Siegmeyer appears in his Lost Izalth spot """

    SiegmeyerBattle = 1504
    """" enabled when the player finishes Siegmeyer's dialog and he charges into battle """

    SiegmeyerNoBattle = 1505
    """ enabled when the four chaos eaters die before Siegmeyer charges into battle """

    SiegmeyerLostBattle = 1506
    """ enabled when the four chaos eaters die and Siegmeyer has < 50% HP """

    SiegmeyerWonBattle = 1507
    """ enabled when the four chaos eaters die and Siegmeyer has >= 50% HP """

    SiegmeyerAshLake = 1511
    """ enabled after exhausting Siegmeyer's dialog after the battle is won (<= 50% HP) and\n
    Sieglinde's Firelink return dialog has been exhausted (see SieglindeFirelinkReturnDialogExhausted)\n
    used to determine if Siegmeyer and Sieglinde should spawn at Ash Lake for their final scene """

    SiegmeyerHostile = 1512
    """ enabled when Siegmeyer becomes hostile to the player """

    SiegmeyerDead = 1513
    """ enabled when Siegmeyer dies prematurely """

    SiegmeyerDone = 1514
    """ enabled after exhausting Siegmeyer's dialog after avoiding the Lost Izalth battle or\n
    after Ash Lake scene with Sieglinde TODO: better details """

    SieglindeStart = 1540
    SieglindeGolemSpawned = 1541
    """ enabled when the gold crystal golem carrying Sieglinde is enabled\n
    the conditions for this happening are as follows:\n
        Sieglinde has not been made hostile (impossible anyway)\n
        SieglindeStart is enabled (true by default)\n
        SiegmeyerHostile and SiegmeyerDead are disabled\n
        at least one flag in the range 1501-1511 is enabled, meaning
        siegmeyer's quest has been progressed to at least the point where
        Siegmeyer spawns at Blighttown (has left Firelink) and the player has not finished his 
        dialog after killing the chaos eaters before Siegmeyer charges against them
        nor has Siegmeyer died at Lost Izalth (or otherwise);
        if Siegmeyer's battle ends and he has less than 50% HP, Sieglinde can still spawn
        by not allowing Siegmeyer's dialog to complete\n
        the Duke's Archives map has been loaded so that the relevant event is running
        while all of the above conditions are true
    once enabled, the golem will continue to spawn until Sieglinde's quest is progressed
    (ie, the golem is killed) regardless of the initial spawn requirements """

    SieglindeGolemKilled = 1542
    """ enabled when the gold crystal golem carrying Sieglinde dies """

    SieglindeFirelink = 1543
    """ enabled when Firelink loads after exhausting Sieglinde's dialog at the Archives
    (Sieglinde is enabled at Firelink) """

    SieglindeFirelinkDone = 1544
    """ enabled when Firelink is loaded after exhausting Sieglinde's Firelink dialog regardless
    of the player's answer to her question """

    SieglindeFirelinkReturn = 1545
    """ enabled when 1544 is enabled and SiegmeyerLiveAfterIzalithBattle is enabled """

    SieglindeAshLake = 1546
    """ enabled when Ash Lake loads, SieglindeFirelinkReturn is enabled, SiegmeyerAshLake is
    enabled, and SieglindeFirelinkReturnDialogExhausted is enabled """

    SieglindeHostile = 1547
    SieglindeDead = 1548
    SieglindeDone = 1549
    """ enabled when Sieglinde has awarded the player with the Titanite Slab and the player gets
    far enough away to unload Sieglinde """

    LautrecHostile = 1574
    """ enabled when making Lautrec hostile at the Parish or at Firelink """

    ShivaHostile = 1603
    ShivaDead = 1604

    PatchesHostile = 1627

    FramptHostile = 1646
    """ unrelated to Frampt being mad and going away forever - unused hostility flag that's never
    enabled and redundantly disabled on absolution """

    KaatheHostile = 1675
    """ unrelated to Kaathe being mad and going away forever - unused hostility flag that's never
    enabled and redundantly disabled on absolution """

    PriscillaHostile = 1691

    AlvinaStart = 1710
    AlvinaGone = 1711
    """ enabled when Alvina is attacked or after Alvina berates you and disappears for
    betraying the forest hunters """
    AlvinaBetrayed = 1712
    """ enabled when the forest hunters are betrayed """

    ShivaBodyguardHostile = 1763
    ShivaBodyguardDead = 1764

    GoughHostile = 1822

    ChesterHostile = 1841

    CiaranHostile = 1863

    ElizabethHostile = 1871
    """ Elizabeth will never turn hostile, and so this flag is never enabled;
    disabled on absolution """

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

    PreventLordvesselRiteOfKindlingPopup = 9121
    """ enabled when m12_01 (DLC) is loaded by approaching the spot in the basin where the portal appears\n
    if enabled, three status messages will not appear:\n
        - 'In Lordran, level up and kindle at bonfires' upon entering Firelink for the first time\n
        - 'By the Rite of Kindling, you may now kindle beyond the normal limit' upon obtaining the Rite of Kindling\n
        - 'By the power of the Lordvessel, you may now warp between bonfires' upon obtaining the Lordvessel\n
    disabled if, on a subsequent load of the DLC map, any of the flags that control displaying
    these statuses is enabled. however, this flag is immediately re-enabled anyway, so it effectively stays on permanently\n
    interestingly, this means that approaching the spot where the portal is/will be prior to obtaining the
    Lordvessel or Rite of Kindling will prevent those statuses from displaying as normal\n
    TODO: why is this like this??? what's the point??? """


    GivePurgingStoneSiegmeyer = 11000591
    """ when enabled, give the player a purging stone\n
    ununused, seemingly intended for siegmeyer in the depths """

    GiveWhiteSignSoapstone = 11010591
    """ when enabled, give the player the white sign soapstone\n
    enabled when talking to solaire and answering yes to both questions """
    
    GiveLightningSpear = 11010594
    """ when enabled, give the player the lightning spear miracle\n
    used by the sunlight altar when entering covenant\n
    TODO: also used a lot in bonfires - investigate esp and return here """

    GiveGreatLightningSpear = 11010595
    """ when enabled, give the player the great lightning spear miracle\n
    enabled when reaching rank 1 of sunbro covenant """

    GiveSunlightSpear = 11010598
    """ when enabled, give the player the sunligh spear miracle\n
    enabled when gwyn's soul is traded in at the sunlight altar """

    KilledTaurusDemon = 11010901
    """ enabled when the Taurus Demon boss dies """

    KilledCapraDemon = 11010902
    """ enabled when the Capra Demon boss dies """

    GiveWarriorOfSunlightTrinket = 11010905
    """ when enabled, give the player the warrior of sunlight trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    ObtainedOrangeSignSoapstone = 11017020
    """ enabled when the player buys the orange sign soapstone from the male undead merchant\n
    also enabled when the orange sign soapstone is awarded after the male undead merchant dies """

    ObtainedResidenceKey = 11017030
    """ enabled when the player buys the residence key from the male undead merchant\n
    also enabled when the residence key is awarded after the male undead merchant dies """

    ObtainedRepairBoxUndeadMerchant = 11017040
    """ enabled when the player buys the repair box from the male undead merchant\n
    also enabled when the repair box is bought from Andre via an event (819 from common) """

    PurchasedRheaDivineBlessing = 11017050
    """ enabled when Rhea's Divine Blessing is purchased """
    PurchasedRheaHeal = 11017060
    """ enabled when Rhea's Heal is purchased """
    PurchasedRheaGreatHealExcerpt = 11017070
    """ enabled when Rhea's Great Heal Excerpt is purchased """
    PurchasedRheaHomeward = 11017080
    """ enabled when Rhea's Homeward is purchased """
    PurchasedRheaForce = 11017090
    """ enabled when Rhea's Force is purchased """
    PurchasedRheaGreatHeal = 11017100
    """ enabled when Rhea's Great Heal is purchased """
    PurchasedRheaWrathoftheGods = 11017110
    """ enabled when Rhea's Wrath of the Gods is purchased """
    PurchasedRheaSeekGuidance = 11017120
    """ enabled when Rhea's Seek Guidance is purchased """
    PurchasedRheaMagicBarrier = 11017130
    """ enabled when Rhea's Magic Barrier is purchased """

    ObtainedCrestOfArtorias = 11017140
    """ enabled when the player buys the crest of artorias from andre\n
    (or after it's awarded if you murder andre, you monster) """

    ObtainedRepairBoxAndre = 11017170
    """ enabled when the player buys the repair box from Andre\n
    also enabled when the repair box is bought from the male undead merchant via an event (819 from common) """

    ObtainedDriedFinger = 11017210
    """ enabled when the player buys the dried finger from the male undead merchant\n
    also enabled when the dried finger is awarded after the male undead merchant dies """

    LaurentiusInterestedInSpectacularPyromancy = 11020102
    """ enabled when the player has a pyromancy that Laurentius will find spectacular and will ask about\n
    more specifically, those pyromancies are: Great Fireball, Firestorm, Fire Tempest, Fire Whip,
    Great Combustion, Great Chaos Fireball, Chaos Storm, and Chaos Fire Whip """

    GiveWayOfWhiteTrinket = 11020905
    """ when enabled, give the player the way of white trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    SiegmeyerFirelinkConversation = 11020592
    """ enabled when the player exhausts Siegmeyer's dialog at Firelink, regardless of the player's answer """

    GiveEmitForce = 11020594
    """ when enabled, the emit force miracle is awarded\n
    enabled when talking to siegmeyer at firelink and answering yes to his question """

    GiveSpeckledStoneplateRingUnused = 11020595
    """ when enabled, the speckled stoneplate ring is awarded\n
    unused, but seemingly intended for talking to siegmeyer at firelink """

    GiveCopperCoin = 11020599
    """ when enabled, give the player a copper coin\n
    used by Petrus, when you talk to him again """

    GivePyromancyFlameLaurentius = 11020602
    """ when enabled, give the player the pyromancy glove\n
    enabled when talking to Laurentius after answering his questions\n
    TODO: what if starting class is pyro? """

    SieglindeFirelinkDialogExhausted = 11020605
    """ enabled after exhausting Sieglinde's dialog at Firelink, regardless of player's answer """

    SieglindeFirelinkReturnDialogExhausted = 11020606
    """ enabled after exhausting Sieglinde's dialog at Firelink when she returns and
    tells you she found Siegmeyer """

    GiveSunlightMedal = 11020607
    """ when enabled, give the player a sunlight medal\n
    used by Lautrec, when you talk to him at Firelink after freeing him """

    PurchasedGriggsSoulArrow = 11027130
    """ enabled when Grigg's Soul Arrow is purchased """
    PurchasedGriggsGreatSoulArrow = 11027140
    """ enabled when Grigg's Great Soul Arrow is purchased """
    PurchasedGriggsHeavySoulArrow = 11027150
    """ enabled when Grigg's Heavy Soul Arrow is purchased """
    PurchasedGriggsGreatHeavySoulArrow = 11027160
    """ enabled when Grigg's Great Heavy Soul Arrow is purchased """
    PurchasedGriggsMagicWeapon = 11027170
    """ enabled when Grigg's Magic Weapon is purchased """
    PurchasedGriggsMagicShield = 11027180
    """ enabled when Grigg's Magic Shield is purchased """
    PurchasedGriggsAuralDecoy = 11027190
    """ enabled when Grigg's Aural Decoy is purchased """
    PurchasedGriggsFallControl = 11027200
    """ enabled when Grigg's Fall Control is purchased """
    PurchasedGriggsBellowingDragoncrestRing = 11027210
    """ enabled when Grigg's Bellowing Dragoncrest Ring is purchased """
    PurchasedGriggsLingeringDragoncrestRing = 11027220
    """ enabled when Grigg's Lingering Dragoncrest Ring is purchased """
    PurchasedGriggsHomingSoulmass = 11027230
    """ enabled when Grigg's Homing Soulmass is purchased """
    PurchasedGriggsSoulSpear = 11027240
    """ enabled when Grigg's Soul Spear is purchased """

    GiveCatCovenantRing = 11200592
    """ enabled while talking to Alvina, re-enabled for NG+ and beyond """
    GiveDivineBlessing = 11200593
    """ when enabled, give the player a divine blessing\n
    used by alvina, when you talk to her after killing a host as a forest hunter """
    GiveRingOfFog = 11200594
    """ when enabled, give the player a ring of fog\n
    used by alvina, when you talk to her after killing three hosts as a forest hunter """

    AlvinaDisappear = 11200596
    """ when enabled along with 1712 (forest hunters betrayed), alvina will disappear
    enabled when the player attacks Alvina """

    KilledMoonlightButterfly = 11200900
    """ enabled when the moonlight butterfly boss dies """

    GiveForestHunterTrinket = 11200905
    """ when enabled, give the player the forest hunter trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    KilledSanctuaryGuardian = 11210000
    """ enabled when the sanctuary guardian boss dies """

    KilledArtorias = 11210001
    """ enabled when artorias dies """

    KilledKalameet = 11210004
    """ enabled when kalameet dies """

    GiveTracersGift = 11210590
    """ when enabled, awards dark silver tracer and gold tracer\n
    enabled when giving artorias' soul to ciaran """

    GiveGoughsGreatbowGift = 11210593
    """ when enabled, awards gough's greatbow\n
    enabled when talking to gough when kalameet is dead """

    ObtainedCarvingHello = 11217010
    """ enabled when the "Hello" carving is purchased from Gough\n
    re-enabled on entering NG+ or beyond if the carving is owned already """

    ObtainedCarvingThankYou = 11217020
    """ enabled when the "Thank you" carving is purchased from Gough\n
    re-enabled on entering NG+ or beyond if the carving is owned already """

    ObtainedCarvingVeryGood = 11217030
    """ enabled when the player owns the "Very Good!" carving and the game is loaded in NG+ or beyond\n
    not actually used anywhere, since this carving is a drop """

    ObtainedCarvingImSorry = 11217040
    """ enabled when the player owns the "I'm sorry" carving and when the game is laoded in NG+ or beyond\n
    not actually used anywhere, since this carving is a drop """

    ObtainedCarvingHelpMe = 11217050
    """ enabled when the player owns the "Help me" carving and when the game is loaded in NG+ or beyond\b
    not actually used anywhere, since this carving is a treasure """

    GiveElizabethsMushroom3 = 50000520
    """ when enabled, awards three elizabeth's mushrooms\n
    enabled when talking to elizabeth when manus is dead """

    GiveSoulOfLostUndead = 11300590
    """ when enabled, soul of lost undead is awarded """

    GiveHumanity = 11300591
    """ when enabled, a humanity is awarded\n
    enabled when talking to patches after answering no to the cleric question and yes to the trickery question """

    GiveGravelordServantTrinket = 11300906
    """ when enabled, give the player the gravelord servant trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    GiveGravelordSwordDance = 11310580
    """ when enabled, the gravelord sword dance miracle is awarded\n
    enabled when joining the gravelord covenant """

    GiveReplenishment = 11310590
    """ when enabled, replenishment miracle is awarded\n
    enabled when talking to rhea after killing her friends """

    GiveGravelordSword = 11310592
    """ when enabled, the gravelord sword is awarded\n
    enabled when joining the gravelord covenant for the first time\n
    due to sequential itemlots, also awards the gravelord sword dance miracle """

    GiveGravelordGreatswordDance = 11310593
    """ when enabled, gravelord greatsword miracle is awarded\n
    enabled when reaching rank 1 of gravelord covenant """

    GiveTwinHumanities = 11310594
    """ when enabled, a twin humanities is awarded\n
    enabled when talking to patches after answering no to the cleric question and no to the forgiveness question in totg """

    GiveDragonEye = 11320581
    """ when enabled, the dragon eye is awarded\n
    enabled when joining the path of the dragon covenant\n
    due to sequential itemlots, also awards dragon head stone """

    GiveTitaniteSlab = 11320590
    """ when enabled, a titanite slab is awarded\n
    enabled when lalking to sieglinde at ash lake """

    GiveDragonHeadStone = 11320592
    """ when enabled, the dragon head stone is awarded\n
    enabled when joining the path of the dragon covenant"""

    GiveDragonTorsoStone = 11320593
    """ when enabled, the dragon torso stone is awarded\n
    enabled when reaching rank 2 of path of the dragon covenant """

    GiveDragonPathTrinket = 11320905
    """ when enabled, give the player the dragon path trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    GivePierceShield = 11400590
    """ when enabled, the pierce shield is awarded\n
    enabled when talking to siegmeyer in blighttown and giving up three purple mossclumps """

    GiveEggVermifuge = 11400591
    """ when enabled, an egg vermifuge is awarded\n
    enabled when talking to Eingyi with an egghead infection active, once per infection """

    GivePyromancyFlameEingyi = 11400592
    """ when enabled, a pyromancy glove is awarded
    enabled when talking to eingyi when egg'd and with 11 int """

    GiveFireTempest = 11400594
    """ when enabled, the fire tempest pyromancy is awarded\n
    enabled when talking to quelana when the bed of chaos is dead """

    GiveGreatChaosFireball = 11400596
    """ when enabled, the great chaos fireball pyromancy is awarded\n
    enabled when joining the chaos servant covenant """

    GiveChaosFireWhip = 11400597
    """ when enabled, the chaos fire whip pyromancy is awarded\n
    TODO: unused? investigate fair lady evs """

    GiveChaosStorm = 11400598
    """ when enabled, the chaos storm pyromancy is awarded\n
    enabled when reaching rank 2 of chaos servant covenant """

    GiveSoulHero = 11400599
    """ when enabled, a soul of a hero is awarded\n
    not used anywhere, but the id suggests that some NPC in the blighttown map 
    (fair lady or eingyi?) would have given this """

    GiveChaosServantTrinket = 11400905
    """ when enabled, give the player the chaos servant trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    PurchasedLaurentiusFireball = 11407030
    """ enabled when Laurentius's Fireball is purchased """
    PurchasedLaurentiusFireOrb = 11407040
    """ enabled when Laurentius's Fire Orb is purchased"""
    PurchasedLaurnentiusCombustion = 11407050
    """ enabled when Laurentius's Combustion is purchased """
    PurchasedLaurnentiusIronFlesh = 11407060
    """ enabled when Laurentius's Iron Flesh is purchased """
    PurchasedLaurnentiusFlashSweat = 11407070
    """ enabled when Laurentius's Flash Sweat is purhcased """

    ObtainedServantRoster = 11407080
    """ enabled when the player obtains the servant roster by buying it from Eingyi\n
    also enabled by itemlot 6160 (Eingyi's event ID) which awards servant roster, but this itemlot is not used """

    PurchasedQuelenaFireball = 11407120
    """ enabled when Quelana's Fireball is purchased """
    PurchasedQuelanaFireOrb = 11407130
    """ enabled when Quelana's Fire Orb is purchased """
    PurchasedQuelanaCombustion = 11407140
    """ enabled when Quelana's Combustion is purchased """
    PurchasedQuelanaGreatFireball = 11407150
    """ enabled when Quelana's Great Fireball is purchased """
    PurchasedQuelanaFirestorm = 11407160
    """ enabled when Quelana's Firestorm is purchased """
    PurchasedQuelanaFireWhip = 11407170
    """ enabled when Quelana's Fire Whip is purchased """
    PurchasedQuelanaGreatCombustion = 11407180
    """ enabled when Quelana's Great Combustion is purchased """
    PurchasedQuelanaUndeadRapport = 11407190
    """ enabled when Quelana's Undead Rapport is purchased """

    KilledDemonFiresage = 11410410
    """ enabled when demon firesage dies """

    SiegmeyerDieAfterIzalthBattle = 11410591
    """ enabled after Siegmeyer says goodbye to his dear little Lin and dies after
    his battle against the chaos eaters is over and he's left with less than 50% hp """

    SiegmeyerLiveAfterIzalithBattle = 11410593
    """ enabled after Siegmeyer finishes thanking the player for saving him after 
    his battle against the chaos eaters is over and he's left with more than or exactly 50% hp"""

    GiveSpeckledStoneplateRingIzalith = 11410594
    """ when enabled, the speckled stoneplate ring is awarded\n
    enabled when talking to siegmeyer after the chaos eaters are dead before siegmeyer joins the fight """

    KilledCeaselessDischarge = 11410900
    """ enabled when ceaseless discharge dies """

    KilledCentipedeDemon = 11410901
    """ enabled when centipede demon dies """

    SensFortressGateOpen = 11500200
    """ enabled when both Bells of Awakening have been rung\n
    used to determine whether the gate in front of Sen's Fortress should be opened, as well as
    many characters' dialog """

    SiegmeyerConversationDoneSensBoulder = 11500592
    """ enabled after the player finishes Siegmeyer's dialog about the boulder in Sen's Fortress\n
    once this flag is on, Siegmeyer will instead say his "Perhaps I could try some rolling..." dialog """

    SensBoulderLeverManuallyPushed = 11500850
    """ enabled when the lever controlling the boulder direction is pushed by the player for the first time """

    SiegmeyerConversationDoneSensGate = 11500591
    """ enabled after the player finishes Siegmeyer's first conversation, in front of Sen's Fortress\n
    once this flag is on, Siegmeyer will instead say his "Still closed..." dialog in front of Sen's """

    GwynevereKilled = 11510400
    """ enabled when Gwynevere is killed and Anor Londo is made dark """

    GiveDarkmoonBladeCovenantRing = 11510580
    """ when enabled, the darkmoon blade covenant ring is awarded\n
    enabled when joining the darkmoon blade covenant """

    GiveDarkmoonTalisman = 11510581
    """ when enabled, the darkmoon talisman is awarded\n
    enabled when reaching rank 1 of darkmoon blade covenant """

    GiveTinyBeingsRing = 11510590
    """ when enabled, the tiny beings ring is awarded\n
    enabled when talking to siegmeyer after defeating the three silver knights he's stuck in front of in anor londo """

    GiveLordvessel = 11510592
    """ when enabled, the lordvessel is awarded\n
    enabled when talking to gwynevere """

    GiveRingSunPrincess = 11510595
    """ when enabled, the ring of the sun princess is awarded\n
    enabled when joining the princess guard covenant """

    GiveBlueEyeOrb = 11510596
    """ when enabled, the blue eye orb and darkmoon blade covenant ring are awarded\n
    enabled when joining darkmoon blade covenant\n
    due to sequential itemlots, also awards darkmoon blade covenant ring """

    GiveDarkmoonBlade = 11510597
    """ when enabled, the darkmoon blade miracle is awarded\n
    enabled when reaching rank 1 of the darkmoon blade covenant\n
    due to sequential itemlots, also awards darkmoon talisman """

    KilledGwyndolin = 11510900
    """ enabled when gwyndolin dies """

    GivePrincessGuardTrinket = 11510905
    """ when enabled, give the player the princess guard trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    GiveBladeOfTheDarkmoonTrinket = 11510906
    """ when enabled, give the player the darkmoon blade trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    KilledGiantOrnstein = 11510902
    """ enabled when Giant Ornstein dies """

    KilledGiantSmough = 11510903

    GiveDarkSet = 11600580
    """ when enabled, all four pieces of the dark set are awarded
    if these pieces have not yet been acquired via covenant reward\n
    enabled when joining the darkwraith covenant """

    GiveDarkSetExceptMask = 11600581
    """ when enabled, the dark set minus the mask is awarded (armor and gauntlets and leggings)
    if these pieces have not yet been acquired via covenant reward\n
    enabled when joining the darkwraith covenant """

    GiveDarkGauntletsAndLeggings = 11600582
    """ when enabled, the bottom half of the dark set is awarded
    if these pieces have not yet been acquired via covenant reward\n
    enabled when joining the darkwraith covenant """

    GiveDarkLeggings = 11600583
    """ when enabled, only the dark leggings are awarded
    if this has not yet been acquired via covenant reward\n
    enabled when joining the darkwraith covenant """

    GiveKeyToSeal = 11600592
    """ when enabled, the key to the seal is awarded\n
    enabled when talking to Ingward while possessing the lordvessel """

    GiveDarkHand = 11600594
    """ when enabled, a dark hand is awarded\n
    enabled when joining the darkwraith covenant """

    GiveRedEyeOrb = 11600595
    """ when enabled, the red eye orb is awarded\n
    enabled when reaching rank 1 of the darkwraith covenant """

    GiveDarkSwordAndSet = 11600596
    """ when enabled, the dark sword and all four pieces of the dark set are awarded\n
    enabled when reaching rank 2 of the darkwraith covenant """

    GiveDarkwraithTrinket = 11600905
    """ when enabled, give the player the darkwraith trinket\n
    unused item, unused flag - although enabled if player enters ng+ or beyond with the trinket,
    suggesting you could have only gotten one per character """

    ObtainedBookOfTheGuilty = 11607020
    """ enabled when the book of the guilty is obtained, either by buying it from Oswald
    or from the item lot awarded when Oswald dies """

    GivePierceShieldUnused = 11700591
    """ when enabled, the pierce shield is awarded\n
    unused, but seemingly for sieglinde in duke's archives """

    SieglindeDukesConversationOver = 11700593
    """ enabled when Sieglinde's dialog is exhausted, regardless of the player's answer to her question """

    IsInDukesArchivesPrisonCell = 11705170
    """ enabled when the player is inside the prison cell at the Duke's Archives that they
    may not warp from\n
    disabled when the player exits the prison cell (or gets far enough away from the bonfire) \n
    the event that controls this flag restarts itself, so the flag will continue to toggle as you 
    leave and re-enter the region\n
    this flag is a temporary 5XXX flag, so it resets on every map load """

    HasPurchasedLoganSoulArrow = 11707000
    """ enabled when Logan's Soul Arrow is purchased """
    HasPurchasedLoganGreatSoulArrow = 11707010
    """ enabled when Logan's Great Soul Arrow is purchased """
    HasPurchasedLoganHeavySoulArrow = 11707020
    """ enabled when Logan's Heavy Soul Arrow is purchased """
    HasPurchasedLoganGreatHeavySoulArrow = 11707030
    """ enabled when Logan's Great Heavy Soul Arrow is purchased """
    HasPurchasedLoganMagicWeapon = 11707040
    """ enabled when Logan's Magic Weapon is purchased """
    HasPurchasedLoganMagicShield = 11707050
    """ enabled when Logan's Magic Shield is purchased """
    HasPurchasedLoganHomingSoulmass = 11707060
    """ enabled when Logan's Homing Soulmass is purchased """
    HasPurchasedLoganSoulSpear = 11707070
    # 11707080 skipped
    HasPurchasedLoganCrystalHomingSoulmass = 11707090
    """ enabled when Logan's Crystal Homing Soulmass is purchased """
    HasPurchasedLoganCrystalSoulSpear = 11707100
    """ enabled when Logan's Crystal Soul Spear is purchased """
    HasPurchasedLoganCrystalMagicWeapon = 11707110
    """ enabled when Logan's Crystal Magic Weapon is purchased """

    HasOfferedAllLordSouls = 11800210
    """ enabled after all four lord souls have been offered to the lordvessel
    and the door to the kin has been opened """

    HasWarpedToFirelinkShrine = 11810000
    """ enabled after the two cutscenes play that warp the player
    from the asylum to Firelink """

    GiveEstusFlask = 11810590
    """ when enabled, the estus flask+0 is awarded with 5 charges\n
    enabled when oscar gives you the estus flask"""

    GiveBigPilgrimsKeyOscar = 11810591
    """ when enabled, the big pilgrim's key is awarded\n
    enabled when oscar gives you the big pilgrim's key """

    KilledStrayDemon = 11810900
    """ enabled when stray demon dies """

    # ITEM LOT FLAGS

    ObtainedWhiteSignSoapstone = 50000000

    ObtainedTinyBeingsRingFromSiegmeyer = 50000010

    ObtainedPierceShieldUnused = 50000020

    ObtainedPurgingStoneFromSiegmeyer = 50000030

    ObtainedPierceShield = 50000040
    
    ObtainedEmitForceFromSiegmeyer = 50000060

    ObtainedSpeckledStoneplateRingFromSiegmeyer = 50000070

    ObtainedUndeadAsylumF2EastKey = 50000080

    ObtainedBigPilgrimsKeyFromOscar = 50000081

    ObtainedEstusFlask = 50000082
    """ enabled when the item lot that awards the Estus Flask is rolled\n
    also enabled on loading the Asylum for the first time in NG+ and above """

    ObtainedLordvessel2 = 50000090

    ObtainedKeyToTheSeal = 50000100

    ObtainedPyromancyFlameFromLaurentius = 50000110

    ObtainedLightningSpear = 50000120

    ObtainedGreatLightningSpear = 50000130

    ObtainedPetrusCopperCoin = 50000140

    ObtainedLautrecSunlightMedal = 50000150

    ObtainedCatCovenantRing = 50000160

    ObtainedAlvinaDivineBlessing = 50000170

    ObtainedAlvinaRingOfFog = 50000180

    ObtainedPatchesSoulOfLostUndead = 50000190
    """ TODO: unused? """

    ObtainedPatchesHumanity = 50000200

    ObtainedRheaReplenishment = 50000210

    ObtainedGravelordSword = 50000220
    ObtainedGravelordSwordDance = 50000225
    ObtainedGravelordGreatswordDance = 50000230

    ObtainedPatchesTwinHumanities = 50000240

    ObtainedSieglindeTitaniteSlab = 50000250

    ObtainedDragonHeadStone = 50000260
    ObtainedDragonEye = 50000265
    ObtainedDragonTorsoStone = 50000270

    ObtainedEingyiPyromancyFlame = 50000290

    ObtainedFireTempest = 50000300

    ObtainedGreatChaosFireball = 50000310

    ObtainedChaosFireWhipFairLady = 50000320

    ObtainedChaosStorm = 50000330

    ObtainedSoulHero = 50000340
    """ associated item lot unused, flag always off """

    ObtainedRingSunPrincess = 50000350

    ObtainedBlueEyeOrb = 50000360

    ObtainedDarkmoonBladeCovenantRing = 50000365

    ObtainedDarkmoonBladeMiracle = 50000370
    ObtainedDarkmoonTalisman = 50000375

    ObtainedKaatheDarkHand = 50000380

    ObtainedRedEyeOrb = 50000390

    ObtainedKaatheDarkSword = 50000400
    ObtainedKaatheDarkMask = 50000410
    ObtainedKaatheDarkArmor = 50000420
    ObtainedKaatheDarkGauntlets = 50000430
    ObtainedKaatheDarkLeggings = 50000440

    ObtainedDarkSilverTracerGift = 50000501
    ObtainedGoldSilverGift = 50000501
    """ TODO: flag shared by item lots 1500 and 1501 """

    ObtainedGoughsGreatbowGift = 50000511

    ObtainedElizabethsMushroom3 = 50000520

    ObtainedWayOfWhiteTrinket = 50000800
    ObtainedPrincessGuardTrinket = 50000810
    ObtainedWarriorOfSunlightTrinket = 50000820
    ObtainedDarkwraithTrinket = 50000830
    ObtainedDragonPathTrinket = 50000840
    ObtainedGravelordServantTrinket = 50000850
    ObtainedForestHunterTrinket = 50000860
    ObtainedBladeOfTheDarkmoonTrinket = 50000870
    ObtainedChaosServantCovenant = 50000880


    ObtainedBlighttownKey = 50001500
    """ enabled when the blighttown key is awarded (after gaping dragon dies) """

    ObtainedKeyToDepths = 50001510
    """ enabled when the key to depths is awarded (after the capra demon boss dies) """

    ObtainedPriscillaSoul = 50001520

    ObtainedMoonlightButterflySoul = 50001530

    ObtainedSifDrops = 50001540
    """ enabled when the covenant of artorias is awarded;\n
    enabled again when the soul of sif is awarded """

    ObtainedRiteOfKindling2 = 50001550
    """ enabled when the item lot that contains the rite of kindling is awarded """

    ObtainedLordSoulNito = 50001560

    ObtainedQuelaagSoul = 50001570

    ObtainedLordSoulBedOfChaos = 50001580

    ObtainedIronGolemSoul = 50001590

    ObtainedGwyndolinSoul = 50001600

    ObtainedOrnsteinSoul = 50001610

    ObtainedSmoughSoul = 50001620

    ObtainedLordSoulFourKings = 50001630

    ObtainedLordSoulSeath = 50001640

    ObtainedGwynSoul = 50001650

    ObtainedBigPilgrimsKeyFromAsylumDemon = 50001660

    ObtainedGuardianSoul = 50001680

    ObtainedArtoriasSoul = 50001690

    ObtainedManusSoul = 50001700

    ObtainedCalamityRing = 50001710

    ObtainedMaleUndeadMerchantHumanity = 50006230

    ObtainedRedSignSoapstone = 51100330
    """ enabled when the item lot is awarded corresponding to the red sign soapstone pickup in the painted world """

    # ESP FLAGS

    AlvinaFirstQDone = 71200035
    """ enabled after Alvina's first question is answered, regardless if 'yes' or 'no'\n
    becomes enabled after the user selects the option and before the subsequent reply starts\n
    also becomes enabled after the first conversation in NG+ if the player is already in
    the Forest Hunter covenant before talking to Alvina for the first time """

    AlvinaFirstQYes = 71200036
    """ enabled after answering Alvina's first question with 'yes' """

    AlvinaFirstQNo = 71200042
    """ enabled after answering Alvina's first question with 'no', disabled upon absolution """

    AlvinaShivaDialogue = 71200046
    """ enabled after Alvina gives her dialogue about Shiva (player must have defeated at
    least 4 forest invaders\n
    when enabled, Alvina will not give this dialogue again """

    SiegmeyerConversationDoneSensGate2 = 71500066
    """ enabled alongside 11500591\n
    enabled after the player finishes Siegmeyer's first conversation, in front of Sen's Fortress\n
    once this flag is on, Siegmeyer will instead say his "Still closed..." dialog in front of Sen's """

    SiegmeyerConversationDoneSensBoulder2 = 71500069
    """ enabled alongside 11500592\n
    enabled after the player finishes Siegmeyer's dialog about the boulder in Sen's Fortress\n
    once this flag is on, Siegmeyer will instead say his "Perhaps I could try some rolling..." dialog """
