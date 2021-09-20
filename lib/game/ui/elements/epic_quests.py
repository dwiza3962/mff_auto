﻿from lib.game.ui.general import UIElement, Rect, load_ui_image

EQ_LABEL = UIElement(name='EQ_LABEL')
EQ_LABEL.description = "Epic Quest mission label."
EQ_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_LABEL.text = "EPIC QUEST"
EQ_LABEL.text_threshold = 120

EQ_PAGE_DRAG_FROM = UIElement(name='EQ_PAGE_DRAG_FROM')
EQ_PAGE_DRAG_FROM.description = "Page of Epic Quests: drag position (right) to scroll the list."
EQ_PAGE_DRAG_FROM.button_rect = Rect(0.8421939559821787, 0.17335298567386584, 0.9655672561722649, 0.83001464540615)

EQ_PAGE_DRAG_TO = UIElement(name='EQ_PAGE_DRAG_TO')
EQ_PAGE_DRAG_TO.description = "Page of Epic Quests: drag position (left) to scroll the list."
EQ_PAGE_DRAG_TO.button_rect = Rect(0.036155061406948616, 0.16936516182933778, 0.14906032400514876, 0.8526123138584755)

EQ_DARK_REIGN = UIElement(name='EQ_DARK_REIGN')
EQ_DARK_REIGN.description = "Epic Quest: Dark Reign: mission label and selector."
EQ_DARK_REIGN.text_rect = Rect(0.01222811833978037, 0.779502210042128, 0.10793589060845334, 0.8193804484874085)
EQ_DARK_REIGN.button_rect = Rect(0.038398212319495605, 0.22120687180820242, 0.2612178696324998, 0.730319049292949)
EQ_DARK_REIGN.text = "DARK REIGN"
EQ_DARK_REIGN.text_threshold = 120

EQ_GALACTIC_IMPERATIVE = UIElement(name='EQ_GALACTIC_IMPERATIVE')
EQ_GALACTIC_IMPERATIVE.description = "Epic Quest: The Galactic Imperative: mission label and selector."
EQ_GALACTIC_IMPERATIVE.text_rect = Rect(0.3217829442712695, 0.779502210042128, 0.5176847906337093, 0.818051173872566)
EQ_GALACTIC_IMPERATIVE.button_rect = Rect(0.35094390613438076, 0.22386542103788773, 0.5685295446514419, 0.7263312254484209)
EQ_GALACTIC_IMPERATIVE.text = "THE GALACTIC IMPERATIVE"
EQ_GALACTIC_IMPERATIVE.text_threshold = 120

EQ_FIRST_FAMILY = UIElement(name='EQ_FIRST_FAMILY')
EQ_FIRST_FAMILY.description = "Epic Quest: First Family: mission label and selector."
EQ_FIRST_FAMILY.text_rect = Rect(0.6328332041444565, 0.779502210042128, 0.7345227121799215, 0.8233682723319365)
EQ_FIRST_FAMILY.button_rect = Rect(0.6627418829784169, 0.22785324488241582, 0.8676163329910449, 0.709050655455466)
EQ_FIRST_FAMILY.text = "FIRST FAMILY"
EQ_FIRST_FAMILY.text_threshold = 120

EQ_X_FORCE = UIElement(name='EQ_X_FORCE')
EQ_X_FORCE.description = "Epic Quest: X-Force: mission label and selector."
EQ_X_FORCE.text_rect = Rect(0.074288626920248, 0.7781729354272854, 0.1453217391509037, 0.8167218992577232)
EQ_X_FORCE.button_rect = Rect(0.10644045666675529, 0.22652397026757307, 0.30981947273768534, 0.7210141269890501)
EQ_X_FORCE.text = "X-FORCE"
EQ_X_FORCE.text_threshold = 120

EQ_RISE_OF_X_MEN = UIElement(name='EQ_RISE_OF_X_MEN')
EQ_RISE_OF_X_MEN.description = "Epic Quest: Rise of the X-Men: mission label and selector."
EQ_RISE_OF_X_MEN.text_rect = Rect(0.3830957358808881, 0.7808314846569708, 0.5251619603421994, 0.8220389977170939)
EQ_RISE_OF_X_MEN.button_rect = Rect(0.4197338674524894, 0.22918251949725849, 0.6193742986691745, 0.7183555777593649)
EQ_RISE_OF_X_MEN.text = "RISE OF THE X-MEN"
EQ_RISE_OF_X_MEN.text_threshold = 120

EQ_SORCERER_SUPREME = UIElement(name='EQ_SORCERER_SUPREME')
EQ_SORCERER_SUPREME.description = "Epic Quest: Sorcerer Supreme: mission label and selector."
EQ_SORCERER_SUPREME.text_rect = Rect(0.6933982787832261, 0.779502210042128, 0.8421939559821787, 0.8193804484874085)
EQ_SORCERER_SUPREME.button_rect = Rect(0.7292886933839784, 0.23051179411210115, 0.9379017282508516, 0.7289897746781062)
EQ_SORCERER_SUPREME.text = "SORCERER SUPREME"
EQ_SORCERER_SUPREME.text_threshold = 120

EQ_STUPID_X_MEN_STAGE_LABEL = UIElement(name='EQ_STUPID_X_MEN_STAGE_LABEL')
EQ_STUPID_X_MEN_STAGE_LABEL.description = "Epic Quest : X-Force: Stupid X-Men stage text (to detect if it's loaded)."
EQ_STUPID_X_MEN_STAGE_LABEL.text_rect = Rect(0.05296127562642369, 0.02327935222672065, 0.20273348519362186, 0.0708502024291498)
EQ_STUPID_X_MEN_STAGE_LABEL.text = "STUPID X-MEN"
EQ_STUPID_X_MEN_STAGE_LABEL.text_threshold = 120

