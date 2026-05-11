# ═══════════════════════════════════════════════════════
#  enemy.py — Enemy class (Inheritance + Polymorphism)
# ═══════════════════════════════════════════════════════

import random
from character import Character
from data import MIN_DAMAGE, RED, RESET, BOLD, ITEMS


class Enemy(Character):
    """
    Enemy character. Inherits from Character (ABC).
    Demonstrates:
      - Inheritance   : super().__init__()
      - Polymorphism  : overrides attack() differently from Player
      - Encapsulation : _enemy_type, _exp_reward as private attrs
    """

    def __init__(
        self,
        name: str,
        hp: int,
        attack_power: int,
        enemy_type: str   = "Demon",
        exp_reward: int   = 30,
        drop_table: tuple = None,   # (item_name, chance_float)
    ):
        super().__init__(name, hp, attack_power)
        self._enemy_type: str  = enemy_type
        self._exp_reward: int  = exp_reward
        self._drop_table       = drop_table  # e.g. ("Corps Ration", 0.35)

    # ── properties ───────────────────────────────────────
    @property
    def enemy_type(self) -> str:
        return self._enemy_type

    @property
    def exp_reward(self) -> int:
        return self._exp_reward

    # ── Polymorphism: Enemy attacks differently ──────────
    def attack(self, target: Character) -> int:
        """
        Enemy attack: random swing with possible critical hit (15 % chance).
        Returns damage dealt.
        """
        base   = self._attack_power + random.randint(-3, 3)
        is_crit= random.random() < 0.15
        damage = max(MIN_DAMAGE, base * 2 if is_crit else base)

        target.hp -= damage

        if is_crit:
            print(f"\n  {RED}{BOLD}{self._name} lands a CRITICAL HIT for {damage} damage!{RESET}")
        else:
            print(f"\n  {RED}{self._name} attacks for {damage} damage!{RESET}")

        return damage

    def get_style_name(self) -> str:
        return self._enemy_type

    def drop_item(self) -> str | None:
        """
        Randomly drop an item based on drop_table.
        Returns item name string or None.
        """
        if self._drop_table is None:
            return None
        item_name, chance = self._drop_table
        if random.random() < chance:
            return item_name
        return None

    def get_exp_reward(self) -> int:
        return self._exp_reward

    # ── magic methods ────────────────────────────────────
    def __str__(self) -> str:
        return f"{RED}{BOLD}{self._name}{RESET} [{self._enemy_type}] (HP: {self._hp}/{self._max_hp})"

    def __repr__(self) -> str:
        return (
            f"Enemy(name={self._name!r}, hp={self._hp}, "
            f"attack_power={self._attack_power}, "
            f"enemy_type={self._enemy_type!r}, "
            f"exp_reward={self._exp_reward})"
        )
