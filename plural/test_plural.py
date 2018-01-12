#coding=utf-8
import plural
import unittest

class TestPlural(unittest.TestCase):

    #以sxz结尾，加es
    def test_sxz_es(self):
        li=['bass','fox','waltz']
        for noun in li:
            self.assertEqual((noun+'es'),plural.plural(noun))

     #以发音‘h’结尾，加es
    def test_h_es(self):
        li=['coach','rash']
        for noun in li:
            self.assertEqual((noun+'es'),plural.plural(noun))

    #以不发音'h'结尾，加s
    def test_non_h(self):
        noun = 'cheetah'
        self.assertEqual(noun+'s',plural.plural(noun))

    #以I音的y结尾，变成ies
    def test_y_ies(self):
        li='vacancy'
        noun = li[0:len(li)-1]
        self.assertEqual(noun+'ies',plural.plural(li))

    #以元音加y结尾，加s
    def test_ay_s(self):
        li='day'
        self.assertEqual(li+'s',plural.plural(li))

    #直接加s
    def test_s(self):
        li=['apple','cup']
        for noun in li:
            self.assertEqual(noun+'s',plural.plural(noun))

if __name__=='__main__':
    unittest.main()