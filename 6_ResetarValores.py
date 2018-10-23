import numpy as np
import cv2
import sys
import os
from Core.BDaccess import *

#CONSTANTES UTILIZDAS NO CODIGO
FREQ_DIVIDER = 5
REDMEN_FACTOR = 4
NUM_TREINAMENTO = 20

class ResetarValores:
    #Metodo quando a classe e iniciada
    def __init__(self):
        reseta_valor_presente()
        
if __name__ == '__main__':
    treinar = ResetarValores()
print ("Valores Reestabelecidos com sucesso!")
