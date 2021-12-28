import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.game import Game
from lib.game.missions import HeroesReunited, TheFault, DoomsDay, BeginningOfTheChaos, FateOfTheUniverse, \
    PlayingHero, MutualEnemy, IndustrialComplex, DeviantDiversion, StingOfTheScorpion, SelfDefenseProtocol, GoldenGods, \
    MonasteryInTrouble, PowerOfTheDark, MysteriousAmbush, RoadToMonastery, WeatheringTheStorm, FriendsAndEnemies, \
    GoingRogue, DominoFalls, AwManThisGuy, Hothead, ClobberinTime, WingsOfDarkness, QuantumPower, LegacyOfBlood, \
    Blindsided, IncreasingDarkness, DarkAdvent, MeanAndGreen, InhumanPrincess, CosmicRider, DangerousSisters, \
    VeiledSecret, TwistedWorld, TheBigTwin, StupidXMen

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':
    nox = NoxPlayer("NoxPlayer")  # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)  # Set up your team for common missions to get EXP
    game.set_timeline_team(1)  # Set up your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # # Missions
    # # Deluxe Pack Missions
    # #Eternals - Makkari / Gilgamesh
    # HeroesReunited(game).do_missions()
    # # Fantastic Four - Invisible Woman
    # DoomsDay(game).do_missions()
    # # Galactic Imperative - Nova
    # FateOfTheUniverse(game).do_missions()
    # # Dark Avengers - Moonstone
    # PlayingHero(game).do_missions()
    # # X-Men Magneto
    # MutualEnemy(game).do_missions()
    # # X-Force Psylocke
    # BeginningOfTheChaos(game).do_missions()

    # Other Epic Quest Missions - browsable via content status board.
    # Phylla Vell Dimension Shift - Obelisks
    # TheFault(game).do_missions()
    # GoldenGods(game).do_missions()
    # VeiledSecret(game).do_missions()
    # TwistedWorld(game).do_missions()
    # TheBigTwin(game).do_missions()
    # StupidXMen(game).do_missions()

    # Ten Stages Test
    # IndustrialComplex(game).do_missions(times=1, difficulty=4)
    # DeviantDiversion(game).do_missions(times=1, difficulty=4)

    MonasteryInTrouble.do_missions(times=1, difficulty=6)
    # PowerOfTheDark.do_missions(times=1, difficulty=6)
    # MysteriousAmbush.do_missions(times=1, difficulty=6)
    # RoadToMonastery.do_missions(times=1, difficulty=6)
    # WeatheringTheStorm.do_missions(times=1, difficulty=6)
    # FriendsAndEnemies.do_missions(times=1, difficulty=6)
    # GoingRogue.do_missions(times=1, difficulty=6)
    # DominoFalls.do_missions(times=1, difficulty=6)
    # AwManThisGuy.do_missions(times=1, difficulty=6)
    # Hothead.do_missions(times=1, difficulty=6)
    # ClobberinTime.do_missions(times=1, difficulty=6)
    # WingsOfDarkness.do_missions(times=1, difficulty=6)
    # QuantumPower.do_missions(times=1, difficulty=6)
    # LegacyOfBlood.do_missions(times=1, difficulty=6)
    # Blindsided.do_missions(times=1, difficulty=6)
    # IncreasingDarkness.do_missions(times=1, difficulty=6)
    # DarkAdvent.do_missions(times=1, difficulty=6)
    # MeanAndGreen.do_missions(times=1, difficulty=6)
    # InhumanPrincess.do_missions(times=1, difficulty=6)
    # CosmicRider.do_missions(times=1, difficulty=6)
    # DangerousSisters.do_missions(times=1, difficulty=6)
    # SelfDefenseProtocol.do_missions(times=1, difficulty=6)
    # StingOfTheScorpion.do_missions(times=1, difficulty=6)
