import lib.logger as logging
from lib.emulators.nox_player import NoxPlayer
from lib.game.missions import Shadowland, HeroesReunited, TheFault, DoomsDay, BeginningOfTheChaos, FateOfTheUniverse, \
    PlayingHero, MutualEnemy
from lib.game.game import Game
from lib.game.routines import DailyTrivia, Alliance, Friends, SupportShop
from lib.game.routines.store import EnergyStore, ArtifactStore, CharacterStore

logger = logging.get_logger(__name__)
logging.create_file_handler()

if __name__ == '__main__':

    nox = NoxPlayer("NoxPlayer")              # Use your window's name of emulator to get a handle

    game = Game(nox)
    game.set_mission_team(3)                  # Setup your team for common missions to get EXP
    game.set_timeline_team(1)                 # Setup your team for PVP missions
    game.ACQUIRE_HEROIC_QUEST_REWARDS = True  # Setup ability to collect Heroic Quest rewards

    # Store Purchases - Free Artifact, Free Hero, Gold Purchase Artifact, Support Shop
    # EnergyStore(game).collect_free_energy()
    # EnergyStore(game).collect_energy_via_assemble_points()
    #
    # ArtifactStore(game).acquire_free_artifact_chest()
    ArtifactStore(game).buy_artifact_chest(chests_to_buy=['STORE_ARTIFACT_CHEST_1', 'STORE_ARTIFACT_CHEST_2', 'STORE_ARTIFACT_CHEST_3', 'STORE_ARTIFACT_CHEST_4'])

    # CharacterStore(game).acquire_free_hero_chest()

    # SupportShop(game).buy_materials(materials_list=['SUPPORT_SHOP_MATERIAL_MKRAAN_SHARD', 'SUPPORT_SHOP_MATERIAL_UNIFORM_UPGRADE_KIT'])
