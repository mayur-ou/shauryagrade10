"""Shaurya tracker: single data source -> db documents (JSON) + markdown backup."""
import json, os, sys

OUT = sys.argv[1]
UPDATED = "2026-11-11"

def ch(num, title, sections=None, status="revised", score=None, mx=None, tested_in="", note="", unit=None):
    d = {"num": str(num), "title": title, "sections": sections or [], "status": status,
         "score": score, "max": mx, "testedIn": tested_in, "note": note}
    if unit: d["unit"] = unit
    return d

# ---------------- PHYSICS ----------------
P = [
 ch(1,"Making measurements",["Measuring length and volume","Density","Measuring time"],"tested",6,8,"RT1"),
 ch(2,"Describing motion",["Understanding speed","Distance–time graphs","Understanding acceleration","Calculating speed and acceleration"],"tested",4,6,"RT1"),
 ch(3,"Forces and motion",["We have lift-off","Mass, weight and gravity","Falling and turning","Force, mass and acceleration","Momentum","More about scalars and vectors"],"tested",18,19,"RT1"),
 ch(4,"Turning effects",["The moment of a force","Calculating moments","Stability and centre of gravity"],"tested",4,5,"RT1"),
 ch(5,"Forces and matter",["Forces acting on solids","Stretching springs","The limit of proportionality and the spring constant","Pressure","Calculating pressure"],"tested",9,9,"RT1"),
 ch(6,"Energy stores and transfers",["Energy stores","Energy transfers","Conservation of energy","Energy calculations"],"tested",12,12,"RT3"),
 ch(7,"Energy resources",["The energy we use","Energy from the Sun"],"tested",8,10,"RT3"),
 ch(8,"Work and power",["Doing work","Calculating work done","Power","Calculating power"],"tested",8,9,"RT3"),
 ch(9,"The kinetic particle model of matter",["States of matter","The kinetic particle model of matter","Gases and the kinetic model","Temperature and the Celsius scale","The gas laws"],"tested",6,9,"RT3","Weakest chapter: gas-pressure explanations."),
 ch(10,"Thermal properties of matter",["Thermal expansion","Specific heat capacity","Changing state"],"tested",24,28,"RT5, RT6","RT5: 9/17 (53%). RT6 tested Ch 10–11 together: 24/28 (86%)."),
 ch(11,"Thermal energy transfers",["Conduction","Convection","Radiation","Consequences of thermal energy transfer"],"tested",24,28,"RT6","Tested together with Ch 10 (combined score)."),
 ch(12,"Sound",["Making sounds","How does sound travel?","The speed of sound","Seeing and hearing sounds"],"tested",10,13,"RT2"),
 ch(13,"Light",["Reflection of light","Refraction of light","Total internal reflection","Lenses","Dispersion of light"],"tested",13,14,"RT2"),
 ch(14,"Properties of waves",["Describing waves","Speed, frequency and wavelength","Explaining wave phenomena"],"tested",10,13,"RT2"),
 ch(15,"The electromagnetic spectrum",["Electromagnetic waves","Electromagnetic hazards","Communicating using electromagnetic waves"],"tested",9,11,"RT6"),
 ch(16,"Magnetism",["Permanent magnets","Magnetic fields"],"tested",8,11,"RT6","16.2 Magnetic fields also in RT4."),
 ch(17,"Static electricity",["Charging and discharging","Explaining static electricity","Electric fields"],"missing",None,None,"RT4","RT4 taken 24 Oct, score not recorded."),
 ch(18,"Electrical quantities",["Current in electric circuits","Voltage in electric circuits","Electrical resistance","More about electrical resistance","Electrical energy, work and power"],"missing",None,None,"RT4","RT4 taken 24 Oct, score not recorded."),
 ch(19,"Electrical circuits",["Circuit components","Combinations of resistors","Electrical safety"],"missing",None,None,"RT4","RT4 (incl. 19.3 electrical safety), score not recorded."),
 ch(20,"Electromagnetic forces",["The magnetic effect of a current","Force on a current-carrying conductor","Electric motors","Beams of charged particles and magnetic fields"],"missing",None,None,"RT4","RT4 covered 20.1–20.3; score not recorded."),
 ch(21,"Electromagnetic induction",["Generating electricity","Power lines and transformers","How transformers work"],"revised",None,None,"","Revised by 26 Oct. Not in any test yet."),
 ch(22,"The nuclear atom",["Atomic structure","Protons, neutrons and electrons"],"revised",None,None,"","Revised by 26 Oct. Not in any test yet."),
 ch(23,"Radioactivity",["Radioactivity all around us","Radioactive decay","Activity and half-life","Using radioisotopes"],"tested",15,17,"RT5"),
 ch(24,"Earth and the Solar System",["Earth, Sun and Moon","The Solar System"],"tested",8,8,"RT5"),
 ch(25,"Stars and the Universe",["The Sun","Stars and galaxies","The Universe"],"tested",7,8,"RT5"),
]

