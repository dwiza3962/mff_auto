from lib.game.ui.general import UIElement, Rect, load_ui_image

STORY_LABEL = UIElement(name='STORY_LABEL')
STORY_LABEL.description = "Story label in mission selection."
STORY_LABEL.text_rect = Rect(0.05036168385307978, 0.021815679581800397, 0.11466534334609442, 0.07099884033097952)
STORY_LABEL.text = "STORY"
STORY_LABEL.text_threshold = 150

STORY_MISSION = UIElement(name='STORY_MISSION')
STORY_MISSION.description = "Story missions label in mission selection."
STORY_MISSION.text_rect = Rect(0.008489533485535331, 0.27969495486128026, 0.0690546081243049, 0.3222317425362461)
STORY_MISSION.button_rect = Rect(0.051857117794777766, 0.37141490328542515, 0.20140051196457923, 0.6705016916250284)
STORY_MISSION.text = "STORY"
STORY_MISSION.text_threshold = 150

STORY_ULTIMATE_START_BUTTON = UIElement(name='STORY_ULTIMATE_START_BUTTON')
STORY_ULTIMATE_START_BUTTON.description = "The mission start button."
STORY_ULTIMATE_START_BUTTON.text_rect = Rect(0.8339690693028394, 0.8991369253779693, 0.9304245585423615, 0.9602835576607327)
STORY_ULTIMATE_START_BUTTON.button_rect = Rect(0.8339690693028394, 0.8991369253779693, 0.9304245585423615, 0.9602835576607327)
STORY_ULTIMATE_START_BUTTON.text = "START"
STORY_ULTIMATE_START_BUTTON.text_threshold = 100

STORY_BATTLE_REWARDS = UIElement(name='STORY_BATTLE_REWARDS')
STORY_BATTLE_REWARDS.description = "Story: rewards notice at the end of the battle."
STORY_BATTLE_REWARDS.text_rect = Rect(0.3053331709125912, 0.7595630908194879, 0.6948937127249242, 0.804758427724139)
STORY_BATTLE_REWARDS.text = "Rewards can be found in the Inventory or from your Inbox."
STORY_BATTLE_REWARDS.text_threshold = 100

STORY_REPEAT_BUTTON = UIElement(name='STORY_REPEAT_BUTTON')
STORY_REPEAT_BUTTON.description = "Story repeat button."
STORY_REPEAT_BUTTON.button_rect = Rect(0.6896355353075171, 0.8987854251012146, 0.8052391799544419, 0.9615384615384616)

STORY_HOME_BUTTON = UIElement(name='STORY_HOME_BUTTON')
STORY_HOME_BUTTON.description = "Story home button."
STORY_HOME_BUTTON.button_rect = Rect(0.5535307517084282, 0.8997975708502024, 0.6594533029612756, 0.9615384615384616)

STORY_STAGE_MINUS = UIElement(name='STORY_STAGE_MINUS')
STORY_STAGE_MINUS.description = "Story: stage minus button."
STORY_STAGE_MINUS.button_rect = Rect(0.9229473888338714, 0.1321454726137429, 0.9416403131050965, 0.16404806336996713)

STORY_SELECT_TEAM_1 = UIElement(name='STORY_SELECT_TEAM_1')
STORY_SELECT_TEAM_1.description = "Team selector is first team."
STORY_SELECT_TEAM_1.button_rect = Rect(0.6603595401297643, 0.354592517636274, 0.6712928908365738, 0.37740994519831145)

STORY_SELECT_TEAM_2 = UIElement(name='STORY_SELECT_TEAM_2')
STORY_SELECT_TEAM_2.description = "Team selector is second team."
STORY_SELECT_TEAM_2.button_rect = Rect(0.7169277459606486, 0.35543760754597903, 0.7292871858900857, 0.37867758006286906)

STORY_SELECT_TEAM_3 = UIElement(name='STORY_SELECT_TEAM_3')
STORY_SELECT_TEAM_3.description = "Team selector is third team."
STORY_SELECT_TEAM_3.button_rect = Rect(0.7725452256431151, 0.3541699726814214, 0.7853800286467612, 0.37867758006286906)

