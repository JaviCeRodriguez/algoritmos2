"""
Implemente la clase Lamparita, que sirva para representar el estado de encendido
de una lamparita (encendido o apagado). Defina, asimismo, dos métodos que
permitan encender y apagar la luz de la lamparita y otro que indique en qué
estado se encuentra. La lamparita inicialmente está apagada.
"""

class Lampara:
    def __init__(self):
        self.prendido = False
    
    def encender(self):
        self.prendido = True
    
    def apagar(self):
        self.prendido = False
    
    def estado(self):
        print(f"La lamparita está {'prendida' if self.prendido else 'apagada'}")

if __name__ == '__main__':
    lampara = Lampara()
    lampara.estado()
    lampara.encender()
    lampara.estado()
    lampara.apagar()
    lampara.encender()