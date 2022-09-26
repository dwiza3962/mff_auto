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
STORY_ULTIMATE_START_BUTTON.text_rect = Rect(0.8625907258064516, 0.8958602150537635, 0.9432358870967741, 0.9639605734767025)
STORY_ULTIMATE_START_BUTTON.button_rect = Rect(0.8625907258064516, 0.8958602150537635, 0.9432358870967741, 0.9639605734767025)
STORY_ULTIMATE_START_BUTTON.text = "START"
STORY_ULTIMATE_START_BUTTON.text_threshold = 100

STORY_ULTIMATE_CLEAR_BUTTON = UIElement(name='STORY_ULTIMATE_CLEAR_BUTTON')
STORY_ULTIMATE_CLEAR_BUTTON.description = "The mission clear button."
STORY_ULTIMATE_CLEAR_BUTTON.button_rect = Rect(0.6912197580645162, 0.8743548387096772, 0.7658165322580643, 0.9782974910394263)

STORY_AUTO_PROGRESS_BUTTON = UIElement(name='STORY_AUTO_PROGRESS_BUTTON')
STORY_AUTO_PROGRESS_BUTTON.description = "Popup for Clear Tickets Auto Progress."
STORY_AUTO_PROGRESS_BUTTON.text_rect = Rect(0.3908165322580645, 0.544605734767025, 0.6468649193548387, 0.5983691756272401)
STORY_AUTO_PROGRESS_BUTTON.button_rect = Rect(0.35654233870967744, 0.5446057347670251, 0.39484879032258063, 0.6019534050179212)
STORY_AUTO_PROGRESS_BUTTON.text = "AUTO USE DESIGNATED CHARACTERS"
STORY_AUTO_PROGRESS_BUTTON.text_threshold = 120

STORY_AUTO_PROGRESS_START_BUTTON = UIElement(name='STORY_AUTO_PROGRESS_START_BUTTON')
STORY_AUTO_PROGRESS_START_BUTTON.description = "The mission start button."
STORY_AUTO_PROGRESS_START_BUTTON.text_rect = Rect(0.5037468699366623, 0.7452463521559901, 0.650924289291501, 0.8312242360793036)
STORY_AUTO_PROGRESS_START_BUTTON.button_rect = Rect(0.5037468699366623, 0.7452463521559901, 0.650924289291501, 0.8312242360793036)
STORY_AUTO_PROGRESS_START_BUTTON.text = "START"
STORY_AUTO_PROGRESS_START_BUTTON.text_threshold = 120

STORY_AUTO_POWER_SAVE_BUTTON = UIElement(name='STORY_AUTO_POWER_SAVE_BUTTON')
STORY_AUTO_POWER_SAVE_BUTTON.description = "Power Save Button."
STORY_AUTO_POWER_SAVE_BUTTON.text_rect = Rect(0.3283436441302106, 0.8383890597395798, 0.43519848283988805, 0.8992900608519268)
STORY_AUTO_POWER_SAVE_BUTTON.button_rect = Rect(0.7618113860656944, 0.02159916246810177, 0.810198482839888, 0.10041222273113917)
STORY_AUTO_POWER_SAVE_BUTTON.text = "AUTO PROGRESS"
STORY_AUTO_POWER_SAVE_BUTTON.text_threshold = 120

STORY_AUTO_PROGRESS_LABEL = UIElement(name='STORY_AUTO_PROGRESS_LABEL')
STORY_AUTO_PROGRESS_LABEL.description = "Power Save Auto Progress."
STORY_AUTO_PROGRESS_LABEL.text_rect = Rect(0.4130210634850493, 0.7237518811751619, 0.5843920312269849, 0.795400117777923)
STORY_AUTO_PROGRESS_LABEL.text = "AUTO PROGRESS..."
STORY_AUTO_PROGRESS_LABEL.text_threshold = 120

