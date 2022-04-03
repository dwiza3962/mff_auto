﻿import lib.game.missions as missions
from lib.gui.widgets.queue_items.general import GameMode


class _LegendaryBattle(GameMode):
    legendary_battles = {
        "Thor: Ragnarok": missions.LegendaryBattle.THOR_RAGNAROK,
        "Black Panther": missions.LegendaryBattle.BLACK_PANTHER,
        "Infinity War": missions.LegendaryBattle.INFINITY_WAR,
        "Ant-Man & The Wasp": missions.LegendaryBattle.ANT_MAN,
        "Captain Marvel": missions.LegendaryBattle.CAPTAIN_MARVEL,
        # "Black Widow": missions.LegendaryBattle.BLACK_WIDOW,
        "Shang-Chi": missions.LegendaryBattle.SHANG_CHI
    }

    def __init__(self, game):
        super().__init__(game, "LEGENDARY BATTLE", missions.LegendaryBattle)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="mode",
                                                       text="Select Legendary Battle mode",
                                                       values_dict={
                                                           "Normal": missions.LegendaryBattle.MODE.NORMAL,
                                                           "Extreme": missions.LegendaryBattle.MODE.EXTREME}))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       text="Select Legendary Battle",
                                                       setting_key="battle",
                                                       values_dict=self.legendary_battles))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       text="Select Legendary Battle mission",
                                                       setting_key="stage",
                                                       values_dict={
                                                           "Battle #1": missions.LegendaryBattle.STAGE.BATTLE_1,
                                                           "Battle #2": missions.LegendaryBattle.STAGE.BATTLE_2,
                                                           "Battle #3": missions.LegendaryBattle.STAGE.BATTLE_3
                                                       }))


class _VeiledSecret(GameMode):

    def __init__(self, game):
        super().__init__(game, "VEILED SECRET", missions.VeiledSecret, "Veiled Secret [Feathers/Crystals]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=4))


class _MutualEnemy(GameMode):

    def __init__(self, game):
        super().__init__(game, "MUTUAL ENEMY", missions.MutualEnemy, "Mutual Enemy [Magneto]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=2))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _StupidXMen(GameMode):

    def __init__(self, game):
        super().__init__(game, "STUPID X-MEN", missions.StupidXMen, "Stupid X-Men [Colossus]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=6))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _TheBigTwin(GameMode):

    def __init__(self, game):
        super().__init__(game, "THE BIG TWIN", missions.TheBigTwin, "The Big Twin [Feathers/Crystals]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=6))


class _BeginningOfTheChaos(GameMode):

    def __init__(self, game):
        super().__init__(game, "BEGINNING OF THE CHAOS", missions.BeginningOfTheChaos,
                         "Beginning Of The Chaos [Psylocke]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=2))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _TwistedWorld(GameMode):

    def __init__(self, game):
        super().__init__(game, "TWISTED WORLD", missions.TwistedWorld, "Twisted World [Victorious]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=6))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _DoomsDay(GameMode):

    def __init__(self, game):
        super().__init__(game, "DOOM'S DAY", missions.DoomsDay, "Doom's Day [Invisible Woman]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=2))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _TheFault(GameMode):

    def __init__(self, game):
        super().__init__(game, "THE FAULT", missions.TheFault, "The Fault [Phyla-Vell]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=6))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _FateOfTheUniverse(GameMode):

    def __init__(self, game):
        super().__init__(game, "FATE OF THE UNIVERSE", missions.FateOfTheUniverse, "Fate Of The Universe [Nova]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=2))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _CoopPlay(GameMode):

    def __init__(self, game):
        super().__init__(game, "CO-OP PLAY", missions.CoopPlay)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=5))


class _AllianceBattle(GameMode):

    def __init__(self, game):
        super().__init__(game, "ALLIANCE BATTLE", missions.AllianceBattle)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="mode",
                                                       text="Select Alliance Battle mode",
                                                       values_dict={
                                                           "All battles (Normal and Extreme)": missions.AllianceBattle.MODE.ALL_BATTLES,
                                                           "Only Normal battle": missions.AllianceBattle.MODE.NORMAL
                                                       }))


class _TimelineBattle(GameMode):

    def __init__(self, game):
        super().__init__(game, "TIMELINE BATTLE", missions.TimelineBattle)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=10))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="skip_opponent_count",
                                                       text="Select how many opponents to skip before each battle",
                                                       min=0, initial_value=0))


class _WorldBosses(GameMode):
    world_bosses = {
        "Today's Boss": missions.WorldBoss.BOSS.TODAYS_BOSS,
        "Proxima Midnight": missions.WorldBoss.BOSS.PROXIMA_MIDNIGHT,
        "Black Dwarf": missions.WorldBoss.BOSS.BLACK_DWARF,
        "Corvus Glaive": missions.WorldBoss.BOSS.CORVUS_GLAIVE,
        "Supergiant": missions.WorldBoss.BOSS.SUPERGIANT,
        "Ebony Maw": missions.WorldBoss.BOSS.EBONY_MAW,
        "Thanos": missions.WorldBoss.BOSS.THANOS,
        "Quicksilver": missions.WorldBoss.BOSS.QUICKSILVER,
        "Cable": missions.WorldBoss.BOSS.CABLE,
        "Scarlet Witch": missions.WorldBoss.BOSS.SCARLET_WITCH,
        "Apocalypse": missions.WorldBoss.BOSS.APOCALYPSE,
        "Knull": missions.WorldBoss.BOSS.KNULL,
        "Mephisto": missions.WorldBoss.BOSS.MEPHISTO
    }

    def __init__(self, game):
        super().__init__(game, "WORLD BOSS", missions.WorldBoss)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=5))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="mode",
                                                       text="Select World Boss mode",
                                                       values_dict={
                                                           "Beginner": missions.WorldBoss.MODE.BEGINNER,
                                                           "Normal": missions.WorldBoss.MODE.NORMAL,
                                                           "Ultimate / Legend": missions.WorldBoss.MODE.ULTIMATE
                                                       }))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="boss",
                                                       text="Select World Boss",
                                                       values_dict=self.world_bosses))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select World Boss stage difficulty",
                                                       min=1, max=99))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="sync_character_and_ally_teams",
                                                       initial_state=False,
                                                       text="Synchronize Character Team and Ally Team selection"))


