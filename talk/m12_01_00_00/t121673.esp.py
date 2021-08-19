from soulstruct.darksouls1r.ezstate.esd import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_68


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_41


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_42


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenRegularShop(6400, 6499)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_21
        if IsMenuOpen(11) == 0:
            return State_5


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5]

    def test(self):
        return State_3


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_3, State_16, State_25]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if GetTalkListEntryResult() == 0:
            return State_27
        if GetTalkListEntryResult() == 3:
            return State_32
        if GetTalkListEntryResult() == 1:
            return State_4
        if GetTalkListEntryResult() == 4:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_22

    def exit(self):
        ClearTalkListData()


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7, State_21, State_22]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_18


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_21, State_22]

    def enter(self):
        TalkToPlayer(conversation=59000600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if GetDistanceToPlayer() >= 12:
            return State_6
        if HasTalkEnded() == 1:
            return State_30


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_9, State_73]

    def enter(self):
        SetFlagState(flag=71210004, state=1)

    def test(self):
        return State_10


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=59005000, unk1=-1, unk2=-1)
        SetFlagState(flag=71210004, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if HasTalkEnded() == 1:
            return State_8
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_23


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_8, State_11, State_12, State_50, State_52, State_69]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_18


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_10


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        SetFlagState(flag=71210000, state=1)

    def test(self):
        return State_10


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=59005200, unk1=-1, unk2=-1)
        SetFlagState(flag=71210000, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if HasTalkEnded() == 1:
            return State_12
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59000400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_31, State_34, State_45, State_47, State_49, State_66, State_67, State_78, State_80]

    def test(self):
        return State_5
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_18


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_7, State_14, State_15, State_26, State_28, State_29, State_33, State_35, State_37, State_39, State_43, State_44, State_46, State_48, State_63, State_64, State_74, State_76, State_77, State_79]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_56
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71210004) == 0 and GetSelfHP() <= 90 and GetFlagState(11210536) == 1:
            return State_73
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71210004) == 0 and GetSelfHP() <= 90 and GetFlagState(11210536) == 0:
            return State_9
        if GetFlagState(1841) == 1:
            return State_11
        if GetFlagState(71210003) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71210002) == 1:
            return State_70
        if GetFlagState(71210002) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71210001) == 1:
            return State_53
        if GetFlagState(71210001) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71210000) == 1:
            return State_51
        if GetFlagState(71210000) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_13
        if GetFlagState(71210003) == 1:
            return State_11
        else:
            return State_11

    def exit(self):
        RemoveMyAggro()


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_6, State_10, State_16, State_19, State_20, State_21, State_24, State_25, State_29, State_30, State_36, State_43, State_54, State_56, State_58, State_59, State_65, State_68, State_71, State_72, State_76]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1842) == 0 and GetDistanceToPlayer() <= 5:
            return State_36
        if GetFlagState(1841) == 1 and IsPlayerDead() == 1 and GetFlagState(71210005) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_58
        if GetFlagState(1841) == 1 and GetFlagState(71210007) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5 and GetPlayerRemainingHP() < 10 and IsPlayerDead() == 0:
            return State_72
        if GetFlagState(1841) == 1 and GetFlagState(71210006) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5 and GetSelfHP() <= 70 and IsPlayerDead() == 0:
            return State_71
        if GetFlagState(71210008) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71210010) == 0:
            return State_63
        if GetFlagState(71210009) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71210011) == 0:
            return State_64
        if GetFlagState(71210008) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71210009) == 0:
            return State_28
        if GetFlagState(11210536) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11210900) == 0 and GetFlagState(11210901) == 0:
            return State_37
        if GetFlagState(11210536) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_74
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11216100) == 0 and GetFlagState(71210012) == 1:
            return State_14
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_39
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1841) == 0 and GetFlagState(1842) == 0:
            return State_19
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_20
        if IsAttackedBySomeone() == 1 and GetFlagState(1842) == 0:
            return State_26


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_18


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_18


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_56
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_7
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_6
        else:
            return State_18


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_56
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_7
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_6


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_9, State_13, State_14, State_15, State_28, State_29, State_33, State_35, State_36, State_37, State_39, State_43, State_44, State_46, State_48, State_51, State_53, State_56, State_63, State_64, State_70, State_71, State_72, State_73, State_74, State_76, State_77, State_79]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_24


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_18


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_38, State_40, State_55, State_75]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_5
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_18


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_17


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_5]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 0:
            return State_2
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_1
        else:
            return State_54


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_41, State_42]

    def enter(self):
        TalkToPlayer(conversation=59000600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=11215200, state=1)

    def test(self):
        return State_18


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=71210015, state=1)

    def test(self):
        return State_16


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_5]

    def test(self):
        if GetFlagState(11210537) == 0 and GetFlagState(71210015) == 0 and GetFlagState(11210001) == 0:
            return State_15
        if GetFlagState(11210001) == 1 and GetFlagState(71210054) == 0 and GetFlagState(71210016) == 1:
            return State_79
        if GetFlagState(11210001) == 1 and GetFlagState(71210016) == 0:
            return State_33
        if GetFlagState(71210017) == 0 and GetFlagState(71210038) == 1:
            return State_44
        if GetFlagState(11210536) == 1 and GetFlagState(11210900) == 0 and GetFlagState(11210901) == 0:
            return State_48
        if GetFlagState(11210536) == 1:
            return State_77
        else:
            return State_46


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59000900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_34
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        SetFlagState(flag=71210016, state=1)

    def test(self):
        return State_16