STORY_AUTO_PROGRESS_HAS_ENDED = UIElement(name='STORY_AUTO_PROGRESS_HAS_ENDED')
STORY_AUTO_PROGRESS_HAS_ENDED.description = "Auto Progress has Ended.   Close Button."
STORY_AUTO_PROGRESS_HAS_ENDED.text_rect = Rect(0.3888275150979526, 0.25803834325721375, 0.6085855796140817, 0.34759863901066534)
STORY_AUTO_PROGRESS_HAS_ENDED.button_rect = Rect(0.41906945058182354, 0.7954001177779232, 0.5803597731624687, 0.8670483543806843)
STORY_AUTO_PROGRESS_HAS_ENDED.text = "Auto Progress has ended."
STORY_AUTO_PROGRESS_HAS_ENDED.text_threshold = 120

STORY_AUTO_END_BATTLE_LABEL = UIElement(name='STORY_AUTO_END_BATTLE_LABEL')
STORY_AUTO_END_BATTLE_LABEL.description = "POWER SAVE: END BATTLE"
STORY_AUTO_END_BATTLE_LABEL.text_rect = Rect(0.4250907258064515, 0.713064516129032, 0.5783165322580645, 0.81342293906810)
STORY_AUTO_END_BATTLE_LABEL.button_rect = Rect(0.4250907258064515, 0.713064516129032, 0.5783165322580645, 0.81342293906810)
STORY_AUTO_END_BATTLE_LABEL.text = "END BATTLE"
STORY_AUTO_END_BATTLE_LABEL.text_threshold = 120

STORY_AUTO_CLOSE_BUTTON = UIElement(name='STORY_AUTO_CLOSE_BUTTON')
STORY_AUTO_CLOSE_BUTTON.description = "CLOSE"
STORY_AUTO_CLOSE_BUTTON.text_rect = Rect(0.41501008064516126, 0.7955017921146954, 0.5823487903225807, 0.877939068100)
STORY_AUTO_CLOSE_BUTTON.button_rect = Rect(0.41501008064516126, 0.7955017921146954, 0.5823487903225807, 0.877939068100)
STORY_AUTO_CLOSE_BUTTON.text = "CLOSE"
STORY_AUTO_CLOSE_BUTTON.text_threshold = 120

STORY_AUTO_EXIT_POWER_SAVE_1 = UIElement(name='STORY_AUTO_EXIT_POWER_SAVE_1')
STORY_AUTO_EXIT_POWER_SAVE_1.description = "CLOSE"
STORY_AUTO_EXIT_POWER_SAVE_1.button_rect = Rect(0.46544041832375904, 0.5410488778381207, 0.5037468699366623, 0.5804554079696392)

STORY_AUTO_EXIT_POWER_SAVE_2 = UIElement(name='STORY_AUTO_EXIT_POWER_SAVE_2')
STORY_AUTO_EXIT_POWER_SAVE_2.description = "CLOSE"
STORY_AUTO_EXIT_POWER_SAVE_2.button_rect = Rect(0.46140816025924297, 0.2114669894654191, 0.5057629989689204, 0.2616207550873518)

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

STORY_AUTO_HOME_BUTTON = UIElement(name='STORY_AUTO_HOME_BUTTON')
STORY_AUTO_HOME_BUTTON.description = "Story auto home button."
STORY_AUTO_HOME_BUTTON.button_rect = Rect(0.6811662247753719, 0.8885428253615127, 0.8061662247753719, 0.9530262383039977)

STORY_AVAILABLE_REWARDS = UIElement(name='STORY_AVAILABLE_REWARDS')
STORY_AVAILABLE_REWARDS.description = "Story Available Rewards."
STORY_AVAILABLE_REWARDS.text_rect = Rect(0.4513275150979526, 0.802564941438199, 0.55818235380763, 0.8527187070601319)
STORY_AVAILABLE_REWARDS.text_threshold = 150

STORY_STAGE_MINUS = UIElement(name='STORY_STAGE_MINUS')
STORY_STAGE_MINUS.description = "Story: stage minus button."
STORY_STAGE_MINUS.button_rect = Rect(0.9250907258064516, 0.12525089605734768, 0.9513004032258064, 0.17901433691756286)

STORY_STAGE_PLUS = UIElement(name='STORY_STAGE_PLUS')
STORY_STAGE_PLUS.description = "Story: stage plus button."
STORY_STAGE_PLUS.button_rect = Rect(0.9533165322580643, 0.13241935483870976, 0.9775100806451613, 0.18618279569892465)

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