# ---------------- CHEMISTRY ----------------
LOST = "Chapter test from mid-Oct was lost with a deleted chat."
C = [
 ch(1,"States of matter",["Everything is made of particles","Solids, liquids, and gases","The particles in solids, liquids, and gases","Heating and cooling curves","A closer look at gases"],"revised",note=LOST),
 ch(2,"Atoms and elements",["Meet the elements","More about atoms","How electrons are arranged","Isotopes and Ar","How our model of the atom developed"],"revised",note=LOST),
 ch(3,"Atoms combining",["Compounds, mixtures, and chemical change","Why do atoms form bonds?","The ionic bond","More about ions","The covalent bond","Covalent compounds","Comparing ionic and covalent compounds","Giant covalent structures","The bonding in metals"],"revised",note="Board paper 20 Oct: bonding and structure lost 3 marks. "+LOST),
 ch(4,"Reacting masses, and chemical equations",["The names and formulae of compounds","Equations for chemical reactions","The masses of atoms, molecules, and ions","Calculations about mass and %"],"tested",3,3,"RT 8 Oct"),
 ch(5,"Using moles",["The mole","Calculations from equations","Reactions involving gases","The concentration of a solution","Finding the empirical formula","From empirical to final formula","Finding % yield and % purity"],"tested",13,14,"RT 8 Oct"),
 ch(6,"Redox reactions",["Oxidation and reduction","Redox and electron transfer","Redox and oxidation numbers","Oxidising and reducing agents"],"tested",8,11,"RT 8 Oct"),
 ch(7,"Electricity and chemical change",["Conductors and non-conductors","The principles of electrolysis","The reactions at the electrodes","Electroplating"],"revised",note=LOST),
 ch(8,"Energy changes in reactions",["Energy changes in reactions","A closer look at energy changes","Calculating enthalpy changes","The hydrogen–oxygen fuel cell"],"revised",note=LOST),
 ch(9,"The rate of reaction",["Introducing reaction rates","Measuring the rate of a reaction","Changing the rate (part I)","Changing the rate (part II)","Explaining rate changes","Catalysts","More about enzymes"],"revised",note="Board paper 20 Oct: rate lost 1 mark. "+LOST),
 ch(10,"Reversible reactions and equilibrium",["Reversible reactions","Shifting the equilibrium","The Haber process","The Contact process"],"revised",note="Board paper 20 Oct: Haber vs Contact conditions lost 2 marks. "+LOST),
 ch(11,"Acids, bases, and salts",["Acids and bases","A closer look at acids and alkalis","The reactions of acids and bases","A closer look at neutralisation","Oxides","Making salts (part I)","Making salts (part II)","Finding concentration by titration"],"revised",note=LOST),
 ch(12,"The Periodic Table",["The Periodic Table: an overview","Group I: the alkali metals","Group VII: the halogens","More about the trends","The transition elements","How the Periodic Table developed"],"revised",note=LOST),
 ch(13,"The behaviour of metals",["Comparing metals and non-metals","Comparing metals for reactivity","Metals in competition","The reactivity series","The rusting of iron"],"tested",4,7,"RT 8 Oct","Weak: MgO from steam, Al oxide layer, CuSO4 colour change."),
 ch(14,"Extracting and using metals",["Metal ores and metal extraction","Extracting iron","Extracting aluminium","Making use of metals","Alloys","Metals, civilisation, and you"],"tested",7,11,"RT 8 Oct","Weak: blast-furnace limestone, alloys, sacrificial zinc."),
 ch(15,"Chemistry of the environment",["Our environment and us","What is in river water?","Our water supply","Fertilisers","Air, the gas mixture we live in","Air pollution from fossil fuels","Two greenhouse gases","Tackling climate change"],"revised",note="Board paper 20 Oct: environment / photosynthesis lost 2 marks. "+LOST),
 ch(16,"Organic chemistry",["Petroleum: a fossil fuel","Refining petroleum","Four families of organic compounds","The alkanes","Cracking alkanes","The alkenes","The alcohols","The carboxylic acids"],"revised",note="Biggest loss on the 20 Oct board paper: 9 marks. "+LOST),
 ch(17,"Polymers",["Introducing polymers","Addition polymerisation","Condensation polymerisation","Plastics","The plastics problem","Tackling the plastics problem","Proteins"],"revised",note=LOST),
 ch(18,"Separation and purification",["Making a substance in the lab","Solutions and solubility","Separating a solid from a liquid","Separating by distillation","Paper chromatography (part I)","Paper chromatography (part II)","Checking purity","The chromatography detectives"],"revised",note=LOST),
 ch(19,"Experiments and tests in the lab",["The scientific method, and you","Writing up an experiment","Preparing, and testing, gases","Testing for cations","Testing for anions"],"revised",note=LOST+" Paper 6 practical not attempted."),
]

# ---------------- MATHS ----------------
MDONE = "Finished by 18 Oct. No test score in the record."
M = [
 ch(1,"Number 1",["Arithmetic","Negative numbers","Number facts","Sequences","Approximations and estimation","Indices 1","Standard form","Surds","Calculator"],note=MDONE),
 ch(2,"Algebra 1",["Substitution","Brackets and simplifying","Solving linear equations","Problems solved by linear equations","Simultaneous equations","Problems solved by simultaneous equations"],note=MDONE),
 ch(3,"Number 2",["Ratio and proportion","Map scales","Percentages","Financial mathematics","Time","Rates"],note="Known weak spots: reverse percentages (3.3), compound interest (3.4). "+MDONE),
 ch(4,"Trigonometry 1",["Pythagoras' theorem","Trigonometry","Bearings","Angles of elevation and depression","Scale drawing","Three-dimensional trigonometry"],note=MDONE),
 ch(5,"Mensuration",["Area","The circle","Arc length and sector area","Chords and segments","Volume","Surface area","Similarity"],note="Known weak spot: scale factors k, k², k³ (5.7 Similarity). "+MDONE),
 ch(6,"Algebra 2",["Factorising","Quadratic equations","Solving problems using quadratic equations","Nonlinear simultaneous equations"],note=MDONE),
 ch(7,"Geometry",["Angles","Symmetry","Circle theorems","Constructions","Nets"],note=MDONE),
 ch(8,"Algebra 3",["Algebraic fractions","Changing the subject of a formula","Proportion","Indices 2","Inequalities"],note=MDONE),
 ch(9,"Graphs",["Drawing linear graphs","Coordinate geometry","Equations of straight lines","Plotting curves","Interpreting graphs","Graphical solutions of equations","Differentiation"],note=MDONE),
 ch(10,"Trigonometry 2",["Sine, cosine and tangent for any angle","The sine rule","The cosine rule"],note=MDONE),
 ch(11,"Sets and functions",["Sets","Logical problems","Functions","Composite and inverse functions"],note=MDONE),
 ch(12,"Vectors and transformations",["Vectors","Column vectors","Vector geometry","Simple transformations","Combined transformations"],"confirm",note="The 18 Oct record said Vectors was the one topic still pending. Confirm whether it is done."),
 ch(13,"Statistics",["Pictograms, bar charts and pie charts","Averages and spread","Stem-and-leaf, frequency polygons and histograms","Scatter diagrams","Cumulative frequency","Comparing data sets"],note=MDONE),
 ch(14,"Probability",["Simple probability","Relative frequency","Mutually exclusive and independent events","Tree diagrams","Probability from Venn diagrams","Conditional probability"],note=MDONE),
]

# ---------------- ICT ----------------
RT1 = "RT1 tested Ch 1–4 together (group score)."
I = [
 ch(1,"Types and components of computer systems",["Hardware and software","Main components of computer systems","Operating systems","Types of computer","Emerging technologies"],"tested",48,50,"RT1",RT1,unit="Section 1 · Theory"),
 ch(2,"Input and output devices",["Input devices and their uses","Direct data entry (DDE) devices","Output devices and their uses"],"tested",48,50,"RT1",RT1,unit="Section 1 · Theory"),
 ch(3,"Storage devices and media",["Magnetic media and magnetic storage devices","Optical media and optical storage devices","Solid-state media and solid-state storage devices","The future of storage devices"],"tested",48,50,"RT1",RT1,unit="Section 1 · Theory"),
 ch(4,"Networks and the effects of using them",["Networks","Network issues and communication"],"tested",48,50,"RT1",RT1+" Lost 1 mark: internet vs intranet wording.",unit="Section 1 · Theory"),
 ch(5,"The effects of using IT",["Microprocessor-controlled devices","Potential health problems related to the prolonged use of ICT equipment"],"tested",8,8,"RT2",unit="Section 1 · Theory"),
 ch(6,"ICT applications",["Communication","Modelling applications","Computer controlled systems","School management systems","Booking systems","Banking systems","Computers in medicine","Expert systems","Computers in the retail industry","Recognition systems","Satellite systems"],"tested",26,27,"RT2","Lost 1 mark: batch processing consequence.",unit="Section 1 · Theory"),
 ch(7,"The systems life cycle",["Analysis","Design","Development and testing","Implementation","Documentation","Evaluation"],"tested",13,13,"RT2",unit="Section 1 · Theory"),
 ch(8,"Safety and security",["Physical security","E-safety","Security of data"],"tested",14,15,"RT2",unit="Section 1 · Theory"),
 ch(9,"Audiences",["Audience appreciation","Copyright"],"tested",8,8,"RT2",unit="Section 1 · Theory"),
 ch(10,"Communication",["Communication with other ICT users using email","Effective use of the internet"],"tested",8,9,"RT2","Lost 1 mark: social-networking discussion conclusion.",unit="Section 1 · Theory"),
]
for n,t,s in [(11,"File management",["Manage files effectively","Reduce file sizes for storage or transmission"]),
              (12,"Images",["Software tools","Edit an image"]),
              (13,"Layout",["Create or edit a document","Tables","Headers and footers"]),
              (14,"Styles",["Corporate house styles","Create, modify, update and apply consistent styles"]),
              (15,"Proofing",["Software tools","Proofing techniques"]),
              (16,"Graphs and charts",["Chart types","Create a chart","Label a chart","Use secondary axes"]),
              (17,"Document production",["Organise page layout","Format text"]),
              (18,"Databases",["Create a database structure","Manipulate data","Present data"]),
              (19,"Presentations",["Create a presentation","Use a master slide","Edit a presentation","Output a presentation"]),
              (20,"Spreadsheets",["Create a data model","Manipulate data","Present data"]),
              (21,"Website authoring",["Web development layers","Create a web page","Use stylesheets"])]:
    I.append(ch(n,t,s,"notstarted",note="Practical chapter (Papers 2 and 3).",unit="Section 2 · Practical"))