class _DimensionMissions(GameMode):

    def __init__(self, game):
        super().__init__(game, "DIMENSION MISSION", missions.DimensionMission)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select Dimension Mission stage difficulty",
                                                       min=1, max=15))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="use_hidden_tickets",
                                                       text="Use Hidden Tickets for battle"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="acquire_rewards",
                                                       text="Acquire all contribution rewards at the end"))


class _SquadBattles(GameMode):

    def __init__(self, game):
        super().__init__(game, "SQUAD BATTLE", missions.SquadBattle)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="mode",
                                                       text="Select Squad Battle mode",
                                                       values_dict={
                                                           "All battles": missions.SquadBattle.MODE.ALL_BATTLES,
                                                           "One daily (random)": missions.SquadBattle.MODE.DAILY_RANDOM
                                                       }))


class _WorldBossInvasion(GameMode):

    def __init__(self, game):
        super().__init__(game, "WORLD BOSS INVASION", missions.WorldBossInvasion)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All available"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many times to complete",
                                                       min=1, max=5))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="ignore_coop_mission",
                                                       text="Do not filter characters by Co-op mission",
                                                       initial_state=False))


class _DangerRoom(GameMode):

    def __init__(self, game):
        super().__init__(game, "DANGER ROOM", missions.DangerRoom)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All available daily entries"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="mode",
                                                       text="Select Danger Room mode",
                                                       values_dict={
                                                           "Normal": missions.DangerRoom.MODE.NORMAL,
                                                           "Extreme": missions.DangerRoom.MODE.EXTREME
                                                       }))


