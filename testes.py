import urllib2
from bike_itau_model import *
import unicodedata

if __name__ == '__main__':
    s = session()

    obj = MovimentacaoBikeItau()
    if (obj == None):
        print(obj)

    obj = s.query(MovimentacaoBikeItau).filter(MovimentacaoBikeItau.idEstacao == 114).order_by(MovimentacaoBikeItau.id.desc()).first()

    if (obj == None):
        print(obj)
        
    print(obj.timestamp)

    s.close()