# ---------------- BUSINESS ----------------
B = []
units = [
 ("Section 1 · Understanding business activity",[(1,"Business activity"),(2,"Economic sectors"),(3,"Enterprise, business growth and size"),(4,"Types of business organisations"),(5,"Business objectives and stakeholder objectives")]),
 ("Section 2 · People in business",[(6,"Human resource management (HRM)"),(7,"Organisation and management"),(8,"Methods of communication"),(9,"Motivating employees")]),
 ("Section 3 · Marketing",[(10,"Marketing and the market"),(11,"Market research"),(12,"Marketing mix: product"),(13,"Marketing mix: price"),(14,"Marketing mix: place"),(15,"Marketing mix: promotion"),(16,"Marketing strategy and legal controls")]),
]
for u, chs in units:
    for n,t in chs:
        B.append(ch(n,t,[],"unknown",note="No revision or test recorded yet.",unit=u))
U4,U5,U6 = "Section 4 · Operations management","Section 5 · Financial information and decisions","Section 6 · External influences on business activity"
q1 = "RT1 Q1 (Kaveri Cycles) covered Ch 17, 19 and 20: 16/20."
B += [
 ch(17,"Production of goods and services",[],"tested",16,20,"RT1",q1,unit=U4),
 ch(18,"Costs, scale of production and break-even analysis",[],"tested",17,20,"RT1","RT1 Q2 (Spice Route Foods): 17/20.",unit=U4),
 ch(19,"Quality of goods and services",[],"tested",16,20,"RT1",q1,unit=U4),
 ch(20,"Location decisions",[],"tested",16,20,"RT1",q1,unit=U4),
 ch(21,"Business finance",[],"tested",16,20,"RT1","RT1 Q3 (Tara Tech) covered Ch 21–22: 16/20.",unit=U5),
 ch(22,"Cash flow forecasts",[],"tested",16,20,"RT1","RT1 Q3 (Tara Tech) covered Ch 21–22: 16/20.",unit=U5),
 ch(23,"Statement of profit or loss",[],"tested",19,20,"RT1","RT1 Q4 (Meridian Stores) covered Ch 23–25: 19/20.",unit=U5),
 ch(24,"Statement of financial position",[],"tested",19,20,"RT1","RT1 Q4 (Meridian Stores) covered Ch 23–25: 19/20.",unit=U5),
 ch(25,"Analysis of accounts",[],"tested",19,20,"RT1","RT1 Q4 (Meridian Stores) covered Ch 23–25: 19/20.",unit=U5),
 ch(26,"Economic issues",[],"pending",note="RT2 set 7 Nov, not attempted.",unit=U6),
 ch(27,"Business and the international economy",[],"pending",note="RT2 set 7 Nov, not attempted.",unit=U6),
 ch(28,"Environmental and ethical issues",[],"pending",note="RT2 set 7 Nov, not attempted.",unit=U6),
 ch(29,"Preparing for assessment",[],"pending",note="RT2 Q4 includes an exam-technique task.",unit="Final chapter"),
]

# ---------------- ENGLISH ----------------
E = [
 ch("A","Text A questions",["Short-answer comprehension","Own-words explanations"],"notstarted",note="No graded Text A work recorded yet.",unit="Paper 1 · Reading"),
 ch("B","Text B questions",[],"notstarted",note="No graded Text B work recorded yet.",unit="Paper 1 · Reading"),
 ch("C","Text C · Question 3 extended response",["Journal, letter, interview or talk in role","Reading 15 marks · Writing 10 marks"],"tested",16,25,"Two past papers","Jun 2024 P12: 18/25. Jun 2022 P11: 16/25 (latest).",unit="Paper 1 · Reading"),
 ch("P2","Paper 2 writing",[],"notstarted",note="No graded Paper 2 work recorded yet.",unit="Paper 2 · Writing"),
]

# ---------------- FRENCH ----------------
F = [
 ch(1,"I introduce myself",["My home","My school","My eating habits","My body and my health"],"unknown",note="No record yet."),
 ch(2,"My family and my friends, at home and abroad",["Self, family, pets, personal relationships","Life at home","Leisure, entertainments, invitations","Eating out","Special occasions","Going on holiday","Family and friends abroad"],"unknown",note="No record yet."),
 ch(3,"Where I live and what it's like",["Home town and geographical surroundings","Shopping","Public services","Natural environment","Weather","Finding the way","Travel and transport"],"unknown",note="No record yet."),
 ch(4,"Studying and working",["French schools","Further education and training","Future career plans","Employment","Communication and technology at work"],"unknown",note="No record yet."),
 ch(5,"The international perspective",["International travel","Weather on holiday","Festivals and faiths","International menus","Environmental problems"],"unknown",note="No record yet."),
]

