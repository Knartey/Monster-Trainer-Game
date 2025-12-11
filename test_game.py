# test_game.py

"""
Pytest test suite for Monster Trainer Game.

Covers Move, Item, Monster, and Player classes with both happy-path
and edge case scenarios.
"""

import random
import copy
import pytest

from move import Move
from item import Item
from monster import Monster
from player import Player


def test_move_creation_and_pp_methods():
    """Test Move initialization, PP usage, restoration, and reset."""
    mv = Move("TestStrike", power=10, max_pp=5, type_="Normal")
    assert mv.name == "TestStrike"
    assert mv.power == 10
    assert mv.max_pp == 5
    assert mv.current_pp == 5

    used = mv.use_move()
    assert used == 10
    assert mv.current_pp == 4

    # restore_pp should not exceed max_pp
    restored = mv.restore_pp(2)
    expected_restore = min(2, mv.max_pp - 4)
    assert restored == expected_restore
    assert mv.current_pp == 4 + expected_restore

    mv.reset_pp()
    assert mv.current_pp == mv.max_pp
    assert mv.is_usable()


def test_move_multiplier_and_damage_range():
    """Test type effectiveness multiplier and damage range calculation."""
    mv = Move("Flame", power=12, max_pp=3, type_="Fire")
    multiplier = mv.get_multiplier("Grass")
    assert multiplier == 2.0
    rng = mv.get_damage_range(0.2)
    assert rng[0] <= mv.power <= rng[1]


def test_item_use_and_apply_effects_on_monster():
    """Test healing item application on a monster."""
    mv = Move("Tackle", power=8, max_pp=10, type_="Normal")
    m = Monster("Buddy", "Normal", 40, [mv], level=1)
    m.take_damage(10)
    potion = Item("Health Potion", heal=20, quantity=1)
    assert potion.is_healing_item()
    healed, restored = potion.apply_effect(m)
    assert healed > 0
    assert restored == 0
    # using again should do nothing (quantity 0)
    healed2, restored2 = potion.apply_effect(m)
    assert healed2 == 0 and restored2 == 0


def test_capture_item_flag_and_use():
    """Test capture item usage and quantity reduction."""
    ball = Item("Monster Ball", quantity=1, is_capture=True)
    assert ball.is_capture_item()
    heal, pp = ball.use()
    assert heal == 0 and pp == 0
    assert ball.quantity == 0


def test_monster_attack_and_type_effectiveness():
    """Test attack damage calculation with type effectiveness."""
    mv = Move("Bubble Beam", power=7, max_pp=5, type_="Water")
    attacker = Monster("Aqua", "Water", 50, [mv], level=2)
    defender = Monster("Flare", "Fire", 40, [Move("Scratch", 5, 10)], level=1)
    random.seed(0)
    outcome = attacker.attack(defender, mv, crit_chance=0.0)
    assert outcome["multiplier"] == 2.0
    assert outcome["damage"] == int(7 * 2.0)
    assert not outcome["critical"]
    assert defender.current_hp == 40 - outcome["damage"]


def test_attack_with_no_pp_fails():
    """Test that attack fails when move has no PP left."""
    mv = Move("Weak", power=5, max_pp=1, type_="Normal")
    m1 = Monster("One", "Normal", 30, [mv], level=1)
    m2 = Monster("Two", "Normal", 30, [Move("T", 4, 10)], level=1)
    assert mv.use_move() == 5
    res = m1.attack(m2, mv, crit_chance=0.0)
    assert res["used_pp"] == 0 and res["damage"] == 0


def test_player_inventory_and_use_item_on_monster():
    """Test Player inventory management and item usage."""
    p = Player("Tester")
    m = Monster("Ally", "Normal", 40, [Move("T", 5, 10)], level=1)
    p.add_monster(m)
    idx = p.find_item_by_name("Health Potion")
    assert idx != -1
    success, msg = p.use_item_on_monster(idx, 0)
    assert success
    idx_ball = p.find_item_by_name("Monster Ball")
    assert idx_ball != -1
    ok, message = p.use_item_on_monster(idx_ball, 0)
    assert ok is False


