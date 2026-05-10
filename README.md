━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  DEMON SLAYER RPG — Text-Based Python Game
  DCSN03C | Computer Programming 2 | Finals Project
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOW TO RUN
──────────
  python main.py

REQUIREMENTS
────────────
  Python 3.8 or higher
  No third-party packages required.
  Uses only: random, time, os, abc (standard library)

FILE STRUCTURE
──────────────
  main.py       ← Entry point (run this)
  character.py  ← Abstract base class (abc.ABC)
  player.py     ← Player(Character) — inheritance + polymorphism
  enemy.py      ← Enemy(Character)  — inheritance + polymorphism
  item.py       ← Item class with use() method
  game.py       ← Game controller (game loop, combat, menus)
  anim.py       ← Animated text / visual effects
  data.py       ← All constants, styles, story, item data
  README.txt    ← This file

OOP CONCEPTS DEMONSTRATED
──────────────────────────
  Abstraction   : Character(ABC) with @abstractmethod attack()
  Encapsulation : _private attributes with @property in all classes
  Inheritance   : Player(Character), Enemy(Character)
  Polymorphism  : Player.attack() vs Enemy.attack() behave differently
  Magic Methods : __str__, __repr__ in Character, Player, Enemy, Item
  Constructor   : __init__ with super().__init__() in subclasses

CHARACTER CREATION
──────────────────
  Enter your name, then choose your path (Human or Demon).
  When you press ENTER to reveal your clan, the screen clears
  completely — the Clan Awakening section gets its own clean
  screen with a dramatic animated reveal.

CONTROLS (in-game)
──────────────────
  All menus use numbered options [1], [2], etc.
  In combat, type [M] to activate the Demon Slayer Mark (Slayer only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
