# -*- coding: utf-8 -*-
concert_is_very_soon = 6
concert_approaching = 11
max_quality = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_one_item(item)

    def update_one_item(self, item):
        self.update_quality_of_item(item)
        self.update_sell_in(item)
        self.handle_expiration(item)

    def handle_expiration(self, item):
        if self.has_expired(item):
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = 0
            elif item.quality > 0 and item.name != "Aged Brie" and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality -= 1

    @staticmethod
    def doesnt_have_max_quality(item):
        return item.quality < max_quality

    @staticmethod
    def has_expired(item):
        return item.sell_in < 0

    @staticmethod
    def update_sell_in(item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

    def update_quality_of_item(self, item):
        if item.name == "Aged Brie":
            self.handle_cheese(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.handle_concert(item)
        elif item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
            item.quality -= 1

    def handle_concert(self, item):
        if self.doesnt_have_max_quality(item):
            item.quality += 1
            if item.sell_in < concert_approaching and self.doesnt_have_max_quality(item):
                item.quality += 1
            if item.sell_in < concert_is_very_soon and self.doesnt_have_max_quality(item):
                item.quality += 1

    def handle_cheese(self, item):
        if self.doesnt_have_max_quality(item):
            item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
