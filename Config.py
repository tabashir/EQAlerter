# Configuration File for EQAlerter and EQAlerter-Discord: Config.py
# Purpose: User defined variable configuration for the EQAlerter.py and EQAlerter-Discord utilities
# Usage: The variables below define strings that the program will watch for in the character's log file.
#        The current defaults cover most raid encounters from the RoF expansion and beyond, as well as
#        a few general utilities such as invisibility dropping and feigh death failing.
#
# NOTE: If you add new variables and strings to this configuration file you MUST
#       add the supporting logic code and define alerts in EQAlerter.py to support them.


#### USER DEFINED VARIABILES - CHANGE THE VALUES TO SUIT YOUR NEEDS ####

# eq installation directory
EQHOME = "<EQ Folder HERE>"

## Discord specific settings - only needed if using Discord Bot version ##
# general chat channel ID on discord server
GENERAL_ID = '<INSERT DISCORD CHANNEL ID>'

# Discord Bot TOKEN - DO NOT SHARE!
TOKEN = '<INSERT YOUR BOT TOKEN>'

#### END OF USER DEFINED VARIABLES ####


#### DO NOT EDIT BELOW THIS LINE UNLESS YOU KNOW WHAT YOUR DOING! SEE THE NOTE ABOVE! ####

# defaults adapted from: http://everquest.fanra.info/wiki/Raid_audio_triggers

##### START RoF #####
# A Matter of Life and Death - Chapterhouse
MARNEK1 = "Marnek enters the realm of the dead"
MARNEK2 = "A Corpse Collector begins to drag"

# Dispelling the Shadows - Plane of Shadow
SHADOW1 = "You are struck by a pulse of"                    	# Signals the need for a group heal
SHADOW2 = "points at "                            	        # Target DA or self DA and then stand right underneath Shadow of Luclin, She will perma-aggro this person even if DA and you can continue to DPS
SHADOW3 = "raises its sword at "                          	# Frontal Cone DD at that player, move away from front
SHADOW4 = "aims a straight cut at "                        	# Beam DD (front and back), move out of range
SHADOW5 = "glances around itself"                           	# AE DD, Back away
SHADOW6 = "shadows will consume you, "                      	# Run away from raid, return only when it fades. FAILURE WILL WIPE THE RAID
SHADOW7 = "the chamber flares and trembles"                 	# Casts Shadow Annihilation, a debuff with 100K damage amplifier and snare
                                                                	# When you have this debuff, run and HIDE behind a pillar until she fires Shadow Explosion, 
                                                                	# return only when it fades. If missed, when Luclin casts Shadow Explosion, 
                                                                        # you will PBAE everyone around you for 100K damage. This starts at 15% Luclin health. FAILURE WILL WIPE THE RAID

# Glimpse, the Unseen - The Threshold
GLIMPSE = "You shall not escape my sight, "                     # When you get this you must run over 600' away from the raid
                                                                	# This means from the fight spot you must run east off the platform and into the tunnel to the east
                                                                	# After 12 seconds you can return. You might also want to make yourself invulnerable 
                                                                	# somehow (DA or similar) if you can before the 12 seconds, or you are likely to die

# Ulrich the Ageless - The Threshold
ULRICH1 = "You feel your life drain away"                   	# You have a DoT on you. To remove it before you die, run through one of the auras around the room
                                                                        # Do not linger in the aura or you will get another DoT on you. Just run right through it and do not double back
ULRICH2 = "Your bones ache"                                 	# The DoT above was not cured and it now has entered the terminal stage
                                                                    # Unless you run through an aura or make yourself invulnerable somehow (DA or similar) you will soon lose 5 million hit points

# Monarch Widow - The Threshold
MONARCH = "The Monarch Widow begins to spin a web around"   	# In about 10 seconds, a "sticky web" will spawn at the location the player named in this emote was standing at the time of the emote
                                                                    # The entire raid needs to move about 50' counter-clockwise, fighting the Widow there

# An End to Fear - The Epicenter
ENDFEAR1 = "You have been marked for punishment"            	# Move out of Xarics melee range and wait for it to wear off
ENDFEAR2 = "You feel a weight of impending doom"            	# Call for curse cure, 80 counters
ENDFEAR3 = "The corruption of Cazic infests your body"      	# Call for corruption cure, 55 counters
ENDFEAR4 = "Xaric has become vulnerable to death"           	# Kill Xaric
ENDFEAR5 = "You are oppressed by misery"                    	# Stop all casting and attacking until it wears off
##### END RoF #####