STORY_MISSION_TRUE_SHIELD_NORMAL = UIElement(name='STORY_MISSION_TRUE_SHIELD_NORMAL')
STORY_MISSION_TRUE_SHIELD_NORMAL.description = "Story Mission: True Shield - Normal."
STORY_MISSION_TRUE_SHIELD_NORMAL.text_rect = Rect(0.3666500957431139, 0.7631584113066804, 0.5037468699366623, 0.8276418242491654)
STORY_MISSION_TRUE_SHIELD_NORMAL.button_rect = Rect(0.3666500957431139, 0.7631584113066804, 0.5037468699366623, 0.8276418242491654)
STORY_MISSION_TRUE_SHIELD_NORMAL.text = "NORMAL"
STORY_MISSION_TRUE_SHIELD_NORMAL.text_threshold = 150

STORY_MISSION_TRUE_SHIELD_ULTIMATE = UIElement(name='STORY_MISSION_TRUE_SHIELD_ULTIMATE')
STORY_MISSION_TRUE_SHIELD_ULTIMATE.description = "Story Mission: True Shield - Ultimate."
STORY_MISSION_TRUE_SHIELD_ULTIMATE.text_rect = Rect(0.5158436441302107, 0.7631584113066804, 0.6569726763882752, 0.8455538833998558)
STORY_MISSION_TRUE_SHIELD_ULTIMATE.button_rect = Rect(0.5158436441302107, 0.7631584113066804, 0.6569726763882752, 0.8455538833998558)
STORY_MISSION_TRUE_SHIELD_ULTIMATE.text = "ULTIMATE"
STORY_MISSION_TRUE_SHIELD_ULTIMATE.text_threshold = 150

STORY_MISSION_ALL_WAR_NORMAL = UIElement(name='STORY_MISSION_ALL_WAR_NORMAL')
STORY_MISSION_ALL_WAR_NORMAL.description = "Story Mission: All War - Normal."
STORY_MISSION_ALL_WAR_NORMAL.text_rect = Rect(0.7013275150979527, 0.7667408231368185, 0.840440418323759, 0.8204770005888894)
STORY_MISSION_ALL_WAR_NORMAL.button_rect = Rect(0.7013275150979527, 0.7667408231368185, 0.840440418323759, 0.8204770005888894)
STORY_MISSION_ALL_WAR_NORMAL.text = "NORMAL"
STORY_MISSION_ALL_WAR_NORMAL.text_threshold = 150

STORY_MISSION_ALL_WAR_ULTIMATE = UIElement(name='STORY_MISSION_ALL_WAR_ULTIMATE')
STORY_MISSION_ALL_WAR_ULTIMATE.description = "Story Mission: All War - Ultimate."
STORY_MISSION_ALL_WAR_ULTIMATE.text_rect = Rect(0.8505210634850495, 0.7595759994765424, 0.9916500957431139, 0.8348066479094417)
STORY_MISSION_ALL_WAR_ULTIMATE.button_rect = Rect(0.8505210634850495, 0.7595759994765424, 0.9916500957431139, 0.8348066479094417)
STORY_MISSION_ALL_WAR_ULTIMATE.text = "ULTIMATE"
STORY_MISSION_ALL_WAR_ULTIMATE.text_threshold = 150

STORY_MISSION_DRAG_START_PAGE2 = UIElement(name='STORY_MISSION_DRAG_START_PAGE2')
STORY_MISSION_DRAG_START_PAGE2.description = "Drag to Future Ends Here"
STORY_MISSION_DRAG_START_PAGE2.button_rect = Rect(0.8222952570334366, 0.3583458745010796, 0.840440418323759, 0.3941699928024601)

STORY_MISSION_DRAG_END_PAGE2 = UIElement(name='STORY_MISSION_DRAG_END_PAGE2')
STORY_MISSION_DRAG_END_PAGE2.description = "Drag to Future Ends Here"
STORY_MISSION_DRAG_END_PAGE2.button_rect = Rect(0.18116622477537195, 0.3404338153503892, 0.2093920312269848, 0.37625793365176985)

