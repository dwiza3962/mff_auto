﻿from lib.game.ui.general import UIElement, Rect, load_ui_image

DM_LABEL = UIElement(name='DM_LABEL')
DM_LABEL.description = "Dimension missions label in lobby."
DM_LABEL.text_rect = Rect(0.053125, 0.01574074074074074, 0.23333333333333334, 0.07685185185185185)
DM_LABEL.text = "DIMENSION MISSION"
DM_LABEL.text_threshold = 150

DM_MISSION = UIElement(name='DM_MISSION')
DM_MISSION.description = "Dimension missions label in mission selection."
DM_MISSION.text_rect = Rect(0.2634610205450469, 0.2717193071722242, 0.4324450559569225, 0.3248902917659314)
DM_MISSION.button_rect = Rect(0.2918742654373091, 0.37540272712995326, 0.47880350814956096, 0.6891115362328258)
DM_MISSION.text = "DIMENSION MISSION"
DM_MISSION.text_threshold = 150

DM_LEVEL = UIElement(name='DM_LEVEL')
DM_LEVEL.description = "Dimension missions stage level."
DM_LEVEL.text_rect = Rect(0.4867943810546886, 0.8027836432629681, 0.512712863885551, 0.8463447793670191)
DM_LEVEL.text_threshold = 220
DM_LEVEL.available_characters = "1234567890"

DM_LEVEL_PLUS = UIElement(name='DM_LEVEL_PLUS')
DM_LEVEL_PLUS.description = "Dimension missions stage level PLUS button."
DM_LEVEL_PLUS.button_rect = Rect(0.5380208333333333, 0.8064814814814815, 0.5635416666666667, 0.8444444444444444)

DM_LEVEL_MINUS = UIElement(name='DM_LEVEL_MINUS')
DM_LEVEL_MINUS.description = "Dimension missions stage level MINUS button."
DM_LEVEL_MINUS.button_rect = Rect(0.43385416666666665, 0.8064814814814815, 0.45989583333333334, 0.8435185185185186)

DM_LEVEL_READY = UIElement(name='DM_LEVEL_READY')
DM_LEVEL_READY.description = "Dimension missions stage level READY button."
DM_LEVEL_READY.text_rect = Rect(0.4556242820532418, 0.8991369253779693, 0.5386208658174816, 0.9642713815052608)
DM_LEVEL_READY.button_rect = Rect(0.4556242820532418, 0.8991369253779693, 0.5386208658174816, 0.9642713815052608)
DM_LEVEL_READY.text = "READY"
DM_LEVEL_READY.text_threshold = 150

DM_SELECT_TEAM_1 = UIElement(name='DM_SELECT_TEAM_1')
DM_SELECT_TEAM_1.description = "Team selector is first team."
DM_SELECT_TEAM_1.button_rect = Rect(0.014389119302779344, 0.13944928258854572, 0.0500152303811026, 0.20216968526365203)

DM_SELECT_TEAM_2 = UIElement(name='DM_SELECT_TEAM_2')
DM_SELECT_TEAM_2.description = "Team selector is second team."
DM_SELECT_TEAM_2.button_rect = Rect(0.01404323472920339, 0.22738082751541056, 0.05036111495467856, 0.2894863242819375)

DM_SELECT_TEAM_3 = UIElement(name='DM_SELECT_TEAM_3')
DM_SELECT_TEAM_3.description = "Team selector is third team."
DM_SELECT_TEAM_3.button_rect = Rect(0.014389119302779344, 0.31223784289937795, 0.05070699952825451, 0.37618805739164335)

DM_SELECT_TEAM_4 = UIElement(name='DM_SELECT_TEAM_4')
DM_SELECT_TEAM_4.description = "Team selector is fourth team."
DM_SELECT_TEAM_4.button_rect = Rect(0.014389119302779344, 0.3995544819176633, 0.05036111495467856, 0.4635046964099287)

DM_SELECT_TEAM_5 = UIElement(name='DM_SELECT_TEAM_5')
DM_SELECT_TEAM_5.description = "Team selector is fifth team."
DM_SELECT_TEAM_5.button_rect = Rect(0.014389119302779344, 0.48625621502736915, 0.05070699952825451, 0.5489766177024756)

DM_START_BUTTON = UIElement(name='DM_START_BUTTON')
DM_START_BUTTON.description = "Dimension Missions START button."
DM_START_BUTTON.text_rect = Rect(0.8706072008744409, 0.8805270807701718, 0.9476220488718887, 0.9483200861271485)
DM_START_BUTTON.button_rect = Rect(0.8706072008744409, 0.8805270807701718, 0.9476220488718887, 0.9483200861271485)
DM_START_BUTTON.text = "START"
DM_START_BUTTON.text_threshold = 150

