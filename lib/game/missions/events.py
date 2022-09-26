﻿from asyncio import sleep

import lib.logger as logging
from lib.functions import wait_until, r_sleep, is_strings_similar
from lib.game import ui
from lib.game.battle_bot import ManualBattleBot
from lib.game.missions.missions import Missions
from lib.game.missions.world_boss import WorldBoss

logger = logging.get_logger(__name__)


class EventMissions(Missions):
    """Class for working with Event missions."""

    def __init__(self, game):
        """Class initialization.

        :param lib.game.game.Game game: instance of the game.
        """
        super().__init__(game)

    def _is_event_ui_has_same_name(self, name, event_ui, similar_to_full_line):
        """Checks if event UI element has same name as given event name.

        :param str name: event name.
        :param ui.UIElement event_ui: event UI Element
        :param bool similar_to_full_line: take name of event as full line of text or part of any line.
        """
        event_text = self.emulator.get_screen_text(event_ui)
        logger.debug(f"Found text inside event list: {event_text}")
        if similar_to_full_line and is_strings_similar(event_text, name):
            return True
        if not similar_to_full_line:
            for line in event_text.split("\n"):
                if is_strings_similar(line, name):
                    return True

    def find_event_ui_by_name(self, name, similar_to_full_line=True):
        """Finds UI element of Event by it's name.

        :param str name: name of event.
        :param bool similar_to_full_line: take name of event as full line of text or part of any line.

        :rtype ui.UIElement
        """
        self._drag_event_list_to_the_bottom()
        for ui_index in range(1, 5):
            event_ui = ui.get_by_name(f"EVENT_BUTTON_1_{ui_index}")
            if self._is_event_ui_has_same_name(name=name, event_ui=event_ui, similar_to_full_line=similar_to_full_line):
                return event_ui
        self._drag_event_list_to_the_top()
        for ui_index in range(1, 5):
            event_ui = ui.get_by_name(f"EVENT_BUTTON_2_{ui_index}")
            if self._is_event_ui_has_same_name(name=name, event_ui=event_ui, similar_to_full_line=similar_to_full_line):
                return event_ui

    def _drag_event_list_to_the_top(self):
        """Drags Event List to the top."""
        logger.debug("Dragging Event list to the top.")
        self.emulator.drag(ui.EVENT_LIST_DRAG_FROM, ui.EVENT_LIST_DRAG_TO)
        r_sleep(1)

    def _drag_event_list_to_the_bottom(self):
        """Drags Event List to the bottom."""
        logger.debug("Dragging Event list to the bottom.")
        self.emulator.drag(ui.EVENT_LIST_DRAG_TO, ui.EVENT_LIST_DRAG_FROM)
        r_sleep(1)


