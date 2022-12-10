# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)
    
    def test_normal_item(self):
        items = [Item('foo', 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 9
        assert items[0].quality == 9

    def test_normal_item_outOfDate(self):
        items = [Item('foo', -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == -6
        assert items[0].quality == 8

    def test_backstage_passes_10days(self):
        items = [Item(Item.item1, 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 9
        assert items[0].quality == 12

    def test_backstage_passes_5days(self):
        items = [Item(Item.item1, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 4
        assert items[0].quality == 13

    def test_backstage_passes_outOfDate(self):
        items = [Item(Item.item1, -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == -6
        assert items[0].quality == 0

    def test_aged_brie(self):
        items = [Item('Aged Brie', 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == 9
        assert items[0].quality == 11
    
    def test_aged_brie_outOfDate(self):
        items = [Item('Aged Brie', -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].sell_in == -6
        assert items[0].quality == 12

    

if __name__ == '__main__':
    Item.item1 = "Backstage passes to a TAFKAL80ETC concert"
    unittest.main()