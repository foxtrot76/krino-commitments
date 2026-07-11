#!/usr/bin/env python3
# =============================================================================
# KRINO WEEKLY ISSUE RENDERER — locked 4-page "one anchor per page" structure
#   Page 1  THE RECORD   — what is the instrument saying?  (record-spine anchor)
#   Page 2  THE THESIS   — why is it saying that?          (thesis-forward + evidence)
#   Page 3  METHOD | GOVERNANCE — capabilities & limits / why trust it
#   Page 4  APPENDIX A — AUDIT  — can I verify it?         (durable; glossary sidebar)
# Design locked 2026-07-06 (dual-RT OpenAI+DeepSeek; picks P1V2·P2V2·P3V2·P4V1).
# Principle: the RECORD is the credibility backbone, NOT the product (the product
# is the inference). No decoration (no colour banners / emoji / gauges). Each week
# edit ONLY the CONTENT block; the layout is fixed — that fixedness is the identity.
# =============================================================================

# ------------------------------- CONTENT (EDIT PER ISSUE) --------------------
CONTENT = {
  "out": "/mnt/user-data/outputs/KRINO_WEEKLY_No001.pdf",
  "issue_no": "001", "date": "2026-07-11", "specimen": False,
  "publisher": "KRINO — published by A.G.", "data_cutoff": "markets 2026-07-09/10 · inflation May 2026",
  "asof": "2026-07-11 18:00 CET", "reading_time": "≈ 4 minutes",
  "commit_url": "github.com/foxtrot76/krino-commitments", "intake_email": "krino.reviews@gmail.com",

  # PAGE 1 — THE RECORD
  "headline": "Market stress stays benign; the labour data beneath the calm deteriorated this week.",
  "state_pair": [("Stress","CALM",False),("Inflation","WATCH",True)],
  "evidence_strength": "Low–moderate",
  "state_note": "inflation regime NONE → WATCH since 2026-03",
  "read": ("Market-stress regime unchanged and calm: equity volatility 15.8, the yield curve positive, credit "
           "spreads tight. The inflation axis holds at WATCH — consumer prices 4.5% year-over-year on this "
           "report's merged series, with the May print energy-led. The new information this week came from the "
           "labour side: June payrolls rose 57,000 against roughly 110,000 expected, the two prior months were "
           "revised down a combined 74,000, and the labour force shrank by 720,000 — participation now at its "
           "lowest since March 2021. The unemployment rate fell while fewer people worked or looked for work. "
           "The two axes of this report still disagree, and the labour readings sharpened the disagreement. "
           "Between scheduled data releases, the published state moves only on the pre-registered falsifiers "
           "listed below — headlines and commentary, including this report's own, change nothing by themselves."),
  "sh_stress":    ['C','C','C','C','C','C','C','C','C','C','C','C','C'],
  "sh_inflation": ['N','N','N','N','N','N','N','N','N','W','W','W','W'],
  "sh_end": "2026-06",
  "forward_tests": [("Labour-slack sign","reg. 2026-06-23","grades 2026-08-07","in 27 days"),
                    ("Inflation-regime transition","live","grades on next CPI print (2026-07-14)","monthly")],
  "falsifiers": ["Real policy rate turns restrictive (≤ −1%)",
                 "Sixth straight month of CPI ≥ 4% year-over-year",
                 "Volatility or credit breaks the calm"],

  # PAGE 2 — THE THESIS
  "thesis_active": ("A calm market-stress regime coincident with an inflation axis at WATCH — and, this period, "
      "labour data moving against the calm: payroll growth at a four-month low with downward revisions, and an "
      "unemployment rate falling on labour-force exit rather than hiring. The stress panel is, by construction, "
      "tuned to deflationary and liquidity stress and reads benign; the separately validated inflation axis and "
      "the labour-slack signal carry the divergence. Published state moves only on a pre-registered falsifier — "
      "none was met this period."),
  "thesis_opposing": ("Each of this period's adverse readings has a benign competing explanation with a scheduled "
      "test. The participation decline may be labour supply — an immigration slowdown and ageing — rather than "
      "discouragement; the pre-registered payroll test of 2026-08-07 discriminates. The growth-nowcast decline is "
      "attributed by some analysts largely to trade-gap accounting, with private domestic demand estimates near "
      "2.5%. And an energy-led CPI bump that fades before the six-month arm completes would return the inflation "
      "axis to NONE — the WATCH, in hindsight, a false positive of a young live axis (live record: n = 1)."),
  "rejected": [["Alternative","Rejected because"],
      ["Acute market-stress regime","Volatility 15.8, curve positive, credit benign"],
      ["Imminent recession","Jobless claims 215,000 and flat; the labour-slack question is open, not resolved"]],
  "panel": [["Signal","Reading","Threshold","Status"],
      ["Equity volatility (VIX)","15.84","< 20","calm"],["S&P 500","7,575","—","near high"],
      ["Yield curve (10y − 2y)","+0.35","> 0","positive"],["High-yield credit spread","below tripwire","< 1.44","benign"],
      ["Initial jobless claims","215,000","< 300k","low"],["Market-stress index","MILD","—","below bands"]],
  "irs": [["Component","Value","Threshold","Fires"],
      ["CPI, year-over-year","4.47%","≥ 3%","yes"],["CPI, 3-month annualised","10.6%","accelerating","yes"],
      ["Months ≥ 4% year-over-year","2 of 6","6 to arm","no"],["Real policy rate","−0.88%","≤ −1.0%","no"],
      ["Real-equity erosion","—","depressed","no"]],

  # PAGE 3 — METHOD | GOVERNANCE
  "coverage": [["Coverage area","Stage"],["Market stress — vol, credit, liquidity","Scored"],
      ["Inflation regime","Scored (live)"],["Labour slack","Scored"],["Commodity / energy shocks","Monitored"],
      ["Private credit","Watch"],["Geopolitics / chokepoints","Observed"]],
  "blindspots": ("Commodity and energy supply shocks are monitored but not scored. The stress panel is "
      "structurally insensitive to inflationary regimes; that gap is partially covered by the inflation-regime "
      "axis, added for it. Private-credit stress is not visible in public spreads and is watched, not scored."),
  "layer_status": ("Validated (shown as validated): market-stress axis; inflation-regime axis. Provisional — under "
      "evaluation: the multi-thesis interpretation layer (dual-read shown for transparency; promoted only when its "
      "validator is operational and the evaluation phase clears)."),
  "reviews": [("OpenAI","partially agreed","the report still over-explains its own rigour; let structure speak."),
              ("DeepSeek","partially agreed","wanted stronger visual hierarchy; decoration declined as off-identity.")],
  "governance": "Published state never moves on review count. Challenges are logged (CH-nnn); the state changes only on a pre-registered falsifier.",

  # PAGE 4 — APPENDIX A: AUDIT
  "audit": [["Understanding-model lock","v15  8d4515ed"],["Thesis ontology (frozen)","v1.0  ff5466c3"],
      ["Inflation Regime Sensor","r297 — frozen"],["Commitment log","github.com/foxtrot76/krino-commitments"]],
  # r400 (2026-07-08): DERIVE this table + strongest_challenge from the tracker's
  # "Challenge Log" sheet at issue time — never from memory (the sheet is the source;
  # these rows were seeded INTO it as CH-001/CH-002).
  "open_challenges": [["ID","Challenge","Opened","Status","Severity"],
      ["CH-001","Live inflation axis unvalidated (n=1)","2026-07-06","Open","Med"],
      ["CH-002","Panel deflation-tuned — coverage partial","2026-07-04","Monitored","Med"]],
  "strongest_challenge": ("The inflation-regime axis is live but unvalidated (n=1); its first WATCH could be a "
      "false positive. Open — would change the weight on the inflation reading; adjudication begins with the "
      "July and August consumer-price prints."),
  "glossary": [["WATCH","An inflationary configuration flagged, not a confirmed regime."],
      ["Arms the regime","Meets the count needed to confirm a regime (6 months ≥ 4%)."],
      ["Corroborator","A secondary signal required to confirm the primary one."],
      ["Live axis","A validated signal in its first live readings (small sample)."],
      ["Falsifier","A pre-registered condition that, if met, moves the state."]],
}