STORY_MISSION_FUTURE_ENDS_HERE_NORMAL = UIElement(name='STORY_MISSION_FUTURE_ENDS_HERE_NORMAL')
STORY_MISSION_FUTURE_ENDS_HERE_NORMAL.description = "Story Mission: Future Ends Here: - Normal."
STORY_MISSION_FUTURE_ENDS_HERE_NORMAL.text_rect = Rect(0.6751178376785978, 0.7631584113066804, 0.8142307409044042, 0.8348066479094417)
STORY_MISSION_FUTURE_ENDS_HERE_NORMAL.button_rect = Rect(0.6751178376785978, 0.7631584113066804, 0.8142307409044042, 0.8348066479094417)
STORY_MISSION_FUTURE_ENDS_HERE_NORMAL.text = "NORMAL"
STORY_MISSION_FUTURE_ENDS_HERE_NORMAL.text_threshold = 150

STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE = UIElement(name='STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE')
STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE.description = "Story Mission: Future Ends Here - Ultimate."
STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE.text_rect = Rect(0.8263275150979527, 0.7667408231368187, 0.9573759021947269, 0.8419714715697179)
STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE.button_rect = Rect(0.8263275150979527, 0.7667408231368187, 0.9573759021947269, 0.8419714715697179)
STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE.text = "ULTIMATE"
STORY_MISSION_FUTURE_ENDS_HERE_ULTIMATE.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_1_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_1_1')
STORY_MISSION_DIMENSIONAL_CLASH_1_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 1-1."
STORY_MISSION_DIMENSIONAL_CLASH_1_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_1_1.text = "1-1 Emergency Dispatch"
STORY_MISSION_DIMENSIONAL_CLASH_1_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_1_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_1_2')
STORY_MISSION_DIMENSIONAL_CLASH_1_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 1-2."
STORY_MISSION_DIMENSIONAL_CLASH_1_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_1_2.text = "1-2 An Unexpected Encounter"
STORY_MISSION_DIMENSIONAL_CLASH_1_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_1_3 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_1_3')
STORY_MISSION_DIMENSIONAL_CLASH_1_3.description = "Story Mission: Dimensional Clash - Ultimate: mission 1-3."
STORY_MISSION_DIMENSIONAL_CLASH_1_3.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_1_3.text = "1-3 Robotic Theft"
STORY_MISSION_DIMENSIONAL_CLASH_1_3.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_2_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_2_1')
STORY_MISSION_DIMENSIONAL_CLASH_2_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 2-1."
STORY_MISSION_DIMENSIONAL_CLASH_2_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_2_1.text = "2-1 The Rescue Plan"
STORY_MISSION_DIMENSIONAL_CLASH_2_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_2_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_2_2')
STORY_MISSION_DIMENSIONAL_CLASH_2_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 2-2."
STORY_MISSION_DIMENSIONAL_CLASH_2_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_2_2.text = "2-2 Scheme of Advanced Evil"
STORY_MISSION_DIMENSIONAL_CLASH_2_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_2_3 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_2_3')
STORY_MISSION_DIMENSIONAL_CLASH_2_3.description = "Story Mission: Dimensional Clash - Ultimate: mission 2-3."
STORY_MISSION_DIMENSIONAL_CLASH_2_3.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_2_3.text = "2-3 Mad Science to the Max"
STORY_MISSION_DIMENSIONAL_CLASH_2_3.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_3_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_3_1')
STORY_MISSION_DIMENSIONAL_CLASH_3_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 3-1."
STORY_MISSION_DIMENSIONAL_CLASH_3_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_3_1.text = "3-1 S.H.I.E.L.D. Under Siege"
STORY_MISSION_DIMENSIONAL_CLASH_3_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_3_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_3_2')
STORY_MISSION_DIMENSIONAL_CLASH_3_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 3-2."
STORY_MISSION_DIMENSIONAL_CLASH_3_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_3_2.text = "3-2 Shadow Over the Streets"
STORY_MISSION_DIMENSIONAL_CLASH_3_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_3_3 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_3_3')
STORY_MISSION_DIMENSIONAL_CLASH_3_3.description = "Story Mission: Dimensional Clash - Ultimate: mission 3-3."
STORY_MISSION_DIMENSIONAL_CLASH_3_3.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_3_3.text = "3-3 Chaos Descends"
STORY_MISSION_DIMENSIONAL_CLASH_3_3.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_4_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_4_1')
STORY_MISSION_DIMENSIONAL_CLASH_4_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 4-1."
STORY_MISSION_DIMENSIONAL_CLASH_4_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_4_1.text = "4-1 Crack in the S.H.I.E.L.D."
STORY_MISSION_DIMENSIONAL_CLASH_4_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_4_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_4_2')
STORY_MISSION_DIMENSIONAL_CLASH_4_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 4-2."
STORY_MISSION_DIMENSIONAL_CLASH_4_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_4_2.text = "4-2 The Beginning of the Storm"
STORY_MISSION_DIMENSIONAL_CLASH_4_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_5_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_5_1')
STORY_MISSION_DIMENSIONAL_CLASH_5_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 5-1."
STORY_MISSION_DIMENSIONAL_CLASH_5_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_5_1.text = "5-1 The Battle for Domination"
STORY_MISSION_DIMENSIONAL_CLASH_5_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_6_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_6_1')
STORY_MISSION_DIMENSIONAL_CLASH_6_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 6-1."
STORY_MISSION_DIMENSIONAL_CLASH_6_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_6_1.text = "6-1 An Eternal Nemesis"
STORY_MISSION_DIMENSIONAL_CLASH_6_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_6_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_6_2')
STORY_MISSION_DIMENSIONAL_CLASH_6_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 6-2."
STORY_MISSION_DIMENSIONAL_CLASH_6_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_6_2.text = "6-2 The Red Madness"
STORY_MISSION_DIMENSIONAL_CLASH_6_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_7_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_7_1')
STORY_MISSION_DIMENSIONAL_CLASH_7_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 7-1."
STORY_MISSION_DIMENSIONAL_CLASH_7_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_7_1.text = "7-1 The Criminal Overworld"
STORY_MISSION_DIMENSIONAL_CLASH_7_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_7_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_7_2')
STORY_MISSION_DIMENSIONAL_CLASH_7_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 7-2."
STORY_MISSION_DIMENSIONAL_CLASH_7_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_7_2.text = "7-2 The Not-So-Grand Plan"
STORY_MISSION_DIMENSIONAL_CLASH_7_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_7_3 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_7_3')
STORY_MISSION_DIMENSIONAL_CLASH_7_3.description = "Story Mission: Dimensional Clash - Ultimate: mission 7-3."
STORY_MISSION_DIMENSIONAL_CLASH_7_3.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_7_3.text = "7-3 Order Out of Chaos"
STORY_MISSION_DIMENSIONAL_CLASH_7_3.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_8_1 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_8_1')
STORY_MISSION_DIMENSIONAL_CLASH_8_1.description = "Story Mission: Dimensional Clash - Ultimate: mission 8-1."
STORY_MISSION_DIMENSIONAL_CLASH_8_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_8_1.text = "8-1 Dimensional Shift"
STORY_MISSION_DIMENSIONAL_CLASH_8_1.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_8_2 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_8_2')
STORY_MISSION_DIMENSIONAL_CLASH_8_2.description = "Story Mission: Dimensional Clash - Ultimate: mission 8-2."
STORY_MISSION_DIMENSIONAL_CLASH_8_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_8_2.text = "8-2 Anti-Matter Recovery"
STORY_MISSION_DIMENSIONAL_CLASH_8_2.text_threshold = 150