DM_CLEAR_BUTTON = UIElement(name='DM_CLEAR_BUTTON')
DM_CLEAR_BUTTON.description = "Dimension Missions CLEAR button."
DM_CLEAR_BUTTON.text_rect = Rect(0.4089863409289282, 0.9098476977373177, 0.4896315022192507, 0.9492364272049607)
DM_CLEAR_BUTTON.button_rect = Rect(0.4089863409289282, 0.9098476977373177, 0.4896315022192507, 0.9492364272049607)
DM_CLEAR_BUTTON.text = "CLEAR"
DM_CLEAR_BUTTON.text_threshold = 150

DM_ENERGY_COST = UIElement(name='DM_ENERGY_COST')
DM_ENERGY_COST.description = "Energy cost of staging the Dimension Mission."
DM_ENERGY_COST.text_rect = Rect(0.8199996063914813, 0.8936421049752512, 0.8456944569549456, 0.9324942633598646)
DM_ENERGY_COST.text_threshold = 145
DM_ENERGY_COST.available_characters = "-0123456789"

DM_BOOST_COST = UIElement(name='DM_BOOST_COST')
DM_BOOST_COST.description = "Boost cost of staging the Dimension Mission."
DM_BOOST_COST.text_rect = Rect(0.8128821458152541, 0.8531518203481188, 0.8330206002071651, 0.8855186679152738)
DM_BOOST_COST.text_threshold = 225
DM_BOOST_COST.available_characters = "0123456789-"

DM_ACQUIRE_REWARD = UIElement(name='DM_ACQUIRE_REWARD')
DM_ACQUIRE_REWARD.description = "Dimensions Missions: acquire rewards button."
DM_ACQUIRE_REWARD.button_rect = Rect(0.93125, 0.8805555555555555, 0.9776041666666667, 0.950925925925926)

DM_ACQUIRE_NEXT_REWARD = UIElement(name='DM_ACQUIRE_NEXT_REWARD')
DM_ACQUIRE_NEXT_REWARD.description = "Dimensions Missions: acquire next reward button."
DM_ACQUIRE_NEXT_REWARD.text_rect = Rect(0.5197916666666667, 0.7601851851851852, 0.6390625, 0.8092592592592592)
DM_ACQUIRE_NEXT_REWARD.button_rect = Rect(0.5197916666666667, 0.7601851851851852, 0.6390625, 0.8092592592592592)
DM_ACQUIRE_NEXT_REWARD.text = "Next Reward"
DM_ACQUIRE_NEXT_REWARD.text_threshold = 170

DM_REWARD_ACQUIRED_OK = UIElement(name='DM_REWARD_ACQUIRED_OK')
DM_REWARD_ACQUIRED_OK.description = "Dimensions Missions: OK button at the end of acquiring last reward."
DM_REWARD_ACQUIRED_OK.text_rect = Rect(0.4822916666666667, 0.7592592592592593, 0.5223958333333333, 0.8101851851851852)
DM_REWARD_ACQUIRED_OK.button_rect = Rect(0.4822916666666667, 0.7592592592592593, 0.5223958333333333, 0.8101851851851852)
DM_REWARD_ACQUIRED_OK.text = "OK"
DM_REWARD_ACQUIRED_OK.text_threshold = 150
DM_REWARD_ACQUIRED_OK.available_characters = "OK"

DM_TICKET_NOTIFICATION_USE = UIElement(name='DM_TICKET_NOTIFICATION_USE')
DM_TICKET_NOTIFICATION_USE.description = "Notification of you need to use hidden tickets. Leads to OK (use tickets) button."
DM_TICKET_NOTIFICATION_USE.text_rect = Rect(0.5037197580645162, 0.6987275985663082, 0.6529133064516129, 0.7883333333333333)
DM_TICKET_NOTIFICATION_USE.button_rect = Rect(0.5037197580645162, 0.6987275985663082, 0.6529133064516129, 0.7883333333333333)
DM_TICKET_NOTIFICATION_USE.text = "USE"
DM_TICKET_NOTIFICATION_USE.text_threshold = 150
DM_TICKET_NOTIFICATION_USE.available_characters = "USE"

DM_TICKET_NOTIFICATION_DONT_USE = UIElement(name='DM_TICKET_NOTIFICATION_DONT_USE')
DM_TICKET_NOTIFICATION_DONT_USE.description = "Notification of you need to use hidden tickets. Leads to DON'T (don't use tickets) button."
DM_TICKET_NOTIFICATION_DONT_USE.text_rect = Rect(0.3464616935483871, 0.7058960573476702, 0.49363911290322576, 0.7847491039426523)
DM_TICKET_NOTIFICATION_DONT_USE.button_rect = Rect(0.3464616935483871, 0.7058960573476702, 0.49363911290322576, 0.7847491039426523)
DM_TICKET_NOTIFICATION_DONT_USE.text = "Don't Use"
DM_TICKET_NOTIFICATION_DONT_USE.text_threshold = 150
DM_TICKET_NOTIFICATION_DONT_USE.available_characters = "USE"
