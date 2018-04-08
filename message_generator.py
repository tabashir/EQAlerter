from Config import *
from Actions import *

class MessageGenerator:

    def __init__(self):
        print("DEBUG: Checking dependencies")

    def action_for(line, character_name):

        if (MARNEK1) in line:
            return SimpleMessage("Marnek is in skeleton form, shrouded players DPS now")

        if (MARNEK2) in line:
            return SimpleMessage("Corpse collector is dragging a corpse")


        # Dispelling the Shadows - Plane of Shadow
        if (SHADOW1) in line:
            return SimpleMessage("Group heal")

        SHAD2CHAR = SHADOW2 + character_name
        if (SHAD2CHAR) in line:
            return SimpleMessage("D, A, and get aggro")

        # single player
        SHAD3CHAR = SHADOW3 + character_name
        if (SHAD3CHAR) in line:
            return SimpleMessage("Move away from the front")

        # single player
        SHAD4CHAR = SHADOW4 + character_name
        if (SHAD4CHAR) in line:
            return SimpleMessage("Move out of range")

        if (SHADOW5) in line:
            return SimpleMessage("Back away from the mob A E incoming")


        # single player
        SHAD6CHAR = SHADOW6 + character_name
        if (SHAD6CHAR) in line:
            return SimpleMessage("Run away from the raid")


        if (SHADOW7) in line:
            return SimpleMessage("Hide behind a pillar until the D, O, T, fades")



        # Glimpse, the Unseen - The Threshold
        # single player
        GLIMPCHAR = GLIMPSE + character_name
        if (GLIMPCHAR) in line:
            return SimpleMessage("run far away from the raid, east")



        # Ulrich the Ageless - The Threshold
        # single player
        if (ULRICH1) in line:
            return SimpleMessage("run through an aura, do not linger")


        # single player
        if (ULRICH2) in line:
            return SimpleMessage("run through an aura, or D A")



        # Monarch Widow - The Threshold
        if (MONARCH) in line:
            return SimpleMessage("move raid 50 feet counter-clockwise to avoid web")



        # An End to Fear - The Epicenter
        # single player
        if (ENDFEAR1) in line:
            return SimpleMessage("move out of melee range")


        # single player
        if (ENDFEAR2) in line:
            return SimpleMessage("get curse cure")


        # single player
        if (ENDFEAR3) in line:
            return SimpleMessage("get corruption cure")


        if (ENDFEAR4) in line:
            return SimpleMessage("Xaric is vulnerable, kill kill kill")


        # single player
        if (ENDFEAR5) in line:
            return SimpleMessage("stop D P S until effect wears off")


        ##### END RoF #####


        ##### START CoF #####

        # Bixie Warfront: Pelzia's Plot raid.
        # single player
        PEL1CHAR = PELZIA1 + character_name
        if (PEL1CHAR) in line:
            return SimpleMessage("run west away from raid")


        # single player
        PEL2CHAR = PELZIA2 + character_name
        if (PEL2CHAR) in line:
            return SimpleMessage("run east away from raid")



        # The Dead Hills: Xulous Prime raid.
        # single player
        if (XULOUS1) in line:
            return SimpleMessage("kite the cloud of disease")


        # single player
        if (XULOUS2) in line:
            return SimpleMessage("kite the cloud of disease")


        # single player
        if (XULOUS3) in line:
            return SimpleMessage("get disease cure")


        # single player
        if (XULOUS4) in line:
            return SimpleMessage("move out of the disease aura")


        # single player
        if (XULOUS5) in line:
            return SimpleMessage("gate out now")



        # Neriak - Fourth Gate: Houses of Thex raid.
        if (THEX1) in line:
            return SimpleMessage("move out of range")


        # single player
        THEX2CHAR = THEX2 + character_name
        if (THEX2CHAR) in line:
            return SimpleMessage("run east away from the raid")


        # single player
        THEX3CHAR = THEX3 + character_name
        if (THEX3CHAR) in line:
            return SimpleMessage("kite until the energy pulse fades away")


        # single player
        if (THEX4) in line:
            return SimpleMessage("move out of the lightning pulse")


        # single player
        THEX5CHAR = THEX5 + character_name
        if (THEX5CHAR) in line:
            return SimpleMessage("run away from the raid")



        # Neriak - Fourth Gate: Hate Rising raid.
        # single player
        if (HATERISING1) in line:
            return SimpleMessage("move out of the damaging aura")


        if (HATERISING2) in line:
            return SimpleMessage("move away from the pinned player")



        # Tower of Rot: Lord Kyle Bayle raid.
        if (BAYLE1) in line:
            return SimpleMessage("move out of melee range and hold pets")


        if (BAYLE2) in line:
            return SimpleMessage("resume melee and send in pets")



        # Argin-Hiz: Burn Out raid.
        # single player
        if (BURNOUT1) in line:
            return SimpleMessage("move out of the aura")


        if (BURNOUT2) in line:
            return SimpleMessage("Imps are spawning, invis everyone now")


        if (BURNOUT3) in line:
            return SimpleMessage("balance the mini bosses")


        if (BURNOUT4) in line:
            return SimpleMessage("a phoenix spawned")



        # The Void (H): The Journey Home raid.
        if (JOURNEY1) in line:
            return SimpleMessage("get out of melee range")


        # single player
        if (JOURNEY2) in line:
            return SimpleMessage("take portal to another island")


        if (JOURNEY3) in line:
            return SimpleMessage("Lanys is charming the main tank")


        if (JOURNEY4) in line:
            return SimpleMessage("Lanys is casting beam DoT, prepare to mass a curse cure")


        # single player
        if (JOURNEY5) in line:
            return SimpleMessage("get a curse cure")


        if (JOURNEY6) in line:
            return SimpleMessage("move out of melee range")


        # single player
        JOUR7CHAR = JOURNEY7 + character_name
        if (JOUR7CHAR) in line:
            return SimpleMessage("run away from raid and hide")


        # single player
        JOUR8CHAR = JOURNEY8 + character_name
        if (JOUR8CHAR) in line:
            return SimpleMessage("get a corruption cure")


        # single player
        JOUR9CHAR = JOURNEY9 + character_name
        if (JOUR9CHAR) in line:
            return SimpleMessage("move away from the edge of the island now")


        if (JOURNEY10) in line:
            return SimpleMessage("move to your assigned island now or die")


        # single player
        if (JOURNEY11) in line:
            return SimpleMessage("get a corruption cure")


        ##### END CoF #####


        ##### START Fifteenth Anniversary #####

        # The Plane of War: 15th anniversary raid.
        if (POW15) in line:
            return SimpleMessage("move away from the A E circle")


        ##### END Fifteenth Anniversary #####


        ##### START TDS #####

        # Defense of the City
        # single player
        if (TDSDEF1) in line:
            return SimpleMessage("move away from the raid now")


        # single player
        if (TDSDEF2) in line:
            return SimpleMessage("It is safe to return to the raid")


        # single player
        if (TDSDEF3) in line:
            return SimpleMessage("It is safe to return to the raid")


        # single player
        TDSD4CHAR = TDSDEF4 + character_name
        if (TDSD4CHAR) in line:
            return SimpleMessage("It is safe to return to the raid")


        # single player
        if (TDSDEF5) in line:
            return SimpleMessage("Get a disease cure")



        # Principal Quastori Numicia
        # single player
        if (QUASI1) in line:
            return SimpleMessage("Move out of the aura")


        # single player
        if (QUASI2) in line:
            return SimpleMessage("Move away from the raid")



        # Praetor Vitio
        if (VITIO1) in line:
            return SimpleMessage("Move away from his left side")


        if (VITIO2) in line:
            return SimpleMessage("Move away from his right side")


        if (VITIO3) in line:
            return SimpleMessage("Move away from Vitio")


        if (VITIO4) in line:
            return SimpleMessage("Get close to Vitio")


        if (VITIO5) in line:
            return SimpleMessage("Move away from his back")


        if (VITIO6) in line:
            return SimpleMessage("Main tank drop aggro")


        if (VITIO7) in line:
            return SimpleMessage("Next tank start taunting")



        # Principal Vicarum Nomia
        if (NOMIA1) in line:
            return SimpleMessage("Move away from the target")


        if (NOMIA2) in line:
            return SimpleMessage("Move away from the blob")


        # single player
        NOM3CHAR = character_name + NOMIA3
        if (NOM3CHAR) in line:
            return SimpleMessage("Run away from the raid")


        # single player
        if (NOMIA4) in line:
            return SimpleMessage("Start running or get a corruption cure")


        if (NOMIA5) in line:
            return SimpleMessage("D P S on totems")


        # single player
        if (NOMIA6) in line:
            return SimpleMessage("Move away from the raid")


        if (NOMIA7) in line:
            return SimpleMessage("Move away from the target for 10 seconds")


        if (NOMIA8) in line:
            return SimpleMessage("Heal the totems")


        # single player
        if (NOMIA9) in line:
            return SimpleMessage("Run away you are the target for the A E")


        ##### END TDS #####


        ##### START TBM RAIDS #####

        # Maestro TBM Raid
        if (MAESTRO) in line:
            return SimpleMessage("healer cure")



        # Inny TBM Raid
        if (INNY1) in line:
            return SimpleMessage("fade or feign death")


        if (INNY2) in line:
            return SimpleMessage("run through the aura now")



        # Anashti Sul, Lady of Life
        if (LIFE1) in line:
            return SimpleMessage("Run into the aura")


        # single player
        if (LIFE2) in line:
            return SimpleMessage("Do not get healed, you will explode")


        if (LIFE3) in line:
            return SimpleMessage("Move to the area where the skull is facing")



        # Wither and Decay
        if (WITHER1) in line:
            return SimpleMessage("Run away from the raid")


        # single player
        if (WITHER2) in line:
            return SimpleMessage("Move off of the ooze")



        # Anashti Sul, Damsel of Decay
        # single player
        ANASH1CHAR = ANASHTI1 + character_name
        if (ANASH1CHAR) in line:
            return SimpleMessage("Stop casting disease and corruption based spells")


        if (ANASHTI2) in line:
            return SimpleMessage("The boss has warped")


        # single player
        if (ANASHTI3) in line:
            return SimpleMessage("Your cured")


        # single player
        if (ANASHTI4) in line:
            return SimpleMessage("Do not cure the gift of endless life")


        # single player
        if (ANASHTI5) in line:
            return SimpleMessage("Get curse cure if you do not have gift of endless life buff")


        # single player
        if (ANASHTI6) in line:
            return SimpleMessage("move away from the tendrils")


        # single player
        if (ANASHTI7) in line:
            return SimpleMessage("Cure disease")


        # single player
        if (ANASHTI8) in line:
            return SimpleMessage("Cure disease twice")


        # single player
        if (ANASHTI9) in line:
            return SimpleMessage("Cure disease once")



        # Grannus of the Cleansing Steam
        # single player
        if (GRANNUS1) in line:
            return SimpleMessage("get a corruption cure")


        if (GRANNUS2) in line:
            return SimpleMessage("Pally splash now")


        if (GRANNUS3) in line:
            return SimpleMessage("D P S the portal now")


        if (GRANNUS4) in line:
            return SimpleMessage("Stop nuking")


        if (GRANNUS5) in line:
            return SimpleMessage("Resume nuking")



        # Stem the Tide
        # single player
        TIDECHAR = TIDE + character_name
        if (TIDECHAR) in line:
            return SimpleMessage("Run away from the raid")



        # Grummus!
        # single player
        if (GRUMMUS1) in line:
            return SimpleMessage("Move away from the raid")


        # single player
        GRUM2CHAR = GRUMMUS2 + character_name
        if (GRUM2CHAR) in line:
            return SimpleMessage("Move away from the raid")


        if (GRUMMUS3) in line:
            return SimpleMessage("Grummus is vulnerable, kill, kill, kill")


        if (GRUMMUS4) in line:
            return SimpleMessage("Grummus is invulnerable, your D P S is wasted")



        # High Bokon Boromas
        if (BOKON) in line:
            return SimpleMessage("Cure disease")



        # Anashti Sul, Enslaver of Souls
        # single player
        ENSL1CHAR = ENSLAVER1 + character_name
        if (ENSL1CHAR) in line:
            return SimpleMessage("Run north or south away from the raid")


        if (ENSLAVER2) in line:
            return SimpleMessage("Get close to the raid")


        if (ENSLAVER3) in line:
            return SimpleMessage("Run to the pool with the aura now")


        if (ENSLAVER4) in line:
            return SimpleMessage("Cure disease twice")


        ##### END TBM RAIDS #####


        ##### START 17th Anniversary Raid #####

        # Seventeen pieces of silver raid
        if (HF17) in line:
            return SimpleMessage("run through the aura now")


        ##### END 17th Anniversary Raid #####


        ##### START EoK RAIDS #####

        # Doorstep of War - Lceanium
        if (LCE1) in line:
            return SimpleMessage("Move away from her front")


        if (LCE2) in line:
            return SimpleMessage("Move away from her left side")


        if (LCE3) in line:
            return SimpleMessage("Move away from her right side")


        if (LCE4) in line:
            return SimpleMessage("Move away from her back")



        # The Summoning of Droga - Droga
        # single player
        DROG1CHAR = DROGA1 + character_name
        if (DROG1CHAR) in line:
            return SimpleMessage("move away from droga")


        if (DROGA2) in line:
            return SimpleMessage("move away from the red ring around droga")


        if (DROGA3) in line:
            return SimpleMessage("get corruption cure")


        # single player
        DROG4CHAR = DROGA4 + character_name
        if (DROG4CHAR) in line:
            return SimpleMessage("move away from raid and out of drogas line of sight")


        # single player
        DROG5CHAR = DROGA5 + character_name
        if (DROG5CHAR) in line:
            return SimpleMessage("move out of drogas line of sight")


        # single player
        DROG6CHAR = DROGA6 + character_name
        if (DROG6CHAR) in line:
            return SimpleMessage("you have the red ring. move away from the raid")



        # Queen Velazul Di'zok - Chardok
        if (VELAZUL1) in line:
            return SimpleMessage("move north into the tunnel")

        if (VELAZUL2) in line:
            return SimpleMessage("it is safe to return to the raid")


        ##### END EoK RAIDS #####


        ##### START GENERAL UTILITY ALERTS #####

        # Invis dropped
        if (APPEARING) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE1) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE2) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE3) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE4) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE5) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE6) in line:
            return SimpleMessage("Invisibility Drop")

        if (VISIBLE7) in line:
            return SimpleMessage("Invisibility Drop")

        if (LOST_FOLLOW1) in line:
            return SimpleMessage("Not Following")

        if (LOST_FOLLOW2) in line:
            return SimpleMessage("Not Following")

        if (ALERT_HAIL) in line:
            return SimpleMessage("Hail!")

        if (INVITE) in line:
            return SimpleMessage("Invite")

        if (CHARMBREAK) in line:
            return SimpleMessage("Charm break")

        if (ROOTBREAK1) in line:
            return SimpleMessage("Root break")

        if (ROOTBREAK2) in line:
            return SimpleMessage("Root break")

        if (MEZBREAK1) in line:
            return SimpleMessage("Mez break")

        if (ENTHRALLBREAK1) in line:
            return SimpleMessage("Mez break")

        if (ENTRANCEBREAK1) in line:
            return SimpleMessage("Mez break")

        if (DAZZLEBREAK1) in line:
            return SimpleMessage("Mez break")

        if (FASCINATEBREAK1) in line:
            return SimpleMessage("Mez break")

        if (GENERALBREAK) in line:
            return SimpleMessage("Spell break")

        if (DROPPED_ITEM1) in line:
            return SimpleMessage("Item Drop")

        if (DROPPED_ITEM2) in line:
            return SimpleMessage("Item Drop")

        if (DROPPED_ITEM3) in line:
            return SimpleMessage("Item Drop")

        if (LORE_ITEM) in line:
            return SimpleMessage("Lore Dupe")

        if (REAGENT_FAIL) in line:
            return SimpleMessage("Missing reagent")

        if (NO_MANA) in line:
            return SimpleMessage("Out of Mana")

        if (SPELL_FIZZLE) in line:
            return SimpleMessage("Fizzle")

        if (SPELL_RESIST) in line:
            return SimpleMessage("Resist")

        if (SPELL_INTERRUPT) in line:
            return SimpleMessage("Interrupted")

        if ('tells you,') in line:
            if (TELL_TO_IGNORE1) in line:
                return

            if (TELL_TO_IGNORE2) in line:
                return

            if (TELL_TO_IGNORE3) in line:
                return

            if (TELL_TO_IGNORE4) in line:
                return

            if (TELL_TO_IGNORE5) in line:
                return

            if (TELL_TO_IGNORE6) in line:
                return

            if (TELL_TO_IGNORE7) in line:
                return

            if (TELL_TO_IGNORE8) in line:
                return

            if (TELL_TO_IGNORE9) in line:
                return

            if (TELL_TO_IGNOREA) in line:
                return

            return SimpleMessage("Incoming Tell")


        # Feign death failed
        CHARFALL = character_name + FALLEN
        if (CHARFALL) in line:
            return SimpleMessage("feign death failed")

        if (FDBROKEN) in line:
            return SimpleMessage("feign death was broken")

        # Feign death all clear
        if (FDCLEAR) in line:
            return SimpleMessage("you can get up now")

        # Feign death resist
        if (FDRESIST) in line:
            return SimpleMessage("you resume feigning death")

        # Mez Timers
        if (MEZ) in line:
            return BackgroundTask(19, 'Mez Warn', 'Mez')

        if (FASCINATE) in line:
            return background_task(31, 'Mez Warn', 'Mez')

        if (ENTHRALL) in line:
            return background_task(43, 'Enthrall Warn', 'Mez')

        if (ENTRANCE) in line:
            return background_task(67, 'Entrance Warn', 'Mez')

        if (DAZZLE) in line:
            return background_task(91, 'Dazzle Warn', 'Mez')

