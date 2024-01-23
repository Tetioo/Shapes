import cairo
import math

'''Set up surface'''
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1200, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

'''Red rectangle'''
ctx.rectangle(100, 50, 150, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

'''Green rectangle'''
ctx.rectangle(250, 100, 150, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.fill()

'''Blue Square'''
ctx.rectangle(500, 100, 150, 240)
ctx.set_source_rgb(0, 0, 1)
ctx.fill()

'''Purple non-filled rectangle called stroke'''
ctx.rectangle(350, 400, 150, 240)
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(5)
ctx.stroke()

'''Purple Fill and stroke'''
ctx.rectangle(700, 400, 150, 240)
ctx.set_source_rgb(1, 0, 1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(5)
ctx.stroke()

'''Draw a line'''
ctx.move_to(200, 400)
ctx.line_to(750, 600)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

'''Closed Polygon'''
ctx.move_to(850, 100)
ctx.line_to(1000, 150)
ctx.line_to(1050, 400)
ctx.line_to(900, 300)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

'''Open Polygon Grey'''
ctx.move_to(50, 550)
ctx.line_to(150, 550)
ctx.line_to(250, 600)
ctx.line_to(400, 500)
ctx.line_to(550, 600)
ctx.line_to(700, 500)
ctx.line_to(850, 550)
ctx.line_to(950, 550)
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.set_line_width(8)
ctx.stroke()

'''Draw an arc'''
ctx.arc(600, 300, 200, 0, math.pi / 2)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

'''Yellow small Circle'''
ctx.arc(900, 550, 100, 0, 2 * math.pi)
ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(10)
ctx.stroke()

'''Purple medium Circle'''
ctx.arc(1150, 300, 150, 0, 2 * math.pi)
ctx.set_source_rgb(1, 0, 1)
ctx.set_line_width(10)
ctx.stroke()

'''White large Circle'''
ctx.arc(400, 700, 300, 0, 2 * math.pi)
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(10)
ctx.stroke()

'''Cyan bezier Curve'''
ctx.move_to(200, 400)
ctx.curve_to(400, 300, 700, 500, 850, 400)
ctx.set_source_rgb(0, 1, 1)
ctx.set_line_width(10)
ctx.stroke()

'''Closed bezier curve'''
ctx.move_to(200, 300)
ctx.curve_to(400, 200, 700, 400, 850, 300)
ctx.line_to(850, 500)  # Adjusted coordinates
ctx.curve_to(700, 600, 400, 400, 200, 500)
ctx.close_path()
ctx.set_source_rgb(0, 1, 1)
ctx.set_line_width(10)
ctx.stroke()

'''Setting color and width'''
ctx.set_source_rgb(1, 1, 1)
ctx.set_line_width(10)

'''Butt Cap'''
ctx.move_to(200, 50)
ctx.line_to(750, 50)
ctx.set_line_cap(cairo.LINE_CAP_BUTT)
ctx.stroke()

'''Square Cap'''
ctx.move_to(200, 70)
ctx.line_to(750, 70)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)
ctx.stroke()

'''Round Cap'''
ctx.move_to(200, 90)
ctx.line_to(750, 90)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)
ctx.stroke()

'''Milter join'''
ctx.move_to(150, 200)
ctx.line_to(280, 400)
ctx.line_to(150, 400)
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.stroke()

'''Round join'''
ctx.move_to(350, 200)
ctx.line_to(480, 400)
ctx.line_to(350, 400)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

'''Bevel Join'''
ctx.move_to(550, 200)
ctx.line_to(680, 400)
ctx.line_to(550, 400)
ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
ctx.stroke()

ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(10)

'''Line1'''
ctx.move_to(200, 130)
ctx.line_to(750, 130)
ctx.set_dash([20])
ctx.stroke()

'''Line2'''
ctx.move_to(200,150)
ctx.line_to(750,150)
ctx.set_dash([20,10])
ctx.stroke()

'''Line3'''
ctx.move_to(200,180)
ctx.line_to(750,180)
ctx.set_dash([20,5,5,5])
ctx.stroke()

'''Line4'''
ctx.move_to(200,200)
ctx.line_to(750,200)
ctx.set_dash([5,5,10])
ctx.stroke()
ctx.set_line_width(10)
ctx.set_line_cap(cairo.LINE_CAP_ROUND)

'''Line5'''
ctx.move_to(200,250)
ctx.line_to(750,250)
ctx.set_dash([10,20])
ctx.stroke()

'''Line5'''
ctx.move_to(200,300)
ctx.line_to(750,300)
ctx.set_dash([0,20])
ctx.stroke()
'''Black Circle'''
ctx.arc(900, 100, 150, 0, 2 * math.pi)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_line_width(10)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()

'''Bezier Curve'''
ctx.move_to(100,100)
ctx.curve_to(200,0,400,200,500,100)
ctx.line_to(500,300)
ctx.curve_to(400,400,200,200,100,300)
ctx.close_path()
ctx.set_source_rgb(0.5, 0.5, 0.5)
ctx.set_dash([40,10])
ctx.set_line_width(10)
ctx.set_dash([0,20])
ctx.stroke()



'''Purple medium Circle'''
ctx.arc(1000, 300, 150, 0, 2 * math.pi)
ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(10)
ctx.stroke()
surface.write_to_png("rectangle.png")
