def filter_items(items, item_type=None, rarity=None, usage=None):
    return [
        item for item in items
        if (item_type is None or item["type"] == item_type)
        and (rarity is None or item["rarity"] == rarity)
        and (usage is None or item["usage"] == usage)
    ]

def get_weapons():
    return [
        {"name": "Fist", "type": "melee", "rarity": "common", "usage": "basic"},
        {"name": "Knife", "type": "melee", "rarity": "common", "usage": "stab"},
        {"name": "Club", "type": "melee", "rarity": "uncommon", "usage": "bash"},
        {"name": "Gun", "type": "ranged", "rarity": "rare", "usage": "shoot"},
        {"name": "Bomb", "type": "explosive", "rarity": "rare", "usage": "blast"},
        {"name": "Nuclear Bomb", "type": "explosive", "rarity": "epic", "usage": "annihilate"},
    ]
#Jiung
def sort_items(items, key, reverse=False):
    if key not in ['name', 'type', 'rarity', 'usage']:
        print("Invalid sort key. Sorting skipped.")
        return items
    return sorted(items, key=lambda item: item[key], reverse=reverse)
