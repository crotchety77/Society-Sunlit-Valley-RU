"""
Audit Script: Death Debt & Medical Fee Calculations
Audits logic from globalServer.js, handleDebt.js, and skullCavernTick.js
"""

import sys
import json
from pathlib import Path

def calculate_fee(balance: int, reason: str, has_first_aid: bool = False, entered_skull_cavern: bool = False):
    max_fee = 0
    minimum_fee = 512
    
    if reason == "death":
        max_fee = 4096
        if has_first_aid:
            max_fee = 2048
        amount_to_deduct = min(round(balance * 0.1), max_fee)
    elif reason == "skull_cavern":
        minimum_fee = 1024
        max_fee = 8192
        amount_to_deduct = min(round(balance * 0.15), max_fee)
    else:
        raise ValueError(f"Unknown reason: {reason}")
    
    if amount_to_deduct < minimum_fee:
        amount_to_deduct = minimum_fee
        
    if balance < max_fee and entered_skull_cavern:
        amount_to_deduct = max_fee
        
    fee_paid = 0
    debt_added = 0
    new_balance = balance
    
    if balance < amount_to_deduct:
        debt_added = amount_to_deduct
    else:
        fee_paid = amount_to_deduct
        new_balance = balance - amount_to_deduct
        
    return {
        "balance_initial": balance,
        "reason": reason,
        "has_first_aid": has_first_aid,
        "entered_skull_cavern": entered_skull_cavern,
        "amount_to_deduct": amount_to_deduct,
        "fee_paid": fee_paid,
        "debt_added": debt_added,
        "balance_remaining": new_balance
    }

def main():
    test_cases = [
        {"balance": 0, "reason": "death", "has_first_aid": False, "entered_skull_cavern": False, "name": "Новичок (0 монет)"},
        {"balance": 1000, "reason": "death", "has_first_aid": False, "entered_skull_cavern": False, "name": "Новичок (1 000 монет)"},
        {"balance": 10000, "reason": "death", "has_first_aid": False, "entered_skull_cavern": False, "name": "Обычный игрок (10 000 монет)"},
        {"balance": 50000, "reason": "death", "has_first_aid": False, "entered_skull_cavern": False, "name": "Богатый игрок (50 000 монет)"},
        {"balance": 50000, "reason": "death", "has_first_aid": True, "entered_skull_cavern": False, "name": "Игрок с книгой первой помощи (50 000 монет)"},
        {"balance": 500, "reason": "death", "has_first_aid": False, "entered_skull_cavern": True, "name": "Ветеран Черепа (500 монет, мало денег)"},
        {"balance": 2000, "reason": "skull_cavern", "has_first_aid": False, "entered_skull_cavern": True, "name": "Обморок в Черепе (2 000 монет)"},
        {"balance": 100000, "reason": "skull_cavern", "has_first_aid": False, "entered_skull_cavern": True, "name": "Обморок в Черепе (100 000 монет)"},
    ]

    print("=" * 80)
    print("AUDIT: DEATH DEBT & MEDICAL FEE FORMULAS")
    print("=" * 80)
    
    for tc in test_cases:
        res = calculate_fee(
            balance=tc["balance"],
            reason=tc["reason"],
            has_first_aid=tc["has_first_aid"],
            entered_skull_cavern=tc["entered_skull_cavern"]
        )
        print(f"\nСценарий: {tc['name']}")
        print(f"  Входной баланс: {res['balance_initial']} | Причина: {res['reason']}")
        print(f"  Рассчитанный штраф: {res['amount_to_deduct']}")
        if res['debt_added'] > 0:
            print(f"  -> ИТОГ: Недостаточно средств! Начислен ДОЛГ: {res['debt_added']} (Баланс: {res['balance_remaining']})")
        else:
            print(f"  -> ИТОГ: ОПЛАЧЕНО: {res['fee_paid']} (Остаток на балансе: {res['balance_remaining']})")
            
    print("\n" + "=" * 80)
    print("Audit completed successfully.")

if __name__ == "__main__":
    main()