def test_add_monster_deepcopy_prevents_shared_state():
    """Test that deepcopy prevents shared state between monsters."""
    base = Monster("Proto", "Normal", 30, [Move("T", 5, 10)], level=1)
    p = Player("Deep")
    p.add_monster_deepcopy(base)
    base.take_damage(10)
    assert p.team[0].current_hp == p.team[0].max_hp


def test_reset_stats_resets_hp_and_pp():
    """Test that reset_stats restores HP and PP."""
    mv = Move("X", 6, 3)
    m = Monster("R", "Normal", 50, [mv], level=1)
    mv.use_move()
    m.take_damage(20)
    m.reset_stats()
    assert m.current_hp == m.max_hp
    assert mv.current_pp == mv.max_pp


def test_level_up_changes_max_hp_but_keeps_current_within_bounds():
    """Test that level_up increases max HP and keeps current HP valid."""
    mv = Move("Y", 6, 5)
    m = Monster("Lv", "Normal", 50, [mv], level=1)
    before_max = m.max_hp
    m.level_up(1)
    assert m.level == 2
    assert m.max_hp >= before_max
    assert m.current_hp <= m.max_hp


def test_remove_move_by_name_and_add_move():
    """Test adding and removing moves by name."""
    mv1 = Move("One", 4, 10)
    mv2 = Move("Two", 5, 10)
    m = Monster("Mod", "Normal", 30, [mv1], level=1)
    m.add_move(mv2)
    assert any(x.name == "Two" for x in m.get_moves())
    removed = m.remove_move_by_name("One")
    assert removed
    assert all(x.name != "One" for x in m.get_moves())


def test_capture_probability_low_hp():
    """Test effective HP ratio for low HP monsters with capture items."""
    ball = Item("Monster Ball", quantity=1, is_capture=True)
    mv = Move("M", 5, 5)
    wild = Monster("Wild", "Normal", 100, [mv], level=1)
    wild.take_damage(95)
    ratio = wild.effective_hp_ratio()
    assert 0.0 <= ratio < 0.1
    assert ball.is_capture_item()


# --- Additional edge case tests ---

def test_use_item_on_full_hp_monster():
    """Healing item should have no effect on full HP monster."""
    m = Monster("Tank", "Normal", 50, [Move("Punch", 5, 10)], level=1)
    potion = Item("Health Potion", heal=20, quantity=1)
    healed, restored = potion.apply_effect(m)
    assert healed == 0 and restored == 0


def test_restore_pp_when_already_full():
    """PP restoration item should have no effect if PP is full."""
    mv = Move("Kick", 10, 5)
    m = Monster("Fighter", "Normal", 40, [mv], level=1)
    pp_item = Item("PP Potion", restore_pp=5, quantity=1)
    healed, restored = pp_item.apply_effect(m)
    assert healed == 0
    assert restored == 0


def test_choose_move_random_returns_struggle_when_no_pp():
    """Monster should use Struggle when all moves have 0 PP."""
    mv = Move("Empty", 5, 1)
    m = Monster("Exhausted", "Normal", 30, [mv], level=1)
    mv.use_move()  # consume PP
    chosen = m.choose_move_random()
    assert chosen.name == "Struggle"


def test_effective_hp_ratio_with_zero_max_hp():
    """Effective HP ratio should return 0.0 if max_hp is zero."""
    m = Monster("Bugged", "Normal", 0, [Move("None", 0, 1)], level=1)
    assert m.effective_hp_ratio() == 0.0


def test_remove_invalid_monster_and_item_index():
    """Removing with invalid indices should return False."""
    p = Player("InvalidTester")
    assert not p.remove_monster_by_index(5)
    assert not p.remove_item_by_index(5)


def test_has_usable_monsters_false_when_all_fainted():
    """has_usable_monsters should return False if all monsters fainted."""
    m = Monster("Weakling", "Normal", 10, [Move("Hit", 5, 1)], level=1)
    m.take_damage(10)  # reduce HP to 0
    p = Player("NoHope")
    p.add_monster(m)
    assert not p.has_usable_monsters()


def test_team_and_inventory_size_helpers():
    """Test helper methods for team and inventory size."""
    p = Player("HelperTester")
    assert p.get_team_size() == 0
    assert p.get_inventory_size() >= 1  # starter inventory exists
    m = Monster("HelperMon", "Normal", 20, [Move("Punch", 5, 5)], level=1)
    p.add_monster(m)
    assert p.get_team_size() == 1