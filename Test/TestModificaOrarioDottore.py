import datetime
import os.path
import pickle
from unittest import TestCase

#from Servizio.Dottore import Dottore
from Servizio.Dottore import Dottore


class TestModificaOrarioDottore(TestCase):

    def testModificaOrarioDottore(self):
        self.dottore=Dottore('prova',123)
        prova='9/5/2022 lunedì 9.00'
        self.dottore.salvaOrari(prova)
        orari=None
        with open('dati/Orariprova.pickle','rb+') as f:
            orari=pickle.load(f)
        self.assertIsNotNone(orari)
        self.dottore.leggiOrari()
        orarioPrevisto=datetime.time(9)
        self.assertEqual(self.dottore.OrarioLavoro[1],orarioPrevisto)