SUBJECTS = [
 {"key":"physics","name":"Physics","code":"0625","tier":"Extended","group":"main","order":1,"color":"#2f5bd3",
  "headline":{"score":41,"max":50,"pct":82,"band":"A","label":"RT6 · 31 Oct"},
  "status":"watch","statusText":"Ch 17–20 score missing · Ch 21–22 untested",
  "summary":"All 25 chapters revised. 23 tested. A* needs 45/50.",
  "revisions":"All 25 chapters revised (18–31 Oct). Tests RT1 to RT6 cover every chapter except 21 and 22.",
  "papersUsed":["RT1 · Ch 1–5 · 18 Oct","RT2 · Ch 12–14 · 19 Oct","RT3 · Ch 6–9 · 21 Oct","RT4 · Ch 16.2, 17–20 · 24 Oct (score not recorded)","RT5 · Ch 10, 23–25 · 28 Oct","RT6 · Ch 10, 11, 15, 16 · 31 Oct"],
  "chapters":P,
  "fixes":["Read every digit twice. 4 and 9 have been mixed up in two tests.","Answer both halves of two-part questions. Count the marks before writing.","Write the unit on every answer line: m/s vs m/s², N, Pa.","Explain answers need the full chain. Gas pressure: hotter → faster particles → more frequent, harder collisions with the walls.","Use the constants printed on the paper (340 m/s, not 330).","Ray diagrams: use a ruler; the parallel ray bends through the focal point.","Wave rules: frequency never changes at a boundary; speed and wavelength change together.","Read graph end-points aloud before using them."],
  "gaps":["Mark RT4 (Ch 16.2, 17–20) and enter the score. It is missing.","Take a test on Ch 21 Electromagnetic induction and Ch 22 The nuclear atom. Revised but never tested.","Redo Ch 9 gas-pressure questions until 80%+ (now 67%).","Redo Ch 16 magnetism until 80%+ (now 73%).","Keep Ch 10 thermal explanations sharp (went 53% → 86%)."]},
 {"key":"chemistry","name":"Chemistry","code":"0620","tier":"Extended","group":"main","order":2,"color":"#0f8a6c",
  "headline":{"score":133,"max":160,"pct":83,"band":"A","label":"Board paper Jun 2024, P2 + P4 · 20 Oct"},
  "status":"heavy","statusText":"Priority: organic · Paper 6 not started",
  "summary":"All 19 chapters revised. Board paper at A (83%). Organic lost the most marks.",
  "revisions":"All 19 chapters revised with daily chapter tests by 17 Oct. Those chapter-test papers were lost with a deleted chat, so only Ch 4, 5, 6, 13 and 14 have chapter scores.",
  "papersUsed":["Revision test · Ch 4, 5, 6, 13, 14 · 8 Oct (Q9–12 not photographed)","Board 0620 Jun 2024 · Paper 4 theory · 68/80 · 20 Oct","Board 0620 Jun 2024 · Paper 2 MCQ · 32/40 · 20 Oct","Paper 6 practical · not attempted"],
  "chapters":C,
  "fixes":["Organic (Ch 16): ethene hydration conditions, fermentation, ester naming, homologous series, carboxylic acids.","Metals facts card (Ch 13–14): MgO from steam · Al₂O₃ layer · CuSO₄ blue → colourless · limestone equations and slag · alloy layers · sacrificial zinc.","Redox (Ch 6): label oxidised, reduced, reducing agent and oxidising agent on every equation.","Name things exactly: “carbon monoxide”, not “carbon”.","Check that a memorised answer fits this question before writing it.","Give both halves of two-part answers."],
  "gaps":["Start Paper 6 practical: one past paper this week, then one a week.","Redo Ch 16 organic with a timed 40-mark set until 80%+.","Retake chapter tests for the 14 chapters with no score (originals lost).","Revise chapter by chapter with question tests, not only past papers."]},
 {"key":"maths","name":"Mathematics","code":"0580","tier":"Extended","group":"main","order":3,"color":"#7a4cc8",
  "headline":None,
  "status":"watch","statusText":"No test scores yet · confirm Ch 12",
  "summary":"14 chapters in the book. 13 finished by 18 Oct. Ch 12 to confirm. No maths test is logged yet.",
  "revisions":"Chapters 1–11, 13 and 14 finished by 18 Oct. Ch 12 Vectors and transformations: the 18 Oct record said Vectors was still pending.",
  "papersUsed":["No graded maths paper in the record yet."],
  "chapters":M,
  "fixes":["Show every step, write units, check the answer line.","Scale factor (5.7 Similarity): length × k, area × k², volume × k³. Write k before calculating.","Reverse percentage (3.3): divide by the multiplier; never take the percentage of the final amount.","Compound interest (3.4): write the multiplier first, then raise it to the power."],
  "gaps":["Confirm whether Ch 12 Vectors and transformations is done.","Sit the first logged maths paper so there is a score to track.","Drill 3.3 reverse percentages and 5.7 scale factors until error-free."]},
 {"key":"english","name":"English","code":"0500","tier":"First Language","group":"other","order":4,"color":"#d0662a",
  "headline":{"score":16,"max":25,"pct":64,"band":"Below A","label":"Paper 1 Q3 · 7 Nov"},
  "status":"heavy","statusText":"Priority: develop points, reach 250+ words",
  "summary":"Text C (Question 3) practice only so far. Best 18/25, latest 16/25. A needs about 20/25.",
  "revisions":"Paper 1 Question 3 practice with two past papers. Text A, Text B and Paper 2 not yet recorded.",
  "papersUsed":["0500 Jun 2024 P12 Q3 · Ramesh talk · 18/25 · 4 Nov","0500 Jun 2022 P11 Q3 · Sam interview · 16/25 · 7 Nov"],
  "chapters":E,
  "fixes":["6-box check: split every bullet into its two halves and tick all six before writing.","Develop every point with “because” or “so”.","Write 250 words minimum; aim for 280.","Write as a spoken voice, not an essay.","Reword details from the text; don't copy phrases."],
  "gaps":["Rewrite Jun 2022 Q3 (Sam) at 280 words with the 6-box check, and log the score.","Redo bullet 3 of Jun 2024: what Ramesh himself gained.","Start graded Text A, Text B and Paper 2 work."]},
 {"key":"business","name":"Business Studies","code":"0450","tier":"","group":"other","order":5,"color":"#127e8f",
  "headline":{"score":68,"max":80,"pct":85,"band":"A","label":"RT1 · 7 Nov"},
  "status":"watch","statusText":"Evaluate questions · Ch 1–16 unrecorded",
  "summary":"Ch 17–25 tested at A (85%). Ch 26–29 test waiting. Ch 1–16 not recorded.",
  "revisions":"Ch 17–25 revised and tested (RT1). Ch 26–29 revised; RT2 waiting. Ch 1–16 not recorded.",
  "papersUsed":["RT1 · Ch 17–25 · 68/80 · 7 Nov","RT2 · Ch 26–29 · 40 marks · set, not attempted"],
  "chapters":B,
  "fixes":["Two-part definitions: give both parts.","Evaluate questions: develop each point, weigh both sides with the case figures, end with one justified decision.","Add the “so what”: the effect on cost per unit, cash, or customers.","Show every calculation step and write numbers in full.","Keep the final recommendation consistent with the argument."],
  "gaps":["Sit RT2 (Ch 26–29, 40 marks, 45 min) and log the score.","Record which of Ch 1–16 are done, then test them.","Redo RT1 1e and 2f with fully developed evaluation."]},
 {"key":"ict","name":"ICT","code":"0417","tier":"","group":"other","order":6,"color":"#3b4bb8",
  "headline":{"score":77,"max":80,"pct":96,"band":"A*","label":"RT2 · 3 Nov"},
  "status":"ok","statusText":"Theory done at A* · practical next",
  "summary":"Theory Ch 1–10 done at A* (96% twice). Practical Ch 11–21 not started.",
  "revisions":"Ch 1–10 revised and tested (RT1, RT2). Practical Ch 11–21 not started.",
  "papersUsed":["RT1 · Ch 1–4 · 48/50 · 2 Nov","RT2 · Ch 5–10 · 77/80 · 3 Nov"],
  "chapters":I,
  "fixes":["Finish the consequence; don't stop one step short.","Commit to a firm conclusion. “It depends” loses the mark.","Precise wording: the internet has no single owner.","Name the exact item: ducts or trunking for cables.","Name the exact mechanism: the password is the first factor."],
  "gaps":["Start practical chapters 11–21 in order.","One Paper 2 or Paper 3 practical task each week, saved to the project."]},
 {"key":"french","name":"French","code":"0520","tier":"","group":"other","order":7,"color":"#c43d7a",
  "headline":None,
  "status":"watch","statusText":"No records yet",
  "summary":"Five units in the coursebook. Nothing recorded yet.",
  "revisions":"No revision recorded.",
  "papersUsed":["No graded French paper yet."],
  "chapters":F,
  "fixes":["The fix list starts after the first graded paper."],
  "gaps":["Confirm French stays in the lineup alongside ICT.","Start with one graded Writing paper and log it."]},
]

