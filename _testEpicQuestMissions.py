import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.missions import Shadowland, HeroesReunited, TheFault, DoomsDay, BeginningOfTheChaos, FateOfTheUniverse, \
    PlayingHero, MutualEnemy
from lib.game.game import Game

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # Missions
    # Deluxe Pack Missions
    # Eternals - Makkari / Gilgamesh
    hr = HeroesReunited(game).do_missions()
    # Fantastic Four - Invisible Woman
    # dd = DoomsDay(game).do_missions()
    # # Galactic Imperative - Nova
    # fotu = FateOfTheUniverse(game).do_missions()
    # # Dark Avengers - Moonstone
    # ph = PlayingHero(game).do_missions()
    # # X-Men Magneto
    # xm = MutualEnemy(game).do_missions()
    # # X-Force Psylocke
    # botc = BeginningOfTheChaos(game).do_missions()

    # Other Epic Quest Missions
    # Phylla Vell Dimension Shift - Obelisks
    # tf = TheFault(game).do_missions()
