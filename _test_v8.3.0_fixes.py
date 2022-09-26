import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.dispatch_mission import DispatchMission
from lib.game.game import Game
from lib.game.missions import HeroesReunited, IndustrialComplex, DeviantDiversion, MonasteryInTrouble, PowerOfTheDark, \
    MysteriousAmbush, RoadToMonastery, StingOfTheScorpion, SelfDefenseProtocol, DangerousSisters, CosmicRider, \
    InhumanPrincess, MeanAndGreen, DarkAdvent, IncreasingDarkness, Blindsided, LegacyOfBlood, QuantumPower, \
    WingsOfDarkness, ClobberinTime, Hothead, AwManThisGuy, DominoFalls, GoingRogue, FriendsAndEnemies, \
    WeatheringTheStorm, WorldBoss, WorldBossInvasion, Shadowland, GiantBossRaid, CoopPlay, TimelineBattle, \
    AllianceBattle
from lib.game.missions.epic_quest import SmallerHeadsPrevail, BrainsVsBlades, DeadlyAccuracy, DoomsDay, \
    FateOfTheUniverse, PlayingHero, MutualEnemy, BeginningOfTheChaos, TheFault, GoldenGods, VeiledSecret, TwistedWorld, \
    TheBigTwin, StupidXMen, TrueEvolution
from lib.game.missions.events import EventMissions, WorldEvent, FuturePass, EventQuest
from lib.game.missions.story_auto import StoryAuto
from lib.game.routines import DailyTrivia, Alliance, Friends, ArtifactStore, Artifact, CharacterStore

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':
    nox = NoxPlayer("NoxPlayer")  # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)  # Setup your team for PVP missions
    game.set_story_team(4)  # Setup your team for Story Ultimate
    game.USE_CLEAR_TICKETS = True  # Use Clear Tickets when Possible
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_DIMENSIONAL_CLASH_NORMAL')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_TRUE_SHIELD_NORMAL')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_TRUE_SHIELD_ULTIMATE')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_ALL_WAR_NORMAL')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_ALL_WAR_ULTIMATE')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_FUTURE_ENDS_HERE_NORMAL')
    # StoryAuto(game).do_missions(story_mission='STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE')

    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_DIMENSIONAL_CLASH_NORMAL')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_TRUE_SHIELD_NORMAL')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_TRUE_SHIELD_ULTIMATE')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_ALL_WAR_NORMAL')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_ALL_WAR_ULTIMATE')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_FUTURE_ENDS_HERE_NORMAL')
    # StoryAuto(game).combine_story_fragment(story_mission='STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE', times=9)

    # GiantBossRaid(game).do_missions(times=1, max_rewards=True)

    # AllianceBattle(game).do_missions()

    EventQuest(game).acquire_all_rewards()