EQ_THE_BIG_TWIN_STAGE_LABEL = UIElement(name='EQ_THE_BIG_TWIN_STAGE_LABEL')
EQ_THE_BIG_TWIN_STAGE_LABEL.description = "Epic Quest : X-Force: The Big Twin stage text (to detect if it's loaded)."
EQ_THE_BIG_TWIN_STAGE_LABEL.text_rect = Rect(0.050520833333333334, 0.022222222222222223, 0.19583333333333333, 0.075)
EQ_THE_BIG_TWIN_STAGE_LABEL.text = "THE BIG TWIN"
EQ_THE_BIG_TWIN_STAGE_LABEL.text_threshold = 120

EQ_TWISTED_WORLD_STAGE_LABEL = UIElement(name='EQ_TWISTED_WORLD_STAGE_LABEL')
EQ_TWISTED_WORLD_STAGE_LABEL.description = "Epic Quest : First Family: Twisted World stage text (to detect if it's loaded)."
EQ_TWISTED_WORLD_STAGE_LABEL.text_rect = Rect(0.053125, 0.025925925925925925, 0.22291666666666668, 0.07592592592592592)
EQ_TWISTED_WORLD_STAGE_LABEL.text = "TWISTED WORLD"
EQ_TWISTED_WORLD_STAGE_LABEL.text_threshold = 120

EQ_RECOMMENDED_LVL = UIElement(name='EQ_RECOMMENDED_LVL')
EQ_RECOMMENDED_LVL.description = "Epic Quest: recommended lvl for mission without difficulty (to detect if menu is loaded)."
EQ_RECOMMENDED_LVL.text_rect = Rect(0.5791571753986332, 0.728744939271255, 0.7164009111617312, 0.7692307692307693)
EQ_RECOMMENDED_LVL.text = "RECOMMENDED LV"
EQ_RECOMMENDED_LVL.text_threshold = 120

EQ_STUPID_X_MEN_STAGE_1 = UIElement(name='EQ_STUPID_X_MEN_STAGE_1')
EQ_STUPID_X_MEN_STAGE_1.description = "Epic Quest : X-Force: Stupid X-Men stage #1."
EQ_STUPID_X_MEN_STAGE_1.text_rect = Rect(0.3354214123006834, 0.6902834008097166, 0.37471526195899774, 0.7257085020242915)
EQ_STUPID_X_MEN_STAGE_1.button_rect = Rect(0.2864464692482916, 0.3714574898785425, 0.4185649202733485, 0.6072874493927125)
EQ_STUPID_X_MEN_STAGE_1.text_threshold = 95
EQ_STUPID_X_MEN_STAGE_1.available_characters = "0123456789/"

EQ_STUPID_X_MEN_STAGE_2 = UIElement(name='EQ_STUPID_X_MEN_STAGE_2')
EQ_STUPID_X_MEN_STAGE_2.description = "Epic Quest : X-Force: Stupid X-Men stage #2."
EQ_STUPID_X_MEN_STAGE_2.text_rect = Rect(0.6304100227790432, 0.6892712550607287, 0.6674259681093394, 0.7267206477732794)
EQ_STUPID_X_MEN_STAGE_2.button_rect = Rect(0.5882687927107062, 0.3714574898785425, 0.7118451025056948, 0.5951417004048583)
EQ_STUPID_X_MEN_STAGE_2.text_threshold = 95
EQ_STUPID_X_MEN_STAGE_2.available_characters = "0123456789/"

EQ_THE_BIG_TWIN_STAGE_1 = UIElement(name='EQ_THE_BIG_TWIN_STAGE_1')
EQ_THE_BIG_TWIN_STAGE_1.description = "Epic Quest : X-Force: The Big Twin stage #1."
EQ_THE_BIG_TWIN_STAGE_1.text_rect = Rect(0.33697916666666666, 0.6907407407407408, 0.3697916666666667, 0.725)
EQ_THE_BIG_TWIN_STAGE_1.button_rect = Rect(0.2984375, 0.375, 0.4125, 0.6527777777777778)
EQ_THE_BIG_TWIN_STAGE_1.text_threshold = 95
EQ_THE_BIG_TWIN_STAGE_1.available_characters = "0123456789/"

EQ_THE_BIG_TWIN_STAGE_2 = UIElement(name='EQ_THE_BIG_TWIN_STAGE_2')
EQ_THE_BIG_TWIN_STAGE_2.description = "Epic Quest : X-Force: The Big Twin stage #2."
EQ_THE_BIG_TWIN_STAGE_2.text_rect = Rect(0.6302083333333334, 0.6907407407407408, 0.6614583333333334, 0.725)
EQ_THE_BIG_TWIN_STAGE_2.button_rect = Rect(0.5885416666666666, 0.375, 0.7015625, 0.6527777777777778)
EQ_THE_BIG_TWIN_STAGE_2.text_threshold = 95
EQ_THE_BIG_TWIN_STAGE_2.available_characters = "0123456789/"

EQ_TWISTED_WORLD_STAGE_1 = UIElement(name='EQ_TWISTED_WORLD_STAGE_1')
EQ_TWISTED_WORLD_STAGE_1.description = "Epic Quest : First Family: Twisted World stage #1."
EQ_TWISTED_WORLD_STAGE_1.text_rect = Rect(0.33697916666666666, 0.6907407407407408, 0.3697916666666667, 0.725)
EQ_TWISTED_WORLD_STAGE_1.button_rect = Rect(0.2984375, 0.375, 0.4125, 0.6527777777777778)
EQ_TWISTED_WORLD_STAGE_1.text_threshold = 95
EQ_TWISTED_WORLD_STAGE_1.available_characters = "0123456789/"

