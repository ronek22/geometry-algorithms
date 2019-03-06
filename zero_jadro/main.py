from utility import Utility
from polygon import Polygon

util = Utility()

exercises = [
    'zad1.txt', 'zad2.txt', 'zad3.txt', 'zad4.txt', 'zad4b.txt', 
    'zad5.txt', 'zad6.txt', 'zad7.txt', 'zad8.txt', 'zad9.txt', 'zad10.txt']

for filename in exercises[::-1]:
    polytxt = util.from_txt('data/' + filename)

    util.draw(*polytxt.get_axes())
    print filename,"\tIstnieje jadro? ", polytxt.check_kernel()
    util.draw_spikes(polytxt)


util.show()
