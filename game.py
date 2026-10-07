import random
import time
import os

from player import Player
from enemy  import Enemy
from item   import Item
from data   import (
    RESET, RED, GREEN, YELLOW, CYAN, BOLD, DIM, MAGENTA, BLUE, WHITE,
    CLAN_POOL, RARITY_COLORS, RARITY_WEIGHTS,
    SLAYER_RANKS, DEMON_RANKS,
    BREATHING_STYLES, BREATHING_FORMS,
    DEMON_ART_STYLES, BLOOD_ARTS,
    CUSTOM_BREATHING_TEMPLATE,
    ITEMS, SHOP_STOCK, SHOP_PRICES,
    SLAYER_HQ_MISSIONS, DEMON_HQ_MISSIONS,
    SLAYER_STORY, DEMON_STORY,
    FINAL_SELECTION_ENEMIES,
    NICHIRIN_SWORDS, NICHIRIN_SWORD_WEIGHTS, NICHIRIN_SWORD_RARITY_COLORS, MARK_DESCRIPTIONS,
    MAX_HP, EXP_PER_LEVEL,
)
from anim import (
    breathing_form_banner,
    ultimate_flash,
    style_colored,
    animated_main_menu,
    ascii_header,
    battle_header,
    path_colored_header,
)


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def divider(char: str = "─", width: int = 48) -> None:
    print(DIM + char * width + RESET)

def header(title: str, path: str = None) -> None:
    ascii_header(title, path)

def pause(msg: str = "[ Press ENTER to continue ]") -> None:
    input(DIM + msg + RESET)

def slow_print(lines: list, delay: float = 0.05) -> None:
    for line in lines:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(delay * 0.4)
        print()
        time.sleep(delay)

def get_valid_input(min_val: int, max_val: int) -> int:
    try:
        import termios
        termios.tcflush(0, termios.TCIFLUSH)
    except Exception:
        pass

    while True:
        try:
            choice = int(input("  > "))
            if min_val <= choice <= max_val:
                return choice
            print(f"  {YELLOW}Enter a number between {min_val} and {max_val}.{RESET}")
        except ValueError:
            print(f"  {RED}Invalid input — please enter a number.{RESET}")