# ============================= LOCKED DESIGN (do not edit per-issue) ==========
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Rect, Line, Circle, String
from reportlab.pdfgen.canvas import Canvas as _RLC

LF="/usr/share/fonts/truetype/liberation/"
for n,f in [("Serif","LiberationSerif-Regular"),("Serif-B","LiberationSerif-Bold"),("Serif-I","LiberationSerif-Italic"),
            ("Sans","LiberationSans-Regular"),("Sans-B","LiberationSans-Bold"),("Sans-I","LiberationSans-Italic")]:
    pdfmetrics.registerFont(TTFont(n,LF+f+".ttf"))
INK=colors.HexColor("#1b2430"); GREY=colors.HexColor("#3b4652"); TEAL=colors.HexColor("#0f5a54")
AMBER=colors.HexColor("#9a6600"); TINT=colors.HexColor("#eef1f4"); RULE=colors.HexColor("#c3cad2"); MUTE=colors.HexColor("#6b7885")

def P(txt,font="Sans",size=9.5,lead=14,color=INK,align=TA_LEFT,sb=0,sa=5):
    return Paragraph(txt,ParagraphStyle("x",fontName=font,fontSize=size,leading=lead,textColor=color,alignment=align,spaceBefore=sb,spaceAfter=sa))
def rule(c=RULE,w=0.7,sb=4,sa=4): return HRFlowable(width="100%",thickness=w,color=c,spaceBefore=sb,spaceAfter=sa)
def sechead(t): return P(t,font="Serif-B",size=13,lead=16,color=INK,sb=2,sa=5)
def sub(t,c=GREY,sa=2,sb=6): return P(t,font="Sans-B",size=8.4,lead=12,color=c,sb=sb,sa=sa)