EQ_TWISTED_WORLD_STAGE_2 = UIElement(name='EQ_TWISTED_WORLD_STAGE_2')
EQ_TWISTED_WORLD_STAGE_2.description = "Epic Quest : First Family: Twisted World stage #2."
EQ_TWISTED_WORLD_STAGE_2.text_rect = Rect(0.6302083333333334, 0.6907407407407408, 0.6614583333333334, 0.725)
EQ_TWISTED_WORLD_STAGE_2.button_rect = Rect(0.5885416666666666, 0.375, 0.7015625, 0.6527777777777778)
EQ_TWISTED_WORLD_STAGE_2.text_threshold = 95
EQ_TWISTED_WORLD_STAGE_2.available_characters = "0123456789/"

EQ_VEILED_SECRET_STAGE_1 = UIElement(name='EQ_VEILED_SECRET_STAGE_1')
EQ_VEILED_SECRET_STAGE_1.description = "Epic Quest : Rise Of The X-Men: Veiled Secret stage #1."
EQ_VEILED_SECRET_STAGE_1.text_rect = Rect(0.33697916666666666, 0.6907407407407408, 0.3697916666666667, 0.725)
EQ_VEILED_SECRET_STAGE_1.button_rect = Rect(0.2984375, 0.375, 0.4125, 0.6527777777777778)
EQ_VEILED_SECRET_STAGE_1.text_threshold = 95
EQ_VEILED_SECRET_STAGE_1.available_characters = "0123456789/"

EQ_VEILED_SECRET_STAGE_2 = UIElement(name='EQ_VEILED_SECRET_STAGE_2')
EQ_VEILED_SECRET_STAGE_2.description = "Epic Quest : Rise Of The X-Men: Veiled Secret stage #2."
EQ_VEILED_SECRET_STAGE_2.text_rect = Rect(0.6302083333333334, 0.6907407407407408, 0.6614583333333334, 0.725)
EQ_VEILED_SECRET_STAGE_2.button_rect = Rect(0.5885416666666666, 0.375, 0.7015625, 0.6527777777777778)
EQ_VEILED_SECRET_STAGE_2.text_threshold = 95
EQ_VEILED_SECRET_STAGE_2.available_characters = "0123456789/"

EQ_MUTUAL_ENEMY_STAGE_LABEL = UIElement(name='EQ_MUTUAL_ENEMY_STAGE_LABEL')
EQ_MUTUAL_ENEMY_STAGE_LABEL.description = "Epic Quest : Rise of the X-men : Mutual Enemy stage button and text."
EQ_MUTUAL_ENEMY_STAGE_LABEL.text_rect = Rect(0.646875, 0.8703703703703703, 0.7416666666666667, 0.8972222222222223)
EQ_MUTUAL_ENEMY_STAGE_LABEL.button_rect = Rect(0.6625, 0.7231481481481481, 0.7244791666666667, 0.8240740740740741)
EQ_MUTUAL_ENEMY_STAGE_LABEL.text = "MUTUAL ENEMY"
EQ_MUTUAL_ENEMY_STAGE_LABEL.text_threshold = 120

EQ_MUTUAL_ENEMY_STAGE = UIElement(name='EQ_MUTUAL_ENEMY_STAGE')
EQ_MUTUAL_ENEMY_STAGE.description = "Epic Quest : Rise of the X-men : Mutual Enemy stage counter."
EQ_MUTUAL_ENEMY_STAGE.text_rect = Rect(0.15572916666666667, 0.9092592592592592, 0.19166666666666668, 0.9527777777777777)
EQ_MUTUAL_ENEMY_STAGE.text_threshold = 120
EQ_MUTUAL_ENEMY_STAGE.available_characters = "0123456789/"

EQ_VEILED_SECRET_STAGE_LABEL = UIElement(name='EQ_VEILED_SECRET_STAGE_LABEL')
EQ_VEILED_SECRET_STAGE_LABEL.description = "Epic Quest : Rise of the X-men : Veiled Secret stage button and text."
EQ_VEILED_SECRET_STAGE_LABEL.text_rect = Rect(0.0515625, 0.025925925925925925, 0.20625, 0.07592592592592592)
EQ_VEILED_SECRET_STAGE_LABEL.text = "VEILED SECRET"
EQ_VEILED_SECRET_STAGE_LABEL.text_threshold = 120

EQ_BEGINNING_OF_THE_CHAOS_STAGE_LABEL = UIElement(name='EQ_BEGINNING_OF_THE_CHAOS_STAGE_LABEL')
EQ_BEGINNING_OF_THE_CHAOS_STAGE_LABEL.description = "Epic Quest : X-Force : Beginning Of The Chaos stage button and text."
EQ_BEGINNING_OF_THE_CHAOS_STAGE_LABEL.text = "BEGINNING OF THE CHAOS"

EQ_DOOMSDAY_STAGE_LABEL = UIElement(name='EQ_DOOMSDAY_STAGE_LABEL')
EQ_DOOMSDAY_STAGE_LABEL.description = "Epic Quest : First Family : Doom's Day stage."
EQ_DOOMSDAY_STAGE_LABEL.text = "DOOM'S DAY"

EQ_THE_FAULT_STAGE_LABEL = UIElement(name='EQ_THE_FAULT_STAGE_LABEL')
EQ_THE_FAULT_STAGE_LABEL.description = "Epic Quest : The Galactic Imperative: The Fault stage text (to detect if it's loaded)."
EQ_THE_FAULT_STAGE_LABEL.text_rect = Rect(0.052083333333333336, 0.013888888888888888, 0.16614583333333333, 0.0824074074074074)
EQ_THE_FAULT_STAGE_LABEL.text = "THE FAULT"
EQ_THE_FAULT_STAGE_LABEL.text_threshold = 120