STORY_MISSION_DIMENSIONAL_CLASH_8_3 = UIElement(name='STORY_MISSION_DIMENSIONAL_CLASH_8_3')
STORY_MISSION_DIMENSIONAL_CLASH_8_3.description = "Story Mission: Dimensional Clash - Ultimate: mission 8-3."
STORY_MISSION_DIMENSIONAL_CLASH_8_3.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_DIMENSIONAL_CLASH_8_3.text = "8-3 The Showdown"
STORY_MISSION_DIMENSIONAL_CLASH_8_3.text_threshold = 150

STORY_MISSION_TRUE_SHIELD_9_1 = UIElement(name='STORY_MISSION_TRUE_SHIELD_9_1')
STORY_MISSION_TRUE_SHIELD_9_1.description = "Story Mission: True Shield: mission 9-1."
STORY_MISSION_TRUE_SHIELD_9_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_TRUE_SHIELD_9_1.text = "9-1 Crisis in Another Dimension"
STORY_MISSION_TRUE_SHIELD_9_1.text_threshold = 150

STORY_MISSION_TRUE_SHIELD_9_2 = UIElement(name='STORY_MISSION_TRUE_SHIELD_9_2')
STORY_MISSION_TRUE_SHIELD_9_2.description = "Story Mission: True Shield: mission 9-2."
STORY_MISSION_TRUE_SHIELD_9_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_TRUE_SHIELD_9_2.text = "9-2 Terrigen Rage"
STORY_MISSION_TRUE_SHIELD_9_2.text_threshold = 150

