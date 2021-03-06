"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *

from constants.ARMOR import ARMOR
from constants.CHARACTERS import CHARACTERS
from constants.COLLISIONS import COLLISIONS
from constants.FLAGS import FLAGS
from constants.GOODS import GOODS
from constants.ITEMLOTS import ITEMLOTS
from constants.RINGS import RINGS
from constants.SPECIALEFFECTS import SPECIALEFFECTS
from constants.TEXT import TEXT
from constants.VISUALEFFECTS import VISUALEFFECTS
from constants.WEAPONS import WEAPONS

def TestCondition():
    """ 69: when is this condition ever false??? """
    Await(not IsHuman(PLAYER) and not IsHollow(PLAYER))
    DisplayBanner(BannerType.HumanityRestored)
    Await(IsHuman(PLAYER) or IsHollow(PLAYER))
    DisplayBanner(BannerType.RareRingRevival)
    Restart()

def Constructor():
    """ 0: Event 0 """
    EndIfClient()

    TestCondition()

    DisableFlag(760)
    DisableFlag(762)
    DisableFlag(765)

    DisplayStatusOnFlagEnable(0, FLAGS.HasWarpedToFirelinkShrine, TEXT.InLordranLevelUpAndKindle, 0.0)
    DisplayStatusOnFlagEnable(1, FLAGS.ObtainedRiteOfKindling, TEXT.RiteOfKindling, 0.0)
    DisplayStatusOnFlagEnable(2, FLAGS.ObtainedLordvessel, TEXT.Lordvessel, 0.0)

    Event761()

    Event763()

    EnableGestureLearning()

    EnableVagrants()
    ControlOfferLordSoulsPrompt()

    AllowEscapeFromAbyss()
    DisplayTakenByAbyssMessage()

    ControlWarping()

    CheckIfPlayerIsPyromancerClass()

    Event750()

    Event752()

    Event757()
    Event758()
    Event759()

    IngwardCurseRemoval()

    HandleAbsolution()

    MonitorPvESin()

    Event730()
    Event731()

    Event766()

    EnableLordVesselFlag()

    EnableFlagWhenHasGoodLordSouls(0, 2500, 711)
    EnableFlagWhenHasGoodLordSouls(1, 2501, 712)
    EnableFlagWhenHasGoodLordSouls(2, 2502, 713)
    EnableFlagWhenHasGoodLordSouls(3, 2504, 714)

    ControlGwynSoulForSunlightSpearTrade()
    MonitorEstusFlaskObtained()

    MonitorEstusFlaskUpgrades(
        0, GOODS.EstusFlaskPlus1Empty, GOODS.EstusFlaskPlus1Full)
    MonitorEstusFlaskUpgrades(
        1, GOODS.EstusFlaskPlus2Empty, GOODS.EstusFlaskPlus2Full)
    MonitorEstusFlaskUpgrades(
        2, GOODS.EstusFlaskPlus3Empty, GOODS.EstusFlaskPlus3Full)
    MonitorEstusFlaskUpgrades(
        3, GOODS.EstusFlaskPlus4Empty, GOODS.EstusFlaskPlus4Full)
    MonitorEstusFlaskUpgrades(
        4, GOODS.EstusFlaskPlus5Empty, GOODS.EstusFlaskPlus5Full)
    MonitorEstusFlaskUpgrades(
        5, GOODS.EstusFlaskPlus6Empty, GOODS.EstusFlaskPlus6Full)
    MonitorEstusFlaskUpgrades(
        6, GOODS.EstusFlaskPlus7Empty, GOODS.EstusFlaskPlus7Full)

    PreventMultipleRepairBoxPurchases()

    # the item lots passed in here don't need to be in any specific order, but From uses a specific pattern
    #                             flag to wait for                  soul/ring drop                      humanity drop           homeward bone drop
    AwardItemLotsOnFlagEnable(0,  FLAGS.KilledGapingDragon,         ITEMLOTS.GapingDragonBlighttownKey, ITEMLOTS.TwinHumanity,  ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(1,  FLAGS.KilledTaurusDemon,          0,                                  ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(2,  FLAGS.KilledCapraDemon,           ITEMLOTS.CapraDemonKeyToDepths,     ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(3,  FLAGS.KilledBellGargoyles,        0,                                  ITEMLOTS.TwinHumanity,  0)
    AwardItemLotsOnFlagEnable(4,  FLAGS.KilledPriscilla,            ITEMLOTS.PriscillaSoul,             ITEMLOTS.TwinHumanity,  0)
    AwardItemLotsOnFlagEnable(5,  FLAGS.KilledMoonlightButterfly,   ITEMLOTS.MoonlightButterflySoul,    ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(6,  FLAGS.KilledSif,                  ITEMLOTS.SifCovenantOfArtorias,     ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    # note the absence of the soul of sif item lot - because it is sequentially after the covenant of artorias item lot, both are awarded
    AwardItemLotsOnFlagEnable(7,  FLAGS.KilledPinwheel,             ITEMLOTS.PinwheelRiteOfKindling,    ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(8,  FLAGS.KilledNito,                 ITEMLOTS.NitoSoul,                  ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(9,  FLAGS.KilledQuelaag,              ITEMLOTS.QuelaagSoul,               ITEMLOTS.TwinHumanity,  0)
    AwardItemLotsOnFlagEnable(10, FLAGS.KilledCeaselessDischarge,   0,                                  ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(11, FLAGS.KilledDemonFiresage,        0,                                  ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(12, FLAGS.KilledCentipedeDemon,       0,                                  ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(13, FLAGS.KilledBedOfChaos,           ITEMLOTS.BedOfChaosSoul,            ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(14, FLAGS.KilledIronGolem,            ITEMLOTS.IronGolemSoul,             ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(15, FLAGS.KilledGwyndolin,            ITEMLOTS.GwyndolinSoul,             0,                      0)
    AwardItemLotsOnFlagEnable(16, FLAGS.KilledGiantOrnstein,        ITEMLOTS.OrnsteinSoul,              ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(17, FLAGS.KilledGiantSmough,          ITEMLOTS.SmoughSoul,                ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(18, FLAGS.KilledFourKings,            ITEMLOTS.FourKingsSoul,             ITEMLOTS.Humanity4,     0)
    AwardItemLotsOnFlagEnable(19, FLAGS.KilledSeath,                ITEMLOTS.SeathSoul,                 ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(20, FLAGS.KilledGwyn,                 ITEMLOTS.GwynSoul,                  0,                      0)
    AwardItemLotsOnFlagEnable(21, FLAGS.KilledAsylumDemon,          ITEMLOTS.AsylumDemonBigPilgrimsKey, ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(22, FLAGS.KilledStrayDemon,           0,                                  ITEMLOTS.Humanity,      ITEMLOTS.HomewardBone)
    AwardItemLotsOnFlagEnable(23, FLAGS.KilledSanctuaryGuardian,    ITEMLOTS.SanctuaryGuardianSoul,     ITEMLOTS.Humanity,      0)
    AwardItemLotsOnFlagEnable(24, FLAGS.KilledArtorias,             ITEMLOTS.ArtoriasSoul,              0,                      0)
    AwardItemLotsOnFlagEnable(25, FLAGS.KilledManus,                ITEMLOTS.ManusSoul,                 ITEMLOTS.Humanity10,    0)
    AwardItemLotsOnFlagEnable(26, FLAGS.KilledKalameet,             ITEMLOTS.KalameetRing,              0,                      0)

    EnableFlagWhenHasGoodBonfire(0, GOODS.WeaponSmithbox,
                                 FLAGS.ObtainedWeaponsmithBox)
    EnableFlagWhenHasGoodBonfire(
        1, GOODS.ArmorSmithbox, FLAGS.ObtainedArmorsmithBox)
    EnableFlagWhenHasGoodBonfire(2, GOODS.Repairbox, FLAGS.ObtainedRepairbox)
    # unused - from the Japanese name, 2603 would be an item that allows spell attunement
    EnableFlagWhenHasGoodBonfire(3, 2603, 253)
    # unused - from the Japanese name, 2604 would be an item that allows selling items
    EnableFlagWhenHasGoodBonfire(4, 2604, 254)
    # unused - from the Japanese name, 2605 would be an item that allows warping
    EnableFlagWhenHasGoodBonfire(5, 2605, 255)
    # unused - from the Japanese name, 2606 would be an item that allows leveling up
    EnableFlagWhenHasGoodBonfire(6, 2606, 256)
    EnableFlagWhenHasGoodBonfire(7, GOODS.RiteOfKindling,
                                 FLAGS.ObtainedRiteOfKindling)
    EnableFlagWhenHasGoodBonfire(
        8, GOODS.BottomlessBox, FLAGS.ObtainedBottomlessBox)
    # unused - from the Japanese name, 2609 would be an item that shows a "spare" or "preliminary" menu ?
    EnableFlagWhenHasGoodBonfire(9, 2609, 259)

    RemoveGoodIfFlagEnabled(0, FLAGS.HasGivenLargeEmber, GOODS.LargeEmber)
    RemoveGoodIfFlagEnabled(1, FLAGS.HasGivenVeryLargeEmber, GOODS.VeryLargeEmber)
    RemoveGoodIfFlagEnabled(2, FLAGS.HasGivenCrystalEmber, GOODS.CrystalEmber)
    # slots 3, 4, and 5 not used
    RemoveGoodIfFlagEnabled(6, FLAGS.HasGivenLargeMagicEmber, GOODS.LargeMagicEmber)
    RemoveGoodIfFlagEnabled(7, FLAGS.HasGivenEnchantedEmber, GOODS.EnchantedEmber)
    RemoveGoodIfFlagEnabled(8, FLAGS.HasGivenDivineEmber, GOODS.DivineEmber)
    RemoveGoodIfFlagEnabled(9, FLAGS.HasGivenLargeDivineEmber, GOODS.LargeDivineEmber)
    RemoveGoodIfFlagEnabled(10, FLAGS.HasGivenDarkEmber, GOODS.DarkEmber)
    # slot 11 unused
    RemoveGoodIfFlagEnabled(12, FLAGS.HasGivenLargeFlameEmber, GOODS.LargeFlameEmber)
    RemoveGoodIfFlagEnabled(13, FLAGS.HasGivenChaosFlameEmber, GOODS.ChaosFlameEmber)

    MonitorHasGood(0, GOODS.TitaniteShard, FLAGS.HasTitaniteShard)
    MonitorHasGood(1, GOODS.LargeTitaniteShard, FLAGS.HasLargeTitaniteShard)
    MonitorHasGood(2, GOODS.GreenTitaniteShard, FLAGS.HasGreenTitaniteShard)
    MonitorHasGood(3, GOODS.TitaniteChunk, FLAGS.HasTitaniteChunk)
    MonitorHasGood(4, GOODS.BlueTitaniteChunk, FLAGS.HasBlueTitaniteChunk)
    MonitorHasGood(5, GOODS.WhiteTitaniteChunk, FLAGS.HasWhiteTitaniteChunk)
    MonitorHasGood(6, GOODS.RedTitaniteChunk, FLAGS.HasRedTitaniteChunk)
    MonitorHasGood(7, GOODS.TitaniteSlab, FLAGS.HasTitaniteSlab)
    MonitorHasGood(8, GOODS.BlueTitaniteSlab, FLAGS.HasBlueTitaniteSlab)
    MonitorHasGood(9, GOODS.WhiteTitaniteSlab, FLAGS.HasWhiteTitaniteSlab)
    MonitorHasGood(10, GOODS.RedTitaniteSlab, FLAGS.HasRedTitaniteSlab)
    MonitorHasGood(11, GOODS.DragonScale, FLAGS.HasDragonScale)
    MonitorHasGood(12, GOODS.DemonTitanite, FLAGS.HasDemonTitanite)
    MonitorHasGood(13, GOODS.TwinklingTitanite, FLAGS.HasTwinklingTitanite)

    MonitorInCovenant(0, Covenant.NoCovenant, FLAGS.InNoCovenant)
    MonitorInCovenant(1, Covenant.WayOfWhite, FLAGS.InWayOfWhiteCovenant)
    MonitorInCovenant(2, Covenant.PrincessGuard, FLAGS.InPrincessGuardCovenant)
    MonitorInCovenant(3, Covenant.WarriorOfSunlight, FLAGS.InWarriorOfSunlightCovenant)
    MonitorInCovenant(4, Covenant.Darkwraith, FLAGS.InDarkwraithCovenant)
    MonitorInCovenant(5, Covenant.PathOfTheDragon, FLAGS.InPathOfTheDragonCovenant)
    MonitorInCovenant(6, Covenant.GravelordServant, FLAGS.InGravelordServantCovenant)
    MonitorInCovenant(7, Covenant.ForestHunter, FLAGS.InForestHunterCovenant)
    MonitorInCovenant(8, Covenant.DarkmoonBlade, FLAGS.InDarkmoonBladeCovenant)
    MonitorInCovenant(9, Covenant.ChaosServant, FLAGS.InChaosServantCovenant)

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

    IncrementNumWhenMajorBossKilled(0, FLAGS.RheaBossCount, 4, 16, FLAGS.RheaParish)

    AllowSpellAttunement()

    MonitorLaurentiusIsInterestedInSpectacularPyromancy()
    MonitorLoganInventory()
    MonitorQuelanaCompletion()
    MonitorGriggsCompletion()
    MonitorRheaInventory()
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

    AwardItemLotWhenFlagEnabledAlwaysRepeat(0, FLAGS.GiveEggVermifuge, ITEMLOTS.EingyiEggVermifuge)

    AwardItemLotWhenFlagEnabled(0, FLAGS.GiveWhiteSignSoapstone,            ITEMLOTS.SolaireWhiteSighSoapstone,             1)
    AwardItemLotWhenFlagEnabled(1, FLAGS.GiveTinyBeingsRing,                ITEMLOTS.SiegmeyerTinyBeingsRing,               1)
    AwardItemLotWhenFlagEnabled(2, FLAGS.GivePierceShieldUnused,            ITEMLOTS.SiegmeyerPierceShield,                 1)
    AwardItemLotWhenFlagEnabled(3, FLAGS.GivePurgingStoneSiegmeyer,         ITEMLOTS.SiegmeyerPurgingStone,                 1)
    AwardItemLotWhenFlagEnabled(4, FLAGS.GivePierceShield,                  ITEMLOTS.SiegmeyerPierceShield2,                1)
    AwardItemLotWhenFlagEnabled(5, FLAGS.GiveSpeckledStoneplateRingIzalith, ITEMLOTS.SiegmeyerSpeckledStoneplateRing,       1)
    AwardItemLotWhenFlagEnabled(6, FLAGS.GiveEmitForce,                     ITEMLOTS.SiegmeyerEmitForce,                    1)
    AwardItemLotWhenFlagEnabled(7, FLAGS.GiveSpeckledStoneplateRingUnused,  ITEMLOTS.SiegmeyerSpeckledStoneplateRingUnused, 1)
    AwardItemLotWhenFlagEnabled(8, FLAGS.GiveEstusFlask,                    ITEMLOTS.OscarEstusFlask,                       1)
    AwardItemLotWhenFlagEnabled(9, FLAGS.GiveBigPilgrimsKeyOscar,           ITEMLOTS.OscarUndeadAsylumF2EastKey,            1)
    AwardItemLotWhenFlagEnabled(10, FLAGS.GiveLordvessel,                   ITEMLOTS.GwynevereLordvessel,                   1)
    AwardItemLotWhenFlagEnabled(11, FLAGS.GiveKeyToSeal,                    ITEMLOTS.IngwardKeyToTheSeal,                   1)
    AwardItemLotWhenFlagEnabled(12, FLAGS.GivePyromancyFlameLaurentius,     ITEMLOTS.LaurentiusPyromancyFlame,              1)
    AwardItemLotWhenFlagEnabled(13, FLAGS.GiveLightningSpear,               ITEMLOTS.SunlightAltarLightningSpear,           1)
    AwardItemLotWhenFlagEnabled(14, FLAGS.GiveGreatLightningSpear,          ITEMLOTS.SunlightAltarGreatLightningSpear,      1)
    AwardItemLotWhenFlagEnabled(15, FLAGS.GiveCopperCoin,                   ITEMLOTS.PetrusCopperCoin,                      1)
    AwardItemLotWhenFlagEnabled(16, FLAGS.GiveSunlightMedal,                ITEMLOTS.LautrecSunlightMedal,                  1)
    AwardItemLotWhenFlagEnabled(17, FLAGS.GiveCatCovenantRing,              ITEMLOTS.AlvinaCatCovenantRing,                 1)
    AwardItemLotWhenFlagEnabled(18, FLAGS.GiveDivineBlessing,               ITEMLOTS.AlvinaDivineBlessing,                  1)
    AwardItemLotWhenFlagEnabled(19, FLAGS.GiveRingOfFog,                    ITEMLOTS.AlvinaRingOfFog,                       1)
    AwardItemLotWhenFlagEnabled(20, FLAGS.GiveSoulOfLostUndead,             ITEMLOTS.PatchesSoulOfLostUndead,               1) # TODO: Patches give soul of a lost undead?
    AwardItemLotWhenFlagEnabled(21, FLAGS.GiveHumanity,                     ITEMLOTS.PatchesHumanity,                       1)
    AwardItemLotWhenFlagEnabled(22, FLAGS.GiveReplenishment,                ITEMLOTS.RheaReplenishment,                     1)
    AwardItemLotWhenFlagEnabled(23, FLAGS.GiveGravelordSword,               ITEMLOTS.NitoGravelordSword,                    1)
    AwardItemLotWhenFlagEnabled(24, FLAGS.GiveGravelordGreatswordDance,     ITEMLOTS.NitoGravelordGreatswordDance,          1)
    AwardItemLotWhenFlagEnabled(25, FLAGS.GiveTwinHumanities,               ITEMLOTS.PatchesTwinHumanities,                 1)
    AwardItemLotWhenFlagEnabled(26, FLAGS.GiveTitaniteSlab,                 ITEMLOTS.SieglindeTitaniteSlab,                 1)
    AwardItemLotWhenFlagEnabled(27, FLAGS.GiveDragonEye,                    ITEMLOTS.DragonEye,                             1)
    AwardItemLotWhenFlagEnabled(28, FLAGS.GiveDragonTorsoStone,             ITEMLOTS.DragonTorsoStone,                      1)
    # ITEMLOTS.EingyiEggVermifuge is skipped - see AwardItemLotWhenFlagEnabledAlwaysRepeat usage above
    AwardItemLotWhenFlagEnabled(29, FLAGS.GivePyromancyFlameEingyi,         ITEMLOTS.EingyiPyromancyFlame,                  1)
    AwardItemLotWhenFlagEnabled(30, FLAGS.GiveFireTempest,                  ITEMLOTS.QuelanaFireTempest,                    1)
    AwardItemLotWhenFlagEnabled(31, FLAGS.GiveGreatChaosFireball,           ITEMLOTS.GreatChaosFireball,                    1)
    AwardItemLotWhenFlagEnabled(32, FLAGS.GiveChaosFireWhip,                ITEMLOTS.FairLadyChaosFireWhip,                 1)
    AwardItemLotWhenFlagEnabled(33, FLAGS.GiveChaosStorm,                   ITEMLOTS.ChaosStorm,                            1)
    AwardItemLotWhenFlagEnabled(34, FLAGS.GiveSoulHero,                     ITEMLOTS.SoulHero,                              1)
    AwardItemLotWhenFlagEnabled(35, FLAGS.GiveRingSunPrincess,              ITEMLOTS.RingSunPrincess,                       1)
    AwardItemLotWhenFlagEnabled(36, FLAGS.GiveBlueEyeOrb,                   ITEMLOTS.BlueEyeOrb,                            1)
    AwardItemLotWhenFlagEnabled(37, FLAGS.GiveDarkmoonBlade,                ITEMLOTS.DarkmoonBlade,                         1)
    AwardItemLotWhenFlagEnabled(38, FLAGS.GiveDarkHand,                     ITEMLOTS.KaatheDarkHand,                        1)
    AwardItemLotWhenFlagEnabled(39, FLAGS.GiveRedEyeOrb,                    ITEMLOTS.RedEyeOrb,                             1)
    AwardItemLotWhenFlagEnabled(40, FLAGS.GiveDarkSwordAndSet,              ITEMLOTS.KaatheDarkSword,                       1)
    # note that this slot is the only one with only_once=0, but sadly we can still only ever have one - see ControlGwynSoulForSunlightSpearTrade()
    AwardItemLotWhenFlagEnabled(41, FLAGS.GiveSunlightSpear,                ITEMLOTS.SunlightSpear,                         0)
    AwardItemLotWhenFlagEnabled(42, FLAGS.GiveTracersGift,                  ITEMLOTS.DarkSilverTracerGift,                  1)
    AwardItemLotWhenFlagEnabled(43, FLAGS.GiveGoughsGreatbowGift,           ITEMLOTS.GoughsGreatbowGift,                    1)
    AwardItemLotWhenFlagEnabled(44, FLAGS.GiveElizabethsMushroom3,          ITEMLOTS.ElizabethsMushroom3,                   1)
    # Because these item lots are sequentially after ITEMLOTS.KaatheDarkSword, all of these item lots are awarded
    # with slot 40 - these next four slots are redundant and don't actually do anything
    AwardItemLotWhenFlagEnabled(45, FLAGS.GiveDarkSet,                      ITEMLOTS.KaatheDarkMask,                        1)
    AwardItemLotWhenFlagEnabled(46, FLAGS.GiveDarkSetExceptMask,            ITEMLOTS.KaatheDarkArmor,                       1)
    AwardItemLotWhenFlagEnabled(47, FLAGS.GiveDarkGauntletsAndLeggings,     ITEMLOTS.KaatheDarkGauntlets,                   1)
    AwardItemLotWhenFlagEnabled(48, FLAGS.GiveDarkLeggings,                 ITEMLOTS.KaatheDarkLeggings,                    1)
    AwardItemLotWhenFlagEnabled(49, FLAGS.GiveWayOfWhiteTrinket,            ITEMLOTS.WayOfWhiteTrinket,                     1)
    AwardItemLotWhenFlagEnabled(50, FLAGS.GivePrincessGuardTrinket,         ITEMLOTS.PrincessGuardTrinket,                  1)
    AwardItemLotWhenFlagEnabled(51, FLAGS.GiveWarriorOfSunlightTrinket,     ITEMLOTS.WarriorOfSunlightTrinket,              1)
    AwardItemLotWhenFlagEnabled(52, FLAGS.GiveDarkwraithTrinket,            ITEMLOTS.DarkwraithTrinket,                     1)
    AwardItemLotWhenFlagEnabled(53, FLAGS.GiveDragonPathTrinket,            ITEMLOTS.DragonPathTrinket,                     1)
    AwardItemLotWhenFlagEnabled(54, FLAGS.GiveGravelordServantTrinket,      ITEMLOTS.GravelordServantTrinket,               1)
    AwardItemLotWhenFlagEnabled(55, FLAGS.GiveForestHunterTrinket,          ITEMLOTS.ForestHunterTrinket,                   1)
    AwardItemLotWhenFlagEnabled(56, FLAGS.GiveBladeOfTheDarkmoonTrinket,    ITEMLOTS.BladeOfTheDarkmoonTrinket,             1)
    AwardItemLotWhenFlagEnabled(57, FLAGS.GiveChaosServantTrinket,          ITEMLOTS.ChaosServantTrinket,                   1)

    AwardItemLotWhenFlagEnabled2(0, FLAGS.GiveGravelordSwordDance,          ITEMLOTS.NitoGravelordSwordDance,               1)
    AwardItemLotWhenFlagEnabled2(1, FLAGS.GiveDarkmoonBladeCovenantRing,    ITEMLOTS.DarkmoonBladeCovenantRing,             1)
    AwardItemLotWhenFlagEnabled2(2, FLAGS.GiveDarkmoonTalisman,             ITEMLOTS.DarkmoonTalisman,                      1)
    AwardItemLotWhenFlagEnabled2(3, FLAGS.GiveDragonHeadStone,              ITEMLOTS.DragonHeadStone,                       1)

    AwardItemLotWhenFlagEnabledAndCharDead(0, FLAGS.AndreDead,              CHARACTERS.UNDEADBURG_UNDEADPARISH.Andre,               ITEMLOTS.AndreCrestOfArtorias)
    AwardItemLotWhenFlagEnabledAndCharDead(1, FLAGS.IngwardDead,            CHARACTERS.NEWLONDORUINS_VALLEYOFDRAKES.Ingward,        ITEMLOTS.IngwardKeyToTheSeal)
    AwardItemLotWhenFlagEnabledAndCharDead(2, FLAGS.MaleUndeadMerchantDead, CHARACTERS.UNDEADBURG_UNDEADPARISH.MaleUndeadMerchant,  ITEMLOTS.MaleUndeadMerchantOrangeSoapstone)
    # this itemlot is sequentially after the above itemlot, so this event slot is redundant
    AwardItemLotWhenFlagEnabledAndCharDead(3, FLAGS.MaleUndeadMerchantDead, CHARACTERS.UNDEADBURG_UNDEADPARISH.MaleUndeadMerchant,  ITEMLOTS.MaleUndeadMerchantResidenceKey)

    EnableFlagsIfOwnsItemBeyondNG(0,  ItemType.Good,     GOODS.MiracleLightningSpear,            FLAGS.ObtainedLightningSpear,               FLAGS.GiveLightningSpear)
    EnableFlagsIfOwnsItemBeyondNG(1,  ItemType.Good,     GOODS.MiracleGreatLightningSpear,       FLAGS.ObtainedGreatLightningSpear,          FLAGS.GiveGreatLightningSpear)
    EnableFlagsIfOwnsItemBeyondNG(2,  ItemType.Ring,     RINGS.CatCovenantRing,                  FLAGS.ObtainedCatCovenantRing,              FLAGS.GiveCatCovenantRing)
    # this can prevent Alvina from giving you a divine blessing if you already have one in NG+ or beyond, even if she never gave you one
    EnableFlagsIfOwnsItemBeyondNG(3,  ItemType.Good,     GOODS.DivineBlessing,                   FLAGS.ObtainedAlvinaDivineBlessing,         FLAGS.GiveDivineBlessing)
    EnableFlagsIfOwnsItemBeyondNG(4,  ItemType.Ring,     RINGS.RingOfFog,                        FLAGS.ObtainedAlvinaRingOfFog,              FLAGS.GiveRingOfFog)
    EnableFlagsIfOwnsItemBeyondNG(5,  ItemType.Weapon,   WEAPONS.GravelordSword,                 FLAGS.ObtainedGravelordSword,               FLAGS.GiveGravelordSword)
    EnableFlagsIfOwnsItemBeyondNG(6,  ItemType.Good,     GOODS.MiracleGravelordSwordDance,       FLAGS.ObtainedGravelordSwordDance,          FLAGS.GiveGravelordSwordDance)
    EnableFlagsIfOwnsItemBeyondNG(7,  ItemType.Good,     GOODS.MiracleGravelordGreatswordDance,  FLAGS.ObtainedGravelordGreatswordDance,     FLAGS.GiveGravelordGreatswordDance)
    EnableFlagsIfOwnsItemBeyondNG(8,  ItemType.Good,     GOODS.DragonEye,                        FLAGS.ObtainedDragonEye,                    FLAGS.GiveDragonEye)
    EnableFlagsIfOwnsItemBeyondNG(9,  ItemType.Good,     GOODS.DragonHeadStone,                  FLAGS.ObtainedDragonHeadStone,              FLAGS.GiveDragonHeadStone)
    EnableFlagsIfOwnsItemBeyondNG(10, ItemType.Good,     GOODS.DragonTorsoStone,                 FLAGS.ObtainedDragonTorsoStone,             FLAGS.GiveDragonTorsoStone)
    EnableFlagsIfOwnsItemBeyondNG(11, ItemType.Good,     GOODS.PyromancyGreatChaosFireball,      FLAGS.ObtainedGreatChaosFireball,           FLAGS.GiveGreatChaosFireball)
    EnableFlagsIfOwnsItemBeyondNG(12, ItemType.Good,     GOODS.PyromancyChaosFireWhip,           FLAGS.ObtainedChaosFireWhipFairLady,        FLAGS.GiveChaosFireWhip)
    EnableFlagsIfOwnsItemBeyondNG(13, ItemType.Good,     GOODS.PyromancyChaosStorm,              FLAGS.ObtainedChaosStorm,                   FLAGS.GiveChaosStorm)
    EnableFlagsIfOwnsItemBeyondNG(14, ItemType.Ring,     RINGS.RingOfTheSunPrincess,             FLAGS.ObtainedRingSunPrincess,              FLAGS.GiveRingSunPrincess)
    EnableFlagsIfOwnsItemBeyondNG(15, ItemType.Good,     GOODS.BlueEyeOrb,                       FLAGS.ObtainedBlueEyeOrb,                   FLAGS.GiveBlueEyeOrb)
    EnableFlagsIfOwnsItemBeyondNG(16, ItemType.Ring,     RINGS.DarkmoonBladeCovenantRing,        FLAGS.ObtainedDarkmoonBladeCovenantRing,    FLAGS.GiveDarkmoonBladeCovenantRing)
    EnableFlagsIfOwnsItemBeyondNG(17, ItemType.Good,     GOODS.MiracleDarkmoonBlade,             FLAGS.ObtainedDarkmoonBladeMiracle,         FLAGS.GiveDarkmoonBlade)
    EnableFlagsIfOwnsItemBeyondNG(18, ItemType.Weapon,   WEAPONS.DarkmoonTalisman,               FLAGS.ObtainedDarkmoonTalisman,             FLAGS.GiveDarkmoonTalisman)
    # this can prevent Kaathe from giving you a dark hand if you already have one in NG+ or beyond, even if he never gave you one
    EnableFlagsIfOwnsItemBeyondNG(19, ItemType.Weapon,   WEAPONS.DarkHand,                       FLAGS.ObtainedKaatheDarkHand,               FLAGS.GiveDarkHand)
    EnableFlagsIfOwnsItemBeyondNG(20, ItemType.Good,     GOODS.RedEyeOrb,                        FLAGS.ObtainedRedEyeOrb,                    FLAGS.GiveRedEyeOrb)
    EnableFlagsIfOwnsItemBeyondNG(21, ItemType.Weapon,   WEAPONS.DarkSword,                      FLAGS.ObtainedKaatheDarkSword,              FLAGS.GiveDarkSwordAndSet)
    EnableFlagsIfOwnsItemBeyondNG(22, ItemType.Armor,    ARMOR.DarkMask,                         FLAGS.ObtainedKaatheDarkMask,               FLAGS.GiveDarkSet)
    EnableFlagsIfOwnsItemBeyondNG(23, ItemType.Armor,    ARMOR.DarkArmor,                        FLAGS.ObtainedKaatheDarkArmor,              FLAGS.GiveDarkSetExceptMask)
    EnableFlagsIfOwnsItemBeyondNG(24, ItemType.Armor,    ARMOR.DarkGauntlets,                    FLAGS.ObtainedKaatheDarkGauntlets,          FLAGS.GiveDarkGauntletsAndLeggings)
    EnableFlagsIfOwnsItemBeyondNG(25, ItemType.Armor,    ARMOR.DarkLeggings,                     FLAGS.ObtainedKaatheDarkLeggings,           FLAGS.GiveDarkLeggings)
    # unused covenant "trinkets"
    EnableFlagsIfOwnsItemBeyondNG(26, ItemType.Good,     GOODS.WayOfWhiteTrinket,                FLAGS.ObtainedWayOfWhiteTrinket,            FLAGS.GiveWayOfWhiteTrinket)
    EnableFlagsIfOwnsItemBeyondNG(27, ItemType.Good,     GOODS.PrincessGuardTrinket,             FLAGS.ObtainedPrincessGuardTrinket,         FLAGS.GivePrincessGuardTrinket)
    EnableFlagsIfOwnsItemBeyondNG(28, ItemType.Good,     GOODS.WarriorOfSunlightTrinket,         FLAGS.ObtainedWarriorOfSunlightTrinket,     FLAGS.GiveWarriorOfSunlightTrinket)
    EnableFlagsIfOwnsItemBeyondNG(29, ItemType.Good,     GOODS.DarkwraithTrinket,                FLAGS.ObtainedDarkwraithTrinket,            FLAGS.GiveDarkwraithTrinket)
    EnableFlagsIfOwnsItemBeyondNG(30, ItemType.Good,     GOODS.DragonPathTrinket,                FLAGS.ObtainedDragonPathTrinket,            FLAGS.GiveDragonPathTrinket)
    EnableFlagsIfOwnsItemBeyondNG(31, ItemType.Good,     GOODS.GravelordServantTrinket,          FLAGS.ObtainedGravelordServantTrinket,      FLAGS.GiveGravelordServantTrinket)
    EnableFlagsIfOwnsItemBeyondNG(32, ItemType.Good,     GOODS.ForestHunterTrinket,              FLAGS.ObtainedForestHunterTrinket,          FLAGS.GiveForestHunterTrinket)
    EnableFlagsIfOwnsItemBeyondNG(33, ItemType.Good,     GOODS.BladeOfTheDarkmoonTrinket,        FLAGS.ObtainedBladeOfTheDarkmoonTrinket,    FLAGS.GiveBladeOfTheDarkmoonTrinket)
    EnableFlagsIfOwnsItemBeyondNG(34, ItemType.Good,     GOODS.ChaosServantTrinket,              FLAGS.ObtainedChaosServantCovenant,         FLAGS.GiveChaosServantTrinket)

    EnableFlagIfOwnsItemBeyondNG(0,   ItemType.Good,     GOODS.WhiteSignSoapstone,               FLAGS.ObtainedWhiteSignSoapstone)
    EnableFlagIfOwnsItemBeyondNG(1,   ItemType.Good,     GOODS.RedSignSoapstone,                 FLAGS.ObtainedRedSignSoapstone)
    # redundant since the Red Eye Orb is also a covenant item, already accounted for above
    EnableFlagIfOwnsItemBeyondNG(2,   ItemType.Good,     GOODS.RedEyeOrb,                        FLAGS.ObtainedRedEyeOrb)
    EnableFlagIfOwnsItemBeyondNG(3,   ItemType.Good,     GOODS.OrangeGuidanceSoapstone,          FLAGS.ObtainedOrangeSignSoapstone)
    EnableFlagIfOwnsItemBeyondNG(4,   ItemType.Good,     GOODS.BookOfTheGuilty,                  FLAGS.ObtainedBookOfTheGuilty)
    EnableFlagIfOwnsItemBeyondNG(5,   ItemType.Good,     GOODS.ServantRoster,                    FLAGS.ObtainedServantRoster)
    # 2508 does not refer to a real good - possibly a typo meant to refer to 2608, the bottomless box?
    # TODO: see event 11020800 slot 51 in m10_02 - Firelink relief chest, slot for bottomless box, uses this flag
    EnableFlagIfOwnsItemBeyondNG(6,   ItemType.Good,     2508,                                   11007010)
    EnableFlagIfOwnsItemBeyondNG(7,   ItemType.Good,     GOODS.DriedFinger,                      FLAGS.ObtainedDriedFinger)

    EnableFlagIfOwnsItemBeyondNG2(0,  ItemType.Good,     GOODS.CarvingHello,                     FLAGS.ObtainedCarvingHello)
    EnableFlagIfOwnsItemBeyondNG2(1,  ItemType.Good,     GOODS.CarvingThankYou,                  FLAGS.ObtainedCarvingThankYou)
    EnableFlagIfOwnsItemBeyondNG2(2,  ItemType.Good,     GOODS.CarvingVeryGood,                  FLAGS.ObtainedCarvingVeryGood)
    EnableFlagIfOwnsItemBeyondNG2(3,  ItemType.Good,     GOODS.CarvingImSorry,                   FLAGS.ObtainedCarvingImSorry)
    EnableFlagIfOwnsItemBeyondNG2(4,  ItemType.Good,     GOODS.CarvingHelpMe,                    FLAGS.ObtainedCarvingHelpMe)


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

    Await(FlagDisabled(FLAGS.ObtainedLordvessel) and InsideMap(NEW_LONDO_RUINS)
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
    Await(FlagEnabled(FLAGS.ObtainedLordvessel))

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

    EnableFlag(FLAGS.ObtainedLordvessel)


def EnableFlagWhenHasGoodLordSouls(_, good: int, flag: int):
    """ 711: enables a flag when the player obtains a good\n
    functionally identical to 250, but this one is used specifically for lord souls """
    EndIfThisEventSlotOn()

    Await(HasGood(good))
    EnableFlag(flag)


def ControlGwynSoulForSunlightSpearTrade():
    """ 715: determines whether the option to obtain the sunlight spear miracle is enabled """
    DisableFlag(FLAGS.CanOfferGwynSoul)

    # condition group 1 consists of the following joined by AND:
    IfPlayerHasGood(1, GOODS.GwynSoul, including_box=False)
    IfPlayerDoesNotHaveGood(1, GOODS.MiracleSunlightSpear, including_box=True)
    IfPlayerCovenant(1, Covenant.WarriorOfSunlight)

    # condition group 2 consists of condition group 1, plus a flag check joined by AND:
    IfFlagOn(2, FLAGS.ObtainedGreatLightningSpear)
    IfConditionTrue(2, 1)

    AwaitConditionTrue(2)

    EnableFlag(FLAGS.CanOfferGwynSoul)

    AwaitConditionFalse(1)

    Restart()


def MonitorEstusFlaskObtained():
    """ 716: Whenever EstusFlaskObtained is enabled, enable another (redundant) EstusFlaskObtained flag """
    EndIfThisEventOn()

    Await(FlagEnabled(FLAGS.ObtainedEstusFlask))
    EnableFlag(FLAGS.ObtainedEstusFlask2)


def MonitorEstusFlaskUpgrades(_, EstusFlaskEmptyGood: int, EstusFlaskFullGood: int):
    """ 8131: enables relevant flags when player obtains upgraded estus flask """
    EndIfThisEventSlotOn()

    Await(HasGood(EstusFlaskEmptyGood) or HasGood(EstusFlaskFullGood))

    # when the player obtains some upgraded estus flask, enable all of the flags
    # corresponding to obtaining all of the upgraded flasks that should have came before it

    # this prevents one of the flags from being skipped if the player somehow obtained
    # estus flask upgrades out of order
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus1Empty:
        EnableFlag(FLAGS.ObtainedEstusFlaskPlus1)
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus2Empty:
        EnableFlagRange((FLAGS.ObtainedEstusFlaskPlus1,
                        FLAGS.ObtainedEstusFlaskPlus2))
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus3Empty:
        EnableFlagRange((FLAGS.ObtainedEstusFlaskPlus1,
                        FLAGS.ObtainedEstusFlaskPlus3))
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus4Empty:
        EnableFlagRange((FLAGS.ObtainedEstusFlaskPlus1,
                        FLAGS.ObtainedEstusFlaskPlus4))
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus5Empty:
        EnableFlagRange((FLAGS.ObtainedEstusFlaskPlus1,
                        FLAGS.ObtainedEstusFlaskPlus5))
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus6Empty:
        EnableFlagRange((FLAGS.ObtainedEstusFlaskPlus1,
                        FLAGS.ObtainedEstusFlaskPlus6))
    if EstusFlaskEmptyGood == GOODS.EstusFlaskPlus7Empty:
        EnableFlagRange((FLAGS.ObtainedEstusFlaskPlus1,
                        FLAGS.ObtainedEstusFlaskPlus7))


def PreventMultipleRepairBoxPurchases():
    """ 819: disallows buying repair boxes from multiple vendors """
    EndIfThisEventOn()

    # these flags are enabled when the item is bought from the merchant
    Await(FlagEnabled(FLAGS.ObtainedRepairBoxUndeadMerchant)
          or FlagEnabled(FLAGS.ObtainedRepairBoxAndre))

    # if the flag assigned to an item is already enabled, the item won't appear to buy at all
    EnableFlag(FLAGS.ObtainedRepairBoxUndeadMerchant)
    EnableFlag(FLAGS.ObtainedRepairBoxAndre)


def AllowSpellAttunement():
    """ 719: enables a flag when the player obtains any spell (sorcery, pyromancy, or miracle)
    which allows for spell attunement at bonfires """
    EndIfThisEventOn()

    Await(HasGood(GOODS.SorcerySoulArrow) or
          HasGood(GOODS.SorceryGreatSoulArrow) or
          HasGood(GOODS.SorceryHeavySoulArrow) or
          HasGood(GOODS.SorceryGreatHeavySoulArrow) or
          HasGood(GOODS.SorceryHomingSoulmass) or
          HasGood(GOODS.SorceryHomingCrystalSoulmass) or
          HasGood(GOODS.SorcerySoulSpear) or
          HasGood(GOODS.SorceryCrystalSoulSpear) or
          HasGood(GOODS.SorceryMagicWeapon) or
          HasGood(GOODS.SorceryGreatMagicWeapon) or
          HasGood(GOODS.SorceryCrystalMagicWeapon) or
          HasGood(GOODS.SorceryMagicShield) or
          HasGood(GOODS.SorceryStrongMagicShield) or
          HasGood(GOODS.SorceryHiddenWeapon) or
          HasGood(GOODS.SorceryHiddenBody) or
          HasGood(GOODS.SorceryCastLight) or
          HasGood(GOODS.SorceryHush) or
          HasGood(GOODS.SorceryAuralDecoy) or
          HasGood(GOODS.SorceryRepair) or
          HasGood(GOODS.SorceryFallControl) or
          HasGood(GOODS.SorceryChameleon) or
          HasGood(GOODS.SorceryResistCurse) or
          HasGood(GOODS.SorceryRemedy) or
          HasGood(GOODS.SorceryWhiteDragonBreath) or
          # note that the DLC sorceries are below
          HasGood(GOODS.PyromancyFireball) or
          HasGood(GOODS.PyromancyFireOrb) or
          HasGood(GOODS.PyromancyGreatFireball) or
          HasGood(GOODS.PyromancyFirestorm) or
          HasGood(GOODS.PyromancyFireTempest) or
          HasGood(GOODS.PyromancyFireSurge) or
          HasGood(GOODS.PyromancyFireWhip) or
          HasGood(GOODS.PyromancyCombustion) or
          HasGood(GOODS.PyromancyGreatCombustion) or
          HasGood(GOODS.PyromancyPoisonMist) or
          HasGood(GOODS.PyromancyToxicMist) or
          HasGood(GOODS.PyromancyAcidSurge) or
          HasGood(GOODS.PyromancyIronFlesh) or
          HasGood(GOODS.PyromancyFlashSweat) or
          HasGood(GOODS.PyromancyUndeadRapport) or
          HasGood(GOODS.PyromancyPowerWithin) or
          HasGood(GOODS.PyromancyGreatChaosFireball) or
          HasGood(GOODS.PyromancyChaosStorm) or
          HasGood(GOODS.PyromancyChaosFireWhip) or
          # note that the DLC pyromancy is below
          HasGood(GOODS.MiracleHeal) or
          HasGood(GOODS.MiracleGreatHeal) or
          HasGood(GOODS.MiracleGreatHealExcerpt) or
          HasGood(GOODS.MiracleSoothingSunlight) or
          HasGood(GOODS.MiracleReplenishment) or
          HasGood(GOODS.MiracleBountifulSunlight) or
          HasGood(GOODS.MiracleGravelordSwordDance) or
          HasGood(GOODS.MiracleGravelordGreatswordDance) or
          HasGood(GOODS.MiracleEscapeDeath) or
          HasGood(GOODS.MiracleHomeward) or
          HasGood(GOODS.MiracleForce) or
          HasGood(GOODS.MiracleWrathOfTheGods) or
          HasGood(GOODS.MiracleEmitForce) or
          HasGood(GOODS.MiracleSeekGuidance) or
          HasGood(GOODS.MiracleLightningSpear) or
          HasGood(GOODS.MiracleGreatLightningSpear) or
          HasGood(GOODS.MiracleSunlightSpear) or
          HasGood(GOODS.MiracleMagicBarrier) or
          HasGood(GOODS.MiracleGreatMagicBarrier) or
          HasGood(GOODS.MiracleKarmicJustice) or
          HasGood(5710) or  # note that this isn't a real good
          HasGood(GOODS.MiracleTranquilWalkOfPeace) or
          HasGood(GOODS.MiracleVowOfSilence) or
          HasGood(GOODS.MiracleSunlightBlade) or
          HasGood(GOODS.MiracleDarkmoonBlade) or
          HasGood(GOODS.SorceryDarkOrb) or
          HasGood(GOODS.SorceryDarkBead) or
          HasGood(GOODS.SorceryDarkFog) or
          HasGood(GOODS.SorceryPursuers) or
          HasGood(GOODS.PyromancyBlackFlame))

    EnableFlag(FLAGS.CanAttuneSpells)


def MonitorLaurentiusIsInterestedInSpectacularPyromancy():
    """ 720: enables a flag that will make Laurentius ask about a 'spectacular' pyromancy
    when the player obtains one """
    EndIfThisEventOn()

    Await(HasGood(GOODS.PyromancyGreatFireball) or
          HasGood(GOODS.PyromancyFirestorm) or
          HasGood(GOODS.PyromancyFireTempest) or
          HasGood(GOODS.PyromancyFireWhip) or
          HasGood(GOODS.PyromancyGreatCombustion) or
          HasGood(GOODS.PyromancyGreatChaosFireball) or
          HasGood(GOODS.PyromancyChaosStorm) or
          HasGood(GOODS.PyromancyChaosFireWhip))

    EnableFlag(FLAGS.LaurentiusInterestedInSpectacularPyromancy)


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


def EnableFlagWhenHasGoodBonfire(_, good: int, flag: int):
    """ 250: enables the flag when the player obtains a good\n
    functionally identical to 711, but this one is used specifically for items that enable bonfire menus (like Repairbox) """
    EndIfThisEventSlotOn()

    Await(HasGood(good))

    EnableFlag(flag)


def RemoveGoodIfFlagEnabled(_, flag: int, good: int):
    """ 350: Removes one of a good when a flag is enabled.\n
    Used exclusively for removing embers when the player gives them to blacksmiths.\n
    For some reason, the passed in flag is always also the event slot flag.\n
    if the flag stays on, then this event will try to keep removing one of the passed in good
    every load """
    if THIS_SLOT_FLAG and not HasGood(good):
        End()

    AwaitFlagOn(flag)

    RemoveGoodFromPlayer(good, quantity=1)


def MonitorHasGood(_, good: int, flag: int):
    """ 780: keeps a flag enabled if the player has at least one of a good and keeps the flag disabled if they don't have any\n
    used exclusively for monitoring all of the upgrade materials for the option to feed them to Frampt (to break down) """
    DisableFlag(flag)

    Await(HasGood(good))

    EnableFlag(flag)

    Await(not HasGood(good))

    Restart()


def MonitorInCovenant(_, covenant: uchar, flag: int):
    """ 870: keeps a flag enabled if the player is in a covenant and keeps the flag disabled if they are not """

    Await(PlayerInCovenant(covenant))

    EnableFlag(flag)

    Await(not PlayerInCovenant(covenant))

    DisableFlag(flag)
    Restart()


def DisplayStatusOnFlagEnable(_, flag: int, status: int, timeout: float):
    """ 260: awaits for a flag to become enabled, and displays a status message when it does\n
    if the flag is already enabled on load, doesn't display the status\n
    accepts a timeout that adds a delay between when the flag is enabled and when the status is displayed,
    but From always passes in 0.0 anyway\n
    only displays the statuses if flag 9121 is off - effectively, only displays the statuses if
    the player has never approached where the DLC portal appears. see FLAGS.PreventLordvesselRiteOfKindlingPopup """
    EndIfFlagOn(flag)

    AwaitFlagOn(flag)

    if FlagDisabled(FLAGS.PreventLordvesselRiteOfKindlingPopup):
        Wait(timeout)
        DisplayStatus(status, pad_enabled=True)


def AwardItemLotsOnFlagEnable(_, flag: int, item_lot_1: int, item_lot_2: int, item_lot_3: int):
    """ 970: when a flag becomes active, award the host up to three item lots\n
    if the flag is already enabled on load, ends early and does not award anything\n
    used for awarding boss drops """
    EndIfFlagOn(flag)

    AwaitFlagOn(flag)

    if item_lot_1 != 0:
        AwardItemLot(item_lot_1, host_only=True)

    DisableNetworkSync()
    Wait(5.0)

    if item_lot_2 != 0:
        AwardItemLot(item_lot_2, host_only=True)
    if item_lot_3 != 0:
        AwardItemLot(item_lot_3, host_only=True)


def AwardItemLotWhenFlagEnabled(_, flag: int, item_lot: int, only_once: uchar):
    """ 911: awaits for flag to become enabled, and awards item lot when it does\n
    if the flag is already enabled, end and do nothing\n
    after awarding the item lot, set the flag to be the value of only_once\n
    used for awarding items during coversations (including covenant rewards) """
    EndIfFlagOn(flag)

    AwaitFlagOn(flag)

    AwardItemLot(item_lot)

    SetFlagState(flag, state=only_once)
    EndIfFlagOn(flag)

    Restart()


def AwardItemLotWhenFlagEnabled2(_, flag: int, item_lot: int, only_once: uchar):
    """ 890: functionally identical to AwardItemLotWhenFlagEnabled, used exclusively for
    itemlots that are awarded via sequential ids anyway """
    EndIfFlagOn(flag)

    AwaitFlagOn(flag)

    AwardItemLot(item_lot, host_only=True)

    SetFlagState(flag, state=only_once)
    EndIfFlagOn(flag)

    Restart()


def AwardItemLotWhenFlagEnabledAndCharDead(_, flag: int, char: int, itemlot: int):
    """ 960: awaits for an enabled flag and a dead character and awards an item lot\n
    does nothing if event slot is on """
    EndIfThisEventSlotOn()

    Await(FlagEnabled(flag) and IsDead(char))

    AwardItemLot(itemlot)


def EnableFlagsIfOwnsItemBeyondNG(_, item_type: uchar, item: int, flag1: int, flag2: int):
    """ 8200: On a new NG cycle, all flags are reset. This event re-enables flags based on whether
    or not the player has the specified item. If flag1 is already enabled, this event does nothing.\n
    this version is used exclusively for covenant related items """
    EndIfFlagOn(flag1)

    if NEW_GAME_CYCLE < 1:
        End()
    if not OwnsItem(item, item_type=item_type):
        End()

    EnableFlag(flag1)
    EnableFlag(flag2)


def EnableFlagIfOwnsItemBeyondNG(_, item_type: uchar, item: int, flag: int):
    """ 8300: functionally identical to EnableFlagsIfOwnsItemBeyondNG except for one less flag input.\n
    if flag is already enabled this event does nothing. """
    EndIfFlagOn(flag)

    if NEW_GAME_CYCLE < 1:
        End()
    if not OwnsItem(item, item_type=item_type):
        End()

    EnableFlag(flag)


def EnableFlagIfOwnsItemBeyondNG2(_, item_type: uchar, item: int, flag: int):
    """ 8090: functionally identical to EnableFlagIfOwnsItemBeyondNG, but only used for DLC items\n
    if flag is already enabled this event does nothing """
    EndIfFlagOn(flag)

    if NEW_GAME_CYCLE < 1:
        End()
    if not OwnsItem(item, item_type=item_type):
        End()

    EnableFlag(flag)


def AwardItemLotWhenFlagEnabledAlwaysRepeat(_, flag: int, itemlot: int):
    """ 910: functionally identical to AwardItemLotWhenFlagEnabled, except that this event will
    restart when the flag is disabled\n
    only used for Eingyi's egg vermifuge gift """
    if FlagDisabled(flag):
        AwaitFlagOn(flag)
        AwardItemLot(itemlot, host_only=True)

    AwaitFlagOff(flag)
    Restart()


def IncrementNumWhenMajorBossKilled(_, num: int, bit_count: uint, max_value: uint, flag: int):
    """ 690: when flag becomes active for the first time, num begins to increment
    for each major boss slain. \n
    see flags 1-16 for which bosses count\n
    in order for num to begin to increment, flag must be active and one of the applicable bosses
    must be killed within one game load - if flag is disabled and the game is reloaded,
    the event is restarted and the event waits for flag to become enabled again\n
    once num has been incremented, the event restarts and the status of flag no longer has any effect\n
    used for counting how many bosses have been killed after Rhea moves to the Parish """

    if not THIS_SLOT_FLAG:
        AwaitFlagOn(flag)

    # here we conditionally add to the -1 condition group:
    # if the flag is disabled at this point, it's added to the group,
    # and afterwards we check to see when any of these become enabled.
    # the effect is that the IncrementEventValue insrutcion below only
    # happens when one of these flags becomes enabled, rather than letting
    # the increment happen if these flags were already enabled before
    if FlagDisabled(FLAGS.KilledGapingDragon):
        IfFlagOn(-1, FLAGS.KilledGapingDragon)
    if FlagDisabled(FLAGS.KilledBellGargoyles):
        IfFlagOn(-1, FLAGS.KilledBellGargoyles)
    if FlagDisabled(FLAGS.KilledPriscilla):
        IfFlagOn(-1, FLAGS.KilledPriscilla)
    if FlagDisabled(FLAGS.KilledSif):
        IfFlagOn(-1, FLAGS.KilledSif)
    if FlagDisabled(FLAGS.KilledPinwheel):
        IfFlagOn(-1, FLAGS.KilledPinwheel)
    if FlagDisabled(FLAGS.KilledNito):
        IfFlagOn(-1, FLAGS.KilledNito)
    if FlagDisabled(8): # unused - cut boss? order implies ash lake
        IfFlagOn(-1, 8)
    if FlagDisabled(FLAGS.KilledQuelaag):
        IfFlagOn(-1, FLAGS.KilledQuelaag)
    if FlagDisabled(FLAGS.KilledBedOfChaos):
        IfFlagOn(-1, FLAGS.KilledBedOfChaos)
    if FlagDisabled(FLAGS.KilledIronGolem):
        IfFlagOn(-1, FLAGS.KilledIronGolem)
    if FlagDisabled(FLAGS.KilledOandS):
        IfFlagOn(-1, FLAGS.KilledOandS)
    if FlagDisabled(FLAGS.KilledFourKings):
        IfFlagOn(-1, FLAGS.KilledFourKings)
    if FlagDisabled(FLAGS.KilledSeath):
        IfFlagOn(-1, FLAGS.KilledSeath)
    if FlagDisabled(FLAGS.KilledGwyn):
        IfFlagOn(-1, FLAGS.KilledGwyn)

    AwaitConditionTrue(-1)

    IncrementEventValue(num, bit_count=bit_count, max_value=max_value)
    Restart()


def MonitorLoganInventory():
    """ 721: controls flags LoganPurchasedAllSpellsFirelink and LoganPurchasedAllSpellsArchives flags,
    which are enabled when all of the respective spells are bought from Logan\n
    note that spells not bought at Firelink remain available at the Archives, so it's possible for
    LoganPurchasedAllSpellsFirelink to become enabled when buying spells at the Archives """
    EndIfFlagOn(FLAGS.LoganPurchasedAllSpellsArchives)

    Await(FlagEnabled(FLAGS.HasPurchasedLoganSoulArrow) and
          FlagEnabled(FLAGS.HasPurchasedLoganGreatSoulArrow) and
          FlagEnabled(FLAGS.HasPurchasedLoganHeavySoulArrow) and
          FlagEnabled(FLAGS.HasPurchasedLoganGreatHeavySoulArrow) and
          FlagEnabled(FLAGS.HasPurchasedLoganMagicWeapon) and
          FlagEnabled(FLAGS.HasPurchasedLoganMagicShield) and
          FlagEnabled(FLAGS.HasPurchasedLoganHomingSoulmass) and
          FlagEnabled(FLAGS.HasPurchasedLoganSoulSpear))

    EnableFlag(FLAGS.LoganPurchasedAllSpellsFirelink)

    Await(FlagEnabled(FLAGS.HasPurchasedLoganCrystalHomingSoulmass) and 
        FlagEnabled(FLAGS.HasPurchasedLoganCrystalSoulSpear) and 
        FlagEnabled(FLAGS.HasPurchasedLoganCrystalMagicWeapon))

    EnableFlag(FLAGS.LoganPurchasedAllSpellsArchives)


def MonitorQuelanaCompletion():
    """ 722: waits for all of Quelana's pyromancies to be purchased, the bed of chaos to be killed,
    and the ascended pyro glove+5 to be obtained, and activates a flag that causes Quelana to leave """
    EndIfThisEventOn()

    Await(FlagEnabled(FLAGS.PurchasedQuelenaFireball) and
          FlagEnabled(FLAGS.PurchasedQuelanaFireOrb) and
          FlagEnabled(FLAGS.PurchasedQuelanaGreatFireball) and
          FlagEnabled(FLAGS.PurchasedQuelanaFirestorm) and
          FlagEnabled(FLAGS.PurchasedQuelanaFireWhip) and
          FlagEnabled(FLAGS.PurchasedQuelanaCombustion) and
          FlagEnabled(FLAGS.PurchasedQuelanaGreatCombustion) and
          FlagEnabled(FLAGS.PurchasedQuelanaUndeadRapport) and
          FlagEnabled(FLAGS.KilledBedOfChaos) and
          HasWeapon(WEAPONS.PyromancyGloveAscendedPlusFive))

    EnableFlag(FLAGS.QuelanaDone)


def MonitorGriggsCompletion():
    """ 723: waits for all of Grigg's spells and rings to be purchased, then
    enables a flags that triggers his move to sen's """
    EndIfThisEventOn()

    Await(FlagEnabled(FLAGS.PurchasedGriggsSoulArrow) and
          FlagEnabled(FLAGS.PurchasedGriggsGreatSoulArrow) and
          FlagEnabled(FLAGS.PurchasedGriggsHeavySoulArrow) and
          FlagEnabled(FLAGS.PurchasedGriggsGreatHeavySoulArrow) and
          FlagEnabled(FLAGS.PurchasedGriggsMagicWeapon) and
          FlagEnabled(FLAGS.PurchasedGriggsMagicShield) and
          FlagEnabled(FLAGS.PurchasedGriggsAuralDecoy) and
          FlagEnabled(FLAGS.PurchasedGriggsFallControl) and
          FlagEnabled(FLAGS.PurchasedGriggsBellowingDragoncrestRing) and
          FlagEnabled(FLAGS.PurchasedGriggsLingeringDragoncrestRing) and
          FlagEnabled(FLAGS.PurchasedGriggsHomingSoulmass) and
          FlagEnabled(FLAGS.PurchasedGriggsSoulSpear))

    EnableFlag(FLAGS.GriggsDone)


def MonitorRheaInventory():
    """ 724: waits for all of Rhea's miracles and her divine blessing to be purchased
    before enabling a flag (TODO: what does 724 do) """
    EndIfThisEventOn()

    Await(FlagEnabled(FLAGS.PurchasedRheaDivineBlessing) and
          FlagEnabled(FLAGS.PurchasedRheaHeal) and
          FlagEnabled(FLAGS.PurchasedRheaGreatHealExcerpt) and
          FlagEnabled(FLAGS.PurchasedRheaHomeward) and
          FlagEnabled(FLAGS.PurchasedRheaForce) and
          FlagEnabled(FLAGS.PurchasedRheaGreatHeal) and
          FlagEnabled(FLAGS.PurchasedRheaWrathoftheGods) and
          FlagEnabled(FLAGS.PurchasedRheaSeekGuidance) and
          FlagEnabled(FLAGS.PurchasedRheaMagicBarrier))

    EnableFlag(FLAGS.RheaPurchasedAll)


def Event725():
    """ 725: TODO: this doesnt make sense and doesnt do anything? """
    EndIfThisEventOn()
    Await(TrueFlagCount((11707100, 11707190)) >= 2)
    EnableFlag(725)


def Event726():
    """ 726: TODO: this doesn't make sense and doesn't do anything """
    EndIfThisEventOn()
    # these all occur in Oswald's shop EventFlags
    # eg, buying three rings of sacrifice from him trips this flag
    Await(TrueFlagCount((11607000, 11607090)) >= 2)
    EnableFlag(726)


def Event727():
    """ 727: TODO: none of these flags are used """
    EndIfThisEventOn()

    # these IDs imply they have to do with Ash Lake
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


def CheckIfPlayerIsPyromancerClass():
    """ 740: enables a flag if the player class is pyromancer """
    Await(PlayerIsClass(ClassType.Pyromancer)) # weird place for Await
    EnableFlag(FLAGS.PlayerIsPyromancerClass)


def Event745():
    """ 745: TODO: how is 745 used in m12_00 and m14_00? """
    if FlagEnabled(FLAGS.ShivaDead) and FlagEnabled(FLAGS.ShivaBodyguardDead):
        Await(FlagEnabled(703)) # TODO: what is this strange flag?

    # wait until one of these flags become enabled, but only if they were disabled to begin with
    if FlagDisabled(FLAGS.ShivaDead):
        IfFlagOn(-1, FLAGS.ShivaDead)
    if FlagDisabled(FLAGS.ShivaBodyguardDead):
        IfFlagOn(-1, FLAGS.ShivaBodyguardDead)
    AwaitConditionTrue(-1)
    End()


def IngwardCurseRemoval():
    """ 754: When the player gives a soft humanity to Ingward to have curse broken, this event's flag is set\n
    when 754 is enabled, this event re-disables it, applies special effects that break the curse,
    and plays the appropriate visual effect """
    DisableFlag(FLAGS.BreakCurse)

    AwaitFlagOn(FLAGS.BreakCurse)

    DisableFlag(FLAGS.BreakCurse)
    AddSpecialEffect(PLAYER, SPECIALEFFECTS.IngwardBreakCurse)
    AddSpecialEffect(PLAYER, SPECIALEFFECTS.IngwardRemoveCurseBuildup)
    CreateTemporaryVFX(VISUALEFFECTS.CurseBroken, anchor_entity=PLAYER,
                       anchor_type=CoordEntityType.Character, model_point=7)
    Restart()


def HandleAbsolution():
    """ 770: waits until the absolution flag is enabled, then disables all npc hostility flags """
    AwaitFlagOn(FLAGS.ReceiveAbsolution)

    DisableFlag(FLAGS.ReceiveAbsolution)

    # either or both of these flags must already be on, otherwise 'You have not sinned'
    DisableFlag(FLAGS.HasPvESin)
    DisableFlag(FLAGS.CovenantHardBetrayal)

    # these flags are disabled, but are not sufficient to be able to recieve absolution
    # even if enabled, unless either or both af the above flags are also enabled,
    # requesting absolution results in the 'You have not sinned' prompt
    DisableFlag(FLAGS.GwyndolinAngry)
    DisableFlag(FLAGS.ShivaOrBodyguardDead)
    DisableFlag(FLAGS.ForestHuntersBetrayed)

    # these are event slot flags for NPC hostility events
    # if these are disabled while the corresponding hostility flag is enabled,
    # the npc will be disabled and the event slot flag won't be re-enabled
    # TODO: any hostility event slot flags fall outside of these ranges?
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
    # all of the flags that trigger flag 744 (HasPvESin)
    DisableFlag(FLAGS.SolaireHostile)
    DisableFlag(FLAGS.DarkmoonKnightessHostile)
    DisableFlag(FLAGS.LoganHostile)
    DisableFlag(FLAGS.GriggsHostile)
    DisableFlag(FLAGS.RheaHostileFisticuffs)
    DisableFlag(FLAGS.RheaHostileNothing)
    DisableFlag(FLAGS.PetrusHostileGuilty)
    DisableFlag(FLAGS.PetrusHostileInnocent)
    DisableFlag(FLAGS.VinceHostile)
    DisableFlag(FLAGS.NicoHostile)
    DisableFlag(FLAGS.GwyndolinHostile)
    DisableFlag(FLAGS.LaurentiusHostile)
    DisableFlag(FLAGS.EingyiHostileFairLady)
    DisableFlag(FLAGS.EingyiHostileAttackedUnproven)
    DisableFlag(FLAGS.EingyiHostileAttackedProven)
    DisableFlag(FLAGS.QuelanaHostile)
    DisableFlag(FLAGS.IngwardHostile)
    DisableFlag(FLAGS.AndreHostile)
    DisableFlag(FLAGS.VamosHostile)
    DisableFlag(FLAGS.GiantBlacksmithHostile)
    DisableFlag(FLAGS.RickertHostile)
    DisableFlag(FLAGS.MaleUndeadMerchantHostile)
    DisableFlag(FLAGS.FemaleUndeadMerchantHostile)
    DisableFlag(FLAGS.CrestfallenMerchantHostile)
    DisableFlag(FLAGS.DomhnallHostile)
    DisableFlag(FLAGS.CrestfallenWarriorHostile)
    DisableFlag(FLAGS.SiegmeyerHostile)
    DisableFlag(FLAGS.SieglindeHostile)
    DisableFlag(FLAGS.LautrecHostile)
    DisableFlag(FLAGS.ShivaHostile)
    DisableFlag(FLAGS.PatchesHostile)
    DisableFlag(FLAGS.FramptHostile)
    DisableFlag(FLAGS.KaatheHostile)
    DisableFlag(FLAGS.PriscillaHostile)
    EnableFlag(FLAGS.AlvinaStart)  # one of these is not like the others
    DisableFlag(FLAGS.AlvinaGone)
    DisableFlag(FLAGS.AlvinaBetrayed)
    DisableFlag(FLAGS.AlvinaDisappear)
    DisableFlag(FLAGS.AlvinaFirstQDone)
    DisableFlag(FLAGS.AlvinaFirstQNo)
    DisableFlag(FLAGS.ShivaBodyguardHostile)
    DisableFlag(FLAGS.GoughHostile)
    DisableFlag(FLAGS.ChesterHostile)
    DisableFlag(FLAGS.CiaranHostile)
    DisableFlag(FLAGS.ElizabethHostile)
    # Finally, un-aggro affected NPCs in loaded map (would remain hostile until next reload otherwise)
    # m10_01 is the only loaded map near Oswald; a separate event in m10_01 resets their positions
    SetTeamType(CHARACTERS.UNDEADBURG_UNDEADPARISH.Solaire, TeamType.Ally)
    SetTeamType(CHARACTERS.UNDEADBURG_UNDEADPARISH.Griggs, TeamType.Ally)
    SetTeamType(CHARACTERS.UNDEADBURG_UNDEADPARISH.Rhea, TeamType.Ally)
    SetTeamType(CHARACTERS.UNDEADBURG_UNDEADPARISH.Andre, TeamType.Ally)
    SetTeamType(CHARACTERS.UNDEADBURG_UNDEADPARISH.MaleUndeadMerchant, TeamType.Ally)
    SetTeamType(CHARACTERS.UNDEADBURG_UNDEADPARISH.Lautrec, TeamType.Ally)
    Restart()


def MonitorPvESin():
    """ 772: Waits for NPCs to become aggro and enables a flag indicating the player has PvE sin """
    AwaitFlagOff(FLAGS.HasPvESin)

    Await(FlagEnabled(FLAGS.SolaireHostile) or
          FlagEnabled(FLAGS.DarkmoonKnightessHostile) or
          FlagEnabled(FLAGS.LoganHostile) or
          FlagEnabled(FLAGS.GriggsHostile) or
          FlagEnabled(FLAGS.RheaHostileFisticuffs) or
          FlagEnabled(FLAGS.RheaHostileNothing) or
          FlagEnabled(FLAGS.PetrusHostileGuilty) or
          FlagEnabled(FLAGS.PetrusHostileInnocent) or
          FlagEnabled(FLAGS.VinceHostile) or
          FlagEnabled(FLAGS.NicoHostile) or
          FlagEnabled(FLAGS.GwyndolinHostile) or
          FlagEnabled(FLAGS.LaurentiusHostile) or
          FlagEnabled(FLAGS.EingyiHostileFairLady) or # counts as sin, but re-enabled upon loading Blighttown
          FlagEnabled(FLAGS.EingyiHostileAttackedUnproven) or
          FlagEnabled(FLAGS.EingyiHostileAttackedProven) or
          FlagEnabled(FLAGS.QuelanaHostile) or
          FlagEnabled(FLAGS.IngwardHostile) or
          FlagEnabled(FLAGS.AndreHostile) or
          FlagEnabled(FLAGS.VamosHostile) or
          FlagEnabled(FLAGS.GiantBlacksmithHostile) or
          FlagEnabled(FLAGS.RickertHostile) or
          FlagEnabled(FLAGS.MaleUndeadMerchantHostile) or
          FlagEnabled(FLAGS.FemaleUndeadMerchantHostile) or
          FlagEnabled(FLAGS.CrestfallenMerchantHostile) or
          FlagEnabled(FLAGS.DomhnallHostile) or
          FlagEnabled(FLAGS.CrestfallenWarriorHostile) or
          FlagEnabled(FLAGS.SiegmeyerHostile) or
          FlagEnabled(FLAGS.SieglindeHostile) or
          FlagEnabled(FLAGS.LautrecHostile) or
          FlagEnabled(FLAGS.ShivaHostile) or
          FlagEnabled(FLAGS.PatchesHostile) or
          FlagEnabled(FLAGS.FramptHostile) or # never enabled
          FlagEnabled(FLAGS.KaatheHostile) or # never enabled
          FlagEnabled(FLAGS.PriscillaHostile) or
          FlagEnabled(FLAGS.AlvinaGone) or
          FlagEnabled(FLAGS.AlvinaBetrayed) or
          FlagEnabled(FLAGS.AlvinaFirstQDone) or
          FlagEnabled(FLAGS.AlvinaFirstQNo) or
          FlagEnabled(FLAGS.ShivaBodyguardHostile) or
          FlagEnabled(FLAGS.GoughHostile) or
          FlagEnabled(FLAGS.ChesterHostile) or
          FlagEnabled(FLAGS.CiaranHostile) or
          FlagEnabled(FLAGS.ElizabethHostile)) # never enabled

    EnableFlag(FLAGS.HasPvESin)
    AwaitFlagOff(FLAGS.HasPvESin)

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
        FlagDisabled(845) and # note 844 is skipped
        FlagDisabled(846) and
        FlagDisabled(848) and # note 847 is skipped
        FlagDisabled(849) and
        FlagDisabled(860)):   # not 850

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