class _DangerousSisters(GameMode):

    def __init__(self, game):
        super().__init__(game, "DANGEROUS SISTERS", missions.DangerousSisters, "Dangerous Sisters [Nebula]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _CosmicRider(GameMode):

    def __init__(self, game):
        super().__init__(game, "COSMIC RIDER", missions.CosmicRider, "Cosmic Rider [Punisher]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _QuantumPower(GameMode):

    def __init__(self, game):
        super().__init__(game, "QUANTUM POWER", missions.QuantumPower, "Quantum Power [Gamora]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _WingsOfDarkness(GameMode):

    def __init__(self, game):
        super().__init__(game, "WINGS OF DARKNESS", missions.WingsOfDarkness, "Wings Of Darkness [Darkhawk]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _InhumanPrincess(GameMode):

    def __init__(self, game):
        super().__init__(game, "INHUMAN PRINCESS", missions.InhumanPrincess, "Inhuman Princess [Crystal]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _MeanAndGreen(GameMode):

    def __init__(self, game):
        super().__init__(game, "MEAN AND GREEN", missions.MeanAndGreen, "Mean And Green [She-Hulk]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _ClobberinTime(GameMode):

    def __init__(self, game):
        super().__init__(game, "CLOBBERIN TIME", missions.ClobberinTime, "Clobberin Time [Thing]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _Hothead(GameMode):

    def __init__(self, game):
        super().__init__(game, "HOTHEAD", missions.Hothead, "Hothead [Human Torch]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _AwManThisGuy(GameMode):

    def __init__(self, game):
        super().__init__(game, "AW MAN THIS GUY", missions.AwManThisGuy, "Aw, Man. This Guy? [Fantomex]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _DominoFalls(GameMode):

    def __init__(self, game):
        super().__init__(game, "DOMINO FALLS", missions.DominoFalls, "Domino Falls [Domino]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _GoingRogue(GameMode):

    def __init__(self, game):
        super().__init__(game, "GOING ROGUE", missions.GoingRogue, "Going Rogue [Rogue]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _FriendsAndEnemies(GameMode):

    def __init__(self, game):
        super().__init__(game, "FRIENDS AND ENEMIES", missions.FriendsAndEnemies, "Friends And Enemies [Beast]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _WeatheringTheStorm(GameMode):

    def __init__(self, game):
        super().__init__(game, "WEATHERING THE STORM", missions.WeatheringTheStorm, "Weathering The Storm [Storm]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _Blindsided(GameMode):

    def __init__(self, game):
        super().__init__(game, "BLINDSIDED", missions.Blindsided, "Blindsided [Cyclops]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _DarkAdvent(GameMode):

    def __init__(self, game):
        super().__init__(game, "DARK ADVENT", missions.DarkAdvent, "Dark Advent [Satana/Cleo]")

        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _IncreasingDarkness(GameMode):

    def __init__(self, game):
        super().__init__(game, "INCREASING DARKNESS", missions.IncreasingDarkness,
                         "Increasing Darkness [Hellstorm/Cleo]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _RoadToMonastery(GameMode):

    def __init__(self, game):
        super().__init__(game, "ROAD TO MONASTERY", missions.RoadToMonastery, "Road To Monastery [Baron Mordo]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=6))


class _MysteriousAmbush(GameMode):

    def __init__(self, game):
        super().__init__(game, "MYSTERIOUS AMBUSH", missions.MysteriousAmbush, "Mysterious Ambush [Wong]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=6))


class _MonasteryInTrouble(GameMode):

    def __init__(self, game):
        super().__init__(game, "MONASTERY IN TROUBLE", missions.MonasteryInTrouble,
                         "Monastery In Trouble [Ancient One]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=6))


class _PowerOfTheDark(GameMode):

    def __init__(self, game):
        super().__init__(game, "POWER OF THE DARK", missions.PowerOfTheDark, "Power Of The Dark [Kaecilius]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=6))


class _GiantBossRaid(GameMode):
    def __init__(self, game):
        super().__init__(game, "GIANT BOSS RAID", missions.GiantBossRaid)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="max_rewards",
                                                       text="Use maximum boost points for rewards"))


class _StingOfTheScorpion(GameMode):

    def __init__(self, game):
        super().__init__(game, "STING OF THE SCORPION", missions.StingOfTheScorpion, "Sting Of The Scorpion [Scorpion]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _SelfDefenseProtocol(GameMode):

    def __init__(self, game):
        super().__init__(game, "STING OF THE SCORPION", missions.SelfDefenseProtocol,
                         "Self-Defense Protocol [Green Goblin]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))


class _LegacyOfBlood(GameMode):

    def __init__(self, game):
        super().__init__(game, "LEGACY OF BLOOD", missions.LegacyOfBlood, "Legacy Of Blood [Daken]")

        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _DeadlyAccuracy(GameMode):
    def __init__(self, game):
        super().__init__(game, "DEADLY ACCURACY", missions.LegacyOfBlood, "Deadly Accuracy [Hawkeye]")

        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _PlayingHero(GameMode):

    def __init__(self, game):
        super().__init__(game, "PLAYING HERO", missions.PlayingHero, "Playing Hero [Moonstone]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=2))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _GoldenGods(GameMode):

    def __init__(self, game):
        super().__init__(game, "GOLDEN GODS", missions.GoldenGods, "Golden Gods [Ares]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=6))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )


class _Shadowland(GameMode):
    shadowland_modes = {
        "BEGINNER_ROSTER": missions.Shadowland.RosterMode.BEGINNER_ROSTER,
        "STRONG_ROSTER": missions.Shadowland.RosterMode.STRONG_ROSTER,
        "MAXIMUM_ROSTER": missions.Shadowland.RosterMode.MAXIMUM_ROSTER
    }

    def __init__(self, game):
        super().__init__(game, "SHADOWLAND", missions.Shadowland, "Shadowland [BETA]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many floors to complete",
                                                       min=1, max=99))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="roster_mode",
                                                       text="Select Shadowland Mode",
                                                       values_dict=self.shadowland_modes))


class _StoryMission(GameMode):
    story_missions = {
        "Dimensional Clash [Normal]": missions.Story.STORY_MISSION.DIMENSIONAL_CLASH_NORMAL,
        "Dimensional Clash [Ultimate]": missions.Story.STORY_MISSION.DIMENSIONAL_CLASH_ULTIMATE
    }

    story_stage = {
        "1-1 Emergency Dispatch": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_1_1,
        "1-2 An Unexpected Encounter": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_1_2,
        "1-3 Robotic Theft": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_1_3,
        # NOAUTO_"2-1 The Rescue Plan": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_2_1,
        # NOAUTO_"2-2 Scheme of Advanced Evil": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_2_2,
        # NOAUTO_"2-3 Mad Science to the Max": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_2_3,
        # TODO GOLEFT_"3-1 S.H.I.E.D. Under Siege": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_3_1,
        # TODO GORIGHT_"3-2 Shadow Over The Streets": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_3_2,
        "3-3 Chaos Descends": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_3_3,
        # ALLOVER_"4-1 Crack in the S.H.I.E.L.D.": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_4_1,
        "4-2 The Beginning of the Storm": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_4_2,
        # HERO REFLECT AVOID FIRE "5-1 The Battle for Domination": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_5_1,
        "6-1 An Eternal Nemesis": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_6_1,
        "6-2 The Red Madness": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_6_2,
        "7-1 Emergency Dispatch": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_7_1,
        "7-2 An Unexpected Encounter": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_7_2,
        "7-3 Robotic Theft": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_7_3,
        "8-1 Dimensional Shift": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_8_1,
        # NOAUTO_"8-2 Anti-Matter Recovery": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_8_2,
        "8-3 The Showdown": missions.Story.STORY_STAGE.DIMENSIONAL_CLASH_8_3
    }

    def __init__(self, game):
        super().__init__(game, "STORY MISSION", missions.Story)
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="story_mission",
                                                       text="Select Story Mission",
                                                       values_dict=self.story_missions))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Combobox,
                                                       setting_key="story_stage",
                                                       text="Select mission stage",
                                                       values_dict=self.story_stage))


class _HeroesReunited(GameMode):

    def __init__(self, game):
        super().__init__(game, "HEROES REUNITED", missions.HeroesReunited, "Heroes Reunited [Makkari]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=4))


class _IndustrialComplex(GameMode):

    def __init__(self, game):
        super().__init__(game, "INDUSTRIAL COMPLEX", missions.IndustrialComplex, "Industrial Complex [Sersi]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _DeviantDiversion(GameMode):

    def __init__(self, game):
        super().__init__(game, "DEVIANT DIVERSION", missions.DeviantDiversion, "Deviant Diversion [Black Panther]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _SmallerHeadsPrevail(GameMode):

    def __init__(self, game):
        super().__init__(game, "SMALLER HEADS PREVAIL", missions.DeviantDiversion, "Smaller Heads Prevail [Kingo]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _BrainsVsBlades(GameMode):

    def __init__(self, game):
        super().__init__(game, "BRAINS VS BLADES", missions.DeviantDiversion, "Brains VS Blades [??]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="difficulty",
                                                       text="Select stage difficulty",
                                                       min=1, max=4))


class _TrueEvolution(GameMode):

    def __init__(self, game):
        super().__init__(game, "TRUE EVOLUTION", missions.TrueEvolution, "True Evolution [??]")
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="all_stages",
                                                       text="All stages"))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Spinbox,
                                                       setting_key="times",
                                                       text="Select how many stages to complete",
                                                       min=1, max=2))
        self.mode_settings.append(GameMode.ModeSetting(setting_type=GameMode.ModeSetting.Checkbox,
                                                       setting_key="farm_shifter_bios",
                                                       initial_state=False,
                                                       text="Farm shifter's biometrics (requires restartable emulator)")
                                  )
