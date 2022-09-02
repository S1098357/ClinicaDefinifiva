import datetime
from unittest import TestCase

from Amministrazione.Sistema import Sistema
from Servizio.Prenotazione import Prenotazione


class TestPrenotazione(TestCase):

    def testNuovaPrenotazione(self):
        self.prenotazione=Prenotazione()
        self.prenotazione.cliente='prova'
        self.prenotazione.dataOra=datetime.datetime.now()
        self.prenotazione.stampaPrenotazione()
        sistema=Sistema([])
        sistema.listaPrenotazioni=[self.prenotazione]
        sistema.salvaPrenotazioni()
        sistema.leggiPrenotazioni()
        self.assertEqual(self.prenotazione,sistema.listaPrenotazioni[0])