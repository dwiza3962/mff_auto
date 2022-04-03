import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.dispatch_mission import DispatchMission
from lib.game.game import Game
from lib.game.missions import HeroesReunited, IndustrialComplex, DeviantDiversion, MonasteryInTrouble, PowerOfTheDark, \
    MysteriousAmbush, RoadToMonastery, StingOfTheScorpion, SelfDefenseProtocol, DangerousSisters, CosmicRider, \
    InhumanPrincess, MeanAndGreen, DarkAdvent, IncreasingDarkness, Blindsided, LegacyOfBlood, QuantumPower, \
    WingsOfDarkness, ClobberinTime, Hothead, AwManThisGuy, DominoFalls, GoingRogue, FriendsAndEnemies, \
    WeatheringTheStorm, WorldBoss, WorldBossInvasion, Shadowland
from lib.game.missions.epic_quest import SmallerHeadsPrevail, BrainsVsBlades, DeadlyAccuracy, DoomsDay, \
    FateOfTheUniverse, PlayingHero, MutualEnemy, BeginningOfTheChaos, TheFault, GoldenGods, VeiledSecret, TwistedWorld, \
    TheBigTwin, StupidXMen
from lib.game.missions.events import EventMissions, WorldEvent, FuturePass
from lib.game.routines import DailyTrivia, Alliance, Friends, ArtifactStore, Artifact, CharacterStore

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.USE_CLEAR_TICKETS = False            # Use Clear Tickets when Possible
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    #WorldBoss(game).change_world_boss_of_the_day(world_boss=['Proxima Midnight', 'Black Dwarf', 'Corvus Glave', 'Supergiant', 'Ebony Maw'], max_resets=99)
    # WorldBossInvasion(game).do_test()
    # WorldBossInvasion(game).do_missions()

    # DispatchMission(game).acquire_all_rewards()
    # World Event
    # WorldEvent(game).complete_world_event()
    # CharacterStore(game).acquire_free_hero_chest()

    #ArtifactStore(game).acquire_free_artifact_chest()
    #
    # ArtifactStore(game).buy_artifact_chest(chests_to_buy=['1', '2', '3', '4'])

    # WorldBoss(game).do_missions(mode=WorldBoss.MODE.ULTIMATE, difficulty=20, boss=WorldBoss.BOSS.TODAYS_BOSS)

    Shadowland(game).do_missions(times=1, roster_mode=Shadowland.RosterMode.STRONG_ROSTER)


