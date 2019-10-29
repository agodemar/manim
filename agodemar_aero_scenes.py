from manimlib.imports import *
import os
import pyclbr
import manimlib.constants as consts

# Customize LaTeX template
# see constants.py
consts.TEMPLATE_TEX_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "files",
    "tex_template.tex"
)
with open(consts.TEMPLATE_TEX_FILE, "r") as infile:
    print("DEBUG - agodemar_example_scenes - redefine consts.TEMPLATE_TEXT_FILE_BODY")
    consts.TEMPLATE_TEXT_FILE_BODY = infile.read()
    consts.TEMPLATE_TEX_FILE_BODY = consts.TEMPLATE_TEXT_FILE_BODY.replace(
        consts.TEX_TEXT_TO_REPLACE,
        "" + consts.TEX_TEXT_TO_REPLACE + ""
    )
    print("DEBUG - agodemar_example_scenes - __file__: {}".format(os.path.dirname(os.path.realpath(__file__))))
    print("DEBUG - agodemar_example_scenes - TEMPLATE_TEX_FILE: {}".format(consts.TEMPLATE_TEX_FILE))
    #print("DEBUG - agodemar_example_scenes - TEMPLATE_TEX_FILE_BODY:\n{}\n\n".format(consts.TEMPLATE_TEX_FILE_BODY))


class CustomTextMobject(TextMobject):
    CONFIG = {
        "template_tex_file_body": consts.TEMPLATE_TEX_FILE_BODY,
    }


"""
Run this class with the command:

>> python -m manim agodemar_aero_scenes.py TestCustomTextMobject -pl
"""

class TestCustomTextMobject(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text = CustomTextMobject("Writing with manim is fun")
        second_line = CustomTextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line = CustomTextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))


template_tex_file = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "files",
    "tex_template.tex"
)
with open(template_tex_file, "r") as infile:
    template_tex_file_body = infile.read()
    template_tex_file_body = template_tex_file_body.replace(
        consts.TEX_TEXT_TO_REPLACE,
        "\\begin{align*}\n" + consts.TEX_TEXT_TO_REPLACE + "\n\\end{align*}"
    )


class CustomTexMobject(TexMobject):
    CONFIG = {
        "template_tex_file_body": template_tex_file_body,
    }


"""
Run this class with the command:

>> python -m manim agodemar_aero_scenes.py TestCustomTexMobject -pl
"""

class TestCustomTexMobject(Scene):
    def construct(self):
        tex = CustomTexMobject(r"""
            z & = f(x,y) \\
            \dot{x} & = g(z, u)
            """)
        self.add(tex)
        self.wait(2)


class CustomSVGMobject(SVGMobject):
    CONFIG = {
        "stroke_color": YELLOW,
        "stroke_width": 2,
        "fill_color": GRAY,
        "fill_opacity": 0,
    }

class CustomSymbolSVGMobject(SVGMobject):
    CONFIG = {
        "stroke_color": YELLOW,
        "stroke_width": 0,
        "fill_color": ORANGE,
        "fill_opacity": 1,
    }


"""
Run this class with the command:

>> python -m manim agodemar_aero_scenes.py SimpleSVG -pl
"""

class SimpleSVG(Scene): 
    def construct(self): 
        SVG_FILE = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
            "files",
            "ac_coppie_inerziali_vite.svg")
        # "ac_spiral_skid_OK.svg" "ac_coppie_inerziali_vite_OK.svg"
        # "Boeing-727-topview_OK.svg" "isoview_f16_OK.svg" "isoview_mb339_OK.svg"
        # "GuITmeeting_2019_logo.svg" "Mole_silhouette.svg" "pippo.svg" # scrubbed svg
        # NOTICE: get rid of <defs/> tag in svg file
        svg = CustomSVGMobject(SVG_FILE)
        svg.scale(3.5)
        self.add(svg)
        self.play(FadeIn(svg))
        self.wait(3)


"""
Run this class with the command:

>> python -m manim agodemar_aero_scenes.py SimpleSVGandText -pl
"""

class SimpleSVGandText(Scene): 
    def construct(self): 
        SVG_FILE = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
            "files",
            "ac_coppie_inerziali_vite.svg")
        # "ac_spiral_skid_OK.svg" "ac_coppie_inerziali_vite_OK.svg"
        # "Boeing-727-topview_OK.svg" "isoview_f16_OK.svg" "isoview_mb339_OK.svg"
        # "GuITmeeting_2019_logo.svg" "Mole_silhouette.svg" "pippo.svg" # scrubbed svg
        # NOTICE: get rid of <defs/> tag in svg file
        svg0 = CustomSVGMobject(file_name = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "files",
            "ac_coppie_inerziali_vite_00.svg"))
        svg0.scale(3.5)
        self.add(svg0)
        self.play(FadeIn(svg0))
        self.wait(2)
        svg1 = CustomSymbolSVGMobject(file_name = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "files",
            "ac_coppie_inerziali_vite_01.svg"))
        svg1.scale(3.5)
        self.add(svg1)
        self.play(FadeIn(svg1))
        self.wait(3)
