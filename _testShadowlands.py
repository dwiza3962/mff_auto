import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.missions import Shadowland
from lib.game.game import Game

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    #sl = Shadowland(game).do_missions(times=35)
    sl = Shadowland(game).do_missions(times=10)