EQ_THE_FAULT_STAGE_1 = UIElement(name='EQ_THE_FAULT_STAGE_1')
EQ_THE_FAULT_STAGE_1.description = "Epic Quest : The Galactic Imperative: The Fault stage #1."
EQ_THE_FAULT_STAGE_1.text_rect = Rect(0.33697916666666666, 0.6907407407407408, 0.3697916666666667, 0.725)
EQ_THE_FAULT_STAGE_1.button_rect = Rect(0.2984375, 0.375, 0.4125, 0.6527777777777778)
EQ_THE_FAULT_STAGE_1.text_threshold = 160
EQ_THE_FAULT_STAGE_1.available_characters = "0123456789/"

EQ_THE_FAULT_STAGE_2 = UIElement(name='EQ_THE_FAULT_STAGE_2')
EQ_THE_FAULT_STAGE_2.description = "Epic Quest : The Galactic Imperative: The Fault stage #2."
EQ_THE_FAULT_STAGE_2.text_rect = Rect(0.6302083333333334, 0.6907407407407408, 0.6614583333333334, 0.725)
EQ_THE_FAULT_STAGE_2.button_rect = Rect(0.5885416666666666, 0.375, 0.7015625, 0.6527777777777778)
EQ_THE_FAULT_STAGE_2.text_threshold = 120
EQ_THE_FAULT_STAGE_2.available_characters = "0123456789/"

EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL = UIElement(name='EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL')
EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL.description = "Epic Quest : The Galactic Imperative : Fate of the Universe stage button and text."
EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL.text_rect = Rect(0.646875, 0.8703703703703703, 0.7416666666666667, 0.8972222222222223)
EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL.button_rect = Rect(0.6625, 0.7231481481481481, 0.7244791666666667, 0.8240740740740741)
EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL.text = "FATE OF THE UNIVERSE"
EQ_FATE_OF_THE_UNIVERSE_STAGE_LABEL.text_threshold = 120

EQ_NOTIFICATION_OK = UIElement(name='EQ_NOTIFICATION_OK')
EQ_NOTIFICATION_OK.description = "Epic Quests: notification after completing mission (OK button)."
EQ_NOTIFICATION_OK.text_rect = Rect(0.80625, 0.7768518518518519, 0.9104166666666667, 0.825925925925926)
EQ_NOTIFICATION_OK.button_rect = Rect(0.8359375, 0.8694444444444445, 0.8911458333333333, 0.9231481481481482)
EQ_NOTIFICATION_OK.text = "EPIC QUEST"
EQ_NOTIFICATION_OK.text_threshold = 150

EQ_NORMAL_STAGE_1 = UIElement(name='EQ_NORMAL_STAGE_1')
EQ_NORMAL_STAGE_1.description = "Epic Quest : any normal stage #1."
EQ_NORMAL_STAGE_1.button_rect = Rect(0.2984375, 0.375, 0.4125, 0.6527777777777778)

EQ_NORMAL_STAGE_2 = UIElement(name='EQ_NORMAL_STAGE_2')
EQ_NORMAL_STAGE_2.description = "Epic Quest : any normal stage #2."
EQ_NORMAL_STAGE_2.button_rect = Rect(0.5885416666666666, 0.375, 0.7015625, 0.6527777777777778)

EQ_SPACE_PRISON = UIElement(name='EQ_SPACE_PRISON')
EQ_SPACE_PRISON.description = "Epic Quest: The Galactic Imperative: Space Prison mission."
EQ_SPACE_PRISON.text_rect = Rect(0.32864583333333336, 0.8694444444444445, 0.41458333333333336, 0.9)
EQ_SPACE_PRISON.button_rect = Rect(0.34427083333333336, 0.725, 0.39791666666666664, 0.8175925925925925)
EQ_SPACE_PRISON.text = "SPACE PRISON"
EQ_SPACE_PRISON.text_threshold = 120

EQ_SPACE_PRISON_LABEL = UIElement(name='EQ_SPACE_PRISON_LABEL')
EQ_SPACE_PRISON_LABEL.description = "Epic Quest: The Galactic Imperative: Space Prison mission label."
EQ_SPACE_PRISON_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_SPACE_PRISON_LABEL.text = "SPACE PRISON"
EQ_SPACE_PRISON_LABEL.text_threshold = 120

EQ_QUANTUM_POWER = UIElement(name='EQ_QUANTUM_POWER')
EQ_QUANTUM_POWER.description = "Epic Quest: The Galactic Imperative: Space Prison: Quantum Power mission."
EQ_QUANTUM_POWER.text_rect = Rect(0.35052083333333334, 0.6611111111111111, 0.4635416666666667, 0.7185185185185186)
EQ_QUANTUM_POWER.button_rect = Rect(0.3515625, 0.30833333333333335, 0.4640625, 0.6157407407407407)
EQ_QUANTUM_POWER.text = "Quantum Power"
EQ_QUANTUM_POWER.text_threshold = 120

EQ_WINGS_OF_DARKNESS = UIElement(name='EQ_WINGS_OF_DARKNESS')
EQ_WINGS_OF_DARKNESS.description = "Epic Quest: The Galactic Imperative: Space Prison: Wings of Darkness mission."
EQ_WINGS_OF_DARKNESS.text_rect = Rect(0.5307291666666667, 0.6601851851851852, 0.6583333333333333, 0.7222222222222222)
EQ_WINGS_OF_DARKNESS.button_rect = Rect(0.5401041666666667, 0.30092592592592593, 0.653125, 0.6092592592592593)
EQ_WINGS_OF_DARKNESS.text = "Wings of Darkness"
EQ_WINGS_OF_DARKNESS.text_threshold = 120

