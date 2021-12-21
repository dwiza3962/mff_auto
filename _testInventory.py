import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.game import Game
from lib.game.routines import ComicCards, CustomGear, Iso8, Artifact

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # cc = ComicCards(game).upgrade_all_cards()
    # cg = CustomGear(game).quick_upgrade_gear(times=99)
    #
    # iso8upgrade = Iso8(game).upgrade_iso8(times_for_each_upgrade=99,
    #                                       iso_to_use=['ISO8_POWERFUL_ENHANCE', 'ISO8_AMPLIFYING_ENHANCE',
    #                                                      'ISO8_IMPREGNABLE_ENHANCE',
    #                                                      'ISO8_ABSORBING_ENHANCE', 'ISO8_VITAL_ENHANCE',
    #                                                      'ISO8_FIERCE_ENHANCE', 'ISO8_NIMBLE_ENHANCE',
    #                                                      'ISO8_CHAOTIC_ENHANCE'],
    #                                       stars_to_use=['ISO8_ENHANCE_1_STAR', 'ISO8_ENHANCE_2_STAR',
    #                                                                      'ISO8_ENHANCE_3_STAR', 'ISO8_ENHANCE_4_STAR'])
    #
    # iso8combine = Iso8(game).combine_iso8(times_for_each_combine=99, iso_to_combine=['ISO8_CHAOTIC_TAB'])

    da = Artifact(game).dismantle_artifacts(artifact_stars=['ARTIFACT_DISMANTLE_STAR_1', 'ARTIFACT_DISMANTLE_STAR_2'])