PAPERS = [
 ("2026-10-08","chemistry","Ch 4, 5, 6, 13, 14 test","Ch 4, 5, 6, 13, 14",35,46,"","Q9–12 not photographed; paper out of 50."),
 ("2026-10-18","physics","RT1","Ch 1–5",41,47,"","3 MCQs not photographed; paper out of 50."),
 ("2026-10-19","physics","RT2","Ch 12–14",33,40,"A",""),
 ("2026-10-20","chemistry","Board Jun 2024 · Paper 4 theory","Full paper",68,80,"A",""),
 ("2026-10-20","chemistry","Board Jun 2024 · Paper 2 MCQ","Full paper",32,40,"A",""),
 ("2026-10-21","physics","RT3","Ch 6–9",34,40,"A","No process errors."),
 ("2026-10-24","physics","RT4","Ch 16.2, 17–20",None,None,"","Score not recorded."),
 ("2026-10-28","physics","RT5","Ch 10, 23–25",39,50,"B",""),
 ("2026-10-31","physics","RT6","Ch 10, 11, 15, 16",41,50,"A",""),
 ("2026-11-02","ict","RT1","Ch 1–4",48,50,"A*",""),
 ("2026-11-03","ict","RT2","Ch 5–10",77,80,"A*",""),
 ("2026-11-04","english","Paper 1 Q3 · Jun 2024 P12 (Ramesh talk)","Text C",18,25,"B","Content 10/15 · Writing 8/10"),
 ("2026-11-07","business","RT1","Ch 17–25",68,80,"A",""),
 ("2026-11-07","english","Paper 1 Q3 · Jun 2022 P11 (Sam interview)","Text C",16,25,"Below A","Content 9/15 · Writing 7/10"),
]

PRIORITIES = [
 ("physics","Physics RT4: mark it and enter the score (Ch 16.2, 17–20)."),
 ("physics","Physics Ch 21 and 22: revised but never tested. Take a test."),
 ("maths","Maths: confirm Ch 12, then sit the first logged maths paper."),
 ("chemistry","Chemistry Paper 6 practical: start, one paper a week."),
 ("chemistry","Chemistry: retake chapter tests for the 14 chapters with no score."),
 ("business","Business RT2 (Ch 26–29): sit it. Record Ch 1–16."),
 ("ict","ICT practical Ch 11–21: start."),
 ("english","English Q3: retry at 280 words with the 6-box check."),
 ("french","French: confirm the lineup, then the first graded paper."),
]

# ================= 8 Nov: records recovered from past chats =================
SUB = {s["key"]: s for s in SUBJECTS}
def chap(key, num): return next(c for c in SUB[key]["chapters"] if c["num"] == str(num))

# Physics RT4 found: 66/80 (graded 24 Oct)
PAPERS[6] = ("2026-10-24","physics","RT4","Ch 16.2, 17–20",66,80,"A","A* needs 72/80. 8 of 14 lost marks were imprecise explanations; 3 MCQ slips.")
for n in (17,18,19,20):
    c = chap("physics", n); c.update(status="tested", score=66, max=80, testedIn="RT4",
        note="RT4 tested Ch 16.2 and 17–20 together: 66/80 (group score).")
chap("physics",20)["note"] += " Content gap: reverse the direction for electron beams before Fleming's left-hand rule."
P_ = SUB["physics"]
P_["statusText"] = "Ch 21–22 not tested yet"
P_["summary"] = "All 25 chapters revised. 23 tested. Latest 41/50 (A); A* needs 45/50."
P_["papersUsed"][3] = "RT4 · Ch 16.2, 17–20 · 66/80 · 24 Oct"
P_["fixes"] += ["Electron beams: reverse the direction first, then apply Fleming's left-hand rule.","Reread the MCQ stem before locking in an answer."]
P_["gaps"] = [g for g in P_["gaps"] if not g.startswith("Mark RT4")]

# Chemistry chapter tests found (Oct 2026); per-chapter % from the 18-20 Oct tracker
C_ = SUB["chemistry"]
def cp(n, pct, prev, test, note):
    c = chap("chemistry", n)
    c.update(status="tested", score=None, max=None, pct=pct, scoreText=f"{pct}%", testedIn=test,
             note=(f"Earlier: {prev}%. " if prev is not None else "") + note)