EQ_UNEXPECTED_INTRUDER = UIElement(name='EQ_UNEXPECTED_INTRUDER')
EQ_UNEXPECTED_INTRUDER.description = "Epic Quest: The Galactic Imperative: Unexpected Intruder mission."
EQ_UNEXPECTED_INTRUDER.text_rect = Rect(0.4427083333333333, 0.8703703703703703, 0.5583333333333333, 0.9)
EQ_UNEXPECTED_INTRUDER.button_rect = Rect(0.47291666666666665, 0.7240740740740741, 0.5265625, 0.8203703703703704)
EQ_UNEXPECTED_INTRUDER.text = "UNEXPECTED INTRUDER"
EQ_UNEXPECTED_INTRUDER.text_threshold = 150

EQ_UNEXPECTED_INTRUDER_LABEL = UIElement(name='EQ_UNEXPECTED_INTRUDER_LABEL')
EQ_UNEXPECTED_INTRUDER_LABEL.description = "Epic Quest: The Galactic Imperative: Unexpected Intruder mission label."
EQ_UNEXPECTED_INTRUDER_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_UNEXPECTED_INTRUDER_LABEL.text = "UNEXPECTED INTRUDER"
EQ_UNEXPECTED_INTRUDER_LABEL.text_threshold = 120

EQ_LIKE_BROTHERS = UIElement(name='EQ_LIKE_BROTHERS')
EQ_LIKE_BROTHERS.description = "Epic Quest: First Family: Like Brothers mission."
EQ_LIKE_BROTHERS.text_rect = Rect(0.32431936653928256, 0.869290929840293, 0.4169925781491158, 0.8988700244081679)
EQ_LIKE_BROTHERS.button_rect = Rect(0.3443568176981654, 0.7236218404630178, 0.3960605979206399, 0.8199924388938352)
EQ_LIKE_BROTHERS.text = "LIKE BROTHERS"
EQ_LIKE_BROTHERS.text_threshold = 120

EQ_LIKE_BROTHERS_LABEL = UIElement(name='EQ_LIKE_BROTHERS_LABEL')
EQ_LIKE_BROTHERS_LABEL.description = "Epic Quest: First Family: Like Brothers mission label."
EQ_LIKE_BROTHERS_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_LIKE_BROTHERS_LABEL.text = "LIKE BROTHERS"
EQ_LIKE_BROTHERS_LABEL.text_threshold = 120

EQ_CLOBBERIN_TIME = UIElement(name='EQ_CLOBBERIN_TIME')
EQ_CLOBBERIN_TIME.description = "Epic Quest: First Family: Like Brothers: Cloberrin' Time mission."
EQ_CLOBBERIN_TIME.text_rect = Rect(0.35052083333333334, 0.6611111111111111, 0.4635416666666667, 0.7185185185185186)
EQ_CLOBBERIN_TIME.button_rect = Rect(0.3515625, 0.30833333333333335, 0.4640625, 0.6157407407407407)
EQ_CLOBBERIN_TIME.text = "Cloberrin' Time"
EQ_CLOBBERIN_TIME.text_threshold = 120

EQ_HOTHEAD = UIElement(name='EQ_HOTHEAD')
EQ_HOTHEAD.description = "Epic Quest: First Family: Like Brothers: Hot Head mission."
EQ_HOTHEAD.text_rect = Rect(0.5307291666666667, 0.6601851851851852, 0.6583333333333333, 0.7222222222222222)
EQ_HOTHEAD.button_rect = Rect(0.5401041666666667, 0.30092592592592593, 0.653125, 0.6092592592592593)
EQ_HOTHEAD.text = "Hot Head"
EQ_HOTHEAD.text_threshold = 120

EQ_NEW_FACES = UIElement(name='EQ_NEW_FACES')
EQ_NEW_FACES.description = "Epic Quest: First Family: New Faces mission."
EQ_NEW_FACES.text_rect = Rect(0.464402618837544, 0.8699270394008927, 0.5361438502189013, 0.8988700244081679)
EQ_NEW_FACES.button_rect = Rect(0.4747791560448226, 0.7188510187585216, 0.5250516897559484, 0.8247632605983313)
EQ_NEW_FACES.text = "NEW FACES"
EQ_NEW_FACES.text_threshold = 120

EQ_NEW_FACES_LABEL = UIElement(name='EQ_NEW_FACES_LABEL')
EQ_NEW_FACES_LABEL.description = "Epic Quest: First Family: New Faces mission label."
EQ_NEW_FACES_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_NEW_FACES_LABEL.text = "NEW FACES"
EQ_NEW_FACES_LABEL.text_threshold = 120

EQ_MESSY_FRIENDS = UIElement(name='EQ_MESSY_FRIENDS')
EQ_MESSY_FRIENDS.description = "Epic Quest: X-Force: Messy Friends mission."
EQ_MESSY_FRIENDS.text_rect = Rect(0.32469917364301976, 0.868524665195711, 0.4169877377529281, 0.8985879098180422)
EQ_MESSY_FRIENDS.button_rect = Rect(0.34484794397500756, 0.720447194343166, 0.3962992682156192, 0.8227901547596118)
EQ_MESSY_FRIENDS.text = "MESSY FRIENDS"
EQ_MESSY_FRIENDS.text_threshold = 120

EQ_MESSY_FRIENDS_LABEL = UIElement(name='EQ_MESSY_FRIENDS_LABEL')
EQ_MESSY_FRIENDS_LABEL.description = "Epic Quest: X-Force: Messy Friends mission label."
EQ_MESSY_FRIENDS_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_MESSY_FRIENDS_LABEL.text = "MESSY FRIENDS"
EQ_MESSY_FRIENDS_LABEL.text_threshold = 120