class EventWorldBoss(EventMissions, WorldBoss):
    """Class for working with Event World Boss."""

    EVENT_NAME = "Event World Boss\nEVENT"

    def __init__(self, game):
        """Class initialization.

        :param lib.game.game.Game game: instance of the game.
        """
        super(EventMissions, self).__init__(game)
        self._stages = 5

    @property
    def battle_over_conditions(self):
        def allies():
            return self.emulator.is_ui_element_on_screen(ui.EVENT_WORLD_BOSS_ALLIES)

        def cannot_enter():
            if self.emulator.is_ui_element_on_screen(ui.EVENT_WORLD_BOSS_LIMIT_REACHED):
                logger.info("Reached limit of missions.")
                self._stages = 0
                self.emulator.click_button(ui.EVENT_WORLD_BOSS_LIMIT_REACHED)
                return True

        return [allies, cannot_enter]

    def open_event_world_boss(self):
        """Opens Event World Boss from Event List."""
        self.game.go_to_main_menu()
        event_ui = self.find_event_ui_by_name(self.EVENT_NAME)
        if not event_ui:
            return logger.warning("Can't find Event World Boss, probably event isn't on right now.")
        self.emulator.click_button(event_ui)
        return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_BOSS_LABEL)

    def complete_event_world_boss(self, sync_character_and_ally_teams=False):
        """Completes all available stages in Event World Boss."""
        self.open_event_world_boss()
        if not self.emulator.is_ui_element_on_screen(ui.EVENT_WORLD_BOSS_ENTER):
            logger.info("No available Event World Boss battles.")
            return self.game.go_to_main_menu()
        self._sync_character_and_ally_teams = sync_character_and_ally_teams
        self.emulator.click_button(ui.EVENT_WORLD_BOSS_ENTER)
        while self._stages > 0:
            if not self._start_world_boss_battle():
                logger.error("Failed to start battle. Returning to main menu.")
                return self.game.go_to_main_menu()
            self._stages -= 1
            if self._stages > 0:
                self.press_repeat_button()
            else:
                self.press_home_button(home_button=ui.EVENT_WORLD_BOSS_HOME_BUTTON)
        logger.info("No more stages.")

    def press_repeat_button(self, repeat_button_ui=ui.EVENT_WORLD_BOSS_REPEAT_BUTTON, start_button_ui=ui.WB_SET_TEAM):
        """Presses repeat button of the mission."""
        logger.debug(f"Clicking REPEAT button with UI Element: {repeat_button_ui}.")
        self.emulator.click_button(repeat_button_ui)
        while not self.emulator.is_ui_element_on_screen(ui_element=start_button_ui):
            if self.emulator.is_ui_element_on_screen(ui.EVENT_WORLD_BOSS_LIMIT_REACHED):
                logger.debug("Reached limit of missions.")
                self._stages = 0
                self.emulator.click_button(ui.EVENT_WORLD_BOSS_LIMIT_REACHED)
                return True
            self.close_after_mission_notifications(timeout=1)
        return True

    def _start_world_boss_battle(self, check_inventory=True):
        """Starts World Boss battle."""
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_SET_TEAM):
            self._deploy_characters()
            self.emulator.click_button(ui.WB_SET_TEAM)
            if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_UNAVAILABLE_CHARACTER):
                logger.warning("Stopping battle because your team has unavailable characters.")
                self.emulator.click_button(ui.WB_UNAVAILABLE_CHARACTER)
                return False
            if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_LOW_VALOR_OR_ATTACK):
                self.emulator.click_button(ui.WB_LOW_VALOR_OR_ATTACK)
                # Second notification about ATK is similar
                if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_LOW_VALOR_OR_ATTACK):
                    self.emulator.click_button(ui.WB_LOW_VALOR_OR_ATTACK)
            if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_START_BUTTON):
                self._deploy_allies()
                self.emulator.click_button(ui.WB_START_BUTTON)
                if check_inventory and wait_until(self.emulator.is_ui_element_on_screen, timeout=2,
                                                  ui_element=ui.INVENTORY_FULL):
                    logger.warning("Stopping battle because inventory is full.")
                    self.emulator.click_button(ui.INVENTORY_FULL)
                    self.stages *= 0
                    return False
                if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_NOT_FULL_ALLY_TEAM):
                    self.emulator.click_button(ui.WB_NOT_FULL_ALLY_TEAM)
                if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.WB_EXCLUDE_CHARACTERS_FROM_ALLIES):
                    self.emulator.click_button(ui.WB_EXCLUDE_CHARACTERS_FROM_ALLIES)
                ManualBattleBot(self.game, self.battle_over_conditions).fight(move_around=True)
                self.close_mission_notifications()
                return True
            logger.error(f"Failed to locate {ui.WB_START_BUTTON} button.")
            return False
        logger.error("Failed to set team.")


