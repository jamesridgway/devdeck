# Dev Deck
![CI](https://github.com/jamesridgway/devdeck/workflows/CI/badge.svg?branch=main)

Stream Deck control software for software developer's.

[![DevDeck Demo](https://files.james-ridgway.co.uk/images/streamdeck-yt-thumbnail.png)](https://www.youtube.com/watch?v=4ZvrVFW562w)

## Getting Started

If this is your fist time using a StreamDeck make sure to follow the [Pre-requisite: LibUSB HIDAPI Backend](https://github.com/jamesridgway/devdeck/wiki/Installation#pre-requisite-libusb-hidapi-backend) steps documented in the wiki

Install DevDeck

    pip install devdeck


You should then be able to run DevDeck by running:

    devdeck

The first time that DevDeck is run, it will generate a basic `~/.devdeck/settings.yml` populated with the clock control for any Stream Decks that are connected.


## Built-in Controls
Dev Deck ships with the following controls:

* [Clock Control](https://github.com/jamesridgway/devdeck/wiki/Controls#clock-control)
  
  `devdeck.controls.clock_control.ClockControl` is a clock widget for displaying the date and time

* [Command Execution](https://github.com/jamesridgway/devdeck/wiki/Controls#command-control)
  
  `devdeck.controls.command_control.CommandControl` is a control for executing commands on your computer. You can
   specify any command and icon for the given action.

* [Microphone Mute Toggle](https://github.com/jamesridgway/devdeck/wiki/Controls#mic-mute-control)

  `devdeck.controls.mic_mute_control.MicMuteControl` toggles the mute on a given microphone input.

* [Name List](https://github.com/jamesridgway/devdeck/wiki/Controls#name-list-control)

  `devdeck.controls.name_list_control.NameListControl` cycles through initials from a list of names. Useful for things
  like stand-ups were you need to rotate through a team and make sure you cover everyone.
  
* [Timer](https://github.com/jamesridgway/devdeck/wiki/Controls#timer-control)
  
  `devdeck.controls.timer_control.TimerControl` a basic stopwatch timer that can be used to start/stop/reset timing.

* [Volume Control](https://github.com/jamesridgway/devdeck/wiki/Controls#volume-level-control)

  `devdeck.controls.volume_level_control.VolumeLevelControl` sets the volume for a given output to a specified volume 
  level.


* [Volume Mute Control](https://github.com/jamesridgway/devdeck/wiki/Controls#volume-mute-control)

  `devdeck.controls.volume_mute_control.VolumeMuteControl` toggles the muting of a given output.


## Built-in Decks

* [Single Page Deck](https://github.com/jamesridgway/devdeck/wiki/Decks#singlepagedeckcontroller)

  `devdeck.decks.single_page_deck_controller.SinglePageDeckController` provides a basic single page deck for
  controls to be arranged on.

* [Volume Deck](https://github.com/jamesridgway/devdeck/wiki/Decks#volumedeck)

  `devdeck.decks.volume_deck.VolumeDeck` is a pre-built volume deck which will show volume toggles between 0% and 100%
  at 10% increments.

## Plugins
There are a few controls that are provided as plugins. You can always write your own plugin if you can't find the
functionality that you're after:

* [devdeck-slack](https://github.com/jamesridgway/devdeck-slack)

  Controls and decks for Slack. Toggle presence, change status, snooze notifications, etc.

* [devdeck-home-assistant](https://github.com/jamesridgway/devdeck-home-assistant)

  Controls and decks for Home Assistant. Toggle lights, switches, etc.

## Implementing Custom Controls
Can't find support for what you want? Implement your own `DeckControl` or `DeckController`·

* `DeckControl`
  
  A `DeckControl` is an individual button that can be placed on a deck.
  
* `DeckController`

  A `DeckController` is fronted by a button, pressing the button will take you to a deck screen tailored for the
  given functionality.
  
  For example: Slack is implemented as a DeckController. Pressing the slack button will then present you with buttons
  for specific statuses.
 
 ## Developing for DevDeck
 Pull requesta and contributions to this project are welcome.
 
 You can get setup with a virtual environment and all necessary dependencies by running:
 
    ./setup.sh
    
Tests can be run by running:

    ./run-tests.sh

