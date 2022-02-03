import lib.logger as logging
from lib.functions import wait_until
from lib.game import ui
from lib.game.battle_bot import ManualBattleBot
from lib.game.missions.missions import Missions

logger = logging.get_logger(__name__)


class Story(Missions):
    """Class for working with Story missions."""

    class STORY_MISSION:
        DIMENSIONAL_CLASH_NORMAL = "STORY_MISSION_DIMENSIONAL_CLASH_NORMAL"
        DIMENSIONAL_CLASH_ULTIMATE = "STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE"

    class STORY_STAGE:
        DIMENSIONAL_CLASH_1_1 = "STORY_MISSION_DIMENSIONAL_CLASH_1_1"
        DIMENSIONAL_CLASH_1_2 = "STORY_MISSION_DIMENSIONAL_CLASH_1_2"
        DIMENSIONAL_CLASH_1_3 = "STORY_MISSION_DIMENSIONAL_CLASH_1_3"
        DIMENSIONAL_CLASH_2_1 = "STORY_MISSION_DIMENSIONAL_CLASH_2_1"
        DIMENSIONAL_CLASH_2_2 = "STORY_MISSION_DIMENSIONAL_CLASH_2_2"
        DIMENSIONAL_CLASH_2_3 = "STORY_MISSION_DIMENSIONAL_CLASH_2_3"
        DIMENSIONAL_CLASH_3_1 = "STORY_MISSION_DIMENSIONAL_CLASH_3_1"
        DIMENSIONAL_CLASH_3_2 = "STORY_MISSION_DIMENSIONAL_CLASH_3_2"
        DIMENSIONAL_CLASH_3_3 = "STORY_MISSION_DIMENSIONAL_CLASH_3_3"
        DIMENSIONAL_CLASH_4_1 = "STORY_MISSION_DIMENSIONAL_CLASH_4_1"
        DIMENSIONAL_CLASH_4_2 = "STORY_MISSION_DIMENSIONAL_CLASH_4_2"
        DIMENSIONAL_CLASH_5_1 = "STORY_MISSION_DIMENSIONAL_CLASH_5_1"
        DIMENSIONAL_CLASH_6_1 = "STORY_MISSION_DIMENSIONAL_CLASH_6_1"
        DIMENSIONAL_CLASH_6_2 = "STORY_MISSION_DIMENSIONAL_CLASH_6_2"
        DIMENSIONAL_CLASH_7_1 = "STORY_MISSION_DIMENSIONAL_CLASH_7_1"
        DIMENSIONAL_CLASH_7_2 = "STORY_MISSION_DIMENSIONAL_CLASH_7_2"
        DIMENSIONAL_CLASH_7_3 = "STORY_MISSION_DIMENSIONAL_CLASH_7_3"
        DIMENSIONAL_CLASH_8_1 = "STORY_MISSION_DIMENSIONAL_CLASH_8_1"
        DIMENSIONAL_CLASH_8_2 = "STORY_MISSION_DIMENSIONAL_CLASH_8_2"
        DIMENSIONAL_CLASH_8_3 = "STORY_MISSION_DIMENSIONAL_CLASH_8_3"

    def __init__(self, game):
        """Class initialization.

        :param lib.game.game.Game game: instance of the game.
        """
        super().__init__(game, mode_name='STORY')

    @property
    def battle_over_conditions(self):
        def rewards():
            return self.emulator.is_ui_element_on_screen(ui.STORY_BATTLE_REWARDS)

        def home_button():
            if self.emulator.is_image_on_screen(ui.HOME_BUTTON) or \
                    self.emulator.is_image_on_screen(ui.HOME_BUTTON_POSITION_2) or \
                    self.emulator.is_image_on_screen(ui.HOME_BUTTON_POSITION_3):
                return True

        return [rewards, home_button]

    def open_story_missions(self):
        """Opens Story missions from Mission selector.

        :return: was mission lobby opened.
        :rtype: bool
        """
        if not self.game.go_to_mission_selection():
            return logger.error("Can't go into Mission selection.")
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.STORY_MISSION):
            self.emulator.click_button(ui.STORY_MISSION)
            return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.STORY_LABEL)

    def _open_story_mission(self, story_mission):
        """Opens given Story mission from Story lobby.

        :param str story_mission: UI element that represent Story Mission.

        :rtype: bool
        """
        story_mission_ui = ui.get_by_name(story_mission)
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=story_mission_ui):
            logger.debug(f"Opening Story mission {story_mission_ui}")
            self.emulator.click_button(story_mission_ui)
            # TODO: normal start button
            return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.STORY_ULTIMATE_START_BUTTON)
        logger.error(f"Can't open Store mission {story_mission_ui}")

    def _select_story_stage(self, story_stage):
        """Selects stage of Story mission.

        :param str story_stage: UI element that represent mission stage.
        """
        while not self.emulator.is_ui_element_on_screen(ui.get_by_name(story_stage)):
            logger.info(f"Clicking Minus Button")
            self.emulator.click_button(ui.STORY_STAGE_MINUS)
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_DIMENSIONAL_CLASH_1_1):
                break
        while not self.emulator.is_ui_element_on_screen(ui.get_by_name(story_stage)):
            logger.info(f"Clicking Plus Button")
            self.emulator.click_button(ui.STORY_STAGE_PLUS)
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_DIMENSIONAL_CLASH_8_3):
                break



    def select_team(self):
        """Selects team for missions."""
        team_element = ui.get_by_name(f'STORY_SELECT_TEAM_{self.game.mission_team}')
        logger.debug(f"Selecting Story team: {team_element.name}")
        self.emulator.click_button(team_element)

    def do_missions(self, times=None, story_mission=None, story_stage=None):
        """Does missions.

        :param int times: how many stages to complete.
        :param str story_mission: UI element that represent Story Mission.
        :param str story_stage: UI element that represent mission stage.
        """
        self.start_missions(times=times, story_mission=story_mission, story_stage=story_stage)
        self.end_missions()

    def start_missions(self, times=0, story_mission=None, story_stage=None):
        """Starts Story mission."""
        if self.open_story_missions() and self._open_story_mission(story_mission=story_mission):
            logger.info(f"Starting Story {times} times.")
            while times > 0:
                self._select_story_stage(story_stage=story_stage)
                if not self.press_start_button():
                    return
                ManualBattleBot(self.game, self.battle_over_conditions).fight(move_around=False, move_forward=True)
                times -= 1
                if times > 0:
                    self.press_repeat_button(repeat_button_ui=ui.STORY_REPEAT_BUTTON,
                                             start_button_ui=ui.STORY_ULTIMATE_START_BUTTON)
                else:
                    self.press_home_button(home_button=ui.STORY_HOME_BUTTON)
        logger.info("No more stages.")

    def press_start_button(self, start_button_ui=ui.STORY_ULTIMATE_START_BUTTON):
        """Presses start button of the mission."""
        if self.emulator.is_ui_element_on_screen(start_button_ui):
            self.select_team()
            self.emulator.click_button(start_button_ui)
            if wait_until(self.emulator.is_ui_element_on_screen, timeout=2, ui_element=ui.NOT_ENOUGH_ENERGY):
                self.emulator.click_button(ui.NOT_ENOUGH_ENERGY)
                logger.warning(f"Not enough energy for starting mission, current energy: {self.game.energy}")
                return False
            if wait_until(self.emulator.is_ui_element_on_screen, timeout=2, ui_element=ui.INVENTORY_FULL):
                self.emulator.click_button(ui.INVENTORY_FULL)
                logger.warning("Your inventory is full, cannot start mission.")
                return False
            if wait_until(self.emulator.is_ui_element_on_screen, timeout=2,
                          ui_element=ui.STORY_UNUSABLE_CHARACTER_NOTICE):
                self.emulator.click_button(ui.STORY_UNUSABLE_CHARACTER_NOTICE)
                logger.warning("Your team has unusable characters (not 70lvl/T3/Ascended), cannot start mission.")
                return False
            if wait_until(self.emulator.is_ui_element_on_screen, timeout=2, ui_element=ui.STORY_DAILY_REWARD_NOTICE):
                self.emulator.click_button(ui.STORY_DAILY_REWARD_NOTICE)
            if wait_until(self.emulator.is_ui_element_on_screen, timeout=2,
                          ui_element=ui.ITEM_MAX_LIMIT_NOTIFICATION):
                self.emulator.click_button(ui.ITEM_MAX_LIMIT_NOTIFICATION)
            return True
        logger.error(f"Unable to press {start_button_ui} button.")
        return False
