#!/usr/bin/env python


NAME = 'NevisProxy (AdNovum)'


def is_waf(self):
    if self.matchcookie('^Navajo.*?$'):
        return True
    return False