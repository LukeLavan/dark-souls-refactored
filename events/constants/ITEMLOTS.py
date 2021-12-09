from soulstruct.game_types import ItemLotParam

class ITEMLOTS(ItemLotParam):

    SolaireWhiteSighSoapstone = 1000
    """ 100% chance for white sign soapstone\n
    awarded when the player answers yes to Solaire\n
    FLAGS.ObtainedWhiteSignSoapstoneFromSolaire """

    SiegmeyerTinyBeingsRing = 1010
    """ 100% chance for tiny being's ring\n
    awarded during siegmeyer's npc quest\n
    FLAGS.ObtainedTinyBeingsRingFromSiegmeyer """

    SiegmeyerPierceShield = 1020
    """ 100% chance for pierce shield\n
    unused, but seemingly indended for siegmeyer to give you this in the duke's archives\n
    FLAGS.ObtainedPierceShieldUnused """

    SiegmeyerPurgingStone = 1030
    """ 100% chance for a purging stone\n
    unused, but seemingly intended for siegmeyer to give you this in the depths \n
    FLAGS.ObtainedPurgingStoneFromSiegmeyer"""

    SiegmeyerPierceShield2 = 1040
    """ 100% chance for pierce shield\n
    awarded during siegmeyer's npc quest TODO: why are there 2\n
    FLAGS.ObtainedPieceShield"""

    SiegmeyerSpeckledStoneplateRing = 1050
    """ 100% chance for speckled stoneplate ring\n
    awarded during siegmeyer's npc quest\n
    FLAGS.ObtainedSpeckledStoneplateRingFromSiegmeyer """

    SiegmeyerEmitForce = 1060
    """ 100% chance for emit force miracle\n
    awarded during siegmeyer's npc quest\n
    FLAGS.ObtainedEmitForceFromSiegmeyer """

    SiegmeyerSpeckledStoneplateRingUnused = 1070
    """ 100% chance for speckled stoneplate ring\n
    unused, but seemingly intended for siegmeyer to give you this at firelink\n
    FLAGS.ObtainedSpeckledStoneplateFromSiegmeyer """

    OscarUndeadAsylumF2EastKey = 1080
    """ 100% chance for Undead Asylum F2 East Key\n
    awarded when talking to Oscar\n
    FLAGS.ObtainedUndeadAsylumF2EastKey\n
    also awards ITEMLOTS.OscarBigPilgrimsKey and ITEMLOTS.OscarEstusFlask below """

    OscarBigPilgrimsKey = 1081
    """ 100% chance for Big Pilgrim's Key\n
    awarded when talking to Oscar\n
    FLAGS.ObtainedBigPilgrimsKeyFromOscar\n
    also awards ITEMLOTS.OscarEstusFlask below """

    OscarEstusFlask = 1082
    """ 100% chance for 5 full estus flasks (ie, an estus flask with 5 charges)\n
    awarded when talking to oscar\n
    FLAGS.ObtainedEstusFlask """

    GwynevereLordvessel = 1090
    """ 100% chance for the lordvessel\n
    awarded when talking to gwynever\n
    FLAGS.ObtainedLordvessel """

    IngwardKeyToTheSeal = 1100
    """ 100% chance for key to the seal\n
    awarded when talking to ingward (sealer in new londo)\n
    FLAGS.ObtainedKeyToTheSeal """

    LaurentiusPyromancyFlame = 1110
    """ 100% chance for pyromancy glove\n
    awarded when talking to laurentius\n
    FLAGS.ObtainedPyromancyFlameFromLaurentius """

    SunlightAltarLightningSpear = 1120
    """ 100% chance for miracle lightning spear\n
    awarded when the player joins the sunbro covenant\n
    FLAGS.ObtainedLightningSpear """

    SunlightAltarGreatLightningSpear = 1130
    """ 100% chance for miracle great lightning spear\n
    awarded when the player levels up sunbro covenant\n
    FLAGS.ObtainedGreatLightningSpear """

    PetrusCopperCoin = 1140
    """ 100% chance for copper coin\n
    awarded when the player talks to Petrus again\n
    FLAGS.ObtainedPetrusCopperCoin """

    LautrecSunlightMedal = 1150
    """ 100% chance for sunlight medal\n
    awarded when the player talks to Lautrec at Firelink after freeing him\n
    FLAGS.ObtainedLautrecSunlighMedal """

    AlvinaCatCovenantRing = 1160
    """ 100% chance for cat covenant ring\n
    awarded when the player joins the forest hunter covenant\n
    FLAGS.ObtainedCatCovenantRing """

    AlvinaDivineBlessing = 1170
    """ 100% chance for divine blessing\n
    awarded when the player talks to alvina after killing one host as a forest hunter\n
    FLAGS.ObtainedAlvinaDivineBlessing """

    AlvinaRingOfFog = 1180
    """ 100% chance for ring of fog\n
    awarded when the player talks to alvina after killing three hosts as a forest hunter\n
    FLAGS.ObtainedAlvinaRingOfFog """

    PatchesSoulOfLostUndead = 1190
    """ 100% chance for soul of lost undead\n
    TODO: unused? but in patches' esp\n
    FLAGS.ObtainedPatchesSoulLostUndead """

    PatchesHumanity = 1200
    """ 100% chance for humanity\n
    awarded when the player talks to patches after answering no to the cleric question and yes to the trickery question\n
    FLAGS.ObtainedPatchesHumanity """

    RheaReplenishment = 1210
    """ 100% chance for replenishment miracle\n
    awarded when the player talks to rhea after killing her hollowed friends\n
    FLAGS.ObtainedReplenishment """

    NitoGravelordSword = 1220
    """ 100% chance for gravelord sword\n
    awarded when joining the gravelord covenant\n
    FLAGS.ObtainedGravelordSword\n
    also awards ITEMLOTS.NitoGravelordSwordDance below"""

    NitoGravelordSwordDance = 1221
    """ 100% chance for gravelord sword dance miracle\n
    awarded when ITEMLOTS.NitoGravelordSword is awarded (sequential item lot)\n
    FLAGS.ObtainedGravelordSwordDance """

    NitoGravelordGreatswordDance = 1230
    """ 100% chance for gravelord greatsword dance miracle\n
    awarded when reaching rank 1 of gravelord covenant\n
    FLAGS.ObtainedGravelordGreatswordDance """

    PatchesTwinHumanities = 1240
    """ 100% chance for twin humanities\n
    awarded when talking to patches after answering no to the cleric question and no to the forgiveness question in totg\n
    FLAGS.ObtainedPatchesTwinHumanities """

    SieglindeTitaniteSlab = 1250
    """ 100% chance for titanite slab\n
    awarded when talking to sieglinde at ash lake\n
    FLAGS.ObtainedSieglindeTitaniteSlab """

    DragonEye = 1260
    """ 100% chance for dragon eye\n
    awarded when joining the path of the dragon covenant\n
    FLAGS.ObtainedDragonEye\n
    also awards ITEMLOTS.Dragonhead stone """

    DragonHeadStone = 1261
    """ 100% chance for dragon head stone\n
    awarded when ITEMLOTS.DragonEye is awarded (sequential itemlot)\n
    FLAGS.ObtainedDragonHeadStone """

    DragonTorsoStone = 1270
    """ 100% chance for dragon torso stone\n
    awarded when reaching rank 2 of path of the dragon covenant\n
    FLAGS.ObtainedDragonTorsoStone """

    EingyiEggVermifuge = 1280
    """ 100% chance for egg vermifuge\n
    awarded when talking to eingyi when egg'd """

    EingyiPyromancyFlame = 1290
    """ 100% chance for pyromancy flame\n
    awarded when talking to eingyi when egg'd and with at least 11 int\n
    FLAGS.ObtainedEingyiPyromancyFlame """

    QuelanaFireTempest = 1300
    """ 100% chance for fire tempest pyromancy\n
    awarded when talking to quelana when the bed of chaos is dead\n
    FLAGS.ObtainedFireTempest """

    GreatChaosFireball = 1310
    """ 100% chance for great chaos fireball pyromancy\n
    awarded when joining the chaos servant covenant\n
    FLAGS.ObtainedGreatChaosFireball """

    FairLadyChaosFireWhip = 1320
    """ 100% chance for chaos fire whip pyromancy\n
    TODO: unused? investigate fair lady evs\n
    FLAGS.ObtainedChaosFireWhipFairLady """

    ChaosStorm = 1330
    """ 100% chance for chaos storm pyromancy\n
    awarded when reaching rank 2 of chaos servant covenant\n
    FLAGS.ObtainedChaosStorm """

    SoulHero = 1340
    """ 100% chance for soul of a hero\n
    not used, never awarded\n
    FLAGS.ObtainedSoulHero """

    RingSunPrincess = 1350
    """ 100% chance for ring of the sun princess\n
    awarded when joining the princess guard covenant\n
    FLAGS.ObtainedRingRunPrincess """

    BlueEyeOrb = 1360
    """ 100% chance for blue eye orb\n
    awarded when joining the blade of the darkmoon covenant\n
    FLAGS.ObtainedBlueEyeOrb\n
    also awards ITEMLOTS.DarkmoonBladeCovenantRing """

    DarkmoonBladeCovenantRing = 1361
    """ 100% chance for darkmoon blade covenant ring\n
    awarded when ITEMLOTS.BlueEyeOrb is awarded (sequential itemlot)\n
    FLAGS.ObtainedDarkmoonBladeCovenantRing """

    DarkmoonBlade = 1370
    """ 100% chance for darkmoon blade miracle\n
    awarded when reaching rank 1 of the darkmoon blade covenant\n
    FLAGS.ObtainedDarkmoonBladeMiracle\n
    also awards ITEMLOTS.DarkmoonTalisman """

    DarkmoonTalisman = 1371
    """ 100% chance for darkmoon talisman\n
    awarded when ITEMLOTS.DarkmoonBlade is awarded (sequential itemlot)\n
    FLAGS.ObtainedDarkmoonTalisman """

    KaatheDarkHand = 1380
    """ 100% chance for dark hand\n
    awarded when joining the darkwraith covenant\n
    FLAGS.ObtainedKaatheDarkHand """

    RedEyeOrb = 1390
    """ 100% chance for red eye orb\n
    awarded when reaching rank 1 for darkwraith covenant\n
    FLAGS.ObtainedRedEyeOrb """

    KaatheDarkSword = 1400
    """ 100% chance for a dark sword\n
    awarded when reaching rank 2 for darkwraith covenant\b
    FLAGS.ObtainedKaatheDarkSword\n
    also awards ITEMLOTS.KaatheDarkMask, ITEMLOTS.KaatheDarkArmor, 
    ITEMLOTS.KaatheDarkGauntlets, ITEMLOTS.KaatheDarkLeggings """

    KaatheDarkMask = 1401
    """ 100% chance for a dark mash\n
    awarded when reaching rank 2 for darkwraith covenant\b
    FLAGS.ObtainedKaatheDarkMash\n
    also awards ITEMLOTS.KaatheDarkArmor, ITEMLOTS.KaatheDarkGauntlets,
    ITEMLOTS.KaatheDarkLeggings """

    KaatheDarkArmor = 1402
    """ 100% chance for a dark armor\n
    awarded when reaching rank 2 for darkwraith covenant\b
    FLAGS.ObtainedKaatheDarkArmor\n
    also awards ITEMLOTS.KaatheDarkGauntlets, ITEMLOTS.KaatheDarkLeggings """

    KaatheDarkGauntlets = 1403
    """ 100% chance for a dark gauntlets\n
    awarded when reaching rank 2 for darkwraith covenant\b
    FLAGS.ObtainedKaatheDarkGauntlets\n
    also awards ITEMLOTS.KaatheDarkLeggings """

    KaatheDarkLeggings = 1404
    """ 100% chance for a dark leggings\n
    awarded when reaching rank 2 for darkwraith covenant\b
    FLAGS.ObtainedKaatheDarkLeggings """

    SunlightSpear = 1410
    """ 100% chance for sunlight spear miracle\n
    awarded when trading in gwyn's soul at sunlight altar """

    DarkSilverTracerGift = 1500
    """ 100% chance for dark silver tracer\n
    awarded when giving artorias' soul to Ciaran (not killing her for it)\n
    FLAGS.ObtainedDarkSilverTracerGift\n
    also awards ITEMLOTS.GoldTracerGift """

    GoldTracerGift = 1501
    """ 100% chance for gold tracer\n
    awarded when ITEMLOTS.DarkSilverTracerGift is awarded (sequential lot id)\n
    FLAGS.ObtainedGoldTracerGift """

    GoughsGreatbowGift = 1510
    """ 100% chance for gough;s greatbow\n
    awarded when talking to gough when kalameet is dead\n
    FLAGS.ObtainedGoughsGreatbowGift """

    ElizabethsMushroom3 = 1520
    """ 100% chance for three elizabeth's mushrooms\n
    awarded when talking to elizabeth when manus is dead\n
    FLAGS.ObtainedElizabethsMushroom3 """

    WayOfWhiteTrinket = 1800
    """ 100% chance for way of white trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedWayOfWhiteTrinket """

    PrincessGuardTrinket = 1810
    """ 100% chance for princess guard trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedPrincessGuardTrinket """

    WarriorOfSunlightTrinket = 1820
    """ 100% chance for warrior of sunlight trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedWarriorOfSunlightTrinket """

    DarkwraithTrinket = 1830
    """ 100% chance for darkwraith trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedDarkwraithTrinket """

    DragonPathTrinket = 1840
    """ 100% chance for dragon path trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedDragonPathTrinket """

    GravelordServantTrinket = 1850
    """ 100% chance for gravelord servant trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedGravelordServantTrinket """

    ForestHunterTrinket = 1860
    """ 100% chance for forest hunter trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedForestHunterTrinket """

    BladeOfTheDarkmoonTrinket = 1870
    """ 100% chance for darkmoon blade trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedBladeOfTheDarkmoonTrinket """

    ChaosServantTrinket = 1880
    """ 100% chance for chaos servant trinket\n
    unused item, unused item lot\n
    FLAGS.ObtainedChaosServantTrinket """

    GapingDragonBlighttownKey = 2500
    """ 100% for blighttown key\n
    awarded when gaping dragon dies\n
    FLAGS.ObtainedBlighttownKey """

    CapraDemonKeyToDepths = 2510
    """ 100% chance for key to depths\n
    awarded when the capra demon boss dies\n
    FLAGS.ObtainedKeyToDepths """

    PriscillaSoul = 2520
    """ 100% chance for soul of priscilla\n
    awarded when priscilla dies\n
    FLAGS.ObtainedPriscillaSoul"""

    MoonlightButterflySoul = 2530
    """ 100% chance for soul of moonlight butterfly\n
    awarded when the moonlight butterfly boss dies\n
    FLAGS.ObtainedMoonlightButterflySoul """

    SifCovenantOfArtorias = 2540
    """ 100% chance for covenant of artorias ring\n
    awarded when sif dies\n
    FLAGS.ObtainedSifDrops\n
    also awards ITEMLOTS.SifSoul below """

    SifSoul = 2541
    """ 100% chance for soul of sif\n
    awarded when sif dies
    FLAGS.ObtainedSifDrops """

    PinwheelRiteOfKindling = 2550
    """ 100% chance for rite of kindling\n
    awarded when the pinwheel boss dies\n
    FLAGS.ObtainedRiteOfKindling """

    NitoSoul = 2560
    """ 100% chance for nito's lord soul\n
    awarded when nito dies\n
    FLAGS.ObtainedLordSoulNito"""

    QuelaagSoul = 2570
    """ 100% chance for soul of quelaag\n
    awarded when quelaag dies\n
    FLAGS.ObtainedQuelaagSoul """

    BedOfChaosSoul = 2580
    """ 100% chance for bed of chaos' lord soul\n
    awarded when bed of chaos dies
    FLAGS.ObtainedLordSoulBedOfChaos"""

    IronGolemSoul = 2590
    """ 100% chance for soul of iron golem\n
    awarded when iron golem dies\n
    FLAGS.ObtainedIronGolemSoul """

    GwyndolinSoul = 2600
    """ 100% chance for soul of gwyndolin\n
    awarded when gwyndolin dies\n
    FLAGS.ObtainedGwyndolinSoul """

    OrnsteinSoul = 2610
    """ 100% chance for soul of ornstein\n
    awarded when giant ornstein dies\n
    FLAGS.ObtainedOrnsteinSoul """

    SmoughSoul = 2620
    """ 100% chance for soul of smough\n
    awarded when giant smough dies\n
    FLAGS.ObtainedSmoughSoul """

    FourKingsSoul = 2630
    """ 100% chance for four kings' bequeathed lord soul shard\n
    awarded when four kings boss fight ends\n
    FLAGS.ObtainedLordSoulFourKings """

    SeathSoul = 2640
    """ 100% chance for seath's bequeathed lord soul shard\n
    awarded when seath dies\n
    FLAGS.ObtainedLordSoulSeath """

    GwynSoul = 2650
    """ 100% chance for soul of gwyn\n
    awarded when gywn dies\n
    FLAGS.ObtainedGwynSoul """

    AsylumDemonBigPilgrimsKey = 2660
    """ 100% chance for big pilgrim's key\n
    awarded when asylum demon dies\n
    FLAGS.ObtainedBigPilgrimsKeyFromAsylumDemon """

    SanctuaryGuardianSoul = 2680
    """ 100% chance for guardian soul\n
    awarded when the sanctuary guardian boss dies\n
    FLAGS.ObtainedGuardianSoul """

    ArtoriasSoul = 2690
    """ 100% chance for soul of artorias\n
    awarded when artorias dies\n
    FLAGS.ObtainedArtoriasSoul """

    ManusSoul = 2700
    """ 100% chance for soul of manus\n
    awarded when manus dies\n
    FLAGS.ObtainedManusSoul """

    KalameetRing = 2710
    """ 100% chance for calamity ring\n
    awarded when kalameet dies\n
    FLAGS.ObtainedCalamityRing """

    AndreCrestOfArtorias = 6190
    """ 100% chance for crest of artorias\n
    awarded when andre dies\n
    FLAGS.ObtainedCrestOfArtorias
    """

    MaleUndeadMerchantOrangeSoapstone = 6230
    """ 100% chance for orange guidance soapstone\n
    awarded when the male undead merchant dies\n
    FLAGS.ObtainedOrangeSoapstone\n
    also awards MaleUndeadMerchantResidenceKey and MaleUndeadMerchantHumanity and MaleUndeadMerchantDriedFinger """

    MaleUndeadMerchantResidenceKey = 6231
    """ 100% chance for residence key\n
    awarded when MaleUndeadMerchantOrangeSoapstone is awarded\n
    FLAGS.ObtainedResidenceKey"""

    MaleUndeadMerchantHumanity = 6232
    """ 100% chance for 1 humanity\n
    awarded when MaleUndeadMerchantResidenceKey is awarded\n
    FLAGS.ObtainedMaleUndeadMerchantHumanity """

    MaleUndeadMerchantDriedFinger = 6233
    """ 100% chance for dried finger\n
    awarded when MaleUndeadMerchantHumanity is awarded\n
    FLAGS.ObtainedMaleUndeadMerchantDriedFinger """

    Humanity = 9000
    """ 100% chance for 1 humanity\n
    awarded when various bosses die\n
    no flag """

    TwinHumanity = 9020
    """ 100% chance for 1 twin humanity\n
    awarded when various bosses die\n
    no flag """

    Humanity4 = 9030
    """ 100% chance for 4 humanity\n
    awarded when the four kings bos fight ends
    no flag """

    Humanity10 = 9040
    """ 100% chance for 10 humanity\n
    awarded when manus dies\n
    no flag """

    HomewardBone = 9030
    """ 100% chance for 1 homeward bone\n
    awarded when various bosses die\n
    no flag """
