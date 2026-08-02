#!/usr/bin/env python3
# KRINO WEEKLY ISSUE No004 — CONTENT block (locked 4-page design inherited from 001/002/003 verbatim,
# plus the two round-adopted additions that render here for the first time: the serial-correlation
# caveat beside the panel readings (r636, VERBATIM-REQUIRED) and the strongest-contrary-observation
# section (r634, four-week pilot, week 2 of 4).
CONTENT = {
  "out": "/tmp/krino/publication/KRINO_WEEKLY_No004.pdf",
  "issue_no": "004", "date": "2026-08-02", "specimen": False,
  "publisher": "KRINO \u2014 published by A.G.", "data_cutoff": "markets 2026-07-31/30 mixed \u00b7 inflation June 2026",
  "asof": "2026-08-02 \u00b7 Sunday (the 1 August slot fell on the Swiss national holiday)", "reading_time": "\u2248 4 minutes",
  "commit_url": "github.com/foxtrot76/krino-commitments", "intake_email": "krino.reviews@gmail.com",

  "headline": "Shipping through the Strait of Hormuz fell to its lowest level of the crisis. Crude fell with it.",
  "state_pair": [("Stress","CALM",False),("Inflation","WATCH",True)],
  "evidence_strength": "Low",
  "state_note": "inflation regime WATCH since 2026-03 \u2014 fifth live reading",
  "read": ("Market-stress regime unchanged and calm, and this week the calm deepened. Equity volatility fell "
           "from 20.66 to 17.09 in a single session, reversing a spike that was larger on the way up than "
           "anything else in this window; the S&P 500 rose 1.0 percent on the week to 7,489.72 and its "
           "twelve-month drawdown narrowed to 1.6 percent; the yield curve steepened again to +0.47, further "
           "from inversion for a third consecutive report; the high-yield credit gap sits at 1.10 against a "
           "1.44 tripwire and both of its legs narrowed. Jobless claims printed 197,000 for the week ending "
           "25 July, and the four-week average fell to 202,750 from 222,500 a month earlier. "
           "The physical picture moved the other way and moved hard: naval reporting put crossings of the "
           "Strait of Hormuz down 52 percent week-on-week, in single digits per day, the lowest since the "
           "conflict began in March; Red Sea transits fell to 225 from 311; the war-risk insurance zone was "
           "extended; and around fifty nations convened in Riyadh on a maritime coalition, fourteen pledging "
           "support. Crude did not follow. The settled Brent series fell from $100.31 to $91.82 across the "
           "same window. Between scheduled releases the published state moves only on the pre-registered "
           "falsifiers below \u2014 headlines and commentary, including this report's own, change nothing by "
           "themselves."),
  "sh_stress":    ['C','C','C','C','C','C','C','C','C','C','C','C','C'],
  "sh_inflation": ['N','N','N','N','N','N','N','W','W','W','W','W','W'],
  "sh_end": "2026-08",
  "forward_tests": [("Labour-slack sign","reg. 2026-06-23","grades 2026-08-07","in 5 days"),
                    ("Inflation-regime transition","live","next test: August print (3-month window rolls)","monthly"),
                    ("Coalition-response explanation","proposed 2026-08-01","WITHDRAWN before registration \u2014 see below","not registered")],
  "falsifiers": ["Jobless claims sustained above 300,000",
                 "Yield curve back below zero",
                 "High-yield credit through its divergence tripwire",
                 "Sixth straight month of consumer inflation at or above 4% year-over-year"],

  "thesis_active": ("The observation this period is the same disagreement as last period, wider and with the "
      "sign reversed on one side. The scored financial panel is not merely failing to confirm the physical "
      "picture \u2014 it is moving away from it. Volatility fell, equities rose, the curve steepened further "
      "from inversion, and both legs of the credit instrument narrowed, so the gap that would signal "
      "transmission is 1.10 against a 1.44 tripwire and has not reached that tripwire since April 2025. "
      "Against that, the physical measures reached their worst readings of the crisis. The report's standing "
      "explanation is that transmission is lagged or masked rather than absent; that explanation remains the "
      "least-contradicted of the eight the report scores, and the explanation that nothing unusual is "
      "happening remains the most contradicted by a wide margin."),
  "thesis_opposing": ("The strongest opposing case is now stronger than it was, and it comes from the energy "
      "market itself. If a supply chokepoint tightens to its worst level of a crisis and the price of what "
      "passes through it falls, the simplest reading is that the disruption is being absorbed \u2014 by "
      "rerouting, by consolidation onto fewer larger cargoes, by inventory, or by the expectation that the "
      "announced coalition will restore passage. Saudi cargoes rerouting through Suez at longer voyage times "
      "are adaptation observed and dated. A reader who concluded that the physical readings describe a "
      "logistics problem rather than a financial one would be reading the scored panel correctly, and would "
      "have the price on their side this period."),
  "strongest_contrary": ("Required section, second of a four-week trial. (1) The strongest single "
      "observation against this report's reading is that the settled crude price FELL, from $100.31 to "
      "$91.82, across the same days in which shipping through the strait reached its lowest level of the "
      "crisis. (2) It most supports the competing explanation that the disruption is being absorbed "
      "rather than transmitted. (3) The interpretation is retained this period for one stated reason: "
      "the settled price series publishes with a multi-day lag and last printed for 27 July, while the "
      "timely front-month contract rose over the following days to $90.12 \u2014 the two instruments may "
      "be on different clocks rather than in disagreement. That is a reason to wait one week, not a "
      "rebuttal. If next week's settled price confirms sub-$90 while transits stay at these levels, the "
      "energy channel of this reading has a real problem and this section will say so."),
  "rejected": [["Alternative","Rejected because"],
      ["Acute market-stress regime","Volatility 17.09, curve +0.47, credit gap 1.10 against a 1.44 tripwire \u2014 no scored stress"],
      ["Inflation regime confirmed","One of six qualifying months; June printed 3.53%, below the 4% bar"],
      ["All-clear / watch retired","Transits at their crisis low and the war-risk zone extended; the scored panel is calm but the physical picture is not, and the divergence is what the report is tracking"]],
  "panel": [["Signal","Reading","Threshold","Status"],
      ["Equity volatility (VIX)","17.09","< 20","calm, \u22128.6% on week"],["S&P 500","7,489.72","\u2014","+1.0% on week"],
      ["Yield curve (10y \u2212 2y)","+0.47","> 0","positive, steepening"],
      ["High-yield credit gap","1.10 divergence","< 1.44","benign, both legs narrowed"],
      ["Initial jobless claims","197,000","< 300k","4-week average falling"],
      ["Market-stress index","44th percentile","90th = elevated","below bands"]],
  "irs": [["Component","Value","Threshold","Fires"],
      ["Consumer inflation, year-over-year","3.53%","\u2265 3%","yes"],["Consumer inflation, 3-month annualised","4.61%","\u2265 year-over-year rate","yes"],
      ["Months \u2265 4% year-over-year","1 of 6","6 to arm","no"],["Real policy rate","\u2248 +0.1%","\u2264 \u22121.0%","no"],
      ["Real-equity erosion","\u2014","depressed","no"]],

  "coverage": [["Coverage area","Stage"],["Market stress \u2014 vol, credit, liquidity","Scored"],
      ["Inflation regime","Scored (live)"],["Labour slack","Scored"],["Commodity / energy shocks","Monitored"],
      ["Private credit","Watch"],["Geopolitics / chokepoints","Observed"]],
  "blindspots": ("Two disclosures this period, both measured rather than asserted. FIRST, a sensitivity test on "
      "this report's own weighting. Evidence is graded in tiers: official data and market prints carry double "
      "the weight of independent journalism, and state communications carry none. The competing-explanation "
      "scoreboard behind this issue was re-run with every journalism-sourced item deleted \u2014 46 percent of "
      "the items and 30 percent of the evidence weight. The leading explanation is unchanged and the "
      "\u2018nothing unusual is happening\u2019 explanation remains the worst-supported by a wide margin, so the "
      "tension this issue describes is not an artifact of how sources are weighted. What does change is "
      "discriminating power: without journalism, four explanations tie at the top instead of two, and the "
      "board can no longer separate its own leading candidates. Read the ranking below first place as weakly "
      "held. One consequence is disclosed rather than buried \u2014 the second-place explanation changes "
      "identity under this test, and the physical-inventory instrument this project has prioritised building "
      "was chosen to separate the full-weight pair, not the journalism-free one. SECOND, a known limitation "
      "carried openly while it is being reworked: the tier scheme conflates the CLASS of a source with the "
      "WEIGHT of the evidence it supplies, so a rigorous piece of journalism and a thin one score alike. "
      "The rework is decided and not yet built. Standing limitations unchanged: energy supply shocks "
      "monitored but not scored; private-credit stress not visible in public spreads and watched, "
      "not scored."),
  "layer_status": ("Validated (shown as validated): market-stress axis; inflation-regime axis. Provisional \u2014 "
      "under evaluation: the multi-thesis interpretation layer (dual-read shown for transparency; promoted "
      "only when its validator is operational and the evaluation phase clears)."),
  "reviews": [("OpenAI","hypothesis-grading and forward-test reviews","rejected this period's proposed forward test as unmeasurable \u2014 an absence of reporting is not an absence of activity \u2014 and refused to let a self-disconfirming idea be deleted from the record of how well the generator performs"),
              ("DeepSeek","hypothesis-grading and forward-test reviews","refused the same forward test in stronger terms \u2014 a test that cannot fail honestly is not a test \u2014 and rejected an eight-week deadline chosen by judgement rather than derived")],
  "governance": ("Published state never moves on review count. Challenges are logged; the state changes only on "
      "a pre-registered falsifier. Resolved this period: a proposed forward test was WITHDRAWN before "
      "registration on the unanimous verdict of both outside reviewers \u2014 the second withdrawal on this "
      "subject \u2014 and the explanation it would have tested is published here carrying no credit and no "
      "test. A rule was adopted requiring that an idea killed by its own check at generation still be counted "
      "against the generator's record rather than erased from it."),

  "audit": [["Understanding-model lock","v15  8d4515ed"],["Thesis ontology (frozen)","v1.0  ff5466c3"],
      ["Inflation Regime Sensor","r297 \u2014 frozen"],["Commitment log","github.com/foxtrot76/krino-commitments"]],
  "open_challenges": [["ID","Challenge","Opened","Status","Severity"],
      ["CH-010","Forward tests are weaker than the hypothesis machinery that feeds them","2026-08-02","Open \u2014 raised by an outside reviewer","High"],
      ["CH-009","Project may be over-inspecting its own tools while the forecast clock stands still","2026-07-25","Open \u2014 remedy deferred to Oct review","High"],
      ["CH-008","Grade changed on a single weekly reading; rating asymmetry favoured the leader","2026-07-23","Resolved 30 Jul \u2014 demotion permanent","Med"],
      ["CH-001","Live inflation axis unvalidated (n=1)","2026-07-06","Open \u2014 adjudicating","Med"],
      ["+3 more","CH-002, CH-006, CH-007 \u2014 see the challenge log","\u2014","Logged","\u2014"]],
  "strongest_challenge": ("From an outside reviewer this period, quoted because the paraphrase would soften it: "
      "this project has a much stronger mechanism for generating and comparing explanations than for proving "
      "that its forward tests can genuinely fail. The charge is specific rather than general \u2014 it was made "
      "about the forward test proposed this week, which both reviewers then refused, and it is the second "
      "test on the same subject to be withdrawn before registration. The generating side of this project is "
      "further along than the testing side, and the testing side is the side that decides whether any of it "
      "was right. Open \u2014 remedy outstanding."),
  "glossary": [["WATCH","An inflationary configuration flagged, not a confirmed regime."],
      ["Arms the regime","Meets the count needed to confirm a regime (6 months \u2265 4%)."],
      ["Divergence tripwire","The high-yield vs BB spread gap that would signal credit stress (1.44)."],
      ["Falsifier","A pre-registered condition that, if met, moves the state."],
      ["Withdrawn before registration","A proposed test discarded because no outcome could have proved it wrong."]],
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
    # r618/operator 2026-07-25: the forward-test block rendered on BOTH page 1 and page 3 —
    # identical lines, inherited from 001 and shipped that way in 001 and 002 before anyone
    # read the two pages side by side. Page 3 keeps it (operator ruling); page 1 drops it.
    st+=[sub("Strongest observation against this reading"),P(C["strongest_contrary"],size=8.2,lead=12.2)]
    st+=[sub("WHAT WOULD PROVE THIS WRONG")]+fals_flow(C)
    st+=[rule(RULE,0.5,8,3),P(f'Hash-committed before publication · verify {C["commit_url"]}',font="Sans",size=7,lead=9,color=MUTE),PageBreak()]

    # ===== PAGE 2 — THE THESIS (thesis-forward, evidence below) =====
    st+=[_runhdr(C),sechead("The thesis"),sub("Active reading  (≈70%)"),P(C["thesis_active"],size=9,lead=13.5),
         sub("Strongest opposing case  (≈20%)"),P(C["thesis_opposing"],size=9,lead=13.5),sub("Rejected alternatives  (≈10%)"),ltbl(C["rejected"],[55,115]),
         Spacer(1,9),sechead("The evidence"),ltbl(C["panel"],[58,40,34,38],rjust=(1,)),Spacer(1,3),P("<i>On repeated readings.</i> The panel is re-read each week, but its signals track slow-moving conditions. A reading that persists across several issues is therefore largely the same observation restated, not a series of independent confirmations \u2014 and a longer streak is not stronger evidence. Where this issue cites a run of consecutive readings, read it as duration, not as accumulation.",size=7.6,lead=11,color=MUTE),Spacer(1,5),sub("Inflation-regime axis"),ltbl(C["irs"],[58,40,34,38],rjust=(1,)),PageBreak()]

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
