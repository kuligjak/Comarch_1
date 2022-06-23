def avg_income(income, bonus=1.05, yearly_bonus=1.10):
    """Our function compute next payment based on some criteria"""
    avg = sum(income) / len(income)
    next_income = avg * bonus
    if len(income) >= 5:
        next_income = next_income* yearly_bonus
    return next_income


income_list = [150, 240.34, 193.2, 234.2, 543.2]

print(f"Next income for Kuba: {avg_income(income_list)}")