EQ_AW_MAN_THIS_GUY = UIElement(name='EQ_AW_MAN_THIS_GUY')
EQ_AW_MAN_THIS_GUY.description = "Epic Quest: X-Force: Messy Friends: 'Aw, Man. This Guy?' mission."
EQ_AW_MAN_THIS_GUY.text_rect = Rect(0.35052083333333334, 0.6611111111111111, 0.4635416666666667, 0.7185185185185186)
EQ_AW_MAN_THIS_GUY.button_rect = Rect(0.3515625, 0.30833333333333335, 0.4640625, 0.6157407407407407)
EQ_AW_MAN_THIS_GUY.text = "Aw, Man. This Guy?"
EQ_AW_MAN_THIS_GUY.text_threshold = 120

EQ_DOMINO_FALLS = UIElement(name='EQ_DOMINO_FALLS')
EQ_DOMINO_FALLS.description = "Epic Quest: X-Force: Messy Friends: Domino Falls mission."
EQ_DOMINO_FALLS.text_rect = Rect(0.5307291666666667, 0.6601851851851852, 0.6583333333333333, 0.7222222222222222)
EQ_DOMINO_FALLS.button_rect = Rect(0.5401041666666667, 0.30092592592592593, 0.653125, 0.6092592592592593)
EQ_DOMINO_FALLS.text = "Domino Falls"
EQ_DOMINO_FALLS.text_threshold = 120

EQ_TRACKING = UIElement(name='EQ_TRACKING')
EQ_TRACKING.description = "Epic Quest: X-Force: Tracking mission."
EQ_TRACKING.text_rect = Rect(0.40254805072732047, 0.8694056415977213, 0.47093777986126945, 0.8999671720425217)
EQ_TRACKING.button_rect = Rect(0.409648623697512, 0.7199198948568489, 0.4610343491396867, 0.8235633459305204)
EQ_TRACKING.text = "TRACKING"
EQ_TRACKING.text_threshold = 120

EQ_TRACKING_LABEL = UIElement(name='EQ_TRACKING_LABEL')
EQ_TRACKING_LABEL.description = "Epic Quest: X-Force: Tracking mission label."
EQ_TRACKING_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_TRACKING_LABEL.text = "TRACKING"
EQ_TRACKING_LABEL.text_threshold = 120

EQ_GOING_ROGUE = UIElement(name='EQ_GOING_ROGUE')
EQ_GOING_ROGUE.description = "Epic Quest: X-Force: Tracking: Going Rogue mission."
EQ_GOING_ROGUE.text_rect = Rect(0.15130347491769575, 0.6572089454766016, 0.28439709572881905, 0.7236726762187355)
EQ_GOING_ROGUE.button_rect = Rect(0.15578977674278977, 0.29298770100970706, 0.28290166178712106, 0.6372698262539613)
EQ_GOING_ROGUE.text = "Going Rogue"
EQ_GOING_ROGUE.text_threshold = 120

EQ_FRIENDS_AND_ENEMIES = UIElement(name='EQ_FRIENDS_AND_ENEMIES')
EQ_FRIENDS_AND_ENEMIES.description = "Epic Quest: X-Force: Tracking: Friends and Enemies mission."
EQ_FRIENDS_AND_ENEMIES.text_rect = Rect(0.3389804346007966, 0.6585382200914441, 0.47207405541191994, 0.7236726762187355)
EQ_FRIENDS_AND_ENEMIES.button_rect = Rect(0.34197130248419266, 0.28767060255033644, 0.4713263384410709, 0.6372698262539613)
EQ_FRIENDS_AND_ENEMIES.text = "Friends and Enemies"
EQ_FRIENDS_AND_ENEMIES.text_threshold = 120

EQ_WEATHERING_THE_STORM = UIElement(name='EQ_WEATHERING_THE_STORM')
EQ_WEATHERING_THE_STORM.description = "Epic Quest: X-Force: Tracking: Weathering The Storm mission."
EQ_WEATHERING_THE_STORM.text_rect = Rect(0.5259096773130485, 0.6572089454766016, 0.6597510150950209, 0.7210141269890501)
EQ_WEATHERING_THE_STORM.button_rect = Rect(0.5281528282255955, 0.285012053320651, 0.6597510150950207, 0.638599100868804)
EQ_WEATHERING_THE_STORM.text = "Weathering The Storm"
EQ_WEATHERING_THE_STORM.text_threshold = 120

EQ_BLINDSIDED = UIElement(name='EQ_BLINDSIDED')
EQ_BLINDSIDED.description = "Epic Quest: X-Force: Tracking: Blindsided! mission."
EQ_BLINDSIDED.text_rect = Rect(0.7128389200253004, 0.6585382200914442, 0.8481756917489707, 0.7183555777593649)
EQ_BLINDSIDED.button_rect = Rect(0.7135866369961493, 0.2823535040909657, 0.8474279747781217, 0.6372698262539613)
EQ_BLINDSIDED.text = "Blindsided!"
EQ_BLINDSIDED.text_threshold = 120

EQ_MEMORY_MISSION = UIElement(name='EQ_MEMORY_MISSION')
EQ_MEMORY_MISSION.description = "Epic Quest: Sorcerer Supreme: Memory Mission mission."
EQ_MEMORY_MISSION.text_rect = Rect(0.5101246583236204, 0.8693841552303411, 0.6180644993878407, 0.9000870433552749)
EQ_MEMORY_MISSION.button_rect = Rect(0.5372895183247824, 0.7209868626264945, 0.5883810430951802, 0.826208218804653)
EQ_MEMORY_MISSION.text = "MEMORY MISSION"
EQ_MEMORY_MISSION.text_threshold = 120

