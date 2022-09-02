import datetime
import pickle
from unittest import TestCase

from Servizio.CertificatoMedico import CertificatoMedico


class TestCertificatoMedico(TestCase):

    def testCompilaCertificato(self):
        self.certificato=CertificatoMedico()
        self.certificato.compilaCertificato('prova','test',datetime.datetime.now())
        self.certificato.stampaCertificato()
        appoggio=self.certificato.leggiCertificato()
        self.assertIsNotNone(appoggio)
        self.assertEqual(appoggio.nomePaziente,self.certificato.nomePaziente)