G13 = "Ch 1–3 tests: 26/50 (6 Oct), 13/30 (11 Oct), 25/30 (12 Oct)."
cp(1,83,43,"Ch 1–3 retest 2 · 12 Oct",G13)
cp(2,83,43,"Ch 1–3 retest 2 · 12 Oct",G13)
cp(3,83,43,"Ch 1–3 retest 2 · 12 Oct",G13+" Weak: ion charge notation (+, 2−). Board paper: bonding −3.")
cp(4,100,None,"Ch 4–6, 13–14 · 8 Oct","Test 35/46 (Q9–12 not photographed).")
cp(5,93,None,"Ch 4–6, 13–14 · 8 Oct","Test 35/46.")
cp(6,73,None,"Ch 4–6, 13–14 · 8 Oct","Test 35/46. Weak: naming the reducing agent.")
cp(7,55,None,"Ch 7, 9, 12 · 12 Oct","Test 22/30. Weakest chapter: electrolysis.")
cp(8,60,54,"Ch 8, 10, 11, 15 retest · 17 Oct","Retest 35/40. Still weak: labelling energy-level diagrams.")
cp(9,80,None,"Ch 7, 9, 12 · 12 Oct","Test 22/30. Board paper: rate −1.")
cp(10,100,79,"Ch 8, 10, 11, 15 retest · 17 Oct","Retest 35/40. Board paper: Haber vs Contact conditions −2.")
cp(11,90,80,"Ch 8, 10, 11, 15 retest · 17 Oct","Retest 35/40.")
cp(12,89,None,"Ch 7, 9, 12 · 12 Oct","Test 22/30.")
cp(13,57,None,"Ch 4–6, 13–14 · 8 Oct","Weak: MgO from steam, Al oxide layer, CuSO₄ colour change.")
cp(14,64,None,"Ch 4–6, 13–14 · 8 Oct","Weak: blast-furnace limestone, alloys, sacrificial zinc.")
cp(15,100,13,"Ch 8, 10, 11, 15 retest · 17 Oct","Retest 35/40. Board paper: environment −2.")
cp(16,92,None,"Ch 16–18 · 13 Oct","Test 25/30. But organic lost 9 marks on the 20 Oct board paper.")
cp(17,78,None,"Ch 16–18 · 13 Oct","Test 25/30.")
cp(18,78,None,"Ch 16–18 · 13 Oct","Test 25/30.")
chap("chemistry",19).update(status="revised", note="Revised; no chapter test yet. Paper 6 practical not attempted.")
C_["revisions"] = "All 19 chapters revised. Chapter tests 6–17 Oct cover Ch 1–18 (Ch 1–3 and Ch 8, 10, 11, 15 retested until secure). Ch 19 has no test yet."
C_["summary"] = "All 19 chapters revised, 18 tested. Board paper at A (83%). Weakest: Ch 7, 13, 8, 14, and organic on board questions."
C_["papersUsed"] = ["Ch 1–3 · 26/50 · 6 Oct → 13/30 · 11 Oct → 25/30 · 12 Oct","Ch 4, 5, 6, 13, 14 · 35/46 · 8 Oct","Ch 7, 9, 12 · 22/30 · 12 Oct","Ch 16, 17, 18 · 25/30 · 13 Oct","Ch 8, 10, 11, 15 · 31/50 · 15 Oct → 35/40 · 17 Oct","Board 0620/42 Jun 2024 · Paper 4 · 68/80 · 20 Oct","Board 0620/22 Jun 2024 · Paper 2 · 32/40 · 20 Oct","Paper 6 practical · not attempted"]
C_["fixes"].insert(3, "Energy-level diagrams (Ch 8): label reactants, products, the ΔH arrow and activation energy.")
C_["fixes"].insert(4, "Ion charges: write +, 2+, −, 2− (never +1 or −2).")
C_["fixes"].insert(5, "Electrolysis (Ch 7): name the product at each electrode and write its half-equation.")
C_["gaps"] = ["Start Paper 6 practical: one past paper this week, then one a week.","Retest the four weakest chapters: Ch 7 (55%), Ch 13 (57%), Ch 8 (60%), Ch 14 (64%).","Organic (Ch 16): timed board-style set until 80%+. Chapter test was 92% but the board paper lost 9 marks.","Take a Ch 19 (experiments and tests) chapter test."]

# Physics 7 Oct topic test (school test prep)
for n in (19,20):
    chap("physics",n)["note"] += " Earlier: 7 Oct topic test on 19.3 and 20.1–20.3, 21/30 (70%)."
P_["papersUsed"].insert(0, "Topic test · 19.3, 20.1–20.3 · 21/30 · 7 Oct")

# English: all graded work found
E_ = SUB["english"]
E_["chapters"] = [
 ch("A","Text A comprehension (Question 1)",["Short answers","Own-words explanations"],"tested",12,15,"Jun 2026 P12 Q1 (Rhinos)","8 Nov: 12/15 (range 12–13). Lost: reversed subject in 1(d)(i), missed the plant-recording method in 1(d)(ii), wrote 'will' where the text says 'might'.",unit="Paper 1 · Reading"),
 ch("WE","Writer's effects and vocabulary",["Meaning of words in context","Effect of chosen phrases"],"tested",9,25,"Train passage task","6 Oct: 9/25. Misread literal meaning before analysing. Method: Zoom → Means → Suggests → Effect.",unit="Paper 1 · Reading"),
 ch("C","Text C extended response (Question 3)",["Talk, letter, article, interview or report in role","Reading 15 marks · Writing 10 marks"],"tested",16,25,"Five past-paper answers","13/25 (4 Nov) → 18 (4 Nov) → 18 (5 Nov) → 16 (7 Nov) → 16 (7 Nov). Latest 16/25.",unit="Paper 1 · Reading"),
 ch("P2","Paper 2 writing",[],"notstarted",note="No graded Paper 2 work yet.",unit="Paper 2 · Writing"),
]
E_["headline"] = {"score":16,"max":25,"pct":64,"band":"Below B","label":"Paper 1 Q3 · 7 Nov (latest of five)"}
E_["summary"] = "Five Question 3 answers graded (13–18/25); A needs about 20/25. Text A 12/15 on 8 Nov."
E_["revisions"] = "Paper 1 practice: one writer's-effects task, five Question 3 answers across talk, report, article, interview and letter forms, and one Text A. Paper 2 not started."
E_["papersUsed"] = ["Writer's effects task (train passage) · 9/25 · 6 Oct","Q3 report, dog-sledging text · 13/25 · 4 Nov","0500/12 Jun 2024 Q3 · Ramesh talk · 18/25 · 4 Nov","0500/12 Jun 2022 Q3 · feature article · 18/25 · 5 Nov","0500/11 Jun 2022 Q3 · Sam interview · 16/25 · 7 Nov","0500/11 Oct/Nov 2025 Q3 · Antarctic letter · 16/25 · 7 Nov","0500/12 Jun 2026 Q1 · Text A Rhinos · 12/15 · 8 Nov"]
E_["fixes"] += ["Check the literal meaning of a phrase before analysing its effect.","Copy the text's certainty: 'might' stays 'might'.","Articles need a headline and a one-line standfirst."]
E_["gaps"] = ["Retry a Q3 at 280 words with the 6-box check; aim for 20/25.","Redo the writer's-effects task with the Zoom–Means–Suggests–Effect method.","Start graded Paper 2 work."]
PAPERS[13] = PAPERS[13][:6] + ("Below B",) + PAPERS[13][7:]
PAPERS[11] = PAPERS[11][:7] + ("Content 10/15 · Writing 8/10. First marked 17/25 strictly, then 18/25.",)

# Maths board papers found
M_ = SUB["maths"]
M_["headline"] = {"score":186,"max":200,"pct":93,"band":"A*","label":"Board P2 + P4 combined · 24–25 Oct"}
M_["status"] = "ok"; M_["statusText"] = "A* on board papers · fix similarity, enlargement"
M_["summary"] = "Three board papers at A* level (91%, 95%, 90%). Ch 9 test 24/25. Two content gaps left."
M_["revisions"] = "All 14 chapters revised by 18 Oct except the vectors part of Ch 12; vectors questions still scored full marks on two board papers."
M_["papersUsed"] = ["Ch 9 Graphs test · 24/25 · 11 Oct","Board 0580/22 May/Jun 2025 · Paper 2 · 91/100 · 24 Oct","Board Paper 4 (component 42, 100 marks) · 95/100 · 25 Oct","Board Paper 2 (70-mark format) · 63/70 · 29 Oct"]
chap("maths",9).update(status="tested", score=24, max=25, testedIn="Ch 9 test",
    note="Lost 1 mark: justify each turning point separately.")
