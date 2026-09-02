import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_styled_document(output_path="/Users/rouen/Documents/coding/上海亲子自驾游完整攻略.docx"):
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'''
            <w:tcMar {nsdecls("w")}>
                <w:top w:w="{top}" w:type="dxa"/>
                <w:bottom w:w="{bottom}" w:type="dxa"/>
                <w:left w:w="{left}" w:type="dxa"/>
                <w:right w:w="{right}" w:type="dxa"/>
            </w:tcMar>
        ''')
        tcPr.append(tcMar)

    def set_cell_border(cell, **kwargs):
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
        for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            edge_data = kwargs.get(edge)
            if edge_data:
                b_elm = parse_xml(f'<w:{edge} {nsdecls("w")} w:val="{edge_data.get("val","single")}" w:sz="{edge_data.get("sz","4")}" w:space="0" w:color="{edge_data.get("color","auto")}"/>')
                tcBorders.append(b_elm)
            else:
                b_elm = parse_xml(f'<w:{edge} {nsdecls("w")} w:val="none"/>')
                tcBorders.append(b_elm)
        tcPr.append(tcBorders)

    # 1. Hero Box
    t_hero = doc.add_table(rows=1, cols=1)
    t_hero.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_hero.autofit = False
    c_hero = t_hero.cell(0, 0)
    c_hero.width = Inches(6.8)
    set_cell_background(c_hero, "1E1B4B")
    set_cell_margins(c_hero, top=240, bottom=240, left=240, right=240)
    set_cell_border(c_hero)

    p = c_hero.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("🏰 2026.09.10 - 09.12 · 3天2晚家庭自驾")
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(254, 205, 211)

    p2 = c_hero.add_paragraph()
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(4)
    r2 = p2.add_run("杭州 ➔ 上海亲子自驾游保姆级完整规划")
    r2.font.size = Pt(17)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(255, 255, 255)

    p3 = c_hero.add_paragraph()
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(0)
    r3 = p3.add_run("浙A绿牌 · 2岁女宝 (92cm) ＋ 50+外婆 ＋ 父母 · 轻松慢游 · 保证14:00-16:00午睡")
    r3.font.size = Pt(9.5)
    r3.font.color.rgb = RGBColor(203, 213, 225)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    doc.save(output_path)
    print(f"Generated base docx at {output_path}")

if __name__ == "__main__":
    create_styled_document()
