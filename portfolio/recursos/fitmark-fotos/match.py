#!/usr/bin/env python3
"""Cruza los 152 ejercicios de FitMark contra los 873 de free-exercise-db.
Salida: reporte de cobertura (DIRECTO / PROBABLE / HUÉRFANO) + CSV de mapeo.
No toca código de FitMark: solo lee el JSON exportado."""
import json, re, unicodedata

fm = json.load(open('fm_exercises.json'))
fedb = json.load(open('fedb.json'))

def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode()
    return s.lower()

# --- grupo muscular ES -> conjunto de músculos válidos en fedb ---
MG2MUS = {
    'pecho': {'chest'},
    'espalda': {'lats','middle back','lower back','traps'},
    'hombros': {'shoulders'},
    'biceps': {'biceps','forearms'},
    'triceps': {'triceps'},
    'cuadriceps': {'quadriceps'},
    'femoral': {'hamstrings'},
    'gluteos': {'glutes','adductors','abductors'},
    'core': {'abdominals'},
    'pantorrillas': {'calves'},
}

# --- equipo FM -> tokens/equipment esperados en fedb ---
EQ2TOK = {
    'BARBELL': 'barbell', 'DUMBBELL': 'dumbbell', 'CABLE': 'cable',
    'MACHINE': 'machine', 'SMITH_MACHINE': 'smith', 'KETTLEBELL': 'kettlebell',
    'RESISTANCE_BAND': 'bands', 'BODYWEIGHT': 'body',
}

# --- diccionario de MOVIMIENTO ES -> tokens EN (los que definen el ejercicio) ---
# claves en español normalizado (sin acentos, minúsculas); se buscan como substrings del nombre FM
MOVE = [
    ('aperturas inclinadas', ['incline','fly']),
    ('aperturas posteriores', ['reverse','fly','rear']),
    ('aperturas', ['fly','flye']),
    ('cruce de poleas', ['cable','crossover']),
    ('flexiones de brazos', ['push','up']),
    ('fondos en banco', ['bench','dip']),
    ('fondos en paralelas', ['dip']),
    ('pec deck', ['butterfly','pec']),
    ('press de banca declinado', ['decline','bench','press']),
    ('press de banca inclinado', ['incline','bench','press']),
    ('press de banca', ['bench','press']),
    ('press de pecho', ['chest','press']),
    ('dominadas supinas', ['chin','up']),
    ('dominadas tras nuca', ['pull','up']),
    ('dominadas', ['pull','up','chin']),
    ('encogimientos', ['shrug']),
    ('jalon con brazos rectos', ['straight','arm','pulldown']),
    ('jalon al pecho', ['pulldown','lat']),
    ('jalon tras nuca', ['pulldown','behind']),
    ('peso muerto rumano', ['romanian','deadlift']),
    ('peso muerto piernas rigidas', ['stiff','leg','deadlift']),
    ('peso muerto sumo', ['sumo','deadlift']),
    ('peso muerto convencional', ['deadlift']),
    ('peso muerto a una pierna', ['single','leg','deadlift']),
    ('peso muerto', ['deadlift']),
    ('pullover', ['pullover']),
    ('remo al menton', ['upright','row']),
    ('remo en t', ['t-bar','row','bent']),
    ('remo sentado', ['seated','cable','row']),
    ('remo con mancuerna a una mano', ['one','arm','dumbbell','row']),
    ('remo', ['row']),
    ('elevaciones frontales', ['front','raise']),
    ('elevaciones laterales', ['lateral','raise','side']),
    ('pajaros', ['reverse','fly','rear','delt']),
    ('press de hombros tras nuca', ['behind','neck','press']),
    ('press de hombros', ['shoulder','press']),
    ('press militar', ['military','press']),
    ('push press', ['push','press']),
    ('curl de biceps predicador', ['preacher','curl']),
    ('curl de biceps concentrado', ['concentration','curl']),
    ('curl de muneca', ['wrist','curl']),
    ('curl inverso', ['reverse','curl']),
    ('curl martillo', ['hammer','curl']),
    ('curl de biceps', ['curl','biceps']),
    ('curl femoral', ['leg','curl']),
    ('extensiones de muneca', ['wrist','extension']),
    ('extensiones de triceps tras nuca', ['overhead','triceps','extension']),
    ('extensiones de triceps sobre la cabeza', ['overhead','triceps','extension']),
    ('extensiones de triceps tumbado', ['lying','triceps','extension']),
    ('extensiones de triceps', ['triceps','pushdown','extension']),
    ('patadas de triceps', ['triceps','kickback']),
    ('press cerrado', ['close','grip','bench']),
    ('press frances', ['french','press','skullcrusher','lying','triceps']),
    ('crunch inverso', ['reverse','crunch']),
    ('crunch oblicuo', ['oblique','crunch']),
    ('crunch', ['crunch']),
    ('dead bug', ['dead','bug']),
    ('elevaciones de piernas', ['leg','raise']),
    ('hollow hold', ['hollow']),
    ('pallof press', ['pallof']),
    ('plancha con subidas', ['plank']),
    ('plancha', ['plank']),
    ('rueda abdominal', ['ab','roller','wheel']),
    ('russian twist', ['russian','twist']),
    ('burpees', ['burpee']),
    ('saltos con rodillas al pecho', ['knee','tuck','jump']),
    ('caminata del pato', ['duck','walk']),
    ('extensiones de cuadriceps', ['leg','extension']),
    ('prensa de piernas', ['leg','press']),
    ('sentadillas bulgaras', ['bulgarian','split','squat']),
    ('sentadillas goblet', ['goblet','squat']),
    ('sentadillas hack', ['hack','squat']),
    ('sentadillas frontales', ['front','squat']),
    ('sentadillas isometricas en pared', ['wall','sit']),
    ('sentadillas con salto', ['jump','squat']),
    ('sentadillas', ['squat']),
    ('subidas al cajon', ['step','up','box']),
    ('zancadas', ['lunge']),
    ('buenos dias', ['good','morning']),
    ('good morning', ['good','morning']),
    ('nordic curl', ['nordic','hamstring']),
    ('elevaciones gluteo-femorales', ['glute','ham','raise']),
    ('swing con kettlebell', ['kettlebell','swing']),
    ('abducciones de cadera', ['hip','abduction','thigh','abductor']),
    ('almeja', ['clam']),
    ('bird dog', ['bird','dog']),
    ('caminata lateral', ['band','walk','monster']),
    ('elevaciones de cadera tumbado de lado', ['side','hip','raise']),
    ('elevaciones laterales de pierna', ['side','leg','raise']),
    ('frog pump', ['frog']),
    ('hidrante', ['fire','hydrant']),
    ('hip thrust', ['hip','thrust']),
    ('patadas de burro', ['donkey','kick']),
    ('patadas de gluteo', ['glute','kickback','cable']),
    ('puente de gluteos', ['glute','bridge','bridge']),
    ('elevaciones de pantorrillas', ['calf','raise']),
    ('subidas', ['step','up']),
]