STORY_MISSION_TRUE_SHIELD_10_1 = UIElement(name='STORY_MISSION_TRUE_SHIELD_10_1')
STORY_MISSION_TRUE_SHIELD_10_1.description = "Story Mission: True Shield: mission 10-1."
STORY_MISSION_TRUE_SHIELD_10_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_TRUE_SHIELD_10_1.text = "10-1 Royal Rumble"
STORY_MISSION_TRUE_SHIELD_10_1.text_threshold = 150

STORY_MISSION_TRUE_SHIELD_10_2 = UIElement(name='STORY_MISSION_TRUE_SHIELD_10_2')
STORY_MISSION_TRUE_SHIELD_10_2.description = "Story Mission: True Shield: mission 10-2."
STORY_MISSION_TRUE_SHIELD_10_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_TRUE_SHIELD_10_2.text = "10-2 The Brink of Detonation"
STORY_MISSION_TRUE_SHIELD_10_2.text_threshold = 150

STORY_MISSION_ALL_WAR_11_1 = UIElement(name='STORY_MISSION_ALL_WAR_11_1')
STORY_MISSION_ALL_WAR_11_1.description = "Story Mission: All War: mission 11-1."
STORY_MISSION_ALL_WAR_11_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_ALL_WAR_11_1.text = "11-1 God of Deception"
STORY_MISSION_ALL_WAR_11_1.text_threshold = 150

STORY_MISSION_ALL_WAR_11_2 = UIElement(name='STORY_MISSION_ALL_WAR_11_2')
STORY_MISSION_ALL_WAR_11_2.description = "Story Mission: All War: mission 11-2."
STORY_MISSION_ALL_WAR_11_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_ALL_WAR_11_2.text = "11-2 Frozen Kingdom"
STORY_MISSION_ALL_WAR_11_2.text_threshold = 150

STORY_MISSION_ALL_WAR_12_1 = UIElement(name='STORY_MISSION_ALL_WAR_12_1')
STORY_MISSION_ALL_WAR_12_1.description = "Story Mission: All War: mission 12-1."
STORY_MISSION_ALL_WAR_12_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_ALL_WAR_12_1.text = "12-1 Flaming Frenzy"
STORY_MISSION_ALL_WAR_12_1.text_threshold = 150

STORY_MISSION_ALL_WAR_12_2 = UIElement(name='STORY_MISSION_ALL_WAR_12_2')
STORY_MISSION_ALL_WAR_12_2.description = "Story Mission: All War: mission 12-2."
STORY_MISSION_ALL_WAR_12_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_ALL_WAR_12_2.text = "12-2 Majestic Threat"
STORY_MISSION_ALL_WAR_12_2.text_threshold = 150

STORY_MISSION_FUTURE_ENDS_HERE_13_1 = UIElement(name='STORY_MISSION_FUTURE_ENDS_HERE_13_1')
STORY_MISSION_FUTURE_ENDS_HERE_13_1.description = "Story Mission: Future Ends Here: mission 13-1."
STORY_MISSION_FUTURE_ENDS_HERE_13_1.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_FUTURE_ENDS_HERE_13_1.text = "13-1 The Ultimates"
STORY_MISSION_FUTURE_ENDS_HERE_13_1.text_threshold = 150

