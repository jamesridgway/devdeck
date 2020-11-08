# Dev Deck
Stream Deck control software for software developers.

Dev Deck ships with Controls and Decks for:

* Command Execution
* Microphone Muting
* Slack
* Timer
* Name List

## Custom Controls
Can find support for what you want? Implement your own `DeckControl` or `DeckController`·

* `DeckControl`
  
  A `DeckControl` is an individual button that can be placed on a deck.
  
* `DeckController`

  A `DeckController` is fronted by a button, pressing the button will take you to a deck screen tailored for the
  given functionality.
  
  For example: Slack is implemented as a DeckController. Pressing the slack button will then present you with buttons
  for specific statuses.
 