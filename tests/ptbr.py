# -*- coding: utf-8 -*-
from tests import HangulizeTestCase


class BrazilianPortugueseTestCase(HangulizeTestCase):
    """ http://korean.go.kr/09_new/dic/rule/rule_foreign_0219.jsp """

    def setUp(self):
        from hangulize.langs.ptbr import BrazilianPortuguese
        self.lang = BrazilianPortuguese()

    def test_3rd(self):
        """제3항
        d, t는 ㄷ, ㅌ으로 적는다. i 앞이나 어말 e 및 어말 -es 앞에서는
        ‘ㅈ, ㅊ'으로 적는다.
        """
        assert u'지아만치나' == self.hangulize(u'Diamantina')
        assert u'알레그레치' == self.hangulize(u'Alegrete')
        assert u'몬치스' == self.hangulize(u'Montes')

    def test_5th(self):
        """제5항: l
        1. 어중의 l이 모음 앞에 오거나 모음이 따르지 않는 비음 앞에 오는
           경우에는 ‘?'로 적는다. 다만, 비음 뒤의 l은 모음 앞에 오더라도 ‘ㄹ'로
           적는다.
        2. 어말 또는 자음 앞의 l은 받침 ‘ㄹ'로 적는다. 다만, 브라질
           포르투갈어에서 자음 앞이나 어말에 오는 경우에는 ‘우'로 적되, 어말에
           -ul 이 오는 경우에는 ‘울'로 적는다.
        """
        assert u'지우베르투' == self.hangulize(u'Gilberto')
        assert u'카라코우' == self.hangulize(u'Caracol')

    def test_14th(self):
        """제14항
        e는 ‘에'로 적되, 어두 무강세 음절과 어말에서는 ‘이'로 적는다.
        """
        assert u'시프리' == self.hangulize(u'Chifre')
        assert u'지' == self.hangulize(u'de')

    def test_15th(self):
        """제15항: -es
        어말 -es는 ‘-이스'로 적는다.
        """
        assert u'도르넬리스' == self.hangulize(u'Dorneles')
        assert u'코헨치스' == self.hangulize(u'Correntes')