##### START CoF #####

# Bixie Warfront: Pelzia's Plot raid.

PELZIA1 = "A yellow cloud forms above "                   	# Run west away from others.
PELZIA2 = "A red cloud forms above "                      	# Run east away from others.

# The Dead Hills: Xulous Prime raid.

XULOUS1 = "begins to form around you"                       	# An aura "Cloud of Disease" is heading for you. You need to kite it.
XULOUS2 = "A cloud of disease moves toward you"             	# An aura "Cloud of Disease" is heading for you. You need to kite it.
XULOUS3 = "Your flesh begins to bubble and ooze"            	# You have a disease on you that must be cured.
XULOUS4 = "The stench of decay renders you weak"            	# You are in a disease aura and need to move out of it.
XULOUS5 = "Your flesh rots"                                 	# You need to gate or otherwise get out.


# Neriak - Fourth Gate: Houses of Thex raid.

THEX1 = "Sooo cooooold"                                     	# Move out of range.
THEX2 = "Get the one called "                            	# Run east away from the raid. Note there is a comma after the player name in the trigger phrase.
                                                                	# 10 seconds after that emote, you will get hit by Sonic Shock (you might be lucky and resist it).
                                                                	# Sonic Shock: Targeted AE 75', Chromatic (-900), Decrease Hitpoints by 70000 per tick, lasts for 24 seconds.
                                                                	# If this hits you, unless you get heals spammed on you, you will die. If you are near anyone (75 feet) 
                                                                	# you will also give it to them and you will wipe the raid.
THEX3 = "An energy pulse moves toward "                    	# Kite until the aura fades away.
                                                                	# This one means you have to kite the energy pulse. 
                                                                	# They seem to come from behind the Bone Crusher and move out toward the person called. 
                                                                	# They move slowly. You do NOT run when you get this emote. 
                                                                	# You move a bit toward Bone Crusher away from people and wait for the energy pulse to approach you.
                                                                	# Then you kite it around. After a few minutes it seemed to stop following me or it despawned. 
                                                                	# Either way, I seemed free to go back to rejoin everyone.
THEX4 = "You are zapped by electricity"                     	# Get out of the lightning pulse.
THEX5 = "The one called "                                	# Run away from the raid. 10 seconds after this emote, Nightmare Devourer will cast Grave Chill on you. You can then rejoin the raid.


# Neriak - Fourth Gate: Hate Rising raid.

HATERISING1 = "You are bombarded by icy rain"               	# Move out of the damaging aura.
HATERISING2 = "is pinned to the ground by a spear"          	# Move at least 30' away from whoever is being pinned.

# Tower of Rot: Lord Kyle Bayle raid.

BAYLE1 = "Bayle raises his ancient claymore high"           	# Move out of melee range, call back pets. Main tank remains.
BAYLE2 = "Lord Kyle Bayle swings his ancient claymore"      	# All clear to resume melee, send in pets.

# Argin-Hiz: Burn Out raid.

BURNOUT1 = "The rolling blaze painfully burns your skin"    	# Move out of the aura.
BURNOUT2 = "I call to you, Solusek Ro"                      	# Imps are spawning, make yourself invisible at once.
BURNOUT3 = "the flames of the other grow much stronger"     	# Minibosses are out of balance. Balance them.
BURNOUT4 = "a wildfire phoenix swoops down"                 	# Phoenix spawn.

# The Void (H): The Journey Home raid.

JOURNEY1 = "begins to spin his sickle"                      	# Zebuxoruk is casting Cyclonic Sickle. This is a point blank area effect spell. You need to back off out of range.
JOURNEY2 = "Your mind is penetrated by ravings"             	# Zebuxoruk is casting Zebuxoruk's Ravings or Forsaken Ravings. 
                                                                	# Single target on melee and hybrid only (12 second Countdown to AE charm). 
                                                                	# If missed, 24 second charm on anyone in range of you. You must run away from the raid by taking a portal to another island.