def month_labels(end,n):
    y,m=map(int,end.split("-")); seq=[]
    for _ in range(n):
        seq.append((y,m)); m-=1
        if m==0: m=12; y-=1
    seq=seq[::-1]
    return [f"{mm:02d}-{yy%100:02d}" if (i==0 or mm==1) else f"{mm:02d}" for i,(yy,mm) in enumerate(seq)]

def state_band(C,cell=17):
    S_,I_=C["sh_stress"],C["sh_inflation"]; n=len(S_); P_=month_labels(C["sh_end"],n); gap=3.5; x0=72; top=52; d=Drawing(500,70)
    def sq(x,y,st):
        if st in('C','N'): d.add(Rect(x,y,cell,cell,strokeColor=RULE,strokeWidth=0.8,fillColor=colors.white))
        elif st=='W': d.add(Rect(x,y,cell,cell,strokeColor=AMBER,strokeWidth=0.5,fillColor=AMBER))
        else: d.add(Rect(x,y,cell,cell,strokeColor=INK,strokeWidth=0.5,fillColor=INK))
    d.add(String(0,top+3,"StressState",fontName="Sans",fontSize=7.2,fillColor=GREY)); d.add(String(0,top-cell,"InflationState",fontName="Sans",fontSize=7.2,fillColor=GREY))
    for i in range(n):
        x=x0+i*(cell+gap); sq(x,top,S_[i]); sq(x,top-cell-4,I_[i]); d.add(String(x+cell/2,top-cell-16,P_[i],fontName="Sans",fontSize=5.4,fillColor=MUTE,textAnchor="middle"))
    d.add(Rect(0,4,9,9,strokeColor=RULE,strokeWidth=0.7,fillColor=colors.white)); d.add(String(13,5,"calm / none",fontName="Sans",fontSize=6.6,fillColor=GREY))
    d.add(Rect(88,4,9,9,strokeColor=AMBER,fillColor=AMBER,strokeWidth=0)); d.add(String(101,5,"watch",fontName="Sans",fontSize=6.6,fillColor=GREY))
    d.add(Rect(150,4,9,9,strokeColor=INK,fillColor=INK,strokeWidth=0)); d.add(String(163,5,"regime",fontName="Sans",fontSize=6.6,fillColor=GREY))
    d.add(String(230,5,f"monthly readings {P_[0]} → {P_[-1]}",fontName="Sans",fontSize=6,fillColor=MUTE))
    return d

