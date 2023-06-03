from manim import *

def Fancy_label(text: Tex, mode='normal'):
    mode = mode.lower()
    modes = ['vlow','low','normal','fast','vfast']
    if mode not in modes: mode='normal'
    s = text.get_tex_string().split('$')
    symbols = 0
    for i in range(0,len(s),2):
        symbols += len(s[i])
    time = (symbols + len(s)/2)/6 / (2.71828**(0.4*modes.index(mode)-0.75))
    return AnimationGroup(Write(text.to_edge(UP)),run_time=time)

