from soulstruct.game_types import Character

class CHARACTERS:
    """ this enum is split into maps because one "character" that appears in multiple maps
    will have different entity IDs for each different map """
    
    class UNDEADBURG_UNDEADPARISH(Character):
        """ m10_01_00_00 """

        Solaire = 6001
        """ c0000_0002 """

        Griggs = 6040
        """ c0000_0003 """

        Rhea = 6072
        """ c0000_0005 """

        Andre = 6190
        """ c2640_0000 """

        MaleUndeadMerchant = 6230
        """ c2510_0000 """

        Lautrec = 6300
        """ c0000_0006 """
    
    class FIRELINK(Character):
        """ m10_02_00_00 """

        Siegmeyer = 6287
        """ c0000_0020 """

        Sieglinde = 6292
        """ c0000_0021 """

    class GREATHOLLOW_ASHLAKE(Character):
        """ m13_02_00_00 """

        Siegmeyer = 6288
        """ c0000_0004 """

        Sieglinde = 6290
        """ c0000_0005 """
    
    class BLIGHTTOWN(Character):
        """ m14_00_00_00 """

        Siegmeyer = 6282
        """ c0000_0003 """

    class DEMONRUINS_LOSTIZALITH(Character):
        """ m14_01_00_00 """

        Siegmeyer = 6286
        """ c0000_0005 """

    class SENSFORTRESS(Character):
        """ m15_00_00_00 """

        Logan = 6030
        """ c0000_0004 """

        CrestfallenMerchant = 6250
        """ c0000_0005"""

        Siegmeyer = 6280
        """ c0000_0006 """

        IronTarkus = 6510
        """ c0000_0007 """

        Griggs = 6043
        """ c0000_0008 """

        Ricard = 6600
        """ c0000_0009 """
    
    class ANORLONDO(Character):
        """ m15_01_00_00 """

        Siegmeyer = 6283
        """ c0000_0005 """

    class NEWLONDORUINS_VALLEYOFDRAKES(Character):
        """ m16_00_00_00 """

        Ingward = 6180
        """ c0000_0003 """
    
    class DUKESARCHIVES(Character):
        """ m17_00_00_00 """

        Sieglinde = 6291
        """ c0000_0004 """