def ltbl(data,w,rjust=(),pad=6):
    from reportlab.lib.styles import ParagraphStyle
    import xml.sax.saxutils as _xu
    _n=ParagraphStyle("cN",fontName="Sans",fontSize=8.2,leading=10.4,textColor=INK)
    _h=ParagraphStyle("cH",fontName="Sans-B",fontSize=8.2,leading=10.4,textColor=INK)
    _r=ParagraphStyle("cR",fontName="Sans",fontSize=8.2,leading=10.4,textColor=INK,alignment=TA_RIGHT)
    def _c(t,ri,ci):
        sty=_h if ri==0 else (_r if ci in rjust else _n)
        return Paragraph(_xu.escape(str(t)),sty)
    wd=[[_c(c,ri,ci) for ci,c in enumerate(row)] for ri,row in enumerate(data)]
    t=Table(wd,colWidths=[x*mm for x in w])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
        ("TOPPADDING",(0,0),(-1,-1),3.2),("BOTTOMPADDING",(0,0),(-1,-1),3.2),("LEFTPADDING",(0,0),(-1,-1),pad),("LEFTPADDING",(0,0),(0,-1),0),("RIGHTPADDING",(0,0),(-1,-1),pad),
        ("BACKGROUND",(0,0),(-1,0),TINT),("LINEBELOW",(0,0),(-1,0),0.7,GREY),("LINEBELOW",(0,1),(-1,-1),0.3,RULE)]))
    return t

def ft_flow(C,size=8.4):
    return [P(f'<font name="Sans-B">{t}</font> — {r}; <font color="#0f5a54">{g}</font> ({c})',size=size,lead=13,sa=2) for t,r,g,c in C["forward_tests"]]
def fals_flow(C,size=9):
    return [P(f'<font color="#6b7885">&#9633;</font>&nbsp; {f}',size=size,lead=14,sa=3) for f in C["falsifiers"]]

class NumberedCanvas(_RLC):
    def __init__(self,*a,**k): _RLC.__init__(self,*a,**k); self._pages=[]
    def showPage(self): self._pages.append(dict(self.__dict__)); self._startPage()
    def save(self):
        n=len(self._pages)
        for i,pg in enumerate(self._pages,1):
            self.__dict__.update(pg); self.setFont("Sans",7); self.setFillColor(MUTE)
            self.drawString(20*mm,12*mm,_FOOT); self.drawRightString(190*mm,12*mm,f"Page {i} of {n}")
            self.setStrokeColor(RULE); self.setLineWidth(0.5); self.line(20*mm,14.5*mm,190*mm,14.5*mm); _RLC.showPage(self)
        _RLC.save(self)

