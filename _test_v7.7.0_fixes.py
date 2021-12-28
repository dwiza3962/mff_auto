import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.game import Game
from lib.game.missions import HeroesReunited, IndustrialComplex, DeviantDiversion, MonasteryInTrouble, PowerOfTheDark, \
    MysteriousAmbush, RoadToMonastery, StingOfTheScorpion, SelfDefenseProtocol, DangerousSisters, CosmicRider, \
    InhumanPrincess, MeanAndGreen, DarkAdvent, IncreasingDarkness, Blindsided, LegacyOfBlood, QuantumPower, \
    WingsOfDarkness, ClobberinTime, Hothead, AwManThisGuy, DominoFalls, GoingRogue, FriendsAndEnemies, \
    WeatheringTheStorm
from lib.game.missions.events import EventMissions, WorldEvent, FuturePass
from lib.game.routines import DailyTrivia, Alliance, Friends, ArtifactStore, Artifact, CharacterStore

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    # game.USE_CLEAR_TICKETS = True            # Use Clear Tickets when Possible
    game.USE_CLEAR_TICKETS = False            # Use Clear Tickets when Possible
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # World Event
    #WorldEvent(game).complete_world_event()

    # Future Pass
    # FuturePass(game).acquire_points_and_claim_rewards()

    # ArtifactStore(game).acquire_free_artifact_chest()
    # CharacterStore(game).acquire_free_hero_chest()

    # HeroesReunited(game).do_missions()
    #
    # ArtifactStore(game).buy_artifact_chest(chests_to_buy=['1', '2', '3', '4'])

    # Artifact(game).dismantle_artifacts(artifact_stars=['ARTIFACT_DISMANTLE_STAR_1', 'ARTIFACT_DISMANTLE_STAR_2'])

    #IndustrialComplex(game).do_missions(times=1, difficulty=4)
    #DeviantDiversion(game).do_missions(times=1, difficulty=4)

    # Sorcerer Supreme
    # RoadToMonastery(game).do_missions(times=1, difficulty=6)
    MysteriousAmbush(game).do_missions(times=2, difficulty=6)
    # MonasteryInTrouble(game).do_missions(times=1, difficulty=6)
    # PowerOfTheDark(game).do_missions(times=1, difficulty=6)
    # WeatheringTheStorm(game).do_missions(times=1, difficulty=6)
    # FriendsAndEnemies(game).do_missions(times=1, difficulty=6)
    # GoingRogue(game).do_missions(times=1, difficulty=6)
    # DominoFalls(game).do_missions(times=1, difficulty=6)
    # AwManThisGuy(game).do_missions(times=1, difficulty=6)
    # Hothead(game).do_missions(times=1, difficulty=6)
    # ClobberinTime(game).do_missions(times=1, difficulty=6)
    # WingsOfDarkness(game).do_missions(times=1, difficulty=6)
    # QuantumPower(game).do_missions(times=1, difficulty=6)
    # LegacyOfBlood(game).do_missions(times=1, difficulty=6)
    # Blindsided(game).do_missions(times=1, difficulty=6)
    # IncreasingDarkness(game).do_missions(times=1, difficulty=6)
    # DarkAdvent(game).do_missions(times=1, difficulty=6)
    # MeanAndGreen(game).do_missions(times=1, difficulty=6)
    # InhumanPrincess(game).do_missions(times=1, difficulty=6)
    # CosmicRider(game).do_missions(times=1, difficulty=6)
    # DangerousSisters(game).do_missions(times=1, difficulty=6)
    # SelfDefenseProtocol(game).do_missions(times=1, difficulty=6)
    # StingOfTheScorpion(game).do_missions(times=1, difficulty=6)