class WorldEvent(EventMissions):
    """Class for working with World Event."""

    EVENT_NAME = "WORLD EVENT\nAvailable Now"

    @property
    def battle_over_conditions(self):
        def total_score():
            if self.emulator.is_ui_element_on_screen(ui.EVENT_WORLD_BATTLE_TOTAL_SCORE):
                self.emulator.click_button(ui.EVENT_WORLD_BATTLE_TOTAL_SCORE)
                return True

        return [total_score]

    def open_world_event(self):
        """Opens World Event in Event List."""
        self.game.go_to_main_menu()
        event_ui = self.find_event_ui_by_name(self.EVENT_NAME)
        if not event_ui:
            return logger.warning("Can't find World Event, probably event isn't on right now.")
        self.emulator.click_button(event_ui)
        return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_LABEL)

    def _get_ready_to_battle(self):
        """Gets ready to participate in World Event."""
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_BATTLE_READY_BUTTON):
            logger.debug("Getting ready to battle.")
            self.emulator.click_button(ui.EVENT_WORLD_BATTLE_READY_BUTTON)
            if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_SELECT_BATTLE_READY):
                logger.debug("Selecting battle system.")
                self.emulator.click_button(ui.EVENT_WORLD_SELECT_BATTLE_READY)
                if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_SELECT_BATTLE_READY_OK):
                    logger.debug("System selected.")
                    self.emulator.click_button(ui.EVENT_WORLD_SELECT_BATTLE_READY_OK)

    def complete_world_event(self):
        """Completes available stage in World Event."""
        self.open_world_event()
        self.emulator.click_button(ui.EVENT_WORLD_LOBBY_READY_BUTTON)
        logger.debug("Clicked: EVENT_WORLD_LOBBY_READY_BUTTON: " + ui.EVENT_WORLD_LOBBY_READY_BUTTON.text)
        if self.emulator.is_ui_element_on_screen(ui_element=ui.EVENT_WORLD_BATTLE_READY_BUTTON):
            self.emulator.click_button(ui.EVENT_WORLD_BATTLE_READY_BUTTON)
            logger.debug("Clicked: EVENT_WORLD_BATTLE_READY_BUTTON: " + ui.EVENT_WORLD_BATTLE_READY_BUTTON.text)
            self.emulator.click_button(ui.EVENT_WORLD_SELECT_BATTLE_READY)
            logger.debug("Clicked: EVENT_WORLD_SELECT_BATTLE_READY: " + ui.EVENT_WORLD_SELECT_BATTLE_READY.text)
            # if self.emulator.is_ui_element_on_screen(ui_element = ui.EVENT_WORLD_SELECT_BATTLE_READY):
            #     self.emulator.click_button(ui.EVENT_WORLD_SELECT_BATTLE_READY)
            #     logger.debug("Clicked: EVENT_WORLD_SELECT_BATTLE_READY: " + ui.EVENT_WORLD_SELECT_BATTLE_READY.text)
            # if self.emulator.is_ui_element_on_screen(ui_element = ui.EVENT_WORLD_SELECT_BATTLE_READY_OK):
            self.emulator.click_button(ui.EVENT_WORLD_SELECT_BATTLE_READY_OK)
            logger.debug("Clicked: EVENT_WORLD_SELECT_BATTLE_READY_OK: " + ui.EVENT_WORLD_SELECT_BATTLE_READY_OK.text)
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_BATTLE_START_BUTTON):
            self.emulator.click_button(ui.EVENT_WORLD_BATTLE_START_BUTTON)
            ManualBattleBot(self.game, self.battle_over_conditions).fight(move_around=True)
            self.emulator.click_button(ui.EVENT_WORLD_BATTLE_TOTAL_SCORE)
            self.game.go_to_main_menu()
        return