STORY_SELECT_TEAM_4 = UIElement(name='STORY_SELECT_TEAM_4')
STORY_SELECT_TEAM_4.description = "Team selector is fourth team."
STORY_SELECT_TEAM_4.button_rect = Rect(0.8286380683997905, 0.354592517636274, 0.8414728714034365, 0.3782550351080165)

STORY_SELECT_TEAM_5 = UIElement(name='STORY_SELECT_TEAM_5')
STORY_SELECT_TEAM_5.description = "Team selector is fifth team."
STORY_SELECT_TEAM_5.button_rect = Rect(0.885206274230675, 0.3545925176362739, 0.8973280326230075, 0.37952266997257417)

STORY_DAILY_REWARD_NOTICE = UIElement(name='STORY_DAILY_REWARD_NOTICE')
STORY_DAILY_REWARD_NOTICE.description = "Story Mission: notification when there is no more daily rewards. Leads to OK button."
STORY_DAILY_REWARD_NOTICE.text_rect = Rect(0.380104867997492, 0.3900247478932228, 0.6208697326108724, 0.4378786340275592)
STORY_DAILY_REWARD_NOTICE.button_rect = Rect(0.5580615070595558, 0.7156970285296794, 0.6014290913687982, 0.7728558369679147)
STORY_DAILY_REWARD_NOTICE.text = "Cannot acquire daily reward."
STORY_DAILY_REWARD_NOTICE.text_threshold = 150

STORY_UNUSABLE_CHARACTER_NOTICE = UIElement(name='STORY_UNUSABLE_CHARACTER_NOTICE')
STORY_UNUSABLE_CHARACTER_NOTICE.description = "Story Mission: notification when team contains unusable characters. Leads to OK button."
STORY_UNUSABLE_CHARACTER_NOTICE.text_rect = Rect(0.3389804346007966, 0.3860369240486948, 0.6582555811533228, 0.47775687247283966)
STORY_UNUSABLE_CHARACTER_NOTICE.button_rect = Rect(0.47955122512041004, 0.7143677539148368, 0.5229188094296525, 0.771526562353072)
STORY_UNUSABLE_CHARACTER_NOTICE.text = "Cannot participate in the battle because\nunusable characters have been selected."
STORY_UNUSABLE_CHARACTER_NOTICE.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_NORMAL = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_NORMAL')
STORY_MISSION_DIMENSIONAL_CLASH_NORMAL.description = "Story Mission: Dimensional Clash - Normal."
STORY_MISSION_DIMENSIONAL_CLASH_NORMAL.text_rect = Rect(0.06232515538666388, 0.7755143861976, 0.14307858823835667, 0.8286853707913072)
STORY_MISSION_DIMENSIONAL_CLASH_NORMAL.button_rect = Rect(0.06232515538666388, 0.7755143861976, 0.14307858823835667, 0.8286853707913072)
STORY_MISSION_DIMENSIONAL_CLASH_NORMAL.text = "NORMAL"
STORY_MISSION_DIMENSIONAL_CLASH_NORMAL.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE')
STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE.description = "Story Mission: Dimensional Clash - Ultimate."
STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE.text_rect = Rect(0.2081299647022203, 0.7741851115827575, 0.29935143514579926, 0.8286853707913072)
STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE.button_rect = Rect(0.2081299647022203, 0.7741851115827575, 0.29935143514579926, 0.8286853707913072)
STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE.text = "ULTIMATE"
STORY_MISSION_DIMENSIONAL_CLASH_ULTIMATE.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_1_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_1_1')
STORY_MISSION_DIMENSIONAL_CLASH_1_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 1-1."
STORY_MISSION_DIMENSIONAL_CLASH_1_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_1_1.text = "1-1 Emergency Dispatch"
STORY_MISSION_DIMENSIONAL_CLASH_1_1.text_threshold = 150
