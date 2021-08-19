"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from ..entities.m18_00_00_00_entities import *
from ..entities.m10_02_00_00_entities import Boxes as m10_02_Boxes
from ..entities.m16_00_00_00_entities import Boxes as m16_00_Boxes


def Constructor():
    """ 0: Event 0 """
    SkipLinesIfFlagOff(1, 11800100)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    SkipLinesIfFlagOff(1, 11800210)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=30)
    SkipLinesIfClient(2)
    DisableObject(Objects.o8051_0000)
    DeleteVFX(VFX.MultiplayerFog1, erase_root_only=False)
    SkipLinesIfFlagOff(3, 15)
    DisableObject(Objects.o8310)
    DisableObject(Objects.o8311)
    EnableObject(Objects.o8312)
    RunEvent(11805090)
    RunEvent(11805091)
    RunEvent(11805092)
    RunEvent(20)
    RunEvent(21)
    RunEvent(11800100)
    RunEvent(11800101)
    RunEvent(11800200)
    RunEvent(11800230, slot=0, args=(1, 180005, Objects.o8310))
    RunEvent(11800230, slot=1, args=(2, 180006, Objects.o8310))
    RunEvent(11800230, slot=2, args=(3, 180007, Objects.o8310))
    RunEvent(11800230, slot=3, args=(4, 180008, Objects.o8310))
    RunEvent(11800210)
    RunEvent(11800220)
    RunEvent(11806100, slot=0, args=(Characters.c2791_0000, Boxes.GhostKnightMovement1))
    RunEvent(11806100, slot=1, args=(Characters.c2791_0001, Boxes.GhostKnightMovement2))
    RunEvent(11806100, slot=2, args=(Characters.c2791_0002, Boxes.GhostKnightMovement3))
    RunEvent(11806100, slot=3, args=(Characters.c2791_0003, Boxes.GhostKnightMovement4))
    RunEvent(11806100, slot=4, args=(Characters.c2791_0004, Boxes.GhostKnightMovement5))
    RunEvent(11806100, slot=5, args=(Characters.c2791_0005, Boxes.GhostKnightMovement6))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(11800002)
    DisableSoundEvent(1803800)
    SkipLinesIfFlagOff(4, 15)
    RunEvent(11805392)
    DisableObject(Objects.o8050_0000)
    DeleteVFX(VFX.GwynEntranceFog, erase_root_only=False)
    SkipLines(7)
    RunEvent(11805390)
    RunEvent(11805391)
    RunEvent(11805393)
    RunEvent(11805392)
    RunEvent(11800001)
    RunEvent(11805394)
    RunEvent(11805395)
    HumanityRegistration(Characters.c0000_0002, 8310)
    RunEvent(11805030)
    RunEvent(11805029)
    RunEvent(11805032)
    RunEvent(11805990, slot=0, args=(11805031, Characters.c0000_0002))
    RunEvent(11800550, slot=0, args=(1000, 1029, 1012))
    EnableImmortality(Characters.c5330_0016)
    SkipLinesIfFlagOn(1, 830)
    DisableCharacter(Characters.c5330_0016)
    SkipLinesIfFlagOn(6, 15)
    RunEvent(11800539, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1647))
    RunEvent(11800530, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1644))
    RunEvent(11800531, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1645))
    RunEvent(11800537, slot=0, args=(Characters.c5330_0016, 1640, 1647, 1649))
    RunEvent(11800541, slot=0, args=(Characters.c5330_0016,))
    RunEvent(11806200)
    EnableImmortality(Characters.c5330_0017)
    SkipLinesIfFlagOn(1, 831)
    DisableCharacter(Characters.c5330_0017)
    SkipLinesIfFlagOn(6, 15)
    RunEvent(11800540, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1677))
    RunEvent(11800533, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1673))
    RunEvent(11800534, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1674))
    RunEvent(11800538, slot=0, args=(Characters.c5330_0017, 1670, 1677, 1678))
    RunEvent(11800542, slot=0, args=(Characters.c5330_0017,))
    RunEvent(11806201)


@RestartOnRest
def Event11805090():
    """ 11805090: Event 11805090 """
    EndIfThisEventOn()
    DisableCharacter(Characters.c2790_0006)
    DisableCharacter(Characters.c2790_0007)
    DisableCharacter(Characters.c2790_0008)
    DisableCharacter(Characters.c2790_0009)
    DisableCharacter(Characters.c2790_0010)
    IfFlagOn(0, 11800050)
    EndIfFlagOn(735)
    EnableFlag(5000)
    EnableCharacter(Characters.c2790_0006)
    EnableCharacter(Characters.c2790_0007)
    EnableCharacter(Characters.c2790_0008)
    EnableCharacter(Characters.c2790_0009)
    EnableCharacter(Characters.c2790_0010)