chap("maths",3)["note"] = "Reverse percentages and compound interest were clean on the 25 Oct Paper 4: gap closed. Map-scale conversion slip on 29 Oct. " + MDONE
chap("maths",5)["note"] = "Still open: volume scale factor k³ (lost 2 marks on 25 Oct Paper 4). " + MDONE
chap("maths",12).update(note="Vectors questions: full marks on the 24 Oct and 29 Oct board papers, though the 18 Oct record said vectors wasn't revised yet. Transformation slips: read column vector as (x, y), write the word “Rotation”, negative-scale-factor enlargement. Confirm the chapter is revised.")
M_["fixes"] = ["Similarity (5.7): length × k, area × k², volume × k³. Write k³ before calculating volume.","Negative scale factor enlargement: multiply each vertex's offset from the centre by k; the image lands on the opposite side.","Column vector (a over b): top moves x, bottom moves y.","Name the transformation in words (“Rotation”, “reflection in the line …”) as well as the details.","Compare the final answer with the last line of working: lost signs (−x + 8) and ≥ written like 7.","Keep full calculator values until the final answer; write the substituted line exactly as keyed in.","Simplify fractions fully (divide by the HCF).","After a unit or scale conversion, check the answer is sensible."]
M_["gaps"] = ["Drill similar areas and volumes (k², k³): 15 Save My Exams questions.","Drill negative scale factor enlargements: 5–6 questions.","Confirm Ch 12 Vectors and transformations is revised.","Sit the next Paper 4 to confirm A* on the combined total."]

PAPERS += [
 ("2026-10-06","chemistry","Ch 1–3 test","Ch 1–3",26,50,"","Weak: ionic vs metallic conduction, Ar as weighted average, definitions."),
 ("2026-10-10","maths","Ch 9 Graphs test","Ch 9",24,25,"A*","Lost 1 mark: second turning point not justified."),
 ("2026-10-11","chemistry","Ch 1–3 retest","Ch 1–3",13,30,"","Covalent bonds confused with intermolecular forces."),
 ("2026-10-12","chemistry","Ch 1–3 retest 2","Ch 1–3",25,30,"","9 of 12 earlier weak spots now correct."),
 ("2026-10-12","chemistry","Ch 7, 9, 12 test","Ch 7, 9, 12",22,30,"","Ch 7 electrolysis 55%."),
 ("2026-10-13","chemistry","Ch 16, 17, 18 test","Ch 16–18",25,30,"",""),
 ("2026-10-15","chemistry","Ch 8, 10, 11, 15 test","Ch 8, 10, 11, 15",31,50,"","Deliberately hard; Ch 15 barely studied then."),
 ("2026-10-17","chemistry","Ch 8, 10, 11, 15 retest","Ch 8, 10, 11, 15",35,40,"","Ch 15 full marks; energy-diagram labels still weak."),
 ("2026-10-24","maths","Board 0580/22 May/Jun 2025 · Paper 2","Full paper",91,100,"A*","Marked to the official scheme. 9 marks lost to reading, labelling and copying slips."),
 ("2026-10-25","maths","Board Paper 4 (component 42)","Full paper",95,100,"A*","Lost: volume scale factor (−2), index law (−1), working-line slips (−2)."),
 ("2026-10-29","maths","Board Paper 2 (70-mark format)","Full paper",63,70,"A*","Indicative grade. All 7 marks lost to slips; content gap: negative enlargement."),
 ("2026-10-07","physics","Topic test · 19.3, 20.1–20.3","Ch 19.3, 20.1–20.3",21,30,"B","Stricter marking 19/30. Fleming's rule mix-up; motor rotation direction."),
 ("2026-10-06","english","Writer's effects task (train passage)","Language analysis",9,25,"","Misread literal meaning; named techniques without their effect."),
 ("2026-11-04","english","Q3 report · dog-sledging text","Text C",13,25,"","Content 8/15 · Writing 5/10. About 240 words."),
 ("2026-11-05","english","Paper 1 Q3 · Jun 2022 P12 (feature article)","Text C",18,25,"","Content 11/15 · Writing 7/10. Marked to the question's rubric."),
 ("2026-11-07","english","Paper 1 Q3 · Oct/Nov 2025 P11 (Antarctic letter)","Text C",16,25,"","Content 10/15 · Writing 6/10."),
 ("2026-11-08","english","Paper 1 Q1 · Jun 2026 P12 (Text A: Rhinos)","Text A",12,15,"","Range 12–13."),
]
def band(p):
    return "A*" if p>=90 else "A" if p>=80 else "B" if p>=70 else "Below B"
PAPERS[:] = [r if (r[6] or r[4] is None) else r[:6]+(band(round(r[4]*100/r[5])),)+r[7:] for r in PAPERS]
PRIORITIES[:] = [
 ("physics","Physics Ch 21 and 22: revised but never tested. Take a test."),
 ("chemistry","Chemistry Paper 6 practical: start, one paper a week."),
 ("chemistry","Chemistry: retest Ch 7, 13, 8, 14 (55–64%) and Ch 16 organic on board-style questions."),
 ("maths","Maths: drill similarity (k², k³) and negative enlargements."),
 ("chemistry","Chemistry Ch 19: take the chapter test."),
 ("business","Business RT2 (Ch 26–29): sit it. Record Ch 1–16."),
 ("ict","ICT practical Ch 11–21: start."),
 ("english","English Q3: retry at 280 words with the 6-box check."),
 ("french","French: confirm the lineup, then the first graded paper."),
]

# ================= 9–10 Nov: new graded board papers =================
PID_OVERRIDE = {}

# Chemistry 0620/22 Oct/Nov 2025 Paper 2 MCQ, graded 9 Nov: 37/40 confirmed (range 37–39)
C_ = SUB["chemistry"]
C_["headline"] = {"score":37,"max":40,"pct":92,"band":"A*","label":"Board 0620/22 Oct/Nov 2025 · Paper 2 MCQ · 9 Nov"}
C_["statusText"] = "Paper 6 not started · gas laws slip"
C_["summary"] = "All 19 chapters revised, 18 tested. Latest board MCQ 37/40 (92%, A*), up from 32/40. Paper 4 at A (85%). Paper 6 not started."
C_["papersUsed"].insert(-1, "Board 0620/22 Oct/Nov 2025 · Paper 2 · 37/40 (range 37–39) · 9 Nov")
chap("chemistry",1)["note"] += " 9 Nov MCQ: lost Q1 gas volume (thought higher temperature lowers volume); Q3 diffusion unresolved."
chap("chemistry",16)["note"] += " 9 Nov MCQ: organic 5/6 confirmed; Q32 double-marked (A and D)."
C_["fixes"].insert(0, "Gas volume (Ch 1): hotter → bigger volume; lower pressure → bigger volume. Say it before choosing.")
C_["fixes"].append("MCQ: one clear mark per question. Two marks score zero.")
C_["gaps"].insert(1, "Confirm 0620/22 O/N 2025 Q32 (A or D?) with Shaurya and check the Q3 official key; score is 37–39/40.")

