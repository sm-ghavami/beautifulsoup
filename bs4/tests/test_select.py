from bs4 import BeautifulSoup,Tag
import unittest

class soupSelect(unittest.TestCase):
    def testContainsOwn(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div:containsOwn(mytext)')[0].__str__(),
                          '<div class="content"><b class="first-class a c" id="first">First</b><a class="link" id="first-link">First Link</a><b class="second-class a d" id="second">Second</b>MyText<b class="third-class b c" id="third">Third</b><b class="fourth-class b f" id="fourth">Fourth</b><b class="fifth-class a e d" id="fifth">Fifth</b></div>')
        self.assertEquals(self.soup.select('body > div:containsOwn(first)'),
                          [])

    def testContains(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div:contains(first)')[0].__str__(),
                          '<div class="content"><b class="first-class a c" id="first">First</b><a class="link" id="first-link">First Link</a><b class="second-class a d" id="second">Second</b>MyText<b class="third-class b c" id="third">Third</b><b class="fourth-class b f" id="fourth">Fourth</b><b class="fifth-class a e d" id="fifth">Fifth</b></div>')
        self.assertEquals(self.soup.select('body > div:contains(mytext)')[0].__str__(),
                          '<div class="content"><b class="first-class a c" id="first">First</b><a class="link" id="first-link">First Link</a><b class="second-class a d" id="second">Second</b>MyText<b class="third-class b c" id="third">Third</b><b class="fourth-class b f" id="fourth">Fourth</b><b class="fifth-class a e d" id="fifth">Fifth</b></div>')
        self.assertEquals(self.soup.select('body > div:contains(NoneObj)'),
                          [])
    def testMulticlassAndId(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > b#first.a.c')[0].__str__(),
                          '<b class="first-class a c" id="first">First</b>')
        self.assertEquals(self.soup.select('body > div > #first.a.c')[0].__str__(),
                          '<b class="first-class a c" id="first">First</b>')
        self.assertEquals(self.soup.select('body > div > .a.c')[0].__str__(),
                          '<b class="first-class a c" id="first">First</b>')
        self.assertEquals(self.soup.select('body > div > b#first.a.d'),
                          [])
        self.assertEquals(self.soup.select('body > div > #first.a.d'),
                          [])
        self.assertEquals(self.soup.select('body > div > .a.d')[0].__str__(),
                          '<b class="second-class a d" id="second">Second</b>')

    def testNthChild(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > b:nth-child(2)'),
                          [])
        self.assertEquals(self.soup.select('body > div > a:nth-child(2)')[0].__str__(),
                          '<a class="link" id="first-link">First Link</a>')

    def testNthOfType(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > a:nth-of-type(2)'),
                          [])
        self.assertEquals(self.soup.select('body > div > b:nth-of-type(2)')[0].__str__(),
                          '<b class="second-class a d" id="second">Second</b>')

    def testLT(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > a:lt(2)'),
                          [])
        self.assertEquals(self.soup.select('body > div > a:lt(3)')[0].__str__(),
                          '<a class="link" id="first-link">First Link</a>')

        self.assertEquals(self.soup.select('body > div > :lt(3)')[0].__str__(),
                          '<b class="first-class a c" id="first">First</b>')

        self.assertEquals(self.soup.select('body > div > :lt(3)')[1].__str__(),
                          '<a class="link" id="first-link">First Link</a>')

    def testGT(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > a:gt(3)'),
                          [])
        self.assertEquals(self.soup.select('body > div > a:gt(1)')[0].__str__(),
                          '<a class="link" id="first-link">First Link</a>')

        self.assertEquals(self.soup.select('body > div > b:gt(1)')[0].__str__(),
                          '<b class="second-class a d" id="second">Second</b>')
        self.assertEquals(self.soup.select('body > div > b:gt(1)')[1].__str__(),
                          '<b class="third-class b c" id="third">Third</b>')
        self.assertEquals(self.soup.select('body > div > b:gt(1)')[2].__str__(),
                          '<b class="fourth-class b f" id="fourth">Fourth</b>')
        self.assertEquals(self.soup.select('body > div > b:gt(1)')[3].__str__(),
                          '<b class="fifth-class a e d" id="fifth">Fifth</b>')

    def testGTE(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > a:gte(3)'),
                          [])
        self.assertEquals(self.soup.select('body > div > a:gte(2)')[0].__str__(),
                          '<a class="link" id="first-link">First Link</a>')

        self.assertEquals(self.soup.select('body > div > b:gte(1)')[0].__str__(),
                          '<b class="first-class a c" id="first">First</b>')
        self.assertEquals(self.soup.select('body > div > b:gte(1)')[1].__str__(),
                          '<b class="second-class a d" id="second">Second</b>')
        self.assertEquals(self.soup.select('body > div > b:gte(1)')[2].__str__(),
                          '<b class="third-class b c" id="third">Third</b>')
        self.assertEquals(self.soup.select('body > div > b:gte(1)')[3].__str__(),
                          '<b class="fourth-class b f" id="fourth">Fourth</b>')
        self.assertEquals(self.soup.select('body > div > b:gte(1)')[4].__str__(),
                          '<b class="fifth-class a e d" id="fifth">Fifth</b>')

    def testLTE(self):
        sample_html = """<html><body><div class="content"><b id="first" class="first-class a c">First</b><a id="first-link" class="link">First Link</a><b id="second" class="second-class a d">Second</b>MyText<b id="third" class="third-class b c">Third</b><b id="fourth" class="fourth-class b f">Fourth</b><b id="fifth" class="fifth-class a e d">Fifth</b></div></body></html>"""

        self.soup = BeautifulSoup(sample_html, "lxml")
        self.assertEquals(self.soup.select('body > div > a:lte(1)'),
                          [])
        self.assertEquals(self.soup.select('body > div > a:lte(2)')[0].__str__(),
                          '<a class="link" id="first-link">First Link</a>')

        self.assertEquals(self.soup.select('body > div > :lte(3)')[0].__str__(),
                          '<b class="first-class a c" id="first">First</b>')
        self.assertEquals(self.soup.select('body > div > :lte(3)')[1].__str__(),
                          '<a class="link" id="first-link">First Link</a>')
        self.assertEquals(self.soup.select('body > div > :lte(3)')[2].__str__(),
                          '<b class="second-class a d" id="second">Second</b>')




if __name__ == '__main__':
    unittest.main()