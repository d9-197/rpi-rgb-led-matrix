#!/usr/bin/env python
# coding: utf-8
# Display a runtext with double-buffering.



from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-l", "--loop", help="number of loops (scroll text)", default="0")
        self.parser.add_argument("-s", "--speed", help="speed (scroll text)", default="1")
        self.parser.add_argument("-d", "--duration", help="duration (still text)", default="2")
        self.parser.add_argument("-t1", "--title1", help="Line 1 title", default="")
        self.parser.add_argument("-v1", "--value1", help="Line 1 value", default="")
        self.parser.add_argument("-tc1", "--titlecolor1", help="Line 1 title color", default="255,0,0")
        self.parser.add_argument("-vc1", "--valuecolor1", help="Line 1 value color", default="255,255,0")
        self.parser.add_argument("-f1", "--font1", help="Line 1 font", default="/home/pi/rpi-rgb-led-matrix/fonts/6x12.bdf")
        self.parser.add_argument("-a1", "--align1", help="Line 1 alignment", default="C")
        self.parser.add_argument("-t2", "--title2", help="Line 2 title", default="")
        self.parser.add_argument("-v2", "--value2", help="Line 2 value", default="")
        self.parser.add_argument("-tc2", "--titlecolor2", help="Line 2 title color", default="255,0,0")
        self.parser.add_argument("-vc2", "--valuecolor2", help="Line 2 value color", default="255,255,0")
        self.parser.add_argument("-f2", "--font2", help="Line 2 font", default="/home/pi/rpi-rgb-led-matrix/fonts/6x12.bdf")
        self.parser.add_argument("-a2", "--align2", help="Line 2 alignment", default="C")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        pos = offscreen_canvas.width;
        loops = int(self.args.loop.decode('utf-8'));
        s = int(self.args.speed.decode('utf-8'));
        duration = int(self.args.duration.decode('utf-8'));
        value1 = self.args.value1.decode('utf-8');
        value2 = self.args.value2.decode('utf-8');
        title1 = self.args.title1.decode('utf-8');
        title2 = self.args.title2.decode('utf-8');
        fontPath1 = self.args.font1;
        fontPath2 = self.args.font2;
        titlecolor1 = self.args.titlecolor1.decode('utf-8');
        titlecolor2 = self.args.titlecolor2.decode('utf-8');
        valuecolor1 = self.args.valuecolor1.decode('utf-8');
        valuecolor2 = self.args.valuecolor2.decode('utf-8');
        align1 = self.args.align1.decode('utf-8');
        align2 = self.args.align2.decode('utf-8');
        t1r=int(titlecolor1.split(",")[0]);
        t1g=int(titlecolor1.split(",")[1]);
        t1b=int(titlecolor1.split(",")[2]);
        t1color=graphics.Color(t1r, t1g, t1b);
        t2r=int(titlecolor2.split(",")[0]);
        t2g=int(titlecolor2.split(",")[1]);
        t2b=int(titlecolor2.split(",")[2]);
        t2color=graphics.Color(t2r, t2g, t2b);
        v1r=int(valuecolor1.split(",")[0]);
        v1g=int(valuecolor1.split(",")[1]);
        v1b=int(valuecolor1.split(",")[2]);
        v1color=graphics.Color(v1r, v1g, v1b);
        v2r=int(valuecolor2.split(",")[0]);
        v2g=int(valuecolor2.split(",")[1]);
        v2b=int(valuecolor2.split(",")[2]);
        v2color=graphics.Color(v2r, v2g, v2b);
        font1 = graphics.Font()
        font1.LoadFont(fontPath1)
        font2 = graphics.Font()
        font2.LoadFont(fontPath2)

        centrage_vertical=0
        #print 'taille ecran : ' + str(offscreen_canvas.height)
        
        if (title2=="" and value2==""):
            #print 'taille police 1 : ' + str(font1.baseline)
            centrage_vertical=(offscreen_canvas.height-font1.baseline) /2
        else:
            #print 'taille police 2 : ' + str(font2.baseline)
            centrage_vertical=(offscreen_canvas.height-font1.baseline-font2.baseline)/3

        #print 'centrage vertical : '+ str(centrage_vertical)
        offscreen_canvas.Clear()
        lentitle1= graphics.DrawText(offscreen_canvas, font1, pos, font1.baseline+centrage_vertical, t1color, title1)
        lenvalue1 = graphics.DrawText(offscreen_canvas, font1, pos+lentitle1, font1.baseline+centrage_vertical, v1color, value1)
        lentitle2= graphics.DrawText(offscreen_canvas, font2, pos,font1.baseline+font2.baseline+2*centrage_vertical, t2color, title2)
        lenvalue2 = graphics.DrawText(offscreen_canvas, font2, pos+lentitle2, font1.baseline+font2.baseline+2*centrage_vertical, v2color, value2)
        lentotal1 =lenvalue1+lentitle1
        lentotal2 =lenvalue2+lentitle2
        if (loops <= 0):
            pos1=0;
            pos2=0;
            while (duration>0):
                offscreen_canvas.Clear()
                lentitle1= graphics.DrawText(offscreen_canvas, font1, pos1, font1.baseline+centrage_vertical, t1color, title1)
                lenvalue1 = graphics.DrawText(offscreen_canvas, font1, pos1+lentitle1, font1.baseline+centrage_vertical, v1color, value1)
                lentitle2= graphics.DrawText(offscreen_canvas, font2, pos2,font1.baseline+font2.baseline+2*centrage_vertical, t2color, title2)
                lenvalue2 = graphics.DrawText(offscreen_canvas, font2, pos2+lentitle2, font1.baseline+font2.baseline+2*centrage_vertical, v2color, value2)
                if (align1=="C" ):
                    pos1 = (offscreen_canvas.width-(lentotal1))/2
                else:
                    if (align1=="R"):
                        pos1=(offscreen_canvas.width-(lentotal1));
                    else:
                        pos1=0;
                if (align2=="C" ):
                    pos2 = (offscreen_canvas.width-(lentotal2))/2
                else:
                    if (align2=="R"):
                        pos2=(offscreen_canvas.width-(lentotal2));
                    else:
                        pos2=0;
                offscreen_canvas.Clear()
                lentitle1= graphics.DrawText(offscreen_canvas, font1, pos1, font1.baseline+centrage_vertical, t1color, title1)
                lenvalue1 = graphics.DrawText(offscreen_canvas, font1, pos1+lentitle1, font1.baseline+centrage_vertical, v1color, value1)
                lentitle2= graphics.DrawText(offscreen_canvas, font2, pos2,font1.baseline+font2.baseline+2*centrage_vertical, t2color, title2)
                lenvalue2 = graphics.DrawText(offscreen_canvas, font2, pos2+lentitle2, font1.baseline+font2.baseline+2*centrage_vertical, v2color, value2)            
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(0.01)
                duration-=0.01
        else:
            if (lentotal1>lentotal2):
                pos1=offscreen_canvas.width;
                pos2=offscreen_canvas.width + (lentotal1-lentotal2)/2
            else:
                pos2=offscreen_canvas.width;
                pos1=offscreen_canvas.width + (lentotal2-lentotal1)/2
            while (loops>0):
                offscreen_canvas.Clear()
                lentitle1= graphics.DrawText(offscreen_canvas, font1, pos1, font1.baseline+centrage_vertical, t1color, title1)
                lenvalue1 = graphics.DrawText(offscreen_canvas, font1, pos1+lentitle1, font1.baseline+centrage_vertical, v1color, value1)
                lentitle2= graphics.DrawText(offscreen_canvas, font2, pos2,font1.baseline+font2.baseline+2*centrage_vertical, t2color, title2)
                lenvalue2 = graphics.DrawText(offscreen_canvas, font2, pos2+lentitle2, font1.baseline+font2.baseline+2*centrage_vertical, v2color, value2)

                pos1 -= 1
                pos2 -= 1
                if (lentotal1>lentotal2 and pos1 + lentotal1 < 0):
                    pos1 = offscreen_canvas.width
                    pos2=offscreen_canvas.width + (lentotal1-lentotal2)/2
                    loops -=1
                if (lentotal2>lentotal1 and pos2 + lentotal2 < 0):
                    pos2 = offscreen_canvas.width
                    pos1=offscreen_canvas.width + (lentotal2-lentotal1)/2
                    loops -=1

                time.sleep(0.05/s)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
