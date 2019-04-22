# coding=utf-8

from endesive import pdf


class Assinatura(object):

    def __init__(self, certificado):
        self.certificado = certificado

    def assina_pdf(
        self, arquivo, dados_assinatura, senha, outros_certificados=[],
        altoritimo='sha256'):
        p12 = self.certificado.p12(senha)
        return pdf.cms.sign(
            datau=arquivo,
            udct=dados_assinatura,
            key=p12.get_privatekey().to_cryptography_key(),
            cert=p12.get_certificate().to_cryptography(),
            othercerts=outros_certificados,
            algomd=altoritimo
        )

    def assina_xml(self):
        pass
