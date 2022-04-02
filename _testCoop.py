import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.missions import Shadowland, HeroesReunited, TheFault, DoomsDay, BeginningOfTheChaos, FateOfTheUniverse, \
    PlayingHero, MutualEnemy, CoopPlay
from lib.game.game import Game
from lib.game.routines import DailyTrivia, Alliance, Friends

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # Coop
    CoopPlay(game).do_missions(times=99)
