from correr import FazerCorrida
from falar import IniciarFala
from pessoa import Pessoa


pessoa1 = Pessoa(IniciarFala())
pessoa1.realizar_acao()
pessoa2 = Pessoa(FazerCorrida())
pessoa2.realizar_acao()