class Game:
    def __init__(self):
        self.player: Player        = None
        self.enemies: list[Enemy]  = []

    def _hdr_path(self) -> str:
        if not self.player:
            return None
        if getattr(self.player, "stayed_human", False):
            return "Civilian"
        return self.player.path

    def run(self) -> None:
        self._credits_splash()
        self._cinematic_intro()
        while True:
            animated_main_menu()
            menu_choice = get_valid_input(0, 2)
            if menu_choice == 0:
                print(f"\n  {DIM}Farewell. The night is quieter now.{RESET}\n")
                break
            elif menu_choice == 2:
                loaded = self._load_game()
                if not loaded:
                    continue
                if self.player.stayed_human:
                    self._civilian_loop()
                    continue
                self.game_loop()
            else:
                self.player = self._create_character()
                self._path_intro()
                self.game_loop()

            clear()
            print(f"\n  {BOLD}Play again?{RESET}")
            print("  [1] Yes — start a new adventure")
            print("  [0] No  — exit")
            again = get_valid_input(0, 1)
            if again == 0:
                print(f"\n  {DIM}Farewell. The night is quieter now.{RESET}\n")
                break

    def game_loop(self) -> None:
        game_over: bool = False

        while not game_over:
            clear()
            path_colored_header("THE WORLD OF WISTERIA", self._hdr_path())
            self.player.show_stats()

            nxt, needed = self.player.next_rank_info()
            if nxt != "MAX RANK":
                print(f"  Next rank in {needed} kill(s): {YELLOW}{nxt}{RESET}\n")

            self.display_menu()

            max_opt = 9 if (self.player.path == "Human" and self.player.rank == "Hashira") else 8
            choice  = get_valid_input(0, max_opt)

            if choice == 1:
                self._hq_missions()
            elif choice == 2:
                self._story_missions()
            elif choice == 3:
                self._train()
            elif choice == 4:
                self._choose_style()
            elif choice == 5:
                self._use_item_screen()
            elif choice == 6:
                self._visit_shop()
            elif choice == 7:
                self._show_rank_progress()
            elif choice == 8:
                self._save_game()
            elif choice == 9 and self.player.path == "Human" and self.player.rank == "Hashira":
                self._create_custom_style()
            elif choice == 0:
                clear()
                game_over = True
            else:
                print(f"  {DIM}Invalid choice.{RESET}")
                pause()

    def display_menu(self) -> None:
        print("  [1] HQ Missions    — quick assignments")
        print("  [2] Story Missions — main narrative")
        print("  [3] Train")
        print("  [4] Choose Style")
        print("  [5] Use Item")
        print("  [6] Visit Shop")
        print("  [7] Rank Progress")
        print("  [8] Save Game")
        if self.player.path == "Human" and self.player.rank == "Hashira":
            print(f"  [9] {YELLOW}Forge Custom Breathing Style{RESET}")
        print("  [0] Quit")

    def start_battle(
        self,
        enemy_name: str,
        enemy_hp: int,
        enemy_atk: int,
        is_story: bool   = False,
        gold_reward: int = 0,
        kill_reward: int = 1,
        exp_reward: int  = 0,
        drop_table: tuple= None,
    ) -> bool:
        p = self.player
        enemy = Enemy(
            name         = enemy_name,
            hp           = enemy_hp,
            attack_power = enemy_atk,
            exp_reward   = exp_reward,
            drop_table   = drop_table,
        )

        clear()
        header("BATTLE", self._hdr_path())
        print(f"  {RED}{enemy}{RESET}\n")

        p.mark_used    = False
        mark_active    = False
        is_blocking    = False

        while p.is_alive() and enemy.is_alive():
            clear()
            battle_header()
            print(f"  {RED}{BOLD}{enemy_name}{RESET}  (HP: {enemy.hp}/{enemy.max_hp})\n")
            divider()
            print(f"  YOU   : {p.hp_bar()}")
            if mark_active:
                print(f"  {YELLOW}{BOLD}  ✦ MARK ACTIVE — ATK ×2, Forms ×2{RESET}")
            print(f"  ENEMY : {enemy.hp_bar()}  [{enemy_name}]")
            divider()
            print(f"\n  {BOLD}Your turn:{RESET}")
            print("  [1] Basic Attack")
            print("  [2] Use Style Form")

            if p.path == "Human" and p.custom_style:
                toggle = "Switch to Custom" if not p.using_custom else "Switch to Original"
                print(f"  [3] {toggle} Style")
            else:
                print("  [3] Block")

            print("  [4] Block")
            print("  [5] Use Item")

            has_ult = False
            if p.path == "Human":
                if p.using_custom and p.custom_ult:
                    ult_name = p.custom_ult[0]
                    print(f"  [6] {YELLOW}ULTIMATE: {ult_name}{RESET}")
                    has_ult = True
                elif not p.using_custom and p.original_ult:
                    ult_name = p.original_ult[0]
                    print(f"  [6] {YELLOW}ULTIMATE: {ult_name}{RESET}")
                    has_ult = True

            can_mark = (p.path == "Human" and p.mark_awakened
                        and not p.mark_used and not mark_active)
            if can_mark:
                print(f"  [M] {YELLOW}{BOLD}✦ Activate Demon Slayer Mark{RESET}"
                      f"  {DIM}(once per battle — costs 10 HP){RESET}")

            action = input("\n  > ").strip().lower()

            if action == "m" and can_mark:
                mark_active    = True
                p.mark_used    = True
                p.hp           = max(1, p.hp - 10)
                style_key      = p.breathing or "Water"
                desc           = MARK_DESCRIPTIONS.get(style_key, "A mark blazes across your skin.")
                print(f"\n  {YELLOW}{BOLD}✦ THE MARK AWAKENS ✦{RESET}")
                print(f"  {DIM}{desc}{RESET}")
                print(f"  {RED}-10 HP{RESET}  |  {GREEN}ATK ×2 | Forms ×2 this turn{RESET}")
                time.sleep(0.1)
                action = ""

            if action == "1":
                mark_bonus = 8 if mark_active else 0
                dmg = max(1, p.atk + mark_bonus + random.randint(-2, 3))
                enemy.hp -= dmg
                crit_tag = f" {YELLOW}[MARK]{RESET}" if mark_active else ""
                print(f"\n  You strike for {GREEN}{dmg}{RESET} damage!{crit_tag}")

            elif action == "2":
                forms = p.active_forms
                if not forms:
                    print(f"\n  {YELLOW}You haven't chosen a style yet.{RESET}")
                else:
                    clear()
                    battle_header()
                    print(f"  {RED}{BOLD}{enemy_name}{RESET}  (HP: {enemy.hp}/{enemy.max_hp})\n")
                    divider()
                    print(f"  YOU   : {p.hp_bar()}")
                    print(f"  ENEMY : {enemy.hp_bar()}  [{enemy_name}]")
                    divider()
                    print(f"\n  {BOLD}{p.get_style_name()} Forms:{RESET}")
                    for i, (fname, fpower, fdesc) in enumerate(forms, 1):
                        eff   = fpower * (2 if mark_active else 1)
                        mtag  = f" {YELLOW}[×2]{RESET}" if mark_active else ""
                        print(f"  [{i}] {fname} — dmg {eff}{mtag}")
                        print(f"       {DIM}{fdesc}{RESET}")
                    print("  [0] Cancel")

                    try:
                        import termios
                        termios.tcflush(0, termios.TCIFLUSH)
                    except Exception:
                        pass

                    while True:
                        try:
                            fc = int(input("\n  > "))
                            if fc == 0:
                                print(f"  {DIM}Cancelled.{RESET}")
                                break
                            if 1 <= fc <= len(forms):
                                dmg, fname = p.style_attack(enemy, fc - 1, mark_active)
                                _, _, fdesc = forms[fc - 1]
                                breathing_form_banner(p.breathing or "Water", fname)
                                print(f"  {DIM}{fdesc}{RESET}")
                                print(f"  You deal {style_colored(p.breathing or 'Water', str(dmg))} damage!")
                                break
                            print(f"  {YELLOW}Enter 0–{len(forms)}.{RESET}")
                        except ValueError:
                            print(f"  {RED}Enter a number.{RESET}")

            elif action == "3":
                if p.path == "Human" and p.custom_style:
                    p.using_custom = not p.using_custom
                    label = f"Custom — {p.custom_style}" if p.using_custom else p.breathing
                    print(f"\n  {CYAN}Switched to: {label}{RESET}")
                else:
                    is_blocking = True
                    print(f"\n  {BLUE}You brace for impact.{RESET}")

            elif action == "4":
                is_blocking = True
                print(f"\n  {BLUE}You brace for impact.{RESET}")

            elif action == "5":
                self._use_item_in_combat()

            elif action == "6" and has_ult:
                dmg, uname = p.ultimate_attack(enemy, mark_active)
                ultimate_flash(p.breathing or "Water", uname)
                if p.using_custom and p.custom_ult:
                    print(f"  {DIM}{p.custom_ult[2]}{RESET}")
                elif p.original_ult:
                    print(f"  {DIM}{p.original_ult[2]}{RESET}")
                time.sleep(0.1)
                enemy.hp -= 0
                print(f"  You unleash {GREEN}{BOLD}{dmg}{RESET} damage!!")

            elif action not in ("", "m"):
                print(f"  {DIM}Invalid — you hesitate.{RESET}")

            mark_active = False

            if not enemy.is_alive():
                break

            if is_blocking:
                reduction = 5 + p.end // 3
                raw       = enemy._attack_power + random.randint(-3, 3)
                taken     = max(1, raw - reduction)
                p.hp     -= taken
                print(f"\n  {enemy_name} attacks! {RED}{taken}{RESET} damage (blocked {reduction}).")
            else:
                enemy.attack(p)

            is_blocking = False
            time.sleep(0.8)

        print()
        if p.is_alive():
            print(f"  {GREEN}{BOLD}You defeated {enemy_name}!{RESET}")
            p.full_heal()
            print(f"  {DIM}HP restored to full.{RESET}")

            if not is_story:
                p.add_kill(kill_reward)
                p.add_gold(gold_reward)
                p.temp_atk_up = 0
                print(f"  +{kill_reward} kill(s)  |  +{gold_reward}G  |  +{exp_reward} EXP")

                if exp_reward > 0:
                    p.gain_exp(exp_reward)

            if drop_table:
                dropped = enemy.drop_item()
                if dropped:
                    p.add_item(dropped)
                    print(f"\n  {YELLOW}Item found: {dropped}!{RESET}")
                    print(f"  {DIM}{ITEMS[dropped]['desc']}{RESET}")

            pause()
            return True

        else:
            p.hp = 0
            print(f"  {RED}{BOLD}You were defeated…{RESET}")
            pause()
            return False

    def _hq_missions(self) -> None:
        pool  = SLAYER_HQ_MISSIONS if self.player.path == "Human" else DEMON_HQ_MISSIONS
        tier  = min(len(pool) - 1, self.player.kills // 10)
        lo    = max(0, tier - 1)
        hi    = min(len(pool) - 1, tier + 1)
        offer = random.sample(pool[lo:hi + 1], k=min(3, hi - lo + 1))

        while True:
            clear()
            label = "CORPS HQ — MISSIONS" if self.player.path == "Human" else "MUZAN'S ORDERS"
            header(label, self._hdr_path())
            print("  Available assignments:\n")

            for i, m in enumerate(offer, 1):
                print(f"  [{i}] {BOLD}{m['title']}{RESET}")
                print(f"       {DIM}{m['briefing']}{RESET}")
                print(f"       Target: {RED}{m['enemy']}{RESET}  |  "
                      f"Reward: {YELLOW}{m['gold']}G{RESET} +{m['kills']} kill(s) +{m['exp']} EXP")
                print()
            print("  [0] Back")

            choice = get_valid_input(0, len(offer))
            if choice == 0:
                break

            m = offer[choice - 1]
            clear()
            header("MISSION BRIEFING", self._hdr_path())
            print(f"  {BOLD}{m['title']}{RESET}")
            print(f"\n  {m['briefing']}")
            print(f"\n  Target : {RED}{m['enemy']}{RESET}")
            print(f"  Reward : {YELLOW}{m['gold']}G{RESET}  +{m['kills']} kill(s)  +{m['exp']} EXP")
            print()
            pause("[ ENTER to deploy ]")

            won = self.start_battle(
                m["enemy"], m["hp"], m["atk"],
                is_story    = False,
                gold_reward = m["gold"],
                kill_reward = m["kills"],
                exp_reward  = m["exp"],
                drop_table  = m.get("drop"),
            )
            if won:
                ranked_up = self.player.refresh_rank()
                if ranked_up:
                    print(f"\n  {YELLOW}{BOLD}RANK UP!  You are now: {self.player.rank}{RESET}")
                    pause()
                    self._try_awaken_mark()
            break

    def _story_missions(self) -> None:
        story  = SLAYER_STORY if self.player.path == "Human" else DEMON_STORY
        ladder = SLAYER_RANKS if self.player.path == "Human" else DEMON_RANKS
        rank_names = [r[0] for r in ladder]

        player_idx = rank_names.index(self.player.rank) if self.player.rank in rank_names else 0

        while True:
            clear()
            header("STORY MISSIONS", self._hdr_path())
            print("  Chapters unlock at the required rank.\n")

            entries = []
            for chapter in story:
                ch_idx   = rank_names.index(chapter["rank"]) if chapter["rank"] in rank_names else 999
                unlocked = player_idx >= ch_idx
                key      = chapter["rank"] + chapter["title"]
                played   = key in self.player.story_done

                if unlocked and not played:
                    flag = f"{GREEN}[NEW]{RESET}"
                elif played:
                    flag = f"{DIM}[done]{RESET}"
                else:
                    flag = f"{DIM}[locked — need rank: {chapter['rank']}]{RESET}"

                entries.append((chapter, unlocked))
                print(f"  [{len(entries)}] {chapter['title']}  {flag}\n")

            print("  [0] Back")
            choice = get_valid_input(0, len(entries))

            if choice == 0:
                break

            chapter, unlocked = entries[choice - 1]
            if not unlocked:
                print(f"\n  {YELLOW}Locked. Reach rank {chapter['rank']} first.{RESET}")
                pause()
            else:
                self._play_story_chapter(chapter)
                self.player.story_done.add(chapter["rank"] + chapter["title"])
                if self.player.refresh_rank():
                    self._try_awaken_mark()

    def _play_story_chapter(self, chapter: dict) -> None:
        if chapter.get("multi_stage"):
            self._play_multi_stage_chapter(chapter)
        elif chapter.get("choice_type") == "demon_king":
            self._play_demon_king_chapter(chapter)
        else:
            self._play_single_boss_chapter(chapter)

    def _play_single_boss_chapter(self, chapter: dict) -> None:
        clear()
        header(chapter["title"], self._hdr_path())
        for line in chapter["lines"]:
            print("  " + line)
        print()
        pause("[ Prepare yourself — ENTER to fight ]")

        won = self.start_battle(
            chapter["boss"],
            chapter["boss_hp"],
            chapter["boss_atk"],
            is_story   = True,
            exp_reward = chapter.get("exp", 0),
        )

        if won:
            self.player.gain_exp(chapter.get("exp", 0))
            clear()
            divider("*")
            print(f"  {GREEN}{BOLD}VICTORY{RESET}")
            divider("*")
            for line in chapter["victory_lines"]:
                print("  " + line)
            print()
            if chapter.get("choice_type") == "demon_final":
                self._demon_final_choice(chapter)
            pause()
        else:
            self.player.full_heal()
            print(f"\n  {YELLOW}You fall… but the story isn't over yet.{RESET}")
            print(f"  {DIM}HP restored. Recover and try again.{RESET}")
            pause()

    def _play_multi_stage_chapter(self, chapter: dict) -> None:
        clear()
        header(chapter["title"], self._hdr_path())
        print(f"\n  {DIM}This chapter has {len(chapter['stages'])} stages.{RESET}\n")
        pause("[ ENTER to begin ]")

        total_exp = chapter.get("exp", 0)
        exp_per_stage = total_exp // max(len(chapter["stages"]), 1)

        for i, stage in enumerate(chapter["stages"], 1):
            while True:
                clear()
                print(f"\n  {BOLD}{YELLOW}[ {stage['label']} ]{RESET}\n")
                for line in stage["lines"]:
                    print("  " + line)
                print()

                if stage.get("choice"):
                    print(f"\n  {BOLD}Your choice:{RESET}")
                    choice = get_valid_input(1, 2)
                    self._handle_stage_choice(stage, choice)

                    if not stage.get("boss"):
                        break

                pause("[ Prepare yourself — ENTER to fight ]")

                won = self.start_battle(
                    stage["boss"],
                    stage["boss_hp"],
                    stage["boss_atk"],
                    is_story   = True,
                    exp_reward = exp_per_stage,
                )

                if won:
                    self.player.gain_exp(exp_per_stage)
                    clear()
                    divider("*")
                    print(f"  {GREEN}{BOLD}STAGE {i} CLEAR{RESET}")
                    divider("*")
                    for line in stage.get("victory_lines", []):
                        print("  " + line)
                    print()
                    pause()
                    break
                else:
                    self.player.full_heal()
                    print(f"\n  {YELLOW}You fall… but the story isn't over yet.{RESET}")
                    print(f"  {DIM}HP restored. Retrying this stage.{RESET}")
                    pause()

        clear()
        divider("═")
        print(f"\n  {GREEN}{BOLD}CHAPTER COMPLETE — {chapter['title']}{RESET}\n")
        divider("═")
        print()
        pause()

    def _handle_stage_choice(self, stage: dict, choice: int) -> None:
        label = stage.get("label", "")

        if "AKAZA" in label.upper() and "MUGEN" not in label.upper():
            if choice == 1:
                print(f"\n  {RED}You charge at Akaza alongside Rengoku!{RESET}")
                print(f"  {DIM}His eyes widen. He smiles — this is a real fight now.{RESET}\n")
            else:
                print(f"\n  {CYAN}You hold the line, tending Rengoku's wounds.{RESET}")
                print(f"  {DIM}Every second you buy him is a second closer to dawn.{RESET}\n")
                self.player.atk = max(1, self.player.atk - 5)
                print(f"  {YELLOW}Rengoku inspired you: +3 END permanently.{RESET}")
                self.player.end = getattr(self.player, 'end', 0) + 3
            time.sleep(0.8)

        elif "KAIGAKU" in label.upper():
            if choice == 1:
                print(f"\n  {RED}You fight beside Zenitsu — shoulder to shoulder.{RESET}")
                print(f"  {DIM}Zenitsu glances at you. Something steadies in him.{RESET}\n")
            else:
                print(f"\n  {CYAN}You step back. Zenitsu faces Kaigaku alone.{RESET}")
                print(f"  {DIM}The weight of that silence — and his answer to it — is his alone.{RESET}\n")
            time.sleep(0.8)

        elif "DEMON KING" in label.upper() or "CHAPTER 9" in stage.get("label", "").upper():
            if choice == 2:
                print(f"\n  {RED}You stop fighting the blood. You let it in.{RESET}")
                print(f"  {MAGENTA}The hunger grows — then quiets.{RESET}")
                print(f"  {MAGENTA}You are something new now. Something the night remembers.{RESET}\n")
                time.sleep(1)
            else:
                print(f"\n  {CYAN}You fight it. Every instinct in your body screams.{RESET}")
                print(f"  {YELLOW}But you are still you. You will not let go of that.{RESET}\n")
                time.sleep(0.8)

    def _play_demon_king_chapter(self, chapter: dict) -> None:
        clear()
        header(chapter["title"], self._hdr_path())
        for line in chapter["lines"]:
            print("  " + line)
        print()

        choice = get_valid_input(1, 2)

        if choice == 1:
            print(f"\n  {CYAN}You raise everything you have against the blood.{RESET}\n")
            time.sleep(0.6)
            pause("[ ENTER to fight Muzan's will ]")

            won = self.start_battle(
                chapter["boss"],
                chapter["boss_hp"],
                chapter["boss_atk"],
                is_story   = True,
                exp_reward = chapter.get("exp", 0),
            )

            if won:
                self.player.gain_exp(chapter.get("exp", 0))
                clear()
                divider("*")
                print(f"  {GREEN}{BOLD}HUMANITY PRESERVED{RESET}")
                divider("*")
                for line in chapter["victory_lines"]:
                    print("  " + line)
            else:
                self.player.full_heal()
                clear()
                print(f"\n  {RED}Muzan's blood overwhelms you...{RESET}")
                print(f"  {DIM}But even then — a fragment of you holds on.{RESET}")
                print(f"  {DIM}HP restored. Try again.{RESET}")
        else:
            clear()
            divider("*")
            print(f"  {MAGENTA}{BOLD}THE NIGHT IS YOURS{RESET}")
            divider("*")
            for line in chapter.get("demon_king_lines", []):
                print("  " + line)
            self.player.gain_exp(chapter.get("exp", 0))

        print()
        pause()

    def _demon_final_choice(self, chapter: dict) -> None:
        print(f"\n  {BOLD}One last thing remains.{RESET}")
        print(f"  {YELLOW}What do you do with the world Muzan left behind?{RESET}\n")
        time.sleep(0.5)

    def _train(self) -> None:
        p = self.player
        clear()
        header("TRAINING GROUNDS", self._hdr_path())

        if p.training >= Player.TRAIN_CAP:
            print(f"  {YELLOW}You've pushed your body to its limit for now.{RESET}")
            print(f"  {DIM}(Training cap of {Player.TRAIN_CAP} sessions reached){RESET}")
            pause()
            return

        print(f"  Sessions remaining: {Player.TRAIN_CAP - p.training}/{Player.TRAIN_CAP}\n")
        print(f"  Choose what to train. Each has a mini-game.")
        print(f"  Pass it — gain the stat. Fail it — gain nothing.\n")
        print("  [1] Strength   — Boulder Smash  (STR +2)")
        print("  [2] Speed      — Lightning Dash  (SPD +2)")
        print("  [3] Endurance  — Breath Control  (END +2)")
        print("  [0] Back\n")

        choice = get_valid_input(0, 3)
        if choice == 0:
            return

        stat_map  = {1: "str",  2: "spd",  3: "end"}
        label_map = {1: "STR",  2: "SPD",  3: "END"}
        stat  = stat_map[choice]
        label = label_map[choice]

        if   choice == 1: passed = self._minigame_strength()
        elif choice == 2: passed = self._minigame_speed()
        elif choice == 3: passed = self._minigame_endurance()

        if passed:
            p.train_stat(stat)
            new_val = getattr(p, stat if stat != "str" else "str_stat")
            print(f"\n  {GREEN}{BOLD}Training successful! {label} increased to {new_val}!{RESET}")
        else:
            p._training += 1
            print(f"\n  {RED}You pushed hard but couldn't break through this time.{RESET}")
            print(f"  {DIM}Session used. Try a different approach next time.{RESET}")
        pause()

    def _minigame_strength(self) -> bool:
        clear()
        header("BOULDER SMASH — STRENGTH TRIAL", self._hdr_path())
        slow_print([
            "  A massive boulder sits before you.",
            "  Your master points at the cracks.",
            "  'Strike them in order. Muscle memory is everything.'",
            "",
        ])
        pause("[ ENTER to begin ]")

        import string
        sequence = random.choices(["L", "R", "U", "D"], k=5)
        labels   = {"L": "Left", "R": "Right", "U": "Up", "D": "Down"}

        print(f"\n  {BOLD}Memorize the strike sequence:{RESET}")
        print(f"  {CYAN}{' → '.join(labels[s] for s in sequence)}{RESET}\n")
        time.sleep(2.5)

        clear()
        header("BOULDER SMASH — STRIKE!", self._hdr_path())
        print(f"  {DIM}The sequence has faded. Strike from memory.{RESET}")
        print(f"  Enter: {BOLD}L{RESET}=Left  {BOLD}R{RESET}=Right  {BOLD}U{RESET}=Up  {BOLD}D{RESET}=Down\n")

        correct = 0
        for i, expected in enumerate(sequence, 1):
            while True:
                ans = input(f"  Strike {i}/5: ").strip().upper()
                if ans in ("L", "R", "U", "D"):
                    break
                print(f"  {RED}Enter L, R, U, or D.{RESET}")
            if ans == expected:
                print(f"  {GREEN}✔  Crack!{RESET}")
                correct += 1
            else:
                print(f"  {RED}✘  The stone holds. (Was: {labels[expected]}){RESET}")

        print()
        passed = correct >= 4
        if passed:
            print(f"  {GREEN}{BOLD}The boulder shatters! ({correct}/5 correct){RESET}")
        else:
            print(f"  {YELLOW}The boulder barely moved. ({correct}/5 correct — need 4+){RESET}")
        time.sleep(1)
        return passed

    def _minigame_speed(self) -> bool:
        clear()
        header("LIGHTNING DASH — SPEED TRIAL", self._hdr_path())
        slow_print([
            "  Your master stands at the end of the track.",
            "  'When the signal comes — move. Don't think. Move.'",
            "",
        ])
        pause("[ ENTER to get ready ]")

        for count in ["3", "2", "1", f"{GREEN}{BOLD}GO!{RESET}"]:
            clear()
            header("LIGHTNING DASH — SPEED TRIAL", self._hdr_path())
            print(f"\n  {BOLD}{count}{RESET}\n")
            time.sleep(0.9 if count != f"{GREEN}{BOLD}GO!{RESET}" else 0.1)

        words  = ["RENAN", "JULIANNE", "BENEDICT", "PATRICK", "SIXSEVEN", "WIND", "SURGE"]
        target = random.choice(words)

        clear()
        header("LIGHTNING DASH — GO!", self._hdr_path())
        print(f"\n  Type this word as fast as you can:\n")
        print(f"  {YELLOW}{BOLD}  {target}  {RESET}\n")

        start = time.time()
        ans   = input("  > ").strip().upper()
        elapsed = time.time() - start

        print()
        if ans == target and elapsed <= 3.5:
            print(f"  {GREEN}{BOLD}Like lightning! ({elapsed:.2f}s — target: ≤3.5s){RESET}")
            return True
        elif ans == target:
            print(f"  {YELLOW}Correct word, but too slow ({elapsed:.2f}s — need ≤3.5s).{RESET}")
            return False
        else:
            print(f"  {RED}Wrong word typed. Focus!{RESET}")
            return False

    def _minigame_endurance(self) -> bool:
        clear()
        header("BREATH CONTROL — ENDURANCE TRIAL", self._hdr_path())
        slow_print([
            "  Your master sits across from you.",
            "  'Total Concentration Breathing is not a technique.'",
            "  'It is a state. You must hold it.'",
            "  'Match my rhythm. Breathe with me.'",
            "",
        ])
        pause("[ ENTER to begin breathing ]")

        rounds   = 5
        interval = 2.0
        tolerance= 0.6
        passed_rounds = 0

        clear()
        header("BREATH CONTROL — HOLD IT", self._hdr_path())
        print(f"  Press ENTER every {interval} seconds to match the rhythm.")
        print(f"  {DIM}({rounds} breaths — hit within ±{tolerance}s each time){RESET}\n")
        pause("[ ENTER to start the first breath ]")

        for i in range(1, rounds + 1):
            target_time = time.time() + interval
            print(f"  Breath {i}/{rounds}… ", end="", flush=True)
            start = time.time()
            input("")
            elapsed  = time.time() - start
            diff     = abs(elapsed - interval)

            if diff <= tolerance:
                print(f"  {GREEN}✔  Perfect breath ({elapsed:.2f}s){RESET}")
                passed_rounds += 1
            else:
                direction = "too fast" if elapsed < interval else "too slow"
                print(f"  {RED}✘  Off rhythm ({elapsed:.2f}s — {direction}){RESET}")
            time.sleep(0.3)

        print()
        passed = passed_rounds >= 4
        if passed:
            print(f"  {GREEN}{BOLD}Total Concentration achieved! ({passed_rounds}/{rounds} breaths){RESET}")
        else:
            print(f"  {YELLOW}Your breath broke. ({passed_rounds}/{rounds} — need 4+){RESET}")
        time.sleep(1)
        return passed

    def _choose_style(self) -> None:
        p = self.player

        if p.path == "Human" and p.breathing:
            print(f"\n  {YELLOW}You have already chosen: {p.breathing}{RESET}")
            pause()
            return
        if p.path != "Human" and p.blood_art:
            print(f"\n  {YELLOW}You have already chosen: {p.blood_art}{RESET}")
            pause()
            return

        clear()
        if p.path == "Human":
            header("BREATHING STYLE", self._hdr_path())
            styles = BREATHING_STYLES
            label  = "Breathing Style"
        else:
            header("BLOOD DEMON ART", self._hdr_path())
            styles = DEMON_ART_STYLES
            label  = "Blood Art"

        print(f"  Choose your {label}:\n")
        for i, s in enumerate(styles, 1):
            forms_list = (BREATHING_FORMS if p.path == "Human" else BLOOD_ARTS)[s]
            print(f"  [{i}] {BOLD}{s}{RESET}")
            for fname, fpower, fdesc in forms_list:
                print(f"       {DIM}• {fname} (dmg {fpower}){RESET}")
            print()

        choice = get_valid_input(1, len(styles))
        chosen = styles[choice - 1]

        if p.path == "Human":
            p.breathing = chosen
        else:
            p.blood_art = chosen

        print(f"\n  {GREEN}You have chosen: {chosen}!{RESET}")
        pause()

    def _use_item_screen(self) -> None:
        p = self.player
        clear()
        header("USE ITEM", self._hdr_path())
        if not p.inventory:
            print(f"  {YELLOW}Your bag is empty.{RESET}")
            pause()
            return
        self._show_inventory_menu(p)
        pause()

    def _use_item_in_combat(self) -> None:
        p = self.player
        if not p.inventory:
            print(f"\n  {YELLOW}Your bag is empty.{RESET}")
            return
        print(f"\n  {BOLD}Your bag:{RESET}")
        for i, item in enumerate(p.inventory, 1):
            print(f"  [{i}] {item}")
        print("  [0] Cancel")

        while True:
            try:
                fc = int(input("\n  > "))
                if fc == 0:
                    print(f"  {DIM}Cancelled.{RESET}")
                    return
                if 1 <= fc <= len(p.inventory):
                    result = p.use_item(fc - 1)
                    print(f"\n  {result}")
                    return
                print(f"  {YELLOW}Enter 0–{len(p.inventory)}.{RESET}")
            except ValueError:
                print(f"  {RED}Enter a number.{RESET}")

    def _show_inventory_menu(self, p: Player) -> None:
        print(f"  {BOLD}Your bag:{RESET}\n")
        if not p.inventory:
            print(f"  {DIM}(empty){RESET}")
            return
        for i, item in enumerate(p.inventory, 1):
            print(f"  [{i}] {item}")
        print("  [0] Cancel")
        choice = get_valid_input(0, len(p.inventory))
        if choice == 0:
            return
        result = p.use_item(choice - 1)
        print(f"\n  {result}")

    def _visit_shop(self) -> None:
        p = self.player
        while True:
            clear()
            header("MERCHANT", self._hdr_path())
            print(f"  Your gold: {YELLOW}{p.gold}G{RESET}\n")

            for i, item_name in enumerate(SHOP_STOCK, 1):
                price = SHOP_PRICES[item_name]
                print(f"  [{i}] {item_name:20} {YELLOW}{price}G{RESET}"
                      f"  — {DIM}{ITEMS[item_name]['desc']}{RESET}")

            print("\n  [0] Leave")
            choice = get_valid_input(0, len(SHOP_STOCK))

            if choice == 0:
                break

            item_name = SHOP_STOCK[choice - 1]
            price     = SHOP_PRICES[item_name]

            if p.spend_gold(price):
                p.add_item(item_name)
                print(f"\n  {GREEN}Purchased {item_name}!{RESET}")
            else:
                print(f"\n  {RED}Not enough gold.{RESET}")
            pause()

    def _show_rank_progress(self) -> None:
        p      = self.player
        clear()
        header("RANK PROGRESS", self._hdr_path())
        ladder = SLAYER_RANKS if p.path == "Human" else DEMON_RANKS

        for name, threshold in reversed(ladder):
            if name == p.rank:
                row = f"  {YELLOW}{BOLD}▶ {name:30}{RESET} {DIM}({threshold} kills){RESET}"
            elif p.kills >= threshold:
                row = f"  {GREEN}  {name:30}{RESET} {DIM}({threshold} kills){RESET}"
            else:
                row = f"  {DIM}  {name:30} ({threshold} kills){RESET}"
            print(row)

        nxt, needed = p.next_rank_info()
        print()
        if nxt == "MAX RANK":
            print(f"  {YELLOW}You have reached the highest rank!{RESET}")
        else:
            print(f"  Next rank: {YELLOW}{nxt}{RESET} — {needed} more kill(s).")
        print()
        pause()

    def _roll_sword(self) -> str:
        pool = []
        for colour, data in NICHIRIN_SWORDS.items():
            weight = NICHIRIN_SWORD_WEIGHTS.get(data["rarity"], 10)
            pool.extend([colour] * weight)
        return random.choice(pool)

    def _choose_sword(self) -> None:
        p = self.player
        if p.sword_colour:
            return

        clear()
        header("YOUR NICHIRIN BLADE", self._hdr_path())
        slow_print([
            "  The swordsmith hands you a special ore mined from the mountains.",
            "  Every Nichirin sword absorbs sunlight —",
            "  the one thing demons cannot bear.",
            "  The colour it takes is not chosen.",
            "  It is revealed.",
            "",
            "  Your soul will decide.",
            "",
        ])
        pause("[ ENTER to reveal your blade ]")

        clear()
        header("NICHIRIN BLADE AWAKENING", self._hdr_path())
        sword_names = list(NICHIRIN_SWORDS.keys())
        input("  Press ENTER to reveal your blade colour… ")
        for _ in range(20):
            preview = random.choice(sword_names)
            rcolor  = NICHIRIN_SWORD_RARITY_COLORS[NICHIRIN_SWORDS[preview]["rarity"]]
            print(f"\r  Resonating…  {rcolor}{BOLD}{preview:20}{RESET}", end="", flush=True)
            time.sleep(0.09)

        colour = self._roll_sword()
        data   = NICHIRIN_SWORDS[colour]
        rarity = data["rarity"]
        rcolor = NICHIRIN_SWORD_RARITY_COLORS[rarity]

        print(f"\r  ✦  Blade: {rcolor}{BOLD}{colour:20}{RESET}  ({rarity})   ")
        print()
        time.sleep(0.4)

        print(f"  {DIM}{data['desc']}{RESET}")
        if data['owner'] != "Unknown":
            print(f"  {DIM}Colour also carried by: {data['owner']}{RESET}")
        print(f"  Bonus: {GREEN}{data['bonus']}{RESET}")
        print()

        p.sword_colour = colour

        stat, val = data["stat"]
        if   stat == "str": p.str_stat += val
        elif stat == "spd": p.spd      += val
        elif stat == "end": p.end      += val
        if "stat2" in data:
            s2, v2 = data["stat2"]
            if   s2 == "str": p.str_stat += v2
            elif s2 == "spd": p.spd      += v2
            elif s2 == "end": p.end      += v2

        slow_print([
            f"  Your blade shines {rcolor}{colour}{RESET}.",
            "  This is who you are.",
            "  Carry it well.",
            "",
        ])
        pause()

    def _try_awaken_mark(self) -> None:
        p = self.player
        if p.path != "Human" or p.mark_awakened or p.rank not in ("Kinoe", "Hashira"):
            return
        if not p.breathing:
            return

        clear()
        header("SOMETHING STIRS WITHIN YOU", self._hdr_path())
        slow_print([
            "  You've been pushing your body beyond its limits.",
            "  Your heart rate is climbing. Your skin is burning.",
            "  Something is rising — beneath the surface.",
            "",
            "  The Demon Slayer Mark.",
            "",
        ])
        pause("[ ENTER to awaken the mark ]")

        p.mark_awakened = True
        style_key  = p.breathing or "Water"
        mark_desc  = MARK_DESCRIPTIONS.get(style_key, "A mark blazes across your skin.")

        clear()
        divider("═")
        print(f"\n  {YELLOW}{BOLD}✦ DEMON SLAYER MARK AWAKENED ✦{RESET}\n")
        divider("═")
        print()
        slow_print([
            f"  {mark_desc}",
            "",
            "  Activate [M] in battle once per fight.",
            "  While active: ATK ×2, Forms ×2 — costs 10 HP.",
            "",
        ])
        pause()

    def _create_custom_style(self) -> None:
        p = self.player
        if p.custom_style:
            self._manage_custom_style()
            return

        clear()
        header("FORGE YOUR BREATHING STYLE", self._hdr_path())
        slow_print([
            "  You have reached the pinnacle.",
            "  No master can teach you what comes next.",
            "  This breath — it belongs only to you.",
            "",
        ])
        pause("[ ENTER to begin forging ]")

        clear()
        header("FORGE YOUR BREATHING STYLE", self._hdr_path())
        print(f"  {DIM}What is the name of your Breathing Style?{RESET}")
        print(f"  {DIM}(e.g. 'Glacier', 'Ash', 'Storm'){RESET}\n")
        while True:
            style_name = input("  Breathing Style name: ").strip()
            if style_name:
                break
            print(f"  {YELLOW}Please enter a name.{RESET}")
        print(f"\n  {CYAN}{BOLD}{style_name} Breathing{RESET} — forging your forms...\n")
        pause("[ ENTER to name your forms ]")

        form_powers = [6, 8, 9, 11, 13]
        form_descs  = [
            "A form born from your own instinct — the first step.",
            "A fluid continuation — your body moves on its own.",
            "All energy focused into a single devastating point.",
            "A form that breaks limits — power beyond training.",
            "The pinnacle of your personal style.",
        ]
        custom_forms = []
        for i, (fpower, fdesc) in enumerate(zip(form_powers, form_descs), 1):
            clear()
            header("FORGE YOUR BREATHING STYLE", self._hdr_path())
            print(f"  {CYAN}{BOLD}{style_name} Breathing{RESET}\n")
            print(f"  {BOLD}Form {i} of 5{RESET}  {DIM}(dmg {fpower}){RESET}")
            print(f"  {DIM}{fdesc}{RESET}\n")
            print(f"  {DIM}Give this form a name.{RESET}")
            print(f"  {DIM}(e.g. '1st Form: Rising Tide' or just 'Crashing Wave'){RESET}\n")
            while True:
                fname = input(f"  Form {i} name: ").strip()
                if fname:
                    break
                print(f"  {YELLOW}Please enter a name.{RESET}")
            custom_forms.append((fname, fpower, fdesc))
            print(f"\n  {GREEN}✔  {fname}{RESET}  —  dmg {fpower}")
            time.sleep(0.3)

        clear()
        header("FORGE YOUR BREATHING STYLE", self._hdr_path())
        print(f"  {CYAN}{BOLD}{style_name} Breathing{RESET}\n")
        print(f"  {BOLD}Ultimate Technique{RESET}  {DIM}(dmg 22){RESET}")
        print(f"  {DIM}You still the world. One breath. One strike. Everything ends.{RESET}\n")
        print(f"  {DIM}Name your ultimate technique.{RESET}")
        print(f"  {DIM}(e.g. 'Final Form: Eternal Silence'){RESET}\n")
        while True:
            ult_name = input("  Ultimate name: ").strip()
            if ult_name:
                break
            print(f"  {YELLOW}Please enter a name.{RESET}")
        custom_ult = (ult_name, 22, "You still the world. One breath. One strike. Everything ends.")
        print(f"\n  {YELLOW}{BOLD}✦  {ult_name}{RESET}  —  dmg 22")
        time.sleep(0.3)

        clear()
        header("FORGE YOUR BREATHING STYLE", self._hdr_path())
        print(f"  {CYAN}{BOLD}{style_name} Breathing{RESET}\n")
        for i, (fname, fpower, fdesc) in enumerate(custom_forms, 1):
            print(f"  {BOLD}{i}.{RESET} {fname}  {DIM}(dmg {fpower}){RESET}")
        print()
        print(f"  {YELLOW}{BOLD}ULTIMATE: {ult_name}{RESET}  {DIM}(dmg 22){RESET}")
        print()
        print("  [1] Accept — forge this style")
        print("  [0] Cancel — start over")
        choice = get_valid_input(0, 1)
        if choice == 1:
            p.custom_style = style_name
            p.custom_forms = custom_forms
            p.custom_ult   = custom_ult
            p.using_custom = True
            print(f"\n  {GREEN}{BOLD}Your style has been forged. It is yours alone.{RESET}")
        else:
            print(f"\n  {DIM}The breath returns, unspoken.{RESET}")
        pause()

    def _manage_custom_style(self) -> None:
        p = self.player
        clear()
        header("YOUR CUSTOM STYLE", self._hdr_path())
        print(f"  {CYAN}{p.custom_style}{RESET}\n")
        print("  [1] Use Custom Style in combat")
        print("  [2] Use Original Style in combat")
        print("  [3] Add One-Breath Ultimate to Original Style")
        print("  [0] Back")

        choice = get_valid_input(0, 3)
        if choice == 1:
            p.using_custom = True
            print(f"\n  {GREEN}Switched to Custom: {p.custom_style}{RESET}")
        elif choice == 2:
            p.using_custom = False
            print(f"\n  {GREEN}Switched to Original: {p.breathing}{RESET}")
        elif choice == 3:
            self._add_original_ultimate()
        pause()

    def _add_original_ultimate(self) -> None:
        p = self.player
        if p.original_ult:
            print(f"\n  {YELLOW}Already have: {p.original_ult[0]}{RESET}")
            return
        clear()
        header(f"ONE-BREATH ULTIMATE — {(p.breathing or '').upper()}", self._hdr_path())
        slow_print([
            "  Every style has a breath beyond its last form.",
            "  Not taught. Discovered.",
            "",
        ])
        ult_name = input("  Name your One-Breath Ultimate: ").strip()
        if not ult_name:
            ult_name = f"{p.breathing} Breathing — Final Breath"
        desc = f"The ultimate expression of {p.breathing} Breathing — everything in one strike."
        p.original_ult = (ult_name, 18, desc)
        print(f"\n  {YELLOW}{BOLD}✦ {ult_name} — unlocked!{RESET}")
        pause()

    def _final_selection(self) -> None:
        p = self.player
        clear()
        header("FINAL SELECTION — MT. FUJIKASANE", self._hdr_path())
        slow_print([
            "  Mount Fujikasane. Surrounded by wisteria — demons cannot escape.",
            "  You must survive seven days on this mountain. Alone.",
            "  Every demon that failed to be slain ends up here.",
            "  Including one that has lived for two hundred years.",
            "",
            "  Those who survive become official members of the Corps.",
            "  Those who don't… are never found.",
            "",
        ])
        pause("[ ENTER to begin the Final Selection ]")

        enemies = FINAL_SELECTION_ENEMIES[:]
        random.shuffle(enemies)

        for i, e in enumerate(enemies, 1):
            clear()
            print(f"\n  {DIM}Night {i} of the Final Selection…{RESET}\n")
            time.sleep(0.5)
            won = self.start_battle(
                e["name"], e["hp"], e["atk"],
                is_story    = True,
                gold_reward = 0,
                kill_reward = 0,
                exp_reward  = 0,
            )
            if not won:
                p.full_heal()
                clear()
                header("DEFEATED", self._hdr_path())
                print(f"  {RED}You collapsed on the mountain.{RESET}")
                print(f"  {DIM}But the dawn found you. You survived — barely.{RESET}")
                print(f"  {GREEN}HP restored to full.{RESET}")
                pause()
                break

        p.full_heal()

        clear()
        print(f"\n  {DIM}Seven days have passed.{RESET}")
        time.sleep(0.6)
        print(f"  {YELLOW}You stand at the gate. Dawn light. Wisteria petals falling.{RESET}")
        time.sleep(0.6)
        print(f"\n  Two children wait for you — the Ubuyashiki twins.")
        time.sleep(0.4)
        print(f'  "Congratulations," one says softly.')
        time.sleep(0.4)
        print(f'  "You are now a member of the Demon Slayer Corps."')
        print()
        pause()

        p.joined_corps = True
        p.rank         = "Mizunoto"
        print(f"\n  {GREEN}{BOLD}You have joined the Demon Slayer Corps!{RESET}")
        print(f"  {DIM}Rank: Mizunoto — the lowest rung. The only way is up.{RESET}\n")
        pause()

        print(f"  {YELLOW}The swordsmith is waiting.{RESET}")
        pause("[ ENTER to choose your blade ]")
        self._choose_sword()

    SAVE_FILE = "wisteria_save.json"

    def _save_game(self) -> None:
        p = self.player
        data = {
            "name":          p.name,
            "clan":          p.clan,
            "path":          p.path,
            "level":         p.level,
            "exp":           p.exp,
            "kills":         p.kills,
            "gold":          p.gold,
            "rank":          p.rank,
            "hp":            p.hp,
            "max_hp":        p._max_hp,
            "str":           p.str_stat,
            "spd":           p.spd,
            "end":           p.end,
            "atk_base":      p._attack_power,
            "training":      p.training,
            "breathing":     p.breathing,
            "blood_art":     p.blood_art,
            "sword_colour":  p.sword_colour,
            "mark_awakened": p.mark_awakened,
            "joined_corps":  p.joined_corps,
            "stayed_human":  p.stayed_human,
            "story_done":    list(p.story_done),
            "inventory":     [i.name for i in p.inventory],
            "using_custom":  p.using_custom,
            "custom_style":  p.custom_style,
            "fishing_lvl":   getattr(p, "fishing_lvl", 1),
            "fish_caught":   getattr(p, "fish_caught", 0),
        }
        import json
        try:
            with open(self.SAVE_FILE, "w") as f:
                json.dump(data, f, indent=2)
            print(f"\n  {GREEN}✦ Game saved to {self.SAVE_FILE}{RESET}")
        except Exception as e:
            print(f"\n  {RED}Save failed: {e}{RESET}")
        pause()

    def _load_game(self) -> bool:
        import json
        try:
            with open(self.SAVE_FILE) as f:
                d = json.load(f)
        except FileNotFoundError:
            print(f"\n  {YELLOW}No save file found ({self.SAVE_FILE}).{RESET}")
            pause()
            return False
        except Exception as e:
            print(f"\n  {RED}Load failed: {e}{RESET}")
            pause()
            return False

        p = Player(d["name"], d["clan"], d["path"])
        p._level         = d.get("level", 1)
        p._exp           = d.get("exp", 0)
        p._kills         = d.get("kills", 0)
        p._gold          = d.get("gold", 50)
        p._rank          = d.get("rank", p._rank)
        p._hp            = d.get("hp", p._max_hp)
        p._max_hp        = d.get("max_hp", p._max_hp)
        p._str           = d.get("str", p.str_stat)
        p._spd           = d.get("spd", p.spd)
        p._end           = d.get("end", p.end)
        p._attack_power  = d.get("atk_base", p._attack_power)
        p._training      = d.get("training", 0)
        p._breathing     = d.get("breathing")
        p._blood_art     = d.get("blood_art")
        p.sword_colour   = d.get("sword_colour")
        p.mark_awakened  = d.get("mark_awakened", False)
        p.joined_corps   = d.get("joined_corps", False)
        p.stayed_human   = d.get("stayed_human", False)
        p.story_done     = set(d.get("story_done", []))
        p.using_custom   = d.get("using_custom", False)
        p.custom_style   = d.get("custom_style")
        p.fishing_lvl    = d.get("fishing_lvl", 1)
        p.fish_caught    = d.get("fish_caught", 0)
        for item_name in d.get("inventory", []):
            p.add_item(item_name)

        self.player = p
        clear()
        print(f"\n  {GREEN}✦ Save loaded — welcome back, {p.name}.{RESET}\n")
        p.show_stats()
        pause()
        return True

    FISH_TABLE = [
        ("Small Carp",       2,   5,  "Common",    40),
        ("River Trout",      5,  10,  "Common",    30),
        ("Golden Sweetfish", 12, 20,  "Uncommon",  15),
        ("Iron Eel",        20,  35,  "Rare",       8),
        ("Ghost Fish",      40,  60,  "Epic",       5),
        ("Crimson Koi",     80, 120,  "Legendary",  2),
    ]

    def _civilian_loop(self) -> None:
        p = self.player
        if not hasattr(p, "fishing_lvl"):
            p.fishing_lvl = 1
        if not hasattr(p, "fish_caught"):
            p.fish_caught = 0

        while True:
            clear()
            header("RIVERSIDE LIFE", self._hdr_path())
            print(f"  {BOLD}{p.name}{RESET}  |  Clan: {p.clan}  |  {CYAN}Civilian{RESET}")
            print(f"  Gold : {YELLOW}{p.gold}G{RESET}  |  "
                  f"Fishing Lv: {CYAN}{p.fishing_lvl}{RESET}  |  "
                  f"Fish caught: {p.fish_caught}")
            print(f"  {DIM}The river is quiet. The demons feel far away.{RESET}\n")
            print("  [1] Fish        — cast your line")
            print("  [2] Rest        — restore HP and reflect")
            print("  [3] Visit Town  — spend gold at the market")
            print("  [4] Check Bag   — use items")
            print("  [5] Save Game")
            print("  [0] Quit\n")

            choice = get_valid_input(0, 5)

            if choice == 1:
                self._fish()
            elif choice == 2:
                self._civilian_rest()
            elif choice == 3:
                self._visit_shop()
            elif choice == 4:
                self._use_item_screen()
            elif choice == 5:
                self._save_game()
            elif choice == 0:
                clear()
                break

    def _fish(self) -> None:
        p = self.player
        clear()
        header("FISHING", self._hdr_path())
        slow_print([
            "  You cast your line into the river.",
            "  The water catches the morning light.",
            "  You wait.",
            "",
        ])
        time.sleep(0.4)

        print(f"  {DIM}Watch for the tug… press ENTER when you see ✦ !{RESET}\n")
        time.sleep(random.uniform(1.2, 3.0))

        import threading
        tugged = [False]
        caught = [False]

        print(f"  {YELLOW}{BOLD}✦ TUG! — Press ENTER!{RESET}")
        tug_time = time.time()

        inp = input("  > ")
        react_time = time.time() - tug_time

        window = 1.2 + (p.fishing_lvl * 0.15)

        if react_time <= window:
            pool = []
            for entry in self.FISH_TABLE:
                weight = entry[4]
                if entry[3] in ("Rare", "Epic", "Legendary"):
                    weight += p.fishing_lvl * 2
                pool.extend([entry] * weight)

            fish = random.choice(pool)
            name, min_g, max_g, rarity, _ = fish
            gold_earned = random.randint(min_g, max_g)

            rarity_color = {
                "Common": WHITE, "Uncommon": GREEN,
                "Rare": CYAN, "Epic": MAGENTA, "Legendary": YELLOW,
            }.get(rarity, WHITE)

            p.add_gold(gold_earned)
            p.fish_caught += 1

            print(f"\n  {rarity_color}{BOLD}You caught: {name}!{RESET}  [{rarity}]")
            print(f"  {GREEN}+{gold_earned}G{RESET}  |  Total fish: {p.fish_caught}")

            if p.fish_caught % 5 == 0 and p.fishing_lvl < 10:
                p.fishing_lvl += 1
                print(f"\n  {YELLOW}✦ Fishing Level Up! Now Lv.{p.fishing_lvl}{RESET}")
                print(f"  {DIM}Your patience and skill have grown.{RESET}")
        else:
            print(f"\n  {DIM}The fish slipped away… ({react_time:.2f}s — too slow){RESET}")
            print(f"  {DIM}Try to press ENTER faster next time.{RESET}")

        print()
        pause()

    def _civilian_rest(self) -> None:
        p = self.player
        clear()
        header("RIVERSIDE REST", self._hdr_path())
        slow_print([
            "  You sit by the bank and watch the water go by.",
            "  Somewhere downstream, a bird calls.",
            "  You think about the people you've known.",
            "  You think about the ones who chose to fight.",
            "  You are glad for the peace — and glad someone guards it.",
            "",
        ])
        p.full_heal()
        print(f"  {GREEN}HP fully restored.{RESET}")
        pause()

    def _human_path_choice(self) -> None:
        clear()
        header("YOUR PATH")
        slow_print([
            "  You were born human in a world full of demons.",
            "  The night is dangerous. People disappear.",
            "  And you have a choice.",
            "",
        ])
        print(f"  {BOLD}What will you do?{RESET}\n")
        print("  [1] Join the Demon Slayer Corps")
        print(f"       {DIM}Undergo the Final Selection. Fight for humanity.{RESET}")
        print()
        print("  [2] Remain a Civilian")
        print(f"       {DIM}Stay human. Live quietly. Fate has a way of finding people.{RESET}")
        print()

        choice = get_valid_input(1, 2)
        if choice == 1:
            print(f"\n  {CYAN}You will walk the path of the sword.{RESET}")
            pause()
            self._final_selection()
        else:
            clear()
            header("THE CIVILIAN PATH")
            slow_print([
                "  You choose the quiet life.",
                "  A village by the river. A fire in the hearth.",
                "  No sword. No Corps. No demons — if you're lucky.",
                "  Just the water, the seasons, and a fishing line.",
                "",
            ])
            self.player.stayed_human = True
            self.player.rank         = "Civilian"
            self.player.fishing_lvl  = getattr(self.player, 'fishing_lvl', 1)
            self.player.fish_caught  = getattr(self.player, 'fish_caught', 0)
            print(f"  {YELLOW}You remain a civilian.{RESET}")
            pause()
            self._civilian_loop()

    def _create_character(self) -> Player:
        clear()
        header("CHARACTER CREATION")
        while True:
            name = input("  Enter your name: ").strip()
            if name:
                break
            print("  Name cannot be empty. Please enter a name.")
        print()
        print("  Choose your path:")
        print("  [1] Human  — join the Demon Slayer Corps or forge your own way")
        print("  [2] Demon  — serve Muzan, or seek something else")
        print()
        path_choice = get_valid_input(1, 2)
        path        = "Human" if path_choice == 1 else "Demon"
        print(f"\n  Path chosen: {CYAN if path == 'Human' else RED}{path}{RESET}")
        pause("  [ ENTER to reveal your clan ]")

        clan = self._clan_roll_scene()
        p    = Player(name, clan, path)
        print(f"\n  {GREEN}Character created!{RESET}")
        p.show_stats()
        pause()
        return p

    def _clan_roll_scene(self) -> str:
        clear()
        header("CLAN AWAKENING")
        input("  Press ENTER to reveal your clan… ")
        names = list(CLAN_POOL.keys())
        for _ in range(18):
            print(f"\r  Rolling…  {random.choice(names):12}", end="", flush=True)
            time.sleep(0.08)
        chosen = self._roll_clan()
        info   = CLAN_POOL[chosen]
        rcolor = RARITY_COLORS[info["rarity"]]
        print(f"\r  ✦  Clan: {rcolor}{BOLD}{chosen:12}{RESET}  ({info['rarity']})   ")
        print(f"  Bonus  : STR +{info['stats'][0]}  SPD +{info['stats'][1]}  END +{info['stats'][2]}")
        print()
        pause()
        return chosen

    def _roll_clan(self) -> str:
        pool = []
        for name, data in CLAN_POOL.items():
            pool.extend([name] * RARITY_WEIGHTS[data["rarity"]])
        return random.choice(pool)

    def _path_intro(self) -> None:
        p = self.player
        if p.path == "Human":
            clear()
            header("YOUR STORY BEGINS")
            slow_print([
                f"  Your name is {p.name}.",
                f"  Of the {p.clan} clan.",
                "  The world you were born into has demons in it.",
                "  And now you must decide what to do about that.",
                "",
            ])
            pause()
            self._human_path_choice()
        else:
            clear()
            header("YOUR STORY BEGINS")
            slow_print([
                f"  Your name was {p.name}.",
                "  You don't fully remember how it happened.",
                "  The blood. The hunger. The night that never ended.",
                "  You are a demon now.",
                "  And Muzan's shadow falls over everything.",
                "",
            ])
            pause()

    def _credits_splash(self) -> None:
        import shutil as _sh, sys as _sys
        clear()
        time.sleep(0.2)

        term_w = _sh.get_terminal_size((80, 24)).columns

        def _rgb(r, g, b): return f"\033[38;2;{r};{g};{b}m"

        _PINK_KEYS = [(255,255,255),(255,200,220),(255,140,180),(255,90,140),(255,255,255)]

        def _lerp(keys, t):
            t = t % 1.0
            n = len(keys) - 1
            lo = int(t * n); hi = min(lo + 1, n); f = (t * n) - lo
            r = int(keys[lo][0] + (keys[hi][0] - keys[lo][0]) * f)
            g = int(keys[lo][1] + (keys[hi][1] - keys[lo][1]) * f)
            b = int(keys[lo][2] + (keys[hi][2] - keys[lo][2]) * f)
            return _rgb(r, g, b)

        _ART = [
                r"                                                                                                                                                                                ",
                r"                                                                                                                                                                                ",
                r"           .---.                     ,--,                                                           .---.                       ___                                             ",
                r"          /. ./|                   ,--.'|         ,---,                    .--.,                   /. ./|  ,--,               ,--.'|_                       ,--,                ",
                r"      .--'.  ' ;   ,---.    __  ,-.|  | :       ,---.'|           ,---.  ,--.'  \              .--'.  ' ;,--.'|               |  | :,'             __  ,-.,--.'|                ",
                r"     /__./ \ : |  '   ,'\ ,' ,'/ /|:  : '       |   | :          '   ,'\ |  | /\/             /__./ \ : ||  |,      .--.--.   :  : ' :           ,' ,'/ /||  |,                 ",
                r" .--'.  '   \' . /   /   |'  | |' ||  ' |       |   | |         /   /   |:  : :           .--'.  '   \' .`--'_     /  /    '.;__,'  /     ,---.  '  | |' |`--'_      ,--.--.    ",
                r"/___/ \ |    ' '.   ; ,. :|  |   ,''  | |     ,--.__| |        .   ; ,. ::  | |-,        /___/ \ |    ' ',' ,'|   |  :  /`./|  |   |     /     \ |  |   ,',' ,'|    /       \   ",
                r";   \  \;      :'   | |: :'  :  /  |  | :    /   ,'   |        '   | |: :|  : :/|        ;   \  \;      :'  | |   |  :  ;_  :__,'| :    /    /  |'  :  /  '  | |   .--.  .-. |  ",
                r" \   ;  `      |'   | .; :|  | '   '  : |__ .   '  /  |        '   | .; :|  |  .'         \   ;  `      ||  | :    \  \    `. '  : |__ .    ' / ||  | '   |  | :    \__\/: . .  ",
                r"  .   \    .\  ;|   :    |;  : |   |  | '.'|'   ; |:  |        |   :    |'  : '            .   \    .\  ;'  : |__   `----.   \|  | '.'|'   ;   /|;  : |   '  : |__  ," r"  .--.; |  ",
                r"   \   \   ' \ | \   \  / |  , ;   ;  :    ;|   | '/  '         \   \  / |  | |             \   \   ' \ ||  | '.'| /  /`--'  /;  :    ;'   |  / ||  , ;   |  | '.'|/  /  ,.  |  ",
                r"    :   '  |--" r"   `----'   ---'    |  ,   / |   :    :|          `----'  |  : \              :   '  |--" r" ;  :    ;'--'.     / |  ,   / |   :    | ---'    ;  :    ;  :   .'   \ ",
                r"     \   \ ;                        ---`-'   \   \  /                    |  |,'               \   \ ;    |  ,   /   `--'---'   ---`-'   \   \  /          |  ,   /|  ,     .-./ ",
                r"      '---" r"                                   `----'                     `--'                  '---" r"      ---`-'                         `----'            ---`-'  `--`---'     ",

        ]

        art_w  = max(len(r) for r in _ART)
        pad_a  = max(0, (term_w - art_w) // 2)
        NROWS  = len(_ART)
        FRAMES = 22

        print()
        first = True
        for i in range(FRAMES):
            t   = (i / FRAMES) * 0.75
            col = _lerp(_PINK_KEYS, t)
            if not first:
                _sys.stdout.write(f"\033[{NROWS}A")
            for row in _ART:
                _sys.stdout.write(f"\033[2K{col}\033[1m{' '*pad_a}{row}\033[0m\n")
            _sys.stdout.flush()
            first = False
            time.sleep(0.03)

        print()

        course = "DCSN03C  ·  Computer Programming 2  ·  Finals Project"
        divln  = "═" * min(len(course) + 4, term_w - 4)
        pad_c  = max(0, (term_w - len(course)) // 2)
        pad_d  = max(0, (term_w - len(divln))  // 2)
        print(f"{' '*pad_d}{DIM}{divln}{RESET}")
        print(f"{' '*pad_c}{DIM}{course}{RESET}")
        print(f"{' '*pad_d}{DIM}{divln}{RESET}")
        print()
        time.sleep(0.3)

        label   = "✦  Made by  ✦"
        pad_l   = max(0, (term_w - len(label)) // 2)
        col_lbl = _lerp(_PINK_KEYS, 0.4)
        print(f"{' '*pad_l}{col_lbl}{BOLD}{label}{RESET}")
        print()
        time.sleep(0.2)

        names = [
            ("Min Sun O. Yoo",           "Lead Developer"),
            ("Andrew Carmelo C. Nona",   "Developer"),
            ("Jan Marisse I. Tolentino", "Developer"),
            ("Huhgrant Arffrey D. Frayre","Developer"),
        ]

        NAME_KEYS = [(255,255,255),(255,200,220),(255,140,180),(255,90,140)]
        ROLE_KEYS = [(160,160,160),(180,160,180),(160,140,160),(140,120,140)]

        for name, role in names:
            line    = f"{name}  {DIM}— {role}{RESET}"
            visible = f"{name}  — {role}"
            pad_n   = max(0, (term_w - len(visible)) // 2)
            NF = 12
            first_n = True
            for i in range(NF):
                t   = i / (NF - 1)
                nc  = _lerp(NAME_KEYS, t)
                rc  = _lerp(ROLE_KEYS, t)
                out = f"{nc}{BOLD}{name}{RESET}  {DIM}{rc}— {role}{RESET}"
                if not first_n:
                    _sys.stdout.write("\033[1A")
                _sys.stdout.write(f"\033[2K{' '*pad_n}{out}\n")
                _sys.stdout.flush()
                first_n = False
                time.sleep(0.025)
            time.sleep(0.15)

        print()
        time.sleep(0.4)
        pause("  [ ENTER to begin ]")

    def _cinematic_intro(self) -> None:
        import shutil as _sh
        clear()
        time.sleep(0.3)

        ascii_header("THE WORLD OF WISTERIA", self._hdr_path())
        time.sleep(0.4)
        divider("═")
        print()
        slow_print([
            "  There are demons in this world.",
            "  They walk the night. They feast on the living.",
            "  For over a thousand years — no one could stop them.",
            "",
            "  Until the Demon Slayer Corps.",
            "  Until breathing techniques forged from the soul.",
            "  Until men and women who refused to surrender to the dark.",
            "",
            "  But demons are not born — they are made.",
            "  Each one was human once.",
            "  Each one made a choice. Or had one taken from them.",
            "",
            "  Now it is your turn.",
            "",
        ])
        time.sleep(0.3)
        print(DIM + "  ~ The World of Wisteria ~" + RESET)
        print()
        pause("  [ ENTER to begin your story ]")