STORY_MISSION_FUTURE_ENDS_HERE_13_2 = UIElement(name='STORY_MISSION_FUTURE_ENDS_HERE_13_2')
STORY_MISSION_FUTURE_ENDS_HERE_13_2.description = "Story Mission: Future Ends Here: mission 13-2."
STORY_MISSION_FUTURE_ENDS_HERE_13_2.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_FUTURE_ENDS_HERE_13_2.text = "13-2 Manipulated Justice"
STORY_MISSION_FUTURE_ENDS_HERE_13_2.text_threshold = 150

STORY_MISSION_FUTURE_ENDS_HERE_13_3 = UIElement(name='STORY_MISSION_FUTURE_ENDS_HERE_13_3')
STORY_MISSION_FUTURE_ENDS_HERE_13_3.description = "Story Mission: Future Ends Here: mission 13-3."
STORY_MISSION_FUTURE_ENDS_HERE_13_3.text_rect = Rect(0.6320854871736077, 0.12682837415437204, 0.8392030880987825, 0.1720237110590233)
STORY_MISSION_FUTURE_ENDS_HERE_13_3.text = "13-3 Time Runs Out"
STORY_MISSION_FUTURE_ENDS_HERE_13_3.text_threshold = 150

STORY_COMBINE_FRAGMENT_BUTTON = UIElement(name='STORY_COMBINE_FRAGMENT_BUTTON')
STORY_COMBINE_FRAGMENT_BUTTON.description = "Button to Combine Fragments"
STORY_COMBINE_FRAGMENT_BUTTON.text_rect = Rect(0.2638275150979526, 0.7954001177779231, 0.41100493445279124, 0.85630111889027)
STORY_COMBINE_FRAGMENT_BUTTON.button_rect = Rect(0.30213396671085574, 0.8563011188902699, 0.3626178376785977, 0.9637734737944118)
STORY_COMBINE_FRAGMENT_BUTTON.text = "DAILY REWARD"
STORY_COMBINE_FRAGMENT_BUTTON.text_threshold = 150

STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON = UIElement(name='STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON')
STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON.description = "Extra Button to Combine Fragments"
STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON.text_rect = Rect(0.4130210634850493, 0.8670483543806843, 0.5843920312269849, 0.9422790028135835)
STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON.button_rect = Rect(0.4130210634850493, 0.8670483543806843, 0.5843920312269849, 0.9422790028135835)
STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON.text = "COMBINE FRAGMENTS"
STORY_COMBINE_FRAGMENT_ULTIMATE_BUTTON.text_threshold = 120

STORY_COMBINE_FRAGMENT_UI_COMBINE = UIElement(name='STORY_COMBINE_FRAGMENT_UI_COMBINE')
STORY_COMBINE_FRAGMENT_UI_COMBINE.description = "Button to Combine Fragments - Combine Button"
STORY_COMBINE_FRAGMENT_UI_COMBINE.text_rect = Rect(0.7658436441302107, 0.8885428253615124, 0.9815694505818235, 0.9745207092848261)
STORY_COMBINE_FRAGMENT_UI_COMBINE.button_rect = Rect(0.7658436441302107, 0.8885428253615124, 0.9815694505818235, 0.9745207092848261)
STORY_COMBINE_FRAGMENT_UI_COMBINE.text = "COMBINE"
STORY_COMBINE_FRAGMENT_UI_COMBINE.text_threshold = 120

STORY_COMBINE_FRAGMENT_OK = UIElement(name='STORY_COMBINE_FRAGMENT_OK')
STORY_COMBINE_FRAGMENT_OK.description = "Button to Combine Fragments - OK Button"
STORY_COMBINE_FRAGMENT_OK.text_rect = Rect(0.3343920312269848, 0.1541484001832101, 0.6610049344527914, 0.24012628410652356)
STORY_COMBINE_FRAGMENT_OK.button_rect = Rect(0.43318235380763004, 0.7452463521559901, 0.5662468699366623, 0.8061473532683372)
STORY_COMBINE_FRAGMENT_OK.text = "FRAGMENT COMBINE AWARD"
STORY_COMBINE_FRAGMENT_OK.text_threshold = 120