JOURNEY3 = "prepares to beat Selo's Drum"                   	# Lanys T'Vyl is casting Selo's Frenzy (charm) on the main tank. Next tank needs to get ready.
JOURNEY4 = "stokes the Flame of Ro"                         	# Lanys T'Vyl is casting Ro's Flaming Swath (80' frontal beam doom DoT). 
                                                                	# If not cured in 30 seconds it'll hit everyone nearby for 161k DD. 
                                                                	# Pet Owners: When it fires you must BACK OFF YOUR PET, because the beam can hit your pet 
                                                                	# which then causes the nearby main tanks on Lanys to be hit with the Doom DoT effect, which when it fades kills the tanks.
JOURNEY5 = "You begin to burn"                              	# You have been hit by the Ro's Flaming Swath DoT (above). You have 30 seconds to be cured of 75 curse counters or you will die.
JOURNEY6 = "raises the Qeynos Claymore"                     	# Lanys T'Vyl is about to smack those near her with Qeynos Technique (115K DD plus 23K DoT and AC debuff).
JOURNEY7 = "as strong as you think, "                    	# Lanys T'Vyl is about to cast a frontal AE at the character named. You need to move out of line of sight of her, run and hide. 
                                                                    # This will hit others between you and her, that is why you need to hide from her.
JOURNEY8 = "see how weak you are, "                        	# You got hit by the above. Get corruption cured. May take two casts of the cure.
JOURNEY9 = "this was my island, "                        	# Lanys T'Vyl is about to try to knock you off the island (which would kill you) in 5 seconds. Move away from the edges.
JOURNEY10 = "This island shall be your grave"               	# Lanys T'Vyl is about to kill anyone on the main island. You need to go to the island you were assigned to now.
JOURNEY11 = "Your soul begins to wither"                    	# Zebuxoruk has cast Wasting on you. Spell casters only should get hit by this. You need a corruption cure or you are likely to die.

##### END CoF #####


##### START Fifteenth Anniversary #####

# The Plane of War: 15th anniversary raid.

POW15 = "appears to be taking aim at this area"             	# Tallon Zek is going to put an AE in a circular area, move out of it. 
                                                                    # Most will be able to see the circle on the ground if you have the right particle effects on.

##### END Fifteenth Anniversary #####


##### START TDS #####

# Defense of the City

TDSDEF1 = "You feel faint claws scratching at your back"    	# Get away from everyone else (10 seconds to move).
TDSDEF2 = "Dark claws rake at your body"                    	# You have been hit by the area effect from the trigger above. It is now safe for you to go back to the rest of the raid.
TDSDEF3 = "You resist the Pillar of Claws spell"            	# You have been hit by the area effect from first trigger above but you resisted taking damage. 
                                                                    # It is now safe for you to go back to the rest of the raid.
TDSDEF4 = "unleashes a Pillar of Claws on "                	# You have been hit by the area effect from the first trigger above. It is now safe for you to go back to the rest of the raid.
TDSDEF5 = "Your limbs are bound"                            	# Get disease cured.

# Principal Quastori Numicia

QUASI1 = "cuts you with a"                                  	# You are in a damaging aura. You need to move out of it.
QUASI2 = "You are jolted by a terrible spark of lightning"  	# You need to run away from everyone else and remain away until the effect on you is gone.

# Praetor Vitio
VITIO1 = "holds the hammer in his left hand high overhead"  	# Move away from Praetor Vitio's left side.
VITIO2 = "holds the sword in his right hand high overhead"  	# Move away from Praetor Vitio's right side.
VITIO3 = "holds both of his weapons out to his sides"       	# Move away from Praetor Vitio.
VITIO4 = "begins to focus the power of the citadel"         	# Move close to Praetor Vitio.
VITIO5 = "takes note of the invaders standing behind him"   	# Move away from Praetor Vitio's back.
VITIO6 = "prepares to strike"                                   # This will only happen to the main tank. Praetor Vitio will cast a Death Touch on you if you don't drop aggro. 
                                                                    # You need to drop aggro and let the next tank take him.
VITIO7 = "Someone else should take his attention"               # This happens at the same time as the trigger above. The main tank is dropping aggro and the next tank is taking over. 
                                                                    # Everyone involved needs to be ready for the switch.

# Principal Vicarum Nomia
NOMIA1 = "The principal pulls on your soul"                     # Move away from named.
NOMIA2 = "freezing liquid swirls about your feet"               # Move away from blob.
NOMIA3 = " has attracted the attention"                        # Run away from the raid.
NOMIA4 = "Cold spreads up from your feet"                       # Run around the room until you have moved a total of 60 feet, or get corruption cured. 
                                                                    # When you have succeeded this icon (hand) will disappear from your buff window.