EQ_MEMORY_MISSION_LABEL = UIElement(name='EQ_MEMORY_MISSION_LABEL')
EQ_MEMORY_MISSION_LABEL.description = "Epic Quest: Sorcerer Supreme: Memory Mission label."
EQ_MEMORY_MISSION_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_MEMORY_MISSION_LABEL.text = "MEMORY MISSION"
EQ_MEMORY_MISSION_LABEL.text_threshold = 120

EQ_ROAD_TO_MONASTERY = UIElement(name='EQ_ROAD_TO_MONASTERY')
EQ_ROAD_TO_MONASTERY.description = "Epic Quest: Sorcerer Supreme: Memory Mission: Road to the Monastery mission."
EQ_ROAD_TO_MONASTERY.text_rect = Rect(0.15130347491769575, 0.6572089454766016, 0.28439709572881905, 0.7236726762187355)
EQ_ROAD_TO_MONASTERY.button_rect = Rect(0.15578977674278977, 0.29298770100970706, 0.28290166178712106, 0.6372698262539613)
EQ_ROAD_TO_MONASTERY.text = "Road to the Monastery"
EQ_ROAD_TO_MONASTERY.text_threshold = 120

EQ_MYSTERIOUS_AMBUSH = UIElement(name='EQ_MYSTERIOUS_AMBUSH')
EQ_MYSTERIOUS_AMBUSH.description = "Epic Quest: Sorcerer Supreme: Memory Mission: Mysterious Ambush mission."
EQ_MYSTERIOUS_AMBUSH.text_rect = Rect(0.3389804346007966, 0.6585382200914441, 0.47207405541191994, 0.7236726762187355)
EQ_MYSTERIOUS_AMBUSH.button_rect = Rect(0.34197130248419266, 0.28767060255033644, 0.4713263384410709, 0.6372698262539613)
EQ_MYSTERIOUS_AMBUSH.text = "Mysterious Ambush"
EQ_MYSTERIOUS_AMBUSH.text_threshold = 120

EQ_MONASTERY_IN_TROUBLE = UIElement(name='EQ_MONASTERY_IN_TROUBLE')
EQ_MONASTERY_IN_TROUBLE.description = "Epic Quest: Sorcerer Supreme: Memory Mission: Monastery in Trouble mission."
EQ_MONASTERY_IN_TROUBLE.text_rect = Rect(0.5259096773130485, 0.6572089454766016, 0.6597510150950209, 0.7210141269890501)
EQ_MONASTERY_IN_TROUBLE.button_rect = Rect(0.5281528282255955, 0.285012053320651, 0.6597510150950207, 0.638599100868804)
EQ_MONASTERY_IN_TROUBLE.text = "Monastery in Trouble"
EQ_MONASTERY_IN_TROUBLE.text_threshold = 120

EQ_POWER_OF_THE_DARK = UIElement(name='EQ_POWER_OF_THE_DARK')
EQ_POWER_OF_THE_DARK.description = "Epic Quest: Sorcerer Supreme: Memory Mission: Power of the Dark mission."
EQ_POWER_OF_THE_DARK.text_rect = Rect(0.7128389200253004, 0.6585382200914442, 0.8481756917489707, 0.7183555777593649)
EQ_POWER_OF_THE_DARK.button_rect = Rect(0.7135866369961493, 0.2823535040909657, 0.8474279747781217, 0.6372698262539613)
EQ_POWER_OF_THE_DARK.text = "Power of the Dark"
EQ_POWER_OF_THE_DARK.text_threshold = 120

EQ_DARK_DIMENSION = UIElement(name='EQ_DARK_DIMENSION')
EQ_DARK_DIMENSION.description = "Epic Quest: Sorcerer Supreme: Dark Dimension mission."
EQ_DARK_DIMENSION.text_rect = Rect(0.641091665481541, 0.8684246899764368, 0.7454335118436205, 0.9007266868578776)
EQ_DARK_DIMENSION.button_rect = Rect(0.6673570268071679, 0.721306684377796, 0.720787248133957, 0.8223703577890362)
EQ_DARK_DIMENSION.text = "DARK DIMENSION"
EQ_DARK_DIMENSION.text_threshold = 120

EQ_DARK_DIMENSION_LABEL = UIElement(name='EQ_DARK_DIMENSION_LABEL')
EQ_DARK_DIMENSION_LABEL.description = "Epic Quest: Sorcerer Supreme: Dark Dimension mission label."
EQ_DARK_DIMENSION_LABEL.text_rect = Rect(0.0515625, 0.010185185185185186, 0.19947916666666668, 0.08333333333333333)
EQ_DARK_DIMENSION_LABEL.text = "DARK DIMENSION"
EQ_DARK_DIMENSION_LABEL.text_threshold = 120

EQ_REFORMED_ROGUES = UIElement(name='EQ_REFORMED_ROGUES')
EQ_REFORMED_ROGUES.description = "Epic Quest: Dark Reign: Reformed Rogues."
EQ_REFORMED_ROGUES.text_rect = Rect(0.44230357137999987, 0.868722018186887, 0.5573529307051074, 0.9001122580314685)
EQ_REFORMED_ROGUES.button_rect = Rect(0.4774317279429164, 0.7322570807572851, 0.5233399537156168, 0.8168455165489996)
EQ_REFORMED_ROGUES.text = "REFORMED ROGUES"
EQ_REFORMED_ROGUES.text_threshold = 120