@RestartOnRest
def Event11805091():
    """ 11805091: Event 11805091 """
    IfFlagOn(-1, 11805095)
    IfFlagOn(-1, 735)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOff(1, 735)
    DisableFlag(735)
    DisableFlag(11800050)
    DisableFlag(11805095)
    EnableFlag(5001)
    Kill(Characters.c2790_0006, award_souls=False)
    Kill(Characters.c2790_0007, award_souls=False)
    Kill(Characters.c2790_0008, award_souls=False)
    Kill(Characters.c2790_0009, award_souls=False)
    Kill(Characters.c2790_0010, award_souls=False)


@RestartOnRest
def Event11805092():
    """ 11805092: Event 11805092 """
    EndIfClient()
    IfBlackWorldTendencyComparison(1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, 11800050)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(2, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(2, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11800050)
    RestartIfConditionFalse(-2)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(3, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(3, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 11800050)
    RestartIfConditionFalse(-3)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(4, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(4, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-4, input_condition=4)
    IfFlagOn(-4, 11800050)
    RestartIfConditionFalse(-4)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(5, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(5, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-5, input_condition=5)
    IfFlagOn(-5, 11800050)
    RestartIfConditionFalse(-5)
    WaitFrames(1)
    IfBlackWorldTendencyComparison(6, comparison_type=ComparisonType.GreaterThan, value=50)
    IfInsideMap(6, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(-6, input_condition=6)
    IfFlagOn(-6, 11800050)
    RestartIfConditionFalse(-6)
    EnableFlag(11800050)
    Wait(600.0)
    IfBlackWorldTendencyComparison(7, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    IfInsideMap(7, game_map=KILN_OF_THE_FIRST_FLAME)
    RestartIfConditionFalse(7)
    DisableFlag(11800050)
    EnableFlag(11805095)


def Event11805390():
    """ 11805390: Event 11805390 """
    IfFlagOff(1, 15)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GwynFogPrompt,
        anchor_type=CoordEntityType.Region,
        line_intersects=Objects.o8050_0000,
        boss_version=True,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GwynFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11805391():
    """ 11805391: Event 11805391 """
    IfFlagOff(1, 15)
    IfFlagOn(1, 11805393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(
        1,
        prompt_text=10010403,
        anchor_entity=Boxes.GwynFogPrompt,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o8050_0000,
    )
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, Boxes.GwynFogRotationTarget)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11805393():
    """ 11805393: Event 11805393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 15)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwynCombatStart)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Characters.c5370_0000)


@RestartOnRest
def Event11805392():
    """ 11805392: Event 11805392 """
    SkipLinesIfFlagOff(3, 15)
    DisableCharacter(Characters.c5370_0000)
    Kill(Characters.c5370_0000, award_souls=False)
    End()
    DisableAI(Characters.c5370_0000)
    IfFlagOn(1, 11805393)
    IfCharacterInsideRegion(1, PLAYER, region=Boxes.GwynCombatStart)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Characters.c5370_0000)
    EnableBossHealthBar(Characters.c5370_0000, name=5370, slot=0)


def Event11800001():
    """ 11800001: Event 11800001 """
    DisableObject(Objects.o8312)
    DisableObject(Objects.o0200_0001)
    IfCharacterDead(0, Characters.c5370_0000)
    EnableFlag(15)
    KillBoss(1800800)
    DisableObject(Objects.o8050_0000)
    DeleteVFX(VFX.GwynEntranceFog, erase_root_only=True)
    SkipLinesIfClient(2)
    SetRespawnPoint(SpawnPoints.SpawnPointAtBoss)
    SaveRequest()
    DisableFlag(11807200)
    DisableFlag(11807210)
    DisableFlag(11807220)
    DisableFlag(11807240)
    DisableObject(Objects.o8310)
    DisableObject(Objects.o8311)
    EnableObject(Objects.o8312)
    DeleteObjectVFX(Objects.o8310, erase_root=True)
    CreateTemporaryVFX(90014, anchor_entity=Objects.o0200_0001, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(Objects.o0200_0001)


def Event20():
    """ 20: Event 20 """
    EndIfClient()
    IfFlagOn(1, 15)
    IfActionButton(
        1,
        prompt_text=10010108,
        anchor_entity=Objects.o0200_0001,
        anchor_type=CoordEntityType.Object,
        max_distance=1.5,
        model_point=-1,
    )
    IfConditionTrue(0, input_condition=1)
    IncrementNewGameCycle(1)
    PlayCutscene(180000, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(1)
    EnableFlag(20)


def Event21():
    """ 21: Event 21 """
    EndIfClient()
    IfFlagOn(1, 15)
    IfCharacterOutsideRegion(1, PLAYER, region=Spheres.GwynMusic)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180001, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    IncrementNewGameCycle(1)
    AwardAchievement(2)
    EnableFlag(21)


def Event11805394():
    """ 11805394: Event 11805394 """
    DisableNetworkSync()
    IfFlagOff(1, 15)
    IfFlagOn(1, 11805392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11805391)
    IfCharacterInsideRegion(1, PLAYER, region=Spheres.GwynMusic)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1803800)


def Event11805395():
    """ 11805395: Event 11805395 """
    DisableNetworkSync()
    IfFlagOn(1, 15)
    IfFlagOn(1, 11805394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1803800)


@RestartOnRest
def Event11800002():
    """ 11800002: Event 11800002 """
    IfFlagOn(0, 15)
    DisableCharacter(Characters.c2790_0001)
    DisableCharacter(Characters.c2790_0002)
    DisableCharacter(Characters.c2790_0003)
    DisableCharacter(Characters.c2790_0004)
    DisableCharacter(Characters.c2790_0005)
    DisableCharacter(Characters.c2790_0006)
    DisableCharacter(Characters.c2790_0007)
    DisableCharacter(Characters.c2790_0008)
    DisableCharacter(Characters.c2790_0009)
    DisableCharacter(Characters.c2790_0010)
    DisableCharacter(Characters.c3490_0000)
    DisableCharacter(Characters.c3491_0000)
    DisableCharacter(Characters.c3491_0001)
    Kill(Characters.c2790_0001, award_souls=False)
    Kill(Characters.c2790_0002, award_souls=False)
    Kill(Characters.c2790_0003, award_souls=False)
    Kill(Characters.c2790_0004, award_souls=False)
    Kill(Characters.c2790_0005, award_souls=False)
    Kill(Characters.c2790_0006, award_souls=False)
    Kill(Characters.c2790_0007, award_souls=False)
    Kill(Characters.c2790_0008, award_souls=False)
    Kill(Characters.c2790_0009, award_souls=False)
    Kill(Characters.c2790_0010, award_souls=False)
    Kill(Characters.c3490_0000, award_souls=False)
    Kill(Characters.c3491_0000, award_souls=False)
    Kill(Characters.c3491_0001, award_souls=False)


def Event11800100():
    """ 11800100: Event 11800100 """
    EndIfThisEventOn()
    DisableObject(Objects.o8311)
    IfHost(1)
    IfPlayerHasGood(1, 2510, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010105,
        anchor_entity=Objects.o8310,
        anchor_type=CoordEntityType.Object,
        model_point=150,
    )
    IfConditionTrue(0, input_condition=1)
    PlayCutscene(180015, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableObject(Objects.o8311)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=10)
    RemoveGoodFromPlayer(2510)


def Event11800101():
    """ 11800101: Event 11800101 """
    DisableNetworkSync()
    IfFlagOff(1, 11800100)
    IfPlayerDoesNotHaveGood(1, 2510, including_box=False)
    IfActionButton(
        1,
        prompt_text=10010105,
        anchor_entity=Objects.o8310,
        anchor_type=CoordEntityType.Object,
        model_point=150,
        trigger_attribute=TriggerAttribute.All,
    )
    IfFlagOn(2, 11800100)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisplayDialog(
        10010174,
        anchor_entity=Objects.o8310,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


def Event11800200():
    """ 11800200: Event 11800200 """
    IfFlagOn(0, 756)
    ForceAnimation(PLAYER, 7697)
    WaitFrames(75)
    IfFlagOff(1, 11800201)
    IfPlayerHasGood(1, 2500, including_box=False)
    IfFlagOff(2, 11800202)
    IfPlayerHasGood(2, 2501, including_box=False)
    IfFlagOff(3, 11800203)
    IfPlayerHasGood(3, 2502, including_box=False)
    IfFlagOff(4, 11800204)
    IfPlayerHasGood(4, 2503, including_box=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 1)
    EnableFlag(11800201)
    RemoveGoodFromPlayer(2500)
    SkipLinesIfFinishedConditionFalse(2, 2)
    EnableFlag(11800202)
    RemoveGoodFromPlayer(2501)
    SkipLinesIfFinishedConditionFalse(2, 3)
    EnableFlag(11800203)
    RemoveGoodFromPlayer(2502)
    SkipLinesIfFinishedConditionFalse(2, 4)
    EnableFlag(11800204)
    RemoveGoodFromPlayer(2503)
    EnableFlag(11805111)
    IfFlagOff(0, 11805111)
    WaitFrames(10)
    EndIfFlagOn(11800211)
    DisableFlag(756)
    Restart()


def Event11800230(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11800230: Event 11800230 """
    IfFlagOn(1, 11805111)
    IfTrueFlagCountEqual(1, arg_0_3, (11800201, 11800204))
    IfConditionTrue(0, input_condition=1)
    DeleteObjectVFX(arg_8_11, erase_root=True)
    CreateObjectVFX(arg_4_7, obj=arg_8_11, model_point=100)
    WaitFrames(95)
    SkipLinesIfFlagRangeAllOn(1, (11800201, 11800204))
    ForceAnimation(PLAYER, 7701, loop=True)
    DisableFlag(11805111)


def Event11800210():
    """ 11800210: Event 11800210 """
    SkipLinesIfFlagOn(17, 15)
    IfTrueFlagCountEqual(2, 1, (11800201, 11800204))
    IfTrueFlagCountEqual(3, 2, (11800201, 11800204))
    IfTrueFlagCountEqual(4, 3, (11800201, 11800204))
    IfTrueFlagCountEqual(5, 4, (11800201, 11800204))
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 2)
    CreateObjectVFX(180005, obj=Objects.o8310, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 3)
    CreateObjectVFX(180006, obj=Objects.o8310, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 4)
    CreateObjectVFX(180007, obj=Objects.o8310, model_point=100)
    SkipLinesIfFinishedConditionFalse(1, 5)
    CreateObjectVFX(180008, obj=Objects.o8310, model_point=100)
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(Objects.o8300, 1)
    End()
    IfFlagOn(1, 11800201)
    IfFlagOn(1, 11800202)
    IfFlagOn(1, 11800203)
    IfFlagOn(1, 11800204)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11800211)
    DisableFlag(756)
    PlayCutscene(180010, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(Objects.o8300, 1)
    RegisterBonfire(11800992, obj=Objects.o8310, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=30)


def Event11800220():
    """ 11800220: Event 11800220 """
    DisableNetworkSync()
    IfFlagOff(1, 11800210)
    IfActionButton(
        1,
        prompt_text=10010400,
        anchor_entity=Boxes.FirelinkAltarLocked,
        anchor_type=CoordEntityType.Region,
        trigger_attribute=TriggerAttribute.All,
        line_intersects=Objects.o8300,
    )
    IfFlagOn(2, 11805110)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisplayDialog(
        10010160,
        anchor_entity=Objects.o8300,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    SkipLines(2)
    DisableFlag(11805110)
    DisplayDialog(
        10010171,
        anchor_entity=Objects.o8310,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.NoButton,
    )
    Restart()


@RestartOnRest
def Event11806100(_, arg_0_3: int, arg_4_7: int):
    """ 11806100: Event 11806100 """
    DisableNetworkSync()
    SkipLinesIfThisEventSlotOn(3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 200, loop=True)
    IfCharacterInsideRegion(0, arg_0_3, region=Boxes.GhostKnightMovementGoal)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


@RestartOnRest
def Event11805100(_, arg_0_3: int, arg_4_7: int):
    """ 11805100: Event 11805100 """
    IfCharacterAlive(0, arg_0_3)
    IfCharacterDead(0, arg_0_3)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_4_7, host_only=True)


def Event11800510(_, arg_0_3: int, arg_4_7: int):
    """ 11800510: Event 11800510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11800520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800520: Event 11800520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800530: Event 11800530 """
    IfFlagOn(1, 1643)
    IfFlagOn(1, 830)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800531: Event 11800531 """
    IfFlagOn(1, 1644)
    IfFlagOn(1, 830)
    IfFlagOn(1, 11800210)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800533: Event 11800533 """
    IfFlagOn(1, 1672)
    IfFlagOn(1, 831)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800534: Event 11800534 """
    IfFlagOn(1, 1673)
    IfFlagOn(1, 831)
    IfFlagOn(1, 11800210)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800537: Event 11800537 """
    IfFlagOn(-1, 1642)
    IfFlagOn(-1, 1643)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 830)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800538(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800538: Event 11800538 """
    IfFlagOn(-1, 1671)
    IfFlagOn(-1, 1672)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 831)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11800539(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800539: Event 11800539 """
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-7, 11020598)
    IfHealthLessThanOrEqual(7, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfAttacked(7, arg_0_3, attacker=PLAYER)
    IfEntityBeyondDistance(7, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7009, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11800540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11800540: Event 11800540 """
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-7, 11600590)
    IfHealthLessThanOrEqual(7, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(7, arg_0_3, 0.0)
    IfAttacked(7, arg_0_3, attacker=PLAYER)
    IfEntityBeyondDistance(7, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(1, input_condition=-7)
    IfThisEventOff(1)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11800541(_, arg_0_3: int):
    """ 11800541: Event 11800541 """
    IfFlagOn(1, 830)
    IfFlagOff(1, 1647)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    IfFlagOff(0, 830)
    DisableCharacter(arg_0_3)
    Restart()


def Event11800542(_, arg_0_3: int):
    """ 11800542: Event 11800542 """
    IfFlagOn(1, 831)
    IfFlagOff(1, 1676)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    IfFlagOff(0, 831)
    DisableCharacter(arg_0_3)
    Restart()


def Event11800550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11800550: Event 11800550 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1003)
    IfFlagOn(1, 11410595)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_0_3, arg_4_7))
    EnableFlag(arg_8_11)


def Event11806200():
    """ 11806200: Event 11806200 """
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(1, 824)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(824)
    PlayCutscene(
        180050,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m10_02_Boxes.ArriveFromKiln,
        move_to_map=FIRELINK_SHRINE,
    )
    PlayCutscene(100250, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c5330_0016)
    DisableFlag(830)
    Restart()


def Event11806201():
    """ 11806201: Event 11806201 """
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 1673)
    IfFlagOn(-1, 1674)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(1, 825)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(825)
    PlayCutscene(
        180051,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=m16_00_Boxes.ArrivalFromKiln,
        move_to_map=NEW_LONDO_RUINS,
    )
    PlayCutscene(160050, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableCharacter(Characters.c5330_0017)
    DisableFlag(831)
    Restart()


def Event11805029():
    """ 11805029: Event 11805029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0002, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11805033)
    IfClient(2)
    IfFlagOn(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0002)
    EndIfFlagOn(15)
    IfMultiplayerCount(1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11805031)
    IfFlagOff(1, 11805033)
    IfFlagOn(1, 1012)
    IfCharacterBackreadEnabled(1, Characters.c0000_0002)
    IfEntityWithinDistance(1, Characters.c0000_0002, PLAYER, radius=30.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0002,
        region=Points.SolaireSummonSign,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


def Event11805990(_, arg_0_3: int, arg_4_7: int):
    """ 11805990: Event 11805990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11805030():
    """ 11805030: Event 11805030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Characters.c0000_0002, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11805033)
    IfClient(2)
    IfFlagOn(2, 11805031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(Characters.c0000_0002)
    EndIfFlagOn(15)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 1012)
    IfCharacterBackreadEnabled(1, Characters.c0000_0002)
    IfEntityWithinDistance(1, Characters.c0000_0002, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(
        SummonSignType.BlueEyeSign,
        Characters.c0000_0002,
        region=Points.SolaireSummonSign,
        summon_flag=11805031,
        dismissal_flag=11805033,
    )


def Event11805032():
    """ 11805032: Event 11805032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11805031)
    IfFlagOn(1, 11805393)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.c0000_0002, command_id=10, slot=0)
    ReplanAI(Characters.c0000_0002)
    IfEntityWithinDistance(0, Characters.c0000_0002, Objects.o8050_0000, radius=1.5)
    RotateToFaceEntity(Characters.c0000_0002, Boxes.GwynFogRotationTarget)
    ForceAnimation(Characters.c0000_0002, 7410)
    AICommand(Characters.c0000_0002, command_id=-1, slot=0)
    ReplanAI(Characters.c0000_0002)


@RestartOnRest
def Event11805200():
    """ 11805200: Event 11805200 """
    DisableAI(1800999)
    IfMovingOnCollision(1, 1803000)
    IfRunningOnCollision(2, 1803000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    RequestAnimation(1800999, 1750, loop=False, wait_for_completion=True)
    Restart()
    RequestAnimation(1800999, 2000, loop=False, wait_for_completion=True)
    Restart()
