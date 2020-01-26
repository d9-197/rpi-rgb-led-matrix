#!/bin/sh
cd /home/pi/rpi-rgb-led-matrix
#sudo examples-api-use/scrolling-text-example -l 2 -f fonts/4x6.bdf --led-cols=64 -C 0,255,120 -y 8 Température : 6° C 
#sudo examples-api-use/scrolling-text-example -l 2 -f fonts/6x9.bdf --led-cols=64 -C 255,158,0 -y 8 Température : 6° C 
#sudo examples-api-use/scrolling-text-2lines -l 2 -f fonts/9x18.bdf --led-cols=64 -C 158,255,120 -x 0 -y 0  -1 "Température : 6° C" -2 "TEST 2ème ligne bien plus longue que la première ligne..."
#sudo examples-api-use/scrolling-text-2lines -l 2 -f fonts/9x18.bdf --led-cols=64 -C 158,255,120 -x 0 -y 0  -1 "Température : 6° C"
#sudo examples-api-use/text-example  -f fonts/9x18.bdf --led-cols=64 -C 158,255,120 -x 0 -y 0 
#sudo examples-api-use/clock -f fonts/9x18.bdf --led-cols=64 -C 0,255,120 -x 10 -y 5
#sudo examples-api-use/demo -f fonts/9x18.bdf --led-cols=64 -C 0,255,120 -x 10 -y 5 Température de la piscine : 6° C -t 10
#convert examples-api-use/afficheur.png -resize 64x32! -depth 8 RGB:-  | sudo examples-api-use/ledcat -l 10 --led-cols=64 --geometry 64x32 --transpose zigzag_y apa102 

#PAS BON : convert examples-api-use/afficheur.png -resize 64x32! -depth 8 PPM: >> examples-api-use/afficheur1.ppm

#for f in examples-api-use/images/*.jpg
#do
#	convert $f -resize 64x32! -set filename:mysize 'examples-api-use/images/afficheur.png' '%[filename:mysize]'
#	mogrify -format ppm  examples-api-use/images/afficheur.png
#	sudo examples-api-use/demo --led-cols=64 -D 1 examples-api-use/images/afficheur.ppm -m 0 -t 2
#done

sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 L -tc1 "102,204,255" -vc1 "0,0,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf" -t1 "Texte sur une ligne " -v1 "vitesse 2"  -l 1 -s 2
sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 L -tc1 "102,204,255" -vc1 "0,0,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf" -t1 "Texte sur une ligne " -v1 "vitesse 5"  -l 1 -s 5
sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 L -tc1 "102,204,255" -vc1 "0,0,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf" -t1 "Texte sur une ligne " -v1 "vitesse 15"  -l 1 -s 15
sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 L -tc1 "102,204,255" -vc1 "0,0,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf" -a2 R -tc2 "255,255,51" -vc2 "255,255,179" -f2 "/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf" -t1 "Tex" -v1 "te" -t2 "2 " -v2 "lignes" -d 3
sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 C -tc1 "102,204,255" -vc1 "0,0,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf" -a2 C -tc2 "255,255,51" -vc2 "255,255,179" -f2 "/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf" -t1 "Te" -v1 "xte" -t2 "2 " -v2 "lignes" -d 3
sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 R -tc1 "102,204,255" -vc1 "0,0,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf" -a2 L -tc2 "255,255,51" -vc2 "255,255,179" -f2 "/home/pi/rpi-rgb-led-matrix/fonts/6x13.bdf" -t1 "T" -v1 "exte" -t2 "2 " -v2 "lignes" -d 3
sudo /home/pi/rpi-rgb-led-matrix/bindings/python/samples/domotique.py --led-cols=64 -a1 L -tc1 "102,204,255" -vc1 "0,119,179" -f1 "/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf" -a2 R -tc2 "255,255,51" -vc2 "255,255,179" -f2 "/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf" -t1 "Texte sur " -v1 "deux lignes" -t2 "à faible" -v2 " vitesse" -l 1 -s 1
#	convert examples-api-use/afficheur.png -resize 64x32! -depth 8 RGB:- 
#    sleep 1;
#done | sudo examples-api-use/ledcat --led-cols=64 --geometry 64x32 --transpose zigzag_y apa102  > /dev/null;
cd /home/pi