def fm_tokens(e):
    n = norm(e['name'])
    toks = set()
    for key, ts in MOVE:
        if key in n:
            toks.update(ts)
            break  # el primer match (más específico) gana
    return toks

def fm_modifiers(e):
    """tokens de modificador (ángulo/lado) que suman precisión"""
    n = norm(e['name'])
    mods = set()
    for es, en in [('inclinad','incline'),('declinad','decline'),('sentad','seated'),
                   ('de pie','standing'),('tumbad','lying'),('unilateral','one'),
                   ('a una mano','one'),('a una pierna','single'),('supin','supinated'),
                   ('agarre ancho','wide'),('agarre cerrado','close'),('frontal','front'),
                   ('alta','high'),('baja','low')]:
        if es in n: mods.add(en)
    return mods

# preprocesar fedb
fedb_pp = []
for x in fedb:
    nm = norm(x['name'])
    toks = set(re.findall(r'[a-z]+', nm))
    fedb_pp.append({
        'id': x['id'], 'name': x['name'], 'toks': toks, 'nm': nm,
        'eq': (x.get('equipment') or '').lower(),
        'mus': set(x.get('primaryMuscles') or []),
        'imgs': x.get('images') or [], 'level': x.get('level'),
    })

def score(e, cand, mus_ok):
    mv = fm_tokens(e)
    if not mv:
        return 0
    inter = mv & cand['toks']
    if not inter:
        return 0
    s = len(inter) / len(mv)          # fracción del movimiento cubierta (0..1)
    # gate muscular: si el músculo no coincide, penaliza fuerte
    if not (cand['mus'] & mus_ok):
        s *= 0.35
    # equipo
    eq_toks = {EQ2TOK[q] for q in e['eq'] if q in EQ2TOK}
    if any(t in cand['eq'] or (t=='body' and cand['eq'] in ('body only','other')) or
           (t=='smith' and 'smith' in cand['nm']) or (t=='bands' and cand['eq']=='bands')
           for t in eq_toks):
        s += 0.30
    elif eq_toks and cand['eq'] and not (eq_toks & {cand['eq'].split()[0]}):
        s -= 0.05
    # modificadores
    mods = fm_modifiers(e)
    if mods:
        s += 0.15 * len(mods & cand['toks'])
    return s

rows = []
directo = probable = huerfano = 0
for e in fm:
    mus_ok = MG2MUS.get(e['mg'], set())
    best, bests = None, 0
    for cand in fedb_pp:
        sc = score(e, cand, mus_ok)
        if sc > bests:
            bests, best = sc, cand
    if bests >= 0.95:
        cls = 'DIRECTO'; directo += 1
    elif bests >= 0.55:
        cls = 'PROBABLE'; probable += 1
    else:
        cls = 'HUERFANO'; huerfano += 1
        best = None
    rows.append({
        'fm_name': e['name'], 'fm_slug': e['slug'], 'mg': e['mg'],
        'eq': ','.join(e['eq']), 'main': e['main'],
        'clase': cls, 'score': round(bests, 2),
        'fedb_id': best['id'] if best else '',
        'fedb_name': best['name'] if best else '',
        'img': (best['imgs'][0] if best and best['imgs'] else ''),
    })

# salida
import csv
with open('mapeo_fitmark_fedb.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

total = len(fm)
print(f"TOTAL FitMark: {total}")
print(f"  DIRECTO  (match confiable):  {directo:3d}  ({directo*100//total}%)")
print(f"  PROBABLE (revisar a ojo):    {probable:3d}  ({probable*100//total}%)")
print(f"  HUERFANO (sin foto → Wallace): {huerfano:3d}  ({huerfano*100//total}%)")
print(f"  Cobertura potencial (dir+prob): {directo+probable}/{total} ({(directo+probable)*100//total}%)")
print()
print("=== HUÉRFANOS (primeros en la cola de Wallace) ===")
for r in rows:
    if r['clase']=='HUERFANO':
        print(f"  · {r['fm_name']}  [{r['mg']}/{r['eq']}]")