NOMIA5 = "Now these totems will prove your undoing"             # Totems up, DPS them.
NOMIA6 = "You are hit with an explosion of ice"                 # Move from the area.
NOMIA7 = "Principal Vicarum Nomia begins to cast a spell"       # <Icesplosion> - Back away from boss for 10 seconds.
NOMIA8 = "life cannot be restored to dead flesh"                # Totems up, heal them.
NOMIA9 = "a phasma frigasia points a bony finger at you"        # AE inc on you. Run away.

##### END TDS #####


##### START TBM #####

# Plane of Hate: Revisited raid.

# Maestro of Rancor
MAESTRO = "A dissonant chord rings in your ears"               # You have Dissonant Muse on you. This means you have 6 Seconds to get a corruption cure to avoid the mana drain. 
                                                                    # If not cured and you still have Dissonant Muse on you when the Maestro casts Dissonant Tone you get pretty much death touched. 
                                                                    # Cure Dissonant Muse or you will die shortly.

# Innorukk
INNY1 = "You are done in by bad things"                         # This is the trigger for the increased hate. If you get this you should fade, if possible.
INNY2 = "You feel a sense of doom upon you"                     # Run to the aura (visible as purple/blue sparklies) which will randomly move between one of three circles of runestones, 
                                                                    # running into it removes doom so you do NOT receive the 125k DD.  

# Anashti Sul, Lady of Life
LIFE1 = "Anasthi Sul grants holistic health to her assailants"  # Everyone sees/hears this trigger but it only applies to the names mentioned when it goes off (yellow text across the screen). 
                                                                    # If you get the Holistic Health buff on your screen (melee and tanks only usually but can hit anyone), 
                                                                    # melee Anashti Sul to lower her regen so DPS can burn her down. At 10 seconds left of the buff (which will be in your buff window) 
                                                                    # RUN INTO THE AURA OR YOU DIE AND SPAWN AN ADD. Note that her name is misspelled in this trigger, 
                                                                    # that is Daybreak's error, use the spelling given here.

LIFE2 = "You feel an overwhelming and dangerous burst"          # If anyone heals you, you explode. So run through the hallway away from the raid until the red buff wears off. 
                                                                    # DO NOT HEAL THIS PERSON(S)'. Note that you should make a hot key letting your group and the raid know to not heal you.

LIFE3 = "I, Dartain, do your bidding mistress"                  # This will follow up with text across your screen in yellow with what direction the skull in the center of the room will be facing. 
                                                                    # MOVE TO NOT BE IN THE AREA OF THE ROOM THAT THE SKULL IS FACING.

# Wither and Decay
WITHER1 = "Decay spews a pile of living vomit"                  # Run away from the raid.
WITHER2 = "You decay rapidly. You have taken"                   # You are on top of an ooze, move.

# Anashti Sul, Damsel of Decay
ANASHTI1 = "Anashti Sul, Damsel of Decay moans 'Ahhh, that feels much better. I am disease and corruption incarnate, "    # Stop using disease and corruption spells.
ANASHTI2 = "Anashti Sul laughs, 'I am not even there"           # Boss has Warped
ANASHTI3 = "You've drawn the ire of Anashti Sul"                # You cured Gift of Endless Life (the good one!!)
ANASHTI4 = "You receive the Gift of Endless Life"               # DO NOT CURE!
ANASHTI5 = "You receive the Gift of Living Death"               # Check First! Get Curse Cured if you don't have Endless Life DoT.
ANASHTI6 = "You are lashed by tendrils of pestilence"           # MOVE away from the tendrils
ANASHTI7 = "Your bones are brittle"                             # Tanks and Healers: Cure Disease ONCE! DPS: Cure Disease TWICE!
ANASHTI8 = "Your faith falters"                                 # Healers: Cure Disease TWICE!.
ANASHTI9 = "Your muscles atrophy"                               # DPS: Cure Disease ONCE!

# Grannus of the Cleansing Steam
GRANNUS1 = "Your health is linked to another"                   # Get corruption cure.
GRANNUS2 = "Grannus is now sharing his pain with"               # Paladin's Splash Now!!
GRANNUS3 = "The death of the morphling creature"                # Portal is vulnerable, go DPS it (if instructed to).
GRANNUS4 = "Grannus's life force is reinforced"                 # Spells are being reflected from Grannus - Stop nuking
GRANNUS5 = "Grannus's protective magic has been broken"         # Spell reflection down, nuke away!

