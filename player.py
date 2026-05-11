# ═══════════════════════════════════════════════════════
#  player.py — Player class (Inheritance + Polymorphism)
# ═══════════════════════════════════════════════════════

import random
from character import Character
from item import Item
from data import (
    MAX_HP, EXP_PER_LEVEL, LEVEL_HP_BONUS, LEVEL_ATK_BONUS,
    MIN_DAMAGE, CLAN_POOL, SLAYER_RANKS, DEMON_RANKS,
    BREATHING_FORMS, BLOOD_ARTS,
    GREEN, YELLOW, CYAN, RED, MAGENTA, RESET, BOLD, DIM, WHITE,
    RARITY_COLORS,
)


class Player(Character):
    """
    Player character. Inherits Character (ABC).
    Demonstrates:
      - Inheritance   : super().__init__(), super().heal()
      - Polymorphism  : overrides attack() with style-based damage
      - Encapsulation : private stats accessed via @property
      - level_up()    : EXP-based progression
      - use_item()    : inventory management
    """

    TRAIN_CAP = 5

    def __init__(self, name: str, clan: str, path: str = "Human"):
        # base stats before clan bonus
        super().__init__(name, MAX_HP, 10)

        # ── private stats ────────────────────────────────
        self._clan          = clan
        self._path          = path
        self._str: int      = 1
        self._spd: int      = 1
        self._end: int      = 1

        # ── progression ──────────────────────────────────
        self._level: int    = 1
        self._exp: int      = 0
        self._kills: int    = 0
        self._gold: int     = 50
        self._training: int = 0

        # ── rank ─────────────────────────────────────────
        self._rank: str     = "Mizunoto" if path == "Human" else "Lesser Demon"

        # ── inventory (list of Item objects) ─────────────
        self.inventory: list[Item] = []

        # ── style / combat extras ────────────────────────
        self._breathing     = None
        self._blood_art     = None
        self.temp_atk_up    = 0          # single-battle ATK bonus

        # ── custom breathing (Hashira only) ──────────────
        self.custom_style   = None
        self.custom_forms   = []
        self.custom_ult     = None
        self.using_custom   = False
        self.original_ult   = None

        # ── mark / sword ─────────────────────────────────
        self.sword_colour   = None
        self.mark_awakened  = False
        self.mark_used      = False

        # ── story flags ───────────────────────────────────
        self.joined_corps   = False
        self.stayed_human   = False
        self.story_done: set = set()

        # apply clan bonus
        self._apply_clan()

    # ── clan ─────────────────────────────────────────────
    def _apply_clan(self) -> None:
        s = CLAN_POOL[self._clan]["stats"]
        self._str += s[0]
        self._spd += s[1]
        self._end += s[2]

    # ── properties ───────────────────────────────────────
    @property
    def clan(self) -> str:
        return self._clan

    @property
    def path(self) -> str:
        return self._path

    @property
    def level(self) -> int:
        return self._level

    @property
    def exp(self) -> int:
        return self._exp

    @property
    def kills(self) -> int:
        return self._kills

    @kills.setter
    def kills(self, value: int) -> None:
        self._kills = max(0, value)

    @property
    def gold(self) -> int:
        return self._gold

    @gold.setter
    def gold(self, value: int) -> None:
        self._gold = max(0, value)

    @property
    def rank(self) -> str:
        return self._rank

    @rank.setter
    def rank(self, value: str) -> None:
        self._rank = value

    @property
    def training(self) -> int:
        return self._training

    @property
    def breathing(self):
        return self._breathing

    @breathing.setter
    def breathing(self, value) -> None:
        self._breathing = value

    @property
    def blood_art(self):
        return self._blood_art

    @blood_art.setter
    def blood_art(self, value) -> None:
        self._blood_art = value

    # convenience stat properties
    @property
    def str_stat(self) -> int:
        return self._str

    @str_stat.setter
    def str_stat(self, v: int) -> None:
        self._str = v

    @property
    def spd(self) -> int:
        return self._spd

    @spd.setter
    def spd(self, v: int) -> None:
        self._spd = v

    @property
    def end(self) -> int:
        return self._end

    @end.setter
    def end(self, v: int) -> None:
        self._end = v

    @property
    def atk(self) -> int:
        return self._attack_power + self._str + self.temp_atk_up

    # ── active style / forms ─────────────────────────────
    def get_style_name(self) -> str:
        if self._path == "Human":
            if self.using_custom and self.custom_style:
                return f"Custom — {self.custom_style}"
            return self._breathing or "None"
        return self._blood_art or "None"

    @property
    def active_forms(self) -> list:
        if self._path == "Human":
            if self.using_custom and self.custom_forms:
                return self.custom_forms
            return BREATHING_FORMS.get(self._breathing, [])
        return BLOOD_ARTS.get(self._blood_art, [])

    # ── Polymorphism: Player attacks differently ─────────
    def attack(self, target: Character) -> int:
        """
        Basic attack using the player's ATK stat.
        Returns damage dealt.
        """
        damage = max(MIN_DAMAGE, self.atk + random.randint(-2, 3))
        target.hp -= damage
        return damage

    def style_attack(self, target: Character, form_index: int,
                     mark_active: bool = False) -> tuple[int, str]:
        """
        Attack using a specific style form.
        Returns (damage, form_name).
        """
        forms = self.active_forms
        if not forms or form_index >= len(forms):
            return 0, ""
        fname, fpower, _ = forms[form_index]
        multiplier = 2 if mark_active else 1
        mark_bonus = 8 if mark_active else 0
        damage = max(
            MIN_DAMAGE,
            (fpower * multiplier) + self._str + mark_bonus + random.randint(0, 4)
        )
        target.hp -= damage
        return damage, fname

    def ultimate_attack(self, target: Character, mark_active: bool = False) -> tuple[int, str]:
        """Use the ultimate technique. Returns (damage, name)."""
        ult = self.custom_ult if self.using_custom else self.original_ult
        if not ult:
            return 0, ""
        ult_name, ult_power, _ = ult
        multiplier = 2 if mark_active else 1
        mark_bonus = 8 if mark_active else 0
        damage = max(
            MIN_DAMAGE,
            (ult_power * multiplier) + mark_bonus + self._str + random.randint(2, 8)
        )
        target.hp -= damage
        return damage, ult_name

    # ── Progression ──────────────────────────────────────
    def gain_exp(self, amount: int) -> bool:
        """
        Add exp. Returns True if levelled up.
        Demonstrates: iterative while loop for multiple level-ups.
        """
        self._exp += amount
        levelled = False
        while self._exp >= EXP_PER_LEVEL:
            self._exp      -= EXP_PER_LEVEL
            levelled        = True
            self.level_up()
        return levelled

    def level_up(self) -> None:
        """Increase level and stats."""
        self._level          += 1
        self._max_hp         += LEVEL_HP_BONUS
        self._hp              = self._max_hp        # full heal on level-up
        self._attack_power   += LEVEL_ATK_BONUS
        print(f"\n  {YELLOW}{BOLD}✦ LEVEL UP!  You are now Level {self._level}!{RESET}")
        print(f"  {GREEN}Max HP +{LEVEL_HP_BONUS}  |  ATK +{LEVEL_ATK_BONUS}  |  HP fully restored!{RESET}")

    def add_kill(self, count: int = 1) -> None:
        self._kills += count

    def add_gold(self, amount: int) -> None:
        self._gold += amount

    def spend_gold(self, amount: int) -> bool:
        """Deduct gold. Returns True if successful."""
        if self._gold >= amount:
            self._gold -= amount
            return True
        return False

    def train_stat(self, stat: str) -> bool:
        """
        Increase a stat via training.
        Returns False if training cap reached.
        """
        if self._training >= self.TRAIN_CAP:
            return False
        if stat == "str":
            self._str       += 2
        elif stat == "spd":
            self._spd       += 2
        elif stat == "end":
            self._end       += 2
        else:
            return False
        self._training += 1
        return True

    # ── Inventory ────────────────────────────────────────
    def add_item(self, item_name: str) -> None:
        """Add an Item object to inventory."""
        try:
            self.inventory.append(Item(item_name))
        except ValueError:
            pass   # unknown item — silently ignore

    def use_item(self, index: int) -> str:
        """
        Use item at given index (0-based).
        Returns result string. Removes item from inventory.
        """
        if index < 0 or index >= len(self.inventory):
            return f"{YELLOW}Invalid item index.{RESET}"
        item = self.inventory.pop(index)
        return item.use(self)

    # ── Rank helpers ─────────────────────────────────────
    def refresh_rank(self) -> bool:
        """Recalculate rank from kills. Returns True if rank changed."""
        ladder  = SLAYER_RANKS if self._path == "Human" else DEMON_RANKS
        new     = ladder[0][0]
        for name, threshold in ladder:
            if self._kills >= threshold:
                new = name
        if new != self._rank:
            self._rank = new
            return True
        return False

    def next_rank_info(self) -> tuple[str, int]:
        ladder = SLAYER_RANKS if self._path == "Human" else DEMON_RANKS
        for i, (name, threshold) in enumerate(ladder):
            if name == self._rank and i + 1 < len(ladder):
                nxt_name, nxt_thresh = ladder[i + 1]
                return nxt_name, max(0, nxt_thresh - self._kills)
        return ("MAX RANK", 0)

    # ── Display ──────────────────────────────────────────
    def show_stats(self) -> None:
        from data import DIM, CYAN, RED, YELLOW, MAGENTA, RESET, BOLD, WHITE
        clan_info    = CLAN_POOL[self._clan]
        rarity_color = RARITY_COLORS[clan_info["rarity"]]

        print(f"  {BOLD}{self._name}{RESET}  |  Clan: {rarity_color}{self._clan} ({clan_info['rarity']}){RESET}")
        print(f"  Path : {CYAN if self._path == 'Human' else RED}{self._path}{RESET}  |  Rank: {YELLOW}{self._rank}{RESET}")
        print(f"  Level: {YELLOW}{self._level}{RESET}  |  EXP: {self._exp}/{EXP_PER_LEVEL}  |  Kills: {self._kills}")
        print(f"  HP   : {self.hp_bar()}")
        print(f"  ATK  : {self.atk}  STR: {self._str}  SPD: {self._spd}  END: {self._end}")
        print(f"  Gold : {YELLOW}{self._gold}G{RESET}")

        if self._path == "Human":
            val = self._breathing or "None"
            print(f"  Blade: {RED}{self.sword_colour or 'Not chosen'}{RESET}  |  Breathing: {CYAN}{val}{RESET}", end="")
            if self.custom_style:
                print(f"  |  Custom: {MAGENTA}{self.custom_style}{RESET}", end="")
            if self.mark_awakened:
                print(f"  |  {YELLOW}{BOLD}✦ MARK{RESET}", end="")
            print()
        else:
            val = self._blood_art or "None"
            print(f"  Blood Art: {RED}{val}{RESET}")

        if self.inventory:
            items_str = ", ".join(i.name for i in self.inventory)
            print(f"  Bag  : {items_str}")
        else:
            print(f"  Bag  : {DIM}(empty){RESET}")

    # ── magic methods ────────────────────────────────────
    def __str__(self) -> str:
        return (
            f"{BOLD}{self._name}{RESET} | Lv.{self._level} {self._rank} "
            f"(HP: {self._hp}/{self._max_hp})"
        )

    def __repr__(self) -> str:
        return (
            f"Player(name={self._name!r}, clan={self._clan!r}, "
            f"path={self._path!r}, level={self._level}, "
            f"kills={self._kills})"
        )
