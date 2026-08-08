#!/usr/bin/env python3
# KRINO WEEKLY ISSUE No005 — CONTENT block. Locked 4-page design inherited from 001-004 verbatim
# (r659: per-issue edits go into this inline copy; the locked renderer is not touched).
# Pilot state: strongest-contrary-observation section is at WEEK 4 OF 4 — the operator's ruling on
# whether it earns a permanent place is due at this issue (r634).
CONTENT = {
  "out": "/tmp/krino/publication/KRINO_WEEKLY_No005.pdf",
  "issue_no": "005", "date": "2026-08-08", "specimen": False,
  "publisher": "KRINO — published by A.G.",
  "data_cutoff": "markets 2026-08-05/06 mixed · claims week ending 2026-08-01 · inflation June 2026",
  "asof": "2026-08-08 · Saturday (the 1 August slot was not rendered — see below)",
  "reading_time": "≈ 4 minutes",
  "commit_url": "github.com/foxtrot76/krino-commitments", "intake_email": "krino.reviews@gmail.com",

  "headline": "The measured panel reached its softest reading of this window on every axis at once. Four surfaces the panel does not measure moved the other way in the same week.",
  "state_pair": [("Stress","CALM",False),("Inflation","WATCH",True)],
  "evidence_strength": "Low",
  "state_note": "inflation regime WATCH since 2026-03 — fifth live reading; June print unchanged",
  "read": ("Every measured part of the panel is at or near its calmest level of this observation window, and "
           "credit is the calmest part of it. The market-stress index reads −0.716 standard deviations, the "
           "21.6th percentile of 2018-onward history and a fourth consecutive easing; equity volatility is "
           "15.81; the high-yield credit gap is 1.10 against a 1.44 reference and the high-yield spread itself "
           "sits at 2.75 percent, its 15.4th percentile; the yield curve is +0.44 and not inverted; none of "
           "three leading indicators is flashing. "
           "Four surfaces the panel does not measure moved the other way across the same days. The equity index "
           "recorded a 252-session high of 7,736.52 on 4 August and then closed lower on both following "
           "sessions, to 7,709.96 on 6 August, so the high stands and was not extended. The tail-risk index retraced roughly three fifths of the collapse recorded last week, to "
           "134.73. Initial jobless claims printed 199,000 for the week ending 1 August, a third consecutive "
           "weekly rise from 189,000, with the prior week revised from 197,000 to 198,000. Foreign official "
           "custody holdings of United States Treasuries fell 25.5 billion dollars in the week to 5 August, to "
           "2,631.1 billion, after three consecutive issues recorded that series rising. "
           "This is the first week in this observation window in which the unmeasured surfaces and the measured "
           "panel point different ways. The panel governs the published state; the divergence is recorded rather "
           "than resolved. Between scheduled releases the published state moves only on the pre-registered "
           "falsifiers below — headlines and commentary, including this report's own, change nothing by "
           "themselves."),
  "sh_stress":    ['C','C','C','C','C','C','C','C','C','C','C','C','C'],
  "sh_inflation": ['N','N','N','N','N','N','N','W','W','W','W','W','W'],
  "sh_end": "2026-08",
  "forward_tests": [("Labour-slack sign","reg. 2026-06-23","gate date 2026-08-07 passed — NOT GRADED: the monthly employment series is not collected by this pipeline","blocked"),
                    ("Inflation-regime transition","live","next test: the August print, when the three-month window rolls","monthly"),
                    ("Haven inversion","reg. 2026-06-18","grades on the next genuine risk-off episode","event-driven")],
  "falsifiers": ["Jobless claims sustained above 300,000",
                 "Yield curve back below zero",
                 "High-yield credit through its divergence tripwire",
                 "Sixth straight month of consumer inflation at or above 4% year-over-year"],

  "thesis_active": ("A negotiated arrangement over the Strait of Hormuz is reported to be near, and its terms "
      "changed materially inside one week. On 5 August the reported terms included no transit fees. On 7 August "
      "the principal unresolved term was reported as a transit fee of 5 to 7 per cent of cargo value sought by "
      "Iran, against approximately 3 per cent proposed by Oman. The arrangement is unsigned. Both reports are on "
      "this project's record and neither has replaced the other; the contradiction is published rather than "
      "reconciled. A standing charge on cargo value at a chokepoint is a durable change in the cost of transit "
      "— a different object from a temporary closure, which resolves when the closure ends. That is the "
      "mechanism one of the competing explanations scored here names explicitly, and that explanation had been "
      "marked down the preceding week on price evidence. Confidence: PLAUSIBLE — the arrangement is unsigned, "
      "the fee figures are attributed to unnamed sources, and a prior arrangement was reported as near-final "
      "three weeks earlier and did not conclude."),
  "thesis_opposing": ("The strongest opposing case is that the panel is simply right and this issue is "
      "manufacturing significance out of four unrelated weekly movements. Custody holdings, jobless claims, an "
      "unextended index high and a retraced volatility index are noisy series, and any given week will produce "
      "four of them pointing somewhere. No statistical test here establishes that the co-movement is other than "
      "coincidence, and none is claimed."),
  "strongest_contrary": ("Required section, fourth and final week of the trial. (1) The strongest single "
      "observation against this report's reading is that the measured panel reached its softest level of the "
      "window on every axis simultaneously, and credit — the highest-quality signal family here — "
      "reached its tightest level of the window while the equity index sat within half a per cent of a record "
      "high. (2) It most benefits the reading that the underlying situation is not deteriorating and that this "
      "report's framework has been over-reading a benign environment. (3) The interpretation is retained for "
      "three stated reasons, each able to fail: the reported chokepoint arrangement is unsigned and its "
      "predecessor did not conclude; a transit fee of the reported size is a durable cost change rather than a "
      "temporary condition; and the four unmeasured surfaces named above moved against the panel in the same "
      "week. IDENTITY MISMATCH: YES — the observation named in (1) would give a competing reading more net "
      "support this period than the leading interpretation receives. Disclosed as a flag for the reader. It is "
      "not an automatic correction and it does not change the published state."),
  "rejected": [["Alternative","Rejected because"],
      ["Nothing is happening; premiums revert and the panel is correct throughout","A reported transfer of chokepoint control, and a fee of the reported size, are not consistent with an unchanged environment. Live."],
      ["Measured transit collapse overstates actual flow","The market body attributes reduced traffic to vessel-safety decisions — real vessels, not a measurement artefact. Live."],
      ["Price calm rests on an unexamined spare-capacity belief","An explicitly priced chokepoint is the opposite of an unexamined belief. Weakened this period."]],
  "panel": [["Signal","Reading","Threshold","Status"],
      ["Equity volatility (VIX)","15.81","< 20","calm (08-05)"],
      ["S&P 500","7,709.96","—","08-06; the 08-04 high of 7,736.52 stands, unextended"],
      ["Yield curve (10y − 2y)","+0.44","> 0","positive, not inverted (08-06)"],
      ["High-yield credit gap","1.10 divergence","< 1.44","benign; HY 2.75%, 15.4th pctile (08-05)"],
      ["Initial jobless claims","199,000","< 300k","third weekly rise (wk to 08-01)"],
      ["Market-stress index","−0.716 sd · 21.6th pctile","90th = elevated","fourth easing; equals window low (08-05)"]],
  "irs": [["Component","Value","Threshold","Fires"],
      ["Consumer inflation, year-over-year","3.53%","≥ 3%","yes"],["Consumer inflation, 3-month annualised","4.61%","≥ year-over-year rate","yes"],
      ["Months ≥ 4% year-over-year","1 of 6","6 to arm","no"],["Real policy rate","≈ +0.1%","≤ −1.0%","no"],
      ["Real-equity erosion","—","depressed","no"]],

  "coverage": [["Coverage area","Stage"],["Market stress — vol, credit, liquidity","Scored"],
      ["Inflation regime","Scored (live)"],["Labour slack","Scored"],["Commodity / energy shocks","Monitored"],
      ["Private credit","Watch"],["Geopolitics / chokepoints","Observed"]],
  "blindspots": ("Coverage first, measured rather than asserted. Forty-one data series are collected on each "
      "refresh. Of the readings this issue publishes, 41 of 41 numbers were verified against their source files "
      "by an automated check before publication, with zero mismatches — up from 33 at the previous issue. "
      "That check compares a published figure to the file it was derived from; it does not certify figures this "
      "project computes from those inputs. "
      "FOUR BLINDSPOTS, stated plainly. FIRST, and it is the largest remaining gap: quantities this project "
      "derives — drawdown depths, standardised scores, composite readings — are NOT verified against any "
      "external source. Named here rather than described as covered. SECOND, chokepoint transit counts are not "
      "collected on a fixed schedule; where this issue refers to transit volumes it relies on third-party "
      "reports with their own coverage limits. THIRD, monthly employment data is not collected by this pipeline "
      "at all, and one live forward test depends on it, so that test passed its gate date this week and could "
      "not be graded. The gap is stated rather than left implied, and no source has yet been established. "
      "FOURTH, the publication slot of 1 August was not rendered; the break is recorded rather than absorbed, "
      "this issue is numbered 005, and no issue has been renumbered or backdated. Standing limitations "
      "unchanged: energy supply shocks are monitored but not scored; private-credit stress is not visible in "
      "public spreads and is watched, not scored."),
  "layer_status": ("Validated (shown as validated): market-stress axis; inflation-regime axis. Provisional — "
      "under evaluation: the multi-thesis interpretation layer (dual-read shown for transparency; promoted "
      "only when its validator is operational and the evaluation phase clears)."),
  "reviews": [("No external round this period","the last completed red-team round closed 2026-07-29","no outside review was run on this issue's analytical content. A governance rule adopted this week is marked, by this project's own trigger list, as requiring a review round before it takes effect; that round has not been held. The rule is labelled provisional and is not enforced as a gate. Disclosed here rather than reported at a later date"),
              ("Correction carried this period","an evidence item entered last week on a single day's movement in a tail-risk index","the index retraced roughly three fifths of that movement within two sessions and the item was re-graded. The convention requiring more than one observation had been applied to a competing explanation and not to this project's own entry. The correction is visible in the record")],
  "governance": ("Published state never moves on review count. Challenges are logged; the state changes only on "
      "a pre-registered falsifier. Resolved this period: a pre-registered adjudication that had been reported as "
      "blocked by a nine-day data outage was found to be blocked by a posting lag instead — the series "
      "resumed and backfilled five observations, the adjudication was run, and its price criterion was met while "
      "its transit criterion could not be verified from any source this project collects. The disposition is "
      "held rather than declared. A rule was adopted requiring that any claim that something is unobservable or "
      "unavailable carry a revalidation date and a named re-test."),

  "audit": [["Understanding-model lock","v15  8d4515ed"],["Thesis ontology (frozen)","v1.0  ff5466c3"],
      ["Frozen fixtures","v2  68e56f0a"],
      ["Data bundle for this issue","pulled 2026-08-07 13:54–13:55 CEST, read from the archive's internal timestamps"],
      ["Source verification","41 of 41 published numbers matched to source, 0 mismatches"],
      ["Commitment log","github.com/foxtrot76/krino-commitments"]],
  "open_challenges": [["ID","Challenge","Opened","Status","Severity"],
      ["CH-010","Forward tests are weaker than the hypothesis machinery that feeds them","2026-08-02","Open — raised by an outside reviewer","High"],
      ["CH-009","Project may be over-inspecting its own tools while the forecast clock stands still","2026-07-25","Open in part — remedy deferred to the October review","High"],
      ["CH-003","Rules written to address attention decay may themselves fail under load","2026-07-20","Open — discriminating probe pre-registered for 1 October","Med"],
      ["CH-001","Live inflation axis unvalidated (n=1)","2026-07-06","Open — its adjudicating print is blocked; see Method","Med"],
      ["+1 more","CH-002 — see the challenge log","—","Logged","—"]],
  "strongest_challenge": ("That the panel is simply right and this issue is manufacturing significance from four "
      "unrelated weekly movements. It is the same charge stated on page 2 as the opposing case, and it is "
      "repeated here because it is also the strongest challenge to the report as a whole this period rather than "
      "to one section of it: this report has a stronger mechanism for generating and comparing explanations than "
      "for proving that its forward tests can genuinely fail. Two of the three live tests are blocked or "
      "event-driven, and the third grades monthly. Open — remedy outstanding."),
  "glossary": [["Divergence tripwire","The high-yield vs BB spread gap that would signal credit stress (1.44)."],
      ["Drawdown","The fall from a recent peak, expressed as a percentage."],
      ["Falsifier","A pre-registered condition that, if met, moves the published state."],
      ["Percentile","Where a reading sits within its own history; the 20th percentile means 80% of past readings were higher."],
      ["Standard deviation","A measure of how far a reading sits from its own average."]],
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