class State_35(State):
    """ 35: No description. """

    def enter(self):
        TalkToPlayer(conversation=59000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_18, State_57]

    def enter(self):
        TalkToPlayer(conversation=59005600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_18
        if GetDistanceToPlayer() >= 5:
            return State_23


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=71210014, state=1)

    def test(self):
        return State_25


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71210013, state=1)

    def test(self):
        return State_25


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_1]

    def test(self):
        if GetFlagState(11210536) == 1 and GetFlagState(11210900) == 0 and GetFlagState(11210901) == 0:
            return State_43
        if GetFlagState(11210536) == 1:
            return State_76
        else:
            return State_29


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_2]

    def test(self):
        if GetFlagState(11210536) == 1 and GetFlagState(11210900) == 0 and GetFlagState(11210901) == 0:
            return State_43
        if GetFlagState(11210536) == 1:
            return State_76
        else:
            return State_29


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_41, State_42]

    def enter(self):
        TalkToPlayer(conversation=59000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59001000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        SetFlagState(flag=71210017, state=1)

    def test(self):
        return State_16


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=71210018, state=1)

    def test(self):
        return State_16


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        SetFlagState(flag=71210019, state=1)

    def test(self):
        return State_16


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        SetFlagState(flag=71210001, state=1)

    def test(self):
        return State_10


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=59005210, unk1=-1, unk2=-1)
        SetFlagState(flag=71210001, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        SetFlagState(flag=71210002, state=1)

    def test(self):
        return State_10


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=59005220, unk1=-1, unk2=-1)
        SetFlagState(flag=71210002, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_18


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=71210012, state=1)
        SetFlagState(flag=11216100, state=1)

    def test(self):
        return State_25


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_17, State_21, State_22, State_65]

    def enter(self):
        TalkToPlayer(conversation=59005600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_18
        if GetDistanceToPlayer() >= 5:
            return State_23


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_9, State_13, State_51, State_53, State_70, State_73]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_36

    def exit(self):
        RemoveMyAggro()


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59005500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71210005, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_18


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_18


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        DebugEvent(message='はい')
        SetFlagState(flag=71210008, state=1)

    def test(self):
        return State_63


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        DebugEvent(message='いいえ')
        SetFlagState(flag=71210009, state=1)

    def test(self):
        return State_64


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_59
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_61
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_61
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_60


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_18, State_60]

    def enter(self):
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=59000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_66
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_18, State_61]

    def enter(self):
        TalkToPlayer(conversation=59000200, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_56
        else:
            return State_18


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        SetFlagState(flag=71210010, state=1)

    def test(self):
        return State_16


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        SetFlagState(flag=71210011, state=1)

    def test(self):
        return State_16


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71210005, state=0)
        SetFlagState(flag=71210006, state=0)
        SetFlagState(flag=71210007, state=0)

    def test(self):
        return State_18


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        SetFlagState(flag=71210003, state=1)

    def test(self):
        return State_10


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=59005230, unk1=-1, unk2=-1)
        SetFlagState(flag=71210003, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59005300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71210006, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_18
        if GetDistanceToPlayer() >= 10:
            return State_23


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59005400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71210007, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_18
        if GetDistanceToPlayer() >= 10:
            return State_23


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=59005100, unk1=-1, unk2=-1)
        SetFlagState(flag=71210004, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if HasTalkEnded() == 1:
            return State_8
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_23


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=59001300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        SetFlagState(flag=71210052, state=1)

    def test(self):
        return State_25


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_41, State_42]

    def enter(self):
        TalkToPlayer(conversation=59001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59001500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_78
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_77]

    def enter(self):
        SetFlagState(flag=71210053, state=1)

    def test(self):
        return State_16


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        TalkToPlayer(conversation=59001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_80
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_23


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        SetFlagState(flag=71210054, state=1)

    def test(self):
        return State_16