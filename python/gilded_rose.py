# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.increase_items = {"Aged Brie": 1, "Backstage passes to a TAFKAL80ETC concert": 1}
        self.decrease_items = {"Sulfuras, Hand of Ragnaros": 0}
    
    def increase_quality(self, item):
        if item.sell_in < 0:
            item.quality += 2
        else:
            item.quality += 1

        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                item.quality += 1
            if item.sell_in < 6:
                item.quality += 1
            if item.sell_in < 0:
                item.quality = 0

        if item.quality > 50:
            item.quality = 50
    
    def decrease_quality(self, item):
        if item.sell_in < 0:
            item.quality -= 4
        else:
            item.quality -= 2
        if item.name == "Conjured Mana Cake":
            item.quality -= 2

        if item.quality < 0:
            item.quality = 0

    def change_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

    def change_quality(self, item):
        if item.name in self.increase_items:
            self.increase_quality(item)
        elif item.name in self.decrease_items:
            self.decrease_quality(item)
        else:
            self.decrease_quality(item)
            self.increase_quality(item)
    
    def update_quality(self):
        for item in self.items:
            self.change_sell_in(item)
            self.change_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