PAPERS.append(("2026-11-09","chemistry","Board 0620/22 Oct/Nov 2025 · Paper 2 MCQ","Full paper",37,40,"A*",
  "Confirmed 37/40; range 37–39. Lost Q1 gas volume. Q3 key unverified; Q32 double-marked (scores zero unless resolved)."))

# French 0520/21 Oct/Nov 2024 Paper 2 Reading, graded 10 Nov: Q1–5 32/34 (Q6 pending)
F_ = SUB["french"]
F_.update({
 "headline":{"score":32,"max":34,"pct":94,"band":"A","label":"Board 0520/21 Nov 2024 Reading, Q1–5 · 10 Nov (Q6 pending)"},
 "status":"ok","statusText":"Reading at A* pace · Writing paper next",
 "summary":"First board paper: Reading Q1–5 32/34 (94%). A already secured on the Nov 2024 line (29/45). Q6 still to mark.",
 "revisions":"Board past paper practice started 10 Nov (Paper 2 Reading).",
 "papersUsed":["Board 0520/21 Oct/Nov 2024 · Paper 2 Reading · Q1–5 32/34 · 10 Nov (Q6 pending)"],
 "fixes":["Circle every condition/exception word before answering: sauf, si/s'il, mais, d'habitude, ne…jamais, seulement.",
          "Matching questions: tick each person's conditions (day, time, budget, group size, food) against the ad; all must pass.",
          "Print capital letters clearly (his H reads like M).",
          "Spell key nouns fully: vétérinaire.",
          "Answer with the verb when the question asks what someone did: il a fabriqué des jouets."],
 "gaps":["Send Q6 (pages 10–12) to finish the 0520/21 score.",
         "Sit a Paper 4 Writing past paper next: the real test for the French vs ICT decision.",
         "Confirm French stays in the lineup alongside ICT."],
})
PAPERS.append(("2026-11-10","french","Board 0520/21 Oct/Nov 2024 · Paper 2 Reading","Q1–5 (Q6 not yet photographed)",32,34,"A",
  "Partial: Q6 (11 marks) pending. A secured (Cambridge A line 29/45); A* pace, needs 9/11 on Q6. Lost 3(c) and 5(e): skipped condition/exception words (s'il pleut, sauf les lundis)."))
PID_OVERRIDE[len(PAPERS)] = "2026-11-10-french-01"   # id already used on the live dashboard

PRIORITIES[:] = [
 ("physics","Physics Ch 21 and 22: revised but never tested. Take a test."),
 ("chemistry","Chemistry Paper 6 practical: start, one paper a week."),
 ("chemistry","Chemistry: retest Ch 7, 13, 8, 14 (55–64%) and Ch 16 organic on board-style questions."),
 ("maths","Maths: drill similarity (k², k³) and negative enlargements."),
 ("chemistry","Chemistry: resolve Q32 and Q3 on the 9 Nov MCQ; take the Ch 19 chapter test."),
 ("french","French: send Q6 to finish the Reading paper, then sit Paper 4 Writing."),
 ("business","Business RT2 (Ch 26–29): sit it. Record Ch 1–16."),
 ("ict","ICT practical Ch 11–21: start."),
 ("english","English Q3: retry at 280 words with the 6-box check."),
]

os.makedirs(OUT, exist_ok=True)
for s in SUBJECTS:
    json.dump(s, open(f"{OUT}/subject-{s['key']}.json","w"), ensure_ascii=False)
papers = []
for i,row in enumerate(PAPERS,1):
    d,sub,test,chs,sc,mx,band,note = row[:8]
    doc = {"date":d,"subject":sub,"test":test,"chapters":chs,"score":sc,"max":mx,
           "pct": round(sc*100/mx) if sc is not None else None,"band":band,"note":note}
    if len(row) > 8 and row[8]: doc["dateLabel"] = row[8]
    pid = PID_OVERRIDE.get(i, f"{d}-{sub}-{i:02d}")
    papers.append((pid,doc))
    json.dump(doc, open(f"{OUT}/paper-{pid}.json","w"), ensure_ascii=False)
home = {"updated":UPDATED,"candidate":"Shaurya Gala","centre":"JBCN International School, Parel",
        "series":"Cambridge IGCSE · May/June 2027","priorities":[{"subject":a,"text":b} for a,b in PRIORITIES]}
json.dump(home, open(f"{OUT}/meta-home.json","w"), ensure_ascii=False)
json.dump({"subjects":SUBJECTS,"papers":[dict(id=p,**d) for p,d in papers],"home":home},
          open(f"{OUT}/tracker-data.json","w"), ensure_ascii=False, indent=1)

# ---------- markdown backup ----------
LBL = {"tested":"Tested","revised":"Revised, no score","missing":"Score missing","pending":"Test waiting",
       "confirm":"To confirm","notstarted":"Not started","unknown":"No record"}
L = [f"# Shaurya's Grade 10 Study Plan — Master Tracker (backup of the live dashboard)", f"Last updated: {UPDATED}",
     "Live dashboard: see the link in tracker/README section below. This file is regenerated from the same data the dashboard shows.", "",
     "## Priority gaps"]
for i,p in enumerate(PRIORITIES,1): L.append(f"{i}. {p[1]}")
L += ["", "## Grade log (by date)", "| Date | Subject | Test | Chapters | Score | % | Band | Note |","|---|---|---|---|---|---|---|---|"]
for pid,d in papers:
    sc = f"{d['score']}/{d['max']}" if d['score'] is not None else "not recorded"
    pc = f"{d['pct']}%" if d['pct'] is not None else "—"
    L.append(f"| {d['date']} | {d['subject']} | {d['test']} | {d['chapters']} | {sc} | {pc} | {d['band'] or '—'} | {d['note']} |")
for s in SUBJECTS:
    h = s["headline"]
    L += ["", f"## {s['name']} ({s['code']}{' '+s['tier'] if s['tier'] else ''})",
          f"Latest: {h['score']}/{h['max']} ({h['pct']}%, {h['band']}) — {h['label']}" if h else "Latest: no graded score yet",
          f"Status: {s['statusText']}", f"Summary: {s['summary']}", f"Revisions: {s['revisions']}", "",
          "| Ch | Title | Topics | Status | Tested in | Score | Note |","|---|---|---|---|---|---|---|"]
    for c in s["chapters"]:
        sc = f"{c['score']}/{c['max']}" if c['score'] is not None else (f"{c['pct']}%" if c.get('pct') is not None else "—")
        L.append(f"| {c['num']} | {c['title']} | {'; '.join(c['sections'])} | {LBL[c['status']]} | {c['testedIn'] or '—'} | {sc} | {c['note']} |")
    L += ["", "Papers used:"] + [f"- {x}" for x in s["papersUsed"]]
    L += ["", "Fix list:"] + [f"{i}. {x}" for i,x in enumerate(s["fixes"],1)]
    L += ["", "Gaps (find and fix):"] + [f"{i}. {x}" for i,x in enumerate(s["gaps"],1)]
open(f"{OUT}/shaurya-tracker.md","w").write("\n".join(L)+"\n")
print("ok", len(SUBJECTS), "subjects", len(papers), "papers", sum(len(s['chapters']) for s in SUBJECTS), "chapters")