# Stem the Tide
TIDE = "I will destroy you "                                    # When you get this you have 10 seconds to run away from the raid or you will AE everyone around you for 92k. Possibly can be cured.

# Grummus!
GRUMMUS1 = "Flames erupt where you stand"                       # Viral DoT, move from the raid.
GRUMMUS2 = "Grummus kicks a barrel at "                         # You are targeted with a barrel, so move, and everyone around you needs to also move.
GRUMMUS3 = "You have succeeded in breaking Grummus"             # Grummus is vulnerable, kill him.
GRUMMUS4 = "Grummus is surrounded by a protective aura"         # Shield is up, Grumuus is invulnerable.

# High Bokon Boromas
BOKON = "you feel weak"                                         # Get a disease cure.

# Anashti Sul, Enslaver of Souls

ENSLAVER1 = "Anashti Sul envelops "                             # Run north or south away from the raid. A DoT will appear in your song window. Get heals until it goes away and then you can rejoin the raid.
ENSLAVER2 = "You have been targeted for poison blast"           # Make sure you are close to the majority of the raid.
ENSLAVER3 = "Stand and watch in horror as I melt"               # Run to the pool with the aura. Run now, do not pass Go, do not collect $200.
ENSLAVER4 = "Your flesh begins to rot"                          # Get disease cured. May take more than one cast.

##### END TBM #####


##### START 17th Anniversary #####
# 17th Anniversary raid - Hate's Fury: Seventeen Pieces of Silver

HF17 = "Rise, rise! It is time for you to bring them death"     # When you get this you should locate an aura and start heading toward it, 
                                                                    # when the dot lands 10 seconds later step in then step immediately OUT so others can cure 
                                                                    # (only a small number of people can be cured at the same time). 
                                                                    # NOTE - MIST is cast 4 times in a row so be prepared to move in and out of the Aura repeatedly.

##### END 17th Anniversary #####


##### START EoK #####

# Doorstep of War - Lceanium
LCE1 = "Gorenaire takes a deep inhalation"                  	# Frontal AE incoming
LCE2 = "Gorenaire's left wing twitches"                     	# Directional AE. Move from her left side
LCE3 = "Gorenaire's right wing twitches"                    	# Directional AE. Move from her right side
LCE4 = "Gorenaire's tail twitches"                          	# Rear AE incoming. Move from her back side

# The Summoning of Droga - Droga
DROGA1 = "The Incarnate Droga summons "           	# Move away from the Boss
DROGA2 = "Droga prepares to splash the blood"               	# Boss is about to AE, move away - can see a big red ring to avoid
DROGA3 = "You are marked as a sacrificial offering"         	# Get corruption cure
DROGA4 = "The Incarnate Droga craves "            	# Move out of the boss's line of sight and away from the raid
DROGA5 = "Points his axe at "                     	# Move away from the front of the boss out of line of sight
DROGA6 = "The Incarnate Droga stares at "         	# Red ring around one player, move away from the raid and ask for a poison cure

# Prince Selrach Di'zok - Chardok
# TODO: timers for events, this will take some work to support this event

# Queen Velazul Di'zok - Chardok
VELAZUL1 = "Sunlight gathers around you"                    	# Run away from the raid north until you are in the tunnel (away from the open sky)
VELAZUL2 = "You are safe from the Doomlight"                	# You can now return to the raid

##### END EoK #####


##### START GENERAL UTILITY #####

# adapted from http://www.icynic.com/~don/EQ/triggers/

# Invis dropped
APPEARING = "You feel yourself starting to appear"
VISIBLE1 = "You appear"
VISIBLE2 = "You become visible"
VISIBLE3 = "You return to view"
VISIBLE4 = "Your shadows fade"
VISIBLE5 = "The mystical foliage vanishes"
VISIBLE6 = "The cloud of indifference fades"
VISIBLE7 = "Your body shifts into phase"

# Feign Death
FALLEN = " has fallen to the ground"
FDBROKEN = "You are no longer feigning death"
FDRESIST = "The strength of your will allows you to resume feigning death"
FDCLEAR =  "Your enemies have forgotten you"

LONG_MEZ = " has been mesmerized"

CHARMBREAK = " charm spell has worn off"

ROOTBREAK = " root spell has worn off"

##### END GENERAL UTILITY #####

#### END OF FILE ####
