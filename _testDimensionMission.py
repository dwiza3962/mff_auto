import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.game import Game
from lib.game.missions import DimensionMission
from lib.game.missions.events import EventMissions, WorldEvent, FuturePass
from lib.game.routines import DailyTrivia, Alliance, Friends

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # Dimension Mission
    DimensionMission(game).do_missions(times=1, acquire_rewards=True, use_hidden_tickets=True)