EQ_REFORMED_ROGUES_LABEL = UIElement(name='EQ_REFORMED_ROGUES_LABEL')
EQ_REFORMED_ROGUES_LABEL.description = "Epic Quest: Dark Reign: Reformed Rogues mission label."
EQ_REFORMED_ROGUES_LABEL.text_rect = Rect(0.05036168385307978, 0.015169306507586995, 0.21635485138155938, 0.0749866641755076)
EQ_REFORMED_ROGUES_LABEL.text = "REFORMED ROGUES"
EQ_REFORMED_ROGUES_LABEL.text_threshold = 120

EQ_CUTTHROAT_COMPANIONS = UIElement(name='EQ_CUTTHROAT_COMPANIONS')
EQ_CUTTHROAT_COMPANIONS.description = "Epic Quest: Dark Reign: Cutthroat Companions mission."
EQ_CUTTHROAT_COMPANIONS.text_rect = Rect(0.3123648005395468, 0.8707044182930752, 0.42996456163418284, 0.8975888820834105)
EQ_CUTTHROAT_COMPANIONS.button_rect = Rect(0.34599014826554714, 0.7204677088764954, 0.3966950376936429, 0.819465793186789)
EQ_CUTTHROAT_COMPANIONS.text = "CUTTHROAT COMPANIONS"
EQ_CUTTHROAT_COMPANIONS.text_threshold = 150

EQ_CUTTHROAT_COMPANIONS_LABEL = UIElement(name='EQ_CUTTHROAT_COMPANIONS_LABEL')
EQ_CUTTHROAT_COMPANIONS_LABEL.description = "Epic Quest: Dark Reign: Cutthroat Companions mission label."
EQ_CUTTHROAT_COMPANIONS_LABEL.text_rect = Rect(0.04961396688223072, 0.003205834974002747, 0.16924868221807193, 0.08695013570909164)
EQ_CUTTHROAT_COMPANIONS_LABEL.text = "CUTTHROAT COMPANIONS"
EQ_CUTTHROAT_COMPANIONS_LABEL.text_threshold = 120

EQ_LEGACY_OF_BLOOD = UIElement(name='EQ_LEGACY_OF_BLOOD')
EQ_LEGACY_OF_BLOOD.description = "Epic Quest: Dark Reign: Cutthroat Companions: Legacy Of Blood mission."
EQ_LEGACY_OF_BLOOD.text_rect = Rect(0.34619169063453226, 0.6632320548693976, 0.46799573835625524, 0.7115198384029028)
EQ_LEGACY_OF_BLOOD.button_rect = Rect(0.35213335149900654, 0.3086186445452173, 0.4633272905341684, 0.6164532645713142)
EQ_LEGACY_OF_BLOOD.text = "LEGACY OF BLOOD"
EQ_LEGACY_OF_BLOOD.text_threshold = 150

EQ_PLAYING_HERO_STAGE_LABEL = UIElement(name='EQ_PLAYING_HERO_STAGE_LABEL')
EQ_PLAYING_HERO_STAGE_LABEL.description = "Epic Quest: Dark Reign: Cutthroat Companions: Playing Hero stage button and text."
EQ_PLAYING_HERO_STAGE_LABEL.text_rect = Rect(0.7147805897933649, 0.8711422030284477, 0.8004764746603729, 0.9000851880357229)
EQ_PLAYING_HERO_STAGE_LABEL.button_rect = Rect(0.7319555479295501, 0.7299258805753683, 0.7850905746633734, 0.8065770826276029)
EQ_PLAYING_HERO_STAGE_LABEL.text = "PLAYING HERO"
EQ_PLAYING_HERO_STAGE_LABEL.text_threshold = 120

EQ_GOLDEN_GODS_STAGE_LABEL = UIElement(name='EQ_GOLDEN_GODS_STAGE_LABEL')
EQ_GOLDEN_GODS_STAGE_LABEL.description = "Epic Quest: Dark Reign: Golden Gods stage text (to detect if it's loaded)."
EQ_GOLDEN_GODS_STAGE_LABEL.text_rect = Rect(0.05110940082392877, 0.016498581122429547, 0.172239550101468, 0.0749866641755076)
EQ_GOLDEN_GODS_STAGE_LABEL.text = "GOLDEN GODS"
EQ_GOLDEN_GODS_STAGE_LABEL.text_threshold = 120

EQ_GOLDEN_GODS_STAGE_1 = UIElement(name='EQ_GOLDEN_GODS_STAGE_1')
EQ_GOLDEN_GODS_STAGE_1.description = "Epic Quest: Dark Reign: Golden Gods stage #1."
EQ_GOLDEN_GODS_STAGE_1.text_rect = Rect(0.33697916666666666, 0.6907407407407408, 0.3697916666666667, 0.725)
EQ_GOLDEN_GODS_STAGE_1.button_rect = Rect(0.2984375, 0.375, 0.4125, 0.6527777777777778)
EQ_GOLDEN_GODS_STAGE_1.text_threshold = 160
EQ_GOLDEN_GODS_STAGE_1.available_characters = "0123456789/"

EQ_GOLDEN_GODS_STAGE_2 = UIElement(name='EQ_GOLDEN_GODS_STAGE_2')
EQ_GOLDEN_GODS_STAGE_2.description = "Epic Quest: Dark Reign: Golden Gods stage #2."
EQ_GOLDEN_GODS_STAGE_2.text_rect = Rect(0.6302083333333334, 0.6907407407407408, 0.6614583333333334, 0.725)
EQ_GOLDEN_GODS_STAGE_2.button_rect = Rect(0.5885416666666666, 0.375, 0.7015625, 0.6527777777777778)
EQ_GOLDEN_GODS_STAGE_2.text_threshold = 120
EQ_GOLDEN_GODS_STAGE_2.available_characters = "0123456789/"
