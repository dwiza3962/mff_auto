import lib.logger as logging
from lib.functions import wait_until, r_sleep, is_strings_similar
from lib.game import ui
from lib.game.missions.missions import Missions

logger = logging.get_logger(__name__)


class StoryAuto(Missions):
    """Class for working with Story missions."""

    class STORY_MISSION:
        DIMENSIONAL_CLASH_NORMAL = "STORY_MISSION_DIMENSIONAL_CLASH_NORMAL"
        DIMENSIONAL_CLASH_ULTIMATE = "STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE"
        TRUE_SHIELD_NORMAL = "STORY_MISSION_TRUE_SHIELD_NORMAL"
        TRUE_SHIELD_ULTIMATE = "STORY_MISSION_TRUE_SHIELD_ULTIMATE"
        ALL_WAR_NORMAL = "STORY_MISSION_ALL_WAR_NORMAL"
        ALL_WAR_ULTIMATE = "STORY_MISSION_ALL_WAR_ULTIMATE"
        FUTURE_ENDS_HERE_NORMAL = "STORY_MISSION_FUTURE_ENDS_HERE_NORMAL"
        FUTURE_ENDS_HERE_ULTIMATE = "STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE"

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
        TRUE_SHIELD_9_1 = "STORY_MISSION_TRUE_SHIELD_9_1"
        TRUE_SHIELD_9_2 = "STORY_MISSION_TRUE_SHIELD_9_2"
        TRUE_SHIELD_10_1 = "STORY_MISSION_TRUE_SHIELD_10_1"
        TRUE_SHIELD_10_2 = "STORY_MISSION_TRUE_SHIELD_10_2"
        ALL_WAR_11_1 = "STORY_MISSION_ALL_WAR_11_1"
        ALL_WAR_11_2 = "STORY_MISSION_ALL_WAR_11_2"
        ALL_WAR_12_1 = "STORY_MISSION_ALL_WAR_12_1"
        ALL_WAR_12_2 = "STORY_MISSION_ALL_WAR_12_2"
        FUTURE_ENDS_HERE_13_1 = "STORY_MISSION_FUTURE_ENDS_HERE_13_1"
        FUTURE_ENDS_HERE_13_2 = "STORY_MISSION_FUTURE_ENDS_HERE_13_2"
        FUTURE_ENDS_HERE_13_3 = "STORY_MISSION_FUTURE_ENDS_HERE_13_3"

    def __init__(self, game):
        """Class initialization.

        :param lib.game.game.Game: instance of the game.
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

        logger.info(f"Mission Name: {story_mission}")
        if story_mission.__contains__("FUTURE_ENDS_HERE"):
            self.emulator.drag(ui.STORY_MISSION_DRAG_START_PAGE2, ui.STORY_MISSION_DRAG_END_PAGE2, duration=0.5)
            r_sleep(1)

        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=story_mission_ui):
            logger.debug(f"Opening Story mission {story_mission_ui}")
            self.emulator.click_button(story_mission_ui)
            # TODO: normal start button
            return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.STORY_ULTIMATE_START_BUTTON)
        logger.error(f"Can't open Story mission {story_mission_ui}")

    def _select_start_story_stage(self):
        """Selects stage of Story mission.

        :param str story_stage: UI element that represent mission stage.
        """

        logger.info(f"Moving to the First Mission.")
        while True:
            self.emulator.click_button(ui.STORY_STAGE_MINUS)
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_DIMENSIONAL_CLASH_1_1):
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_TRUE_SHIELD_9_1):
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_ALL_WAR_11_1):
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_FUTURE_ENDS_HERE_13_1):
                break

        # TODO allow this optional param to skip if no daily reward left.   Leaving as default for now.
        logger.info(f"Finding Daily Rewards.")
        available_rewards_str = self.emulator.get_screen_text(ui.STORY_AVAILABLE_REWARDS)
        available_rewards = is_strings_similar(available_rewards_str, "Daily Count 1/1")
        logger.info(f"Available Rewards: {available_rewards}")

        while not available_rewards:
            self.emulator.click_button(ui.STORY_STAGE_PLUS)
            available_rewards_str = self.emulator.get_screen_text(ui.STORY_AVAILABLE_REWARDS)
            available_rewards = is_strings_similar(available_rewards_str, "Daily Count 1/1")
            logger.info(f"Available Rewards: {available_rewards}")
            if available_rewards:
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_DIMENSIONAL_CLASH_8_3):
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_TRUE_SHIELD_10_2):
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_ALL_WAR_12_2):
                break
            if self.emulator.is_ui_element_on_screen(ui.STORY_MISSION_FUTURE_ENDS_HERE_13_3):
                break

        return available_rewards

    def select_team(self):
        """Selects team for missions."""
        team_element = ui.get_by_name(f'STORY_SELECT_TEAM_{self.game.story_team}')
        logger.debug(f"Selecting Story team: {team_element.name}")
        self.emulator.click_button(team_element)

    def do_missions(self, story_mission=None):
        """Does missions.

        :param str story_mission: UI element that represent Story Mission.
        :param str story_stage: UI element that represent mission stage.
        """
        self.start_missions(story_mission=story_mission)
        self.end_missions()

    def start_missions(self, story_mission=None):
        """Starts Story mission."""

        logger.info(f"Params: {story_mission}.")

        do_full_missions = True

        if self.open_story_missions() and self._open_story_mission(story_mission=story_mission):
            logger.info(f"Starting Story Auto.")
            if not self._select_start_story_stage():
                logger.info(f"Daily Rewards already obtained for Story Missions.")
                return
            r_sleep(1)
            if not self.press_start_button():
                return
            while do_full_missions:
                # Running Auto Play
                if wait_until(self.emulator.is_ui_element_on_screen, timeout=3,
                              ui_element=ui.STORY_AUTO_END_BATTLE_LABEL):
                    logger.info("Battle Has Ended.")
                    # Exit Power Save
                    self.emulator.drag(ui.STORY_AUTO_EXIT_POWER_SAVE_1, ui.STORY_AUTO_EXIT_POWER_SAVE_2, duration=0.5)
                    r_sleep(1)
                    self.emulator.drag(ui.STORY_AUTO_EXIT_POWER_SAVE_1, ui.STORY_AUTO_EXIT_POWER_SAVE_2, duration=0.5)
                    do_full_missions = False

                if wait_until(self.emulator.is_ui_element_on_screen, timeout=3,
                              ui_element=ui.STORY_AUTO_POWER_SAVE_BUTTON):
                    logger.info("In Battle Mode, Switching to Power Save.")
                    self.emulator.click_button(ui.STORY_AUTO_POWER_SAVE_BUTTON)

                if wait_until(self.emulator.is_ui_element_on_screen, timeout=3,
                              ui_element=ui.STORY_AUTO_PROGRESS_LABEL):
                    logger.info("In Power Save Mode.")

                if wait_until(self.emulator.is_ui_element_on_screen, timeout=3,
                              ui_element=ui.STORY_AUTO_CLOSE_BUTTON):
                    self.emulator.click_button(ui.STORY_AUTO_CLOSE_BUTTON)
                    do_full_missions = False

                if do_full_missions:
                    logger.info("Battle Still chugging along, continuing to look for mission end.")

        logger.info("No more stages.")
        self.emulator.drag(ui.STORY_AUTO_EXIT_POWER_SAVE_1, ui.STORY_AUTO_EXIT_POWER_SAVE_2, duration=0.5)
        self.emulator.click_button(ui.STORY_AUTO_CLOSE_BUTTON)
        self.press_home_button(home_button=ui.STORY_AUTO_HOME_BUTTON)

    def press_start_button(self, start_button_ui=ui.STORY_ULTIMATE_CLEAR_BUTTON):
        """Presses start button of the mission."""
        self.select_team()
        self.emulator.click_button(start_button_ui)

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=2, ui_element=ui.STORY_AUTO_PROGRESS_BUTTON):
            self.emulator.click_button(ui.STORY_AUTO_PROGRESS_BUTTON)
            logger.info(f"Clicked Auto Use Designated Characters: {self.game.energy}")

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=2, ui_element=ui.STORY_AUTO_PROGRESS_START_BUTTON):
            self.emulator.click_button(ui.STORY_AUTO_PROGRESS_START_BUTTON)
            logger.info(f"Clicked Auto Progress Start: {self.game.energy}")

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=1, ui_element=ui.NOT_ENOUGH_ENERGY):
            self.emulator.click_button(ui.NOT_ENOUGH_ENERGY)
            logger.warning(f"Not enough energy for starting mission, current energy: {self.game.energy}")
            return False

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=1, ui_element=ui.INVENTORY_FULL):
            self.emulator.click_button(ui.INVENTORY_FULL)
            logger.warning("Your inventory is full, cannot start mission.")
            return False

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=1,
                      ui_element=ui.STORY_UNUSABLE_CHARACTER_NOTICE):
            self.emulator.click_button(ui.STORY_UNUSABLE_CHARACTER_NOTICE)
            logger.warning("Your team has unusable characters (not 70lvl/T3/Ascended), cannot start mission.")
            return False

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=1, ui_element=ui.STORY_DAILY_REWARD_NOTICE):
            self.emulator.click_button(ui.STORY_DAILY_REWARD_NOTICE)

        if wait_until(self.emulator.is_ui_element_on_screen, timeout=1,
                      ui_element=ui.ITEM_MAX_LIMIT_NOTIFICATION):
            self.emulator.click_button(ui.ITEM_MAX_LIMIT_NOTIFICATION)

        return True

    def combine_story_fragment(self, story_mission=None, times=1):
        logger.warning(f"Combine Story Fragment for {story_mission}.")
        if self.open_story_missions() and self._open_story_mission(story_mission=story_mission):
            while times > 0:
                if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.STORY_COMBINE_FRAGMENT_BUTTON):
                    self.emulator.click_button(ui.STORY_COMBINE_FRAGMENT_BUTTON)
                    if wait_until(self.emulator.is_ui_element_on_screen,
                                  ui_element=ui.STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON):
                        self.emulator.click_button(ui.STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON)
                    if wait_until(self.emulator.is_ui_element_on_screen,
                                  ui_element=ui.STORY_COMBINE_FRAGMENT_UI_COMBINE):
                        self.emulator.click_button(ui.STORY_COMBINE_FRAGMENT_UI_COMBINE)

                if wait_until(self.emulator.is_ui_element_on_screen, timeout=1, ui_element=ui.INVENTORY_FULL):
                    self.emulator.click_button(ui.INVENTORY_FULL)
                    logger.warning("Your inventory is full,cannot combine.")
                    break

                if wait_until(self.emulator.is_ui_element_on_screen,
                              ui_element=ui.INSUFFICIENT_MATERIALS_NOTIFICATION):
                    self.emulator.click_button(ui.INSUFFICIENT_MATERIALS_NOTIFICATION)
                    self.emulator.click_button(ui.INSUFFICIENT_MATERIALS_NOTIFICATION)
                    logger.warning("Insufficient Materials.")
                    break

                if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.STORY_COMBINE_FRAGMENT_OK, timeout=5):
                    logger.info("Successfully Combined.")
                    self.emulator.click_button(ui.STORY_COMBINE_FRAGMENT_OK)
                    times = times - 1

                if times > 0:
                    logger.info("Combining again.")

        self.end_missions()
