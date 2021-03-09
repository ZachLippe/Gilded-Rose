# -*- coding: utf-8 -*-
max_quality = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_one_item(item)

    def update_one_item(self, item):
        self.update_quality_of_item(item)
        self.update_sellin(item)
        self.handle_expiration(item)

    def handle_expiration(self, item):
        if self.has_expired(item):
            if item.name == "Aged Brie" and self.doesnt_have_max_quality():
                item.quality = item.quality + 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality - item.quality  # why not just set to 0?
            else:
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1  # gets an extra tick in quality if expired

    def doesnt_have_max_quality(item):
        return item.quality < max_quality

    @staticmethod
    def has_expired(item):
        return item.sell_in < 0

    @staticmethod
    def update_sellin(item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def update_quality_of_item(self, item):
        if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.handle_cheese_or_concert(item)
        else:  # Decreases
            if item.quality > 0:  # we cannot go below 0
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality -= 1

    def handle_cheese_or_concert(self, item):
        if self.doesnt_have_max_quality():
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:  # gets an extra increase
                    if self.doesnt_have_max_quality():
                        item.quality = item.quality + 1
                if item.sell_in < 6:  # gets another extra increase
                    if self.doesnt_have_max_quality():
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