def build(C):
    st=[]
    wm=Paragraph('<font name="Serif-B" size=23>KRINO</font>&nbsp;&nbsp;<font name="Sans" size=7.2 color="#6b7885">M A C R O - R E G I M E &nbsp; R E P O R T</font>',ParagraphStyle("wm",leading=24))
    rt=P(f'<font name="Serif-B" size=11>No. {C["issue_no"]}</font><br/><font name="Sans" size=7 color="#6b7885">{C["date"]} · weekly · PDF</font>',align=2,sa=0)
    mast=Table([[Draw_seal(),wm,rt]],colWidths=[15*mm,111*mm,44*mm])
    mast.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(0,0),0),("LEFTPADDING",(1,0),(1,0),4),("RIGHTPADDING",(-1,0),(-1,0),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    st+=[mast,rule(INK,1.1,6,3)]
    spec=" · SPECIMEN" if C["specimen"] else ""
    st+=[P(f'<font name="Sans-B">For professional investors only</font>{spec} &nbsp;|&nbsp; {C["data_cutoff"]} &nbsp;|&nbsp; As-of {C["asof"]} '
           f'&nbsp;|&nbsp; Reading time {C["reading_time"]} &nbsp;|&nbsp; Publisher: <font color="#9a6600">{C["publisher"]}</font>',font="Sans",size=7.2,lead=10,color=MUTE,sa=8)]

    # ===== PAGE 1 — THE RECORD (headline -> state -> record -> read -> tests -> falsifiers) =====
    st+=[P(C["headline"],font="Serif",size=17,lead=21,color=INK,sa=6)]
    sp=C["state_pair"]
    sline=(f'<font name="Sans-B" size=9>{sp[0][0]}</font> {sp[0][1]}<font color="#6b7885">&nbsp;&nbsp;·&nbsp;&nbsp;</font>'
           f'<font name="Sans-B" size=9>{sp[1][0]}</font> <font name="Sans-B" size=9 color="#9a6600">{sp[1][1]}</font>'
           f'<font color="#6b7885">&nbsp;&nbsp;·&nbsp;&nbsp;</font><font name="Sans-B" size=9>Evidence strength</font> {C["evidence_strength"]}'
           f'<font color="#6b7885">&nbsp;&nbsp;·&nbsp;&nbsp;<font size=8>{C["state_note"]}</font></font>')
    sl=Table([[Paragraph(sline,ParagraphStyle("sl",fontName="Sans",fontSize=9,leading=12))]],colWidths=[170*mm],
        style=TableStyle([("LINEABOVE",(0,0),(-1,0),0.6,RULE),("LINEBELOW",(0,0),(-1,0),0.6,RULE),("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),("LEFTPADDING",(0,0),(-1,-1),0)]))
    st+=[sl,Spacer(1,9),sub("THE RECORD — regime history",c=INK),state_band(C),Spacer(1,9),P(C["read"],size=9.5,lead=14)]
    st+=[Spacer(1,3),sub("FORWARD TESTS — pre-registered, counting down")]+ft_flow(C)
    st+=[sub("WHAT WOULD PROVE THIS WRONG")]+fals_flow(C)
    st+=[rule(RULE,0.5,8,3),P(f'Hash-committed before publication · verify {C["commit_url"]}',font="Sans",size=7,lead=9,color=MUTE),PageBreak()]

    # ===== PAGE 2 — THE THESIS (thesis-forward, evidence below) =====
    st+=[_runhdr(C),sechead("The thesis"),sub("Active reading  (≈70%)"),P(C["thesis_active"],size=9,lead=13.5),
         sub("Strongest opposing case  (≈20%)"),P(C["thesis_opposing"],size=9,lead=13.5),sub("Rejected alternatives  (≈10%)"),ltbl(C["rejected"],[55,115]),
         Spacer(1,9),sechead("The evidence"),ltbl(C["panel"],[58,40,34,38],rjust=(1,)),Spacer(1,5),sub("Inflation-regime axis"),ltbl(C["irs"],[58,40,34,38],rjust=(1,)),PageBreak()]

    # ===== PAGE 3 — METHOD | GOVERNANCE (editorial divider) =====
    st+=[_runhdr(C),sechead("Method"),sub("Coverage map — maturation: Observed → Monitored → Instrumented → Scored"),ltbl(C["coverage"],[110,60]),
         sub("Named blindspots"),P(C["blindspots"],size=8.6,lead=12.8),sub("Live forward tests")]+ft_flow(C,8.5)
    st+=[rule(INK,0.9,12,10),sechead("Governance"),sub("Layer status"),P(C["layer_status"],size=8.6,lead=12.8)]
    st+=[sub("Independent review — red-team, not user/subscriber feedback")]
    for fam,disp,concern in C["reviews"]:
        st+=[P(f'<font name="Sans-B">{fam}</font> — {disp}. Main concern: {concern}',size=8.6,lead=12.8,sa=2)]
    st+=[P(C["governance"],font="Sans-I",size=7.8,lead=11,color=MUTE,sa=2),P(f'Submit a challenge (classified under the challenge-intake taxonomy): {C["intake_email"]}',font="Sans-B",size=8,lead=11,color=GREY,sa=2),PageBreak()]

    # ===== PAGE 4 — APPENDIX A: AUDIT (durable; glossary sidebar) =====
    st+=[_runhdr(C),sechead("Appendix A — Audit"),P("For verification. Durable technical record; optional for ordinary readers.",font="Sans-I",size=7.6,lead=10,color=MUTE,sa=6)]
    audit_main=[sub("Locks & provenance",sb=0),ltbl([["Item","Value"]]+C["audit"],[38,66]),
                sub("Open challenges"),ltbl(C["open_challenges"],[16,24,22,21,21],pad=3),
                sub("Strongest outstanding challenge"),P(C["strongest_challenge"],size=8.4,lead=12.4)]
    gloss=[P('<font name="Sans-B" size=8 color="#6b7885">GLOSSARY</font>',size=8,sa=4)]
    for term,mean in C["glossary"]:
        gloss.append(P(f'<font name="Sans-B" size=7.8>{term}</font><br/><font size=7.6 color="#3b4652">{mean}</font>',size=7.8,lead=10,sa=5))
    two=Table([[audit_main,gloss]],colWidths=[118*mm,52*mm])
    two.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LINEAFTER",(0,0),(0,0),0.6,RULE),("BACKGROUND",(1,0),(1,0),TINT),
        ("LEFTPADDING",(0,0),(0,0),0),("RIGHTPADDING",(0,0),(0,0),12),("LEFTPADDING",(1,0),(1,0),8),("RIGHTPADDING",(1,0),(1,0),8),("TOPPADDING",(1,0),(1,0),8)]))
    st+=[two,rule(INK,0.8,10,4),
         P("Method: KRINO classifies macro regimes from public data under a fixed protocol — hypotheses and their falsifiers are "
           "hash-stamped before evaluation; thresholds frozen before validation; instruments adopted only after out-of-sample validation "
           "and independent review; every revision and defect logged.",font="Sans",size=7.4,lead=10,color=MUTE),
         P("Informational research only — not an offer, recommendation, or investment advice. Data: FRED / BLS / public markets. "
           "Report source-file sha256 committed to the public log before publication.",font="Sans",size=7.4,lead=10,color=MUTE)]

    def onpage(canvas,doc):
        canvas.saveState()
        if doc.page!=1:
            canvas.setFont("Serif-B",10); canvas.setFillColor(INK); canvas.drawString(20*mm,285*mm,"KRINO")
            canvas.setFont("Sans",7); canvas.setFillColor(MUTE); canvas.drawString(34*mm,285.5*mm,"MACRO-REGIME REPORT")
            tagr=f'No. {C["issue_no"]}'+(" · SPECIMEN" if C["specimen"] else "")
            canvas.drawRightString(190*mm,285.5*mm,tagr)
            canvas.setStrokeColor(RULE); canvas.setLineWidth(0.6); canvas.line(20*mm,283*mm,190*mm,283*mm)
        canvas.restoreState()
    global _FOOT; _FOOT=f'KRINO Macro-Regime Report · No. {C["issue_no"]}'+(" · SPECIMEN" if C["specimen"] else "")
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
    doc=BaseDocTemplate(C["out"],pagesize=A4,topMargin=16*mm,bottomMargin=18*mm,leftMargin=20*mm,rightMargin=20*mm,title=f"KRINO No. {C['issue_no']}",author="KRINO")
    doc.addPageTemplates([PageTemplate(id="main",frames=[Frame(doc.leftMargin,doc.bottomMargin,doc.width,doc.height,leftPadding=0,rightPadding=0,topPadding=6,bottomPadding=6,id="F")],onPage=onpage)])
    doc.build(st,canvasmaker=NumberedCanvas); print("wrote",C["out"])

def Draw_seal(s=11*mm):
    d=Drawing(s,s); d.add(Rect(0.6,0.6,s-1.2,s-1.2,strokeColor=INK,strokeWidth=1.1,fillColor=None))
    d.add(Line(s/2,s*0.17,s/2,s*0.83,strokeColor=INK,strokeWidth=0.9)); d.add(Line(s*0.17,s/2,s*0.83,s/2,strokeColor=INK,strokeWidth=0.9))
    d.add(Circle(s/2,s/2,s*0.058,fillColor=TEAL,strokeColor=None)); return d
seal=Draw_seal
def _runhdr(C): return P('',font="Sans",size=1,lead=2,sa=0)

if __name__=="__main__":
    build(CONTENT)
