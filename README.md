# mff_auto
Game bot for [Marvel Future Fight](https://play.google.com/store/apps/details?id=com.netmarble.mherosgb&hl=ru) game.
Compatible with **7.9.1** version.

## FAQ
**Q**: What this bot can do?

**A**: **mff_auto** can play almost all game modes: 
  World Bosses, Alliance Battle, Co-op missions, Dimension missions, Timeline battles, Legendary battles, 
  World Boss Invasions, Epic Quests, Danger Room, Giant Boss Raid, Shadowland.

Also it can enable *Autoplay++* feature anywhere and do your daily routines.

**Q**: Which Android emulators are supported?

**A**: [NoxPlayer](https://bignox.com) (up to 6.6.1.5) and [BlueStacks](https://www.bluestacks.com).

**A**: [NoxPlayer](https://bignox.com) (up to 7.0.1.1) - Fails to Detect window handle.

**Q**: Why are you suggesting to use **NoxPlayer**?

**A**: NoxPlayer has shortcut to force close applications (requires to reset game's state).
 **Shifter's biometric farming is available only using NoxPlayer!**

## Video example

Video footage of all game modes running by **mff_auto**: https://youtu.be/QcgZcAwBL-I

## Installation

- Install [NoxPlayer](https://bignox.com) (or [BlueStacks](https://www.bluestacks.com))
 and then install and run [Marvel Future Fight](https://play.google.com/store/apps/details?id=com.netmarble.mherosgb).

- Set [NoxPlayer](https://bignox.com)
 (or [BlueStacks](https://www.bluestacks.com))

- Optimal Nox Settings 
  - Screen Resolution **1920x1080**.
  - Optimal Stability for Nox:
  - Windows Size and Position: **Fixed**
  - Performance: **Enhanced Compatibility Mode (OpenGL)**

- Set in [Marvel Future Fight](https://play.google.com/store/apps/details?id=com.netmarble.mherosgb) 

- Optimal In-Game Settings
  - setting `GRAPHICS` to **Medium** or **High**
  - Set `Performance` to **High**
  - Set `Mission Navigation Auto Popup` to **Off**
  - Set `Future Pass Point Acquired` to **Off**
  - Leave all other settings on

  In the same setting's menu turn off this notifications: 
   and .

- Download last release: [Link to releases](https://github.com/dwiza3962/mff_auto/releases)
- Run `start.bat`

## Usage

### Setup window

On first start you will see `Setup` window. Follow the instructions in the window:
- You need to select one of opened emulators. Name of the emulator will be stored in `settings/gui/game.json`.

  You can change it manually after or delete `settings/gui/game.json` if you want to run `Setup` again.

- **(Only for NoxPlayer)** Then you will be asked questions. Read instructions and select `Yes` or `No`.

  At the end you will be asked to click at **MFF** app in the window. 
  Position of app icon will be stored in `settings/gui/game.json`.
 
  You need to **restart NoxPlayer** and **mff_auto** to apply changes.

  This will allow **mff_auto** to close and start the game.
  
### Main window

![main_window](gui_preview.png)

- `Game screen` shows you game's image at 6-7 fps.

- `Missions Queue` allows you to add, edit or remove available missions in **mff_auto**.

  `Run` button will run all checked missions from top to bottom.
  
- `Setting` allows you to edit available settings.

- `Quick Start` allows you to quick run a few modes without adding them to mission queue.

- `Autoplay++` enables casting skills in the battles (also skips cutscenes).

- `Debug Log` at bottom shows you messages about current running code.

  You can also check it in `logs\debug.log` file.

## Development

At current state Marvel Future Fight bot is at beta stage.

- Timeline battle do not check if your team is available for battle. Please setup team manually.

- Alliance and World Boss battles do not check if your characters can do these modes. 
  Make sure that you have strong characters.

- Shadowland requires a big roaster of powerful heroes. 
  Make sure that you have at least 60 to 90 T2 characters and uniforms for them.

- Shadowland Updates - Added BEGINNER_ROSTER for the default behavior above.
  - This uses the last used characters from shadowland on your emulator, or the top 3 of the filter.
  - Sometimes, if uses too many strong characters in the lower stages leaving weaker ones at the later stages.
- Added STRONG_ROSTER option if you have 20+ t3's and awakened characters.
  - It picks one of those and then sorts by level and picks 2 of the lower level people since most strong T3 and T2 can win by themselves.
- Added MAX_ROSTER option and this currently works the same way as STRONG_ROSTER does for now.
  - This is still in progress.   Likely it'll skip your first page of characters for the lower shadowland levels 1-15 or so.

- Use Clear Tickets option has been added, but I think I only have it where it works in Epic Quests.    
- It's much slower actually that just playing through so just play regularly until I can get some more functionality in.
- I want to add in more options for Dimension Missions.



## Contribution

Feel free to contribute. Don't forget about [license](LICENSE).

### Running from source code

- Install [Python 3.6.5](https://www.python.org/downloads/release/python-365)
- Install [Tesseract OCR 3.05.02](https://digi.bib.uni-mannheim.de/tesseract) 
  and add path to Tesseract to your `PATH` environment.
- Download source code and install all requirements: ```pip install -r requirements.txt```
- Copy `tessdata` folder to your Tesseract folder.
- Add `lib` folder to your `PYTHONPATH` or mark it as lib source.

Highly recommend you use an IDE like PyCharm from Jetbrains.
Check `example.py` for examples of running any modes.

In the terminal window -
run `./app_gui.py` for the same behavior as the start.bat from the install
run `./_test_v7.9.1_fixes.py` or any of the other test files run without the GUI.
run `./_captureRectangle.py` to load a screenshot to grab box coordinates for the game.

### Capture video for debugging

```python
from lib.emulators.nox_player import NoxPlayer
from lib.game.game import Game
from lib.video_capture import EmulatorCapture

nox = NoxPlayer("NoxPlayer")
game = Game(nox)
with EmulatorCapture(nox) as recorder:
    # video file is in `logs` folder
    # ... do your stuff here ...
    recorder.pause()
       # pause recording
    recorder.resume()
```

### Building release package from source code

- Update the `version.py` to update the game version
- Run `build.py`
