import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.missions import Shadowland, HeroesReunited, TheFault, DoomsDay, BeginningOfTheChaos, FateOfTheUniverse, \
    PlayingHero, MutualEnemy
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

    # Trivia
    dt = DailyTrivia(game).do_trivia()

    # Friends
    aa = Friends(game).acquire_all()
    sa = Friends(game).send_all()

    # alliance routines
    dc = Alliance(game).check_in()
    dr = Alliance(game).donate_resources()
    csi = Alliance(game).claim_support_item()
    bifs = Alliance(game).buy_items_from_store()
    cefc = Alliance(game).collect_energy_from_challenges()
    cefc = Alliance(game).request_support_item(support_item=SUPPORT_ITEM.BLACK_ANTI_MATTER)



