﻿from lib.gui.widgets.queue_items.general import Action
import lib.game.missions as missions
import lib.game.routines as routines
from lib.game.dispatch_mission import DispatchMission


class _RestartGame(Action):

    def __init__(self, game):
        super().__init__(game, "RESTART GAME", game.restart_game)


class _DailyTrivia(Action):

    def __init__(self, game):
        self.daily_trivia = routines.DailyTrivia(game)
        super().__init__(game, "DAILY TRIVIA", self.daily_trivia.do_trivia)


class _DailyRewards(Action):

    def __init__(self, game):
        self.daily_rewards = routines.DailyRewards(game)
        super().__init__(game, "DAILY REWARDS: ACQUIRE ALL", self.daily_rewards.acquire_all_daily_rewards)


class _ComicCards(Action):

    def __init__(self, game):
        self.comic_cards = routines.ComicCards(game)
        super().__init__(game, "COMIC CARDS: UPGRADE ALL", self.comic_cards.upgrade_all_cards)


class _CustomGear(Action):

    def __init__(self, game):
        self.custom_gear = routines.CustomGear(game)
        super().__init__(game, "CUSTOM GEAR: UPGRADE", self.custom_gear.quick_upgrade_gear)
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.Spinbox,
                                                     setting_key="times",
                                                     text="Select how many time to upgrade"))


class _WaitBoostPoints(Action):

    def __init__(self, game):
        self.wait_until = routines.WaitUntil(game)
        super().__init__(game, "WAIT FOR BOOST POINTS", self.wait_until.wait_until_boost_points)
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.Spinbox,
                                                     setting_key="value",
                                                     text="Wait until boost points value is equal or greater than",
                                                     initial_value=100,
                                                     max=9999))


class _FriendsSendAll(Action):

    def __init__(self, game):
        self.friends = routines.Friends(game)
        super().__init__(game, "FRIENDS: SEND ALL TOKENS", self.friends.send_all)


class _FriendsAcquireAll(Action):

    def __init__(self, game):
        self.friends = routines.Friends(game)
        super().__init__(game, "FRIENDS: ACQUIRE ALL TOKENS", self.friends.acquire_all)


class _AllianceCheckIn(Action):

    def __init__(self, game):
        self.alliance = routines.Alliance(game)
        super().__init__(game, "ALLIANCE: CHECK-IN", self.alliance.check_in)


class _CollectFreeEnergy(Action):

    def __init__(self, game):
        self.store = routines.EnergyStore(game)
        super().__init__(game, "ENERGY: COLLECT FREE 24H", self.store.collect_free_energy)


class _CollectEnergyViaAssemblePoints(Action):

    def __init__(self, game):
        self.store = routines.EnergyStore(game)
        super().__init__(game, "ENERGY: COLLECT VIA ASSEMBLE POINTS", self.store.collect_energy_via_assemble_points)
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.Checkbox,
                                                     setting_key="use_all_points",
                                                     text="Use all available Assemble Points"))


class _WaitMaxEnergy(Action):

    def __init__(self, game):
        self.wait_until = routines.WaitUntil(game)
        super().__init__(game, "WAIT FOR MAX ENERGY", self.wait_until.wait_until_max_energy)


class _WaitDailyReset(Action):

    def __init__(self, game):
        self.wait_until = routines.WaitUntil(game)
        super().__init__(game, "WAIT DAILY RESET", self.wait_until.wait_until_daily_reset)
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.Spinbox,
                                                     setting_key="hour_offset",
                                                     text="Offset in hours before daily reset",
                                                     initial_value=0, min=0, max=24))


class _AcquireDispatchMissionRewards(Action):

    def __init__(self, game):
        self.dispatch_mission = DispatchMission(game)
        super().__init__(game, "DISPATCH MISSION: ACQUIRE ALL REWARDS", self.dispatch_mission.acquire_all_rewards)


class _AcquireAllGifts(Action):

    def __init__(self, game):
        self.inbox = routines.Inbox(game)
        super().__init__(game, "INBOX - GIFTS: ACQUIRE ALL", self.inbox.acquire_all_gifts)
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.Checkbox,
                                                     setting_key="acquire_energy",
                                                     text="Acquire energy",
                                                     initial_state=False))


class _AcquireAllChests(Action):

    def __init__(self, game):
        self.inbox = routines.Inbox(game)
        super().__init__(game, "INBOX - CHESTS: ACQUIRE ALL", self.inbox.acquire_all_chests)


class _ResetWorldBoss(Action):
    world_bosses = {
        "Proxima Midnight": missions.WorldBoss.BOSS_OF_THE_DAY.PROXIMA_MIDNIGHT,
        "Black Dwarf": missions.WorldBoss.BOSS_OF_THE_DAY.BLACK_DWARF,
        "Corvus Glave": missions.WorldBoss.BOSS_OF_THE_DAY.CORVUS_GLAIVE,
        "Supergiant": missions.WorldBoss.BOSS_OF_THE_DAY.SUPERGIANT,
        "Ebony Maw": missions.WorldBoss.BOSS_OF_THE_DAY.EBONY_MAW,
        "Thanos": missions.WorldBoss.BOSS_OF_THE_DAY.THANOS,
        "Quicksilver": missions.WorldBoss.BOSS_OF_THE_DAY.QUICKSILVER,
        "Cable": missions.WorldBoss.BOSS_OF_THE_DAY.CABLE,
        "Scarlet Witch": missions.WorldBoss.BOSS_OF_THE_DAY.SCARLET_WITCH,
        "Apocalypse": missions.WorldBoss.BOSS_OF_THE_DAY.APOCALYPSE,
        "Knull": missions.WorldBoss.BOSS_OF_THE_DAY.KNULL,
        "Mephisto": missions.WorldBoss.BOSS_OF_THE_DAY.MEPHISTO

    }

    def __init__(self, game):
        self.world_boss = missions.WorldBoss(game)
        super().__init__(game, "RESET TODAY'S WORLD BOSS", self.world_boss.change_world_boss_of_the_day)
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.Spinbox,
                                                     setting_key="max_resets",
                                                     text="Max times of resets",
                                                     min=0, max=99, initial_value=99))
        self.mode_settings.append(Action.ModeSetting(setting_type=Action.ModeSetting.MultiCheckbox,
                                                     setting_key="world_boss",
                                                     values_dict=self.world_bosses))
