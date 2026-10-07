import random
from character import Character
from data import MIN_DAMAGE, RED, RESET, BOLD, ITEMS


class Enemy(Character):
    def __init__(
        self,
        name: str,
        hp: int,
        attack_power: int,
        enemy_type: str   = "Demon",
        exp_reward: int   = 30,
        drop_table: tuple = None,
    ):
        super().__init__(name, hp, attack_power)
        self._enemy_type: str  = enemy_type
        self._exp_reward: int  = exp_reward
        self._drop_table       = drop_table

    @property
    def enemy_type(self) -> str:
        return self._enemy_type

    @property
    def exp_reward(self) -> int:
        return self._exp_reward

    def attack(self, target: Character) -> int:
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
        if self._drop_table is None:
            return None
        item_name, chance = self._drop_table
        if random.random() < chance:
            return item_name
        return None

    def get_exp_reward(self) -> int:
        return self._exp_reward

    def __str__(self) -> str:
        return f"{RED}{BOLD}{self._name}{RESET} [{self._enemy_type}] (HP: {self._hp}/{self._max_hp})"

    def __repr__(self) -> str:
        return (
            f"Enemy(name={self._name!r}, hp={self._hp}, "
            f"attack_power={self._attack_power}, "
            f"enemy_type={self._enemy_type!r}, "
            f"exp_reward={self._exp_reward})"
        )