class FuturePass(EventMissions):
    """Class for working with Future Pass event."""

    EVENT_NAME = "FUTURE PASS"

    def open_future_pass(self):
        """Opens Future Pass in Event List."""
        self.game.go_to_main_menu()
        event_ui = self.find_event_ui_by_name(self.EVENT_NAME, similar_to_full_line=False)
        if not event_ui:
            return logger.warning("Can't find Future Pass, probably event isn't on right now.")
        self.emulator.click_button(event_ui)
        self.close_ads()
        return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_FUTURE_PASS_LABEL)

    def _acquire_free_points(self):
        """Acquires free points.

        :return: were points acquired or not.
        :rtype: bool
        """
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_FUTURE_PASS_ACQUIRE_POINTS):
            logger.info("Acquiring free points.")
            self.emulator.click_button(ui.EVENT_FUTURE_PASS_ACQUIRE_POINTS)
            r_sleep(1)  # Wait for animation
            return True
        logger.info("No available free points.")
        return False

    def _claim_rewards(self):
        """Claims all rewards.

        :return: were points acquired or not.
        :rtype: bool
        """
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_FUTURE_PASS_CLAIM_REWARDS):
            logger.info("Claiming all rewards.")
            self.emulator.click_button(ui.EVENT_FUTURE_PASS_CLAIM_REWARDS)
            if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_FUTURE_PASS_CLAIM_REWARDS_CLOSE):
                self.emulator.click_button(ui.EVENT_FUTURE_PASS_CLAIM_REWARDS_CLOSE)
                return True
        logger.info("No available rewards to claim.")
        return False

    def acquire_points_and_claim_rewards(self):
        """Acquires free points and claim all available rewards."""
        self.open_future_pass()
        self._acquire_free_points()
        self._claim_rewards()
        self.game.go_to_main_menu()


class BattleWorld(EventMissions):
    """Class for working with Future Pass event."""

    EVENT_NAME = "BATTLE WORLD"

    def open_battle_world(self):
        """Opens Future Pass in Event List."""
        self.game.go_to_main_menu()
        event_ui = self.find_event_ui_by_name(self.EVENT_NAME, similar_to_full_line=False)
        if not event_ui:
            return logger.warning("Can't find Battle World, probably event isn't on right now.")
        self.emulator.click_button(event_ui)
        return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_BATTLE_WORLD_LABEL_SELECT)

    # def select_mission(self):

    def complete_battle_world(self):
        """Completes available stage in World Event."""
        self.open_battle_world()
        logger.debug("!!!!get ready for battle")
        # if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_LOBBY_READY_BUTTON):
        #     logger.debug("Entering into team selection lobby.")
        #     self.emulator.click_button(ui.EVENT_WORLD_LOBBY_READY_BUTTON)
        #     logger.debug("Entering into team selection lobby.")
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_WORLD_BATTLE_START_BUTTON):
            self.emulator.click_button(ui.EVENT_WORLD_BATTLE_START_BUTTON)
            ManualBattleBot(self.game, self.battle_over_conditions).fight(move_around=True)
            self.emulator.click_button(ui.EVENT_WORLD_BATTLE_TOTAL_SCORE)
            self.game.go_to_main_menu()

        return

class EventQuest(EventMissions):
    """Class for working with Future Pass event."""

    EVENT_NAME = "EVENT QUEST"

    def open_event_quest(self):
        """Opens Future Pass in Event List."""
        self.game.go_to_main_menu()
        event_ui = self.find_event_ui_by_name(self.EVENT_NAME, similar_to_full_line=False)
        if not event_ui:
            return logger.warning(f"Can't find {self.EVENT_NAME}, probably event isn't on right now.")
        self.emulator.click_button(event_ui)
        self.close_ads()
        return wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_QUEST_LABEL)

    def _acquire_rewards(self):
        if wait_until(self.emulator.is_ui_element_on_screen, ui_element=ui.EVENT_QUEST_ACQUIRE_ALL):
            logger.info("Acquiring all rewards.")
            self.emulator.click_button(ui.EVENT_QUEST_ACQUIRE_ALL)
            r_sleep(1)  # Wait for animation
            return True
        logger.info("No rewards.")
        return False
    def acquire_all_rewards(self):
        """Acquired all available daily rewards from Daily Challenges."""
        self.open_event_quest()
        self._acquire_rewards()
        self.close_mission_notifications(5)
        self.game.go_to_main_menu()
