import random, sympy as sp
from sympy import symbols, solve, diff, integrate, Rational, sqrt, Matrix, lcm

x = symbols('x')

# ── helpers ──────────────────────────────────────────────────────────────────
def _frac(n, d):
    r = Rational(n, d)
    return str(r)

def _check(user: str, correct: str, alts: list = None) -> bool:
    u = user.strip().replace(" ", "").lower().replace("^","**")
    c = correct.strip().replace(" ", "").lower().replace("^","**")
    if u == c: return True
    if alts:
        for a in alts:
            if u == str(a).strip().replace(" ","").lower(): return True
    try:
        ue = sp.sympify(u); ce = sp.sympify(c)
        if sp.simplify(ue - ce) == 0: return True
    except: pass
    try:
        if abs(float(u) - float(c)) < 0.05: return True
    except: pass
    return False

# ── PRIMARIA ─────────────────────────────────────────────────────────────────
def _suma_resta(diff_level):
    op = random.choice(['+', '-'])
    hi = {1: 99, 2: 999, 3: 9999}[diff_level]
    lo = hi // 10
    a = random.randint(lo, hi)
    b = random.randint(lo, a if op=='-' else hi)
    ans = a + b if op=='+' else a - b
    proc = (f"📝 *Procedimiento:*\n```\n  {a}\n{op} {b}\n{'─'*max(len(str(a)),len(str(b))+2)}\n  {ans}\n```\n"
            f"Suma/resta columna por columna de derecha a izquierda.\n✅ *Respuesta: {ans}*")
    return {"q": f"Resuelve: {a} {op} {b} = ?", "a": str(ans), "proc": proc,
            "hint": f"Empieza por las unidades: {a%10} {op} {b%10}"}

def _multiplicacion(diff_level):
    ranges = {1:(2,9,2,9), 2:(10,99,2,12), 3:(10,99,10,99)}
    la,ha,lb,hb = ranges[diff_level]
    a,b = random.randint(la,ha), random.randint(lb,hb)
    ans = a*b
    proc = (f"📝 *Procedimiento:*\n{a} × {b}\n"
            f"• {a} × {b%10} = {a*(b%10)}\n"
            f"• {a} × {(b//10)*10} = {a*((b//10)*10)}\n"
            f"• Total: {ans}\n✅ *Respuesta: {ans}*")
    return {"q": f"Resuelve: {a} × {b} = ?", "a": str(ans), "proc": proc,
            "hint": f"Multiplica primero por las unidades de {b}"}

def _division(diff_level):
    ranges = {1:(2,9,2,12), 2:(2,12,10,50), 3:(2,20,10,99)}
    ld,hd,lq,hq = ranges[diff_level]
    d = random.randint(ld,hd); q = random.randint(lq,hq); n = d*q
    proc = (f"📝 *Procedimiento:*\n{n} ÷ {d}\n"
            f"¿Cuántas veces cabe {d} en {n}?\n"
            f"{d} × {q} = {n}\n✅ *Respuesta: {q}*\n"
            f"*Verificación:* {q} × {d} = {q*d} ✅")
    return {"q": f"Resuelve: {n} ÷ {d} = ?", "a": str(q), "proc": proc,
            "hint": f"Piensa: {d} × ? = {n}"}

def _fracciones(diff_level):
    ops = {1:['suma'], 2:['suma','resta'], 3:['suma','resta','mult','div']}
    op = random.choice(ops[diff_level])
    an,ad = random.randint(1,5), random.randint(2,8)
    bn,bd = random.randint(1,5), random.randint(2,8)
    fa,fb = Rational(an,ad), Rational(bn,bd)
    if op=='resta' and fa<fb: fa,fb=fb,fa; an,ad,bn,bd=bn,bd,an,ad
    if op=='suma':   res=fa+fb; sym='+'
    elif op=='resta':res=fa-fb; sym='-'
    elif op=='mult': res=fa*fb; sym='×'
    else:            res=fa/fb; sym='÷'
    mcm = int(lcm(ad,bd))
    proc = (f"📝 *Procedimiento — {op.capitalize()} de fracciones:*\n"
            f"{an}/{ad} {sym} {bn}/{bd}\n"
            f"MCM({ad},{bd}) = {mcm}\n= {res}\n✅ *Respuesta: {res}*")
    return {"q": f"Resuelve: {an}/{ad} {sym} {bn}/{bd} = ?", "a": str(res),
            "proc": proc, "hint": "Busca el MCM de los denominadores"}

def _porcentaje(diff_level):
    pcts = {1:[10,25,50], 2:[15,20,30,75], 3:[12,17,33,66]}
    p = random.choice(pcts[diff_level])
    base = random.randint(2,20)*10
    ans = round(base*p/100, 2)
    proc = (f"📝 *Procedimiento:*\n{p}% de {base}\n"
            f"= {p}/100 × {base}\n= {p*base}/100\n= {ans}\n✅ *Respuesta: {ans}*")
    return {"q": f"¿Cuánto es el {p}% de {base}?", "a": str(ans),
            "proc": proc, "hint": f"Divide {base} entre 100 y multiplica por {p}"}

# ── SECUNDARIA ────────────────────────────────────────────────────────────────
def _ecuacion_lineal(diff_level):
    a,c = random.randint(2,8), random.randint(1,5)
    b,d = random.randint(-10,10), random.randint(-10,10)
    while a==c: c=random.randint(1,5)
    sol = solve(a*x+b-c*x-d, x)[0]
    proc = (f"📝 *Procedimiento:*\n{a}x + {b} = {c}x + {d}\n\n"
            f"Paso 1: {a}x - {c}x = {d} - {b}\n"
            f"  {a-c}x = {d-b}\n"
            f"Paso 2: x = {d-b}/{a-c} = {sol}\n✅ *x = {sol}*\n\n"
            f"✔ Verificación: {a}({sol})+{b} = {a*sol+b} | {c}({sol})+{d} = {c*sol+d}")
    return {"q": f"Resuelve: {a}x + {b} = {c}x + {d}", "a": str(sol),
            "proc": proc, "hint": "Agrupa los x a un lado y los números al otro"}

def _cuadratica(diff_level):
    r1,r2 = random.randint(-6,6), random.randint(-6,6)
    expr = sp.expand((x-r1)*(x-r2))
    a_c,b_c,c_c = int(expr.coeff(x,2)), int(expr.coeff(x,1)), int(expr.coeff(x,0))
    disc = b_c**2 - 4*a_c*c_c
    proc = (f"📝 *Procedimiento — Fórmula general:*\n"
            f"{expr} = 0\na={a_c}, b={b_c}, c={c_c}\n\n"
            f"x = (-{b_c} ± √({b_c}²-4·{a_c}·{c_c})) / 2·{a_c}\n"
            f"x = ({-b_c} ± √{disc}) / {2*a_c}\n"
            f"x₁ = {r1},  x₂ = {r2}\n✅ *Soluciones: x={r1} y x={r2}*")
    sols = f"{min(r1,r2)} y {max(r1,r2)}"
    return {"q": f"Resuelve: {expr} = 0  (escribe las dos soluciones separadas por 'y')",
            "a": sols, "proc": proc,
            "hint": "Usa la fórmula cuadrática x = (-b ± √(b²-4ac)) / 2a",
            "alts": [f"{max(r1,r2)} y {min(r1,r2)}", f"x={r1},x={r2}", f"{r1},{r2}"]}

def _trigonometria(diff_level):
    tbl = {30:("1/2","√3/2","1/√3"), 45:("√2/2","√2/2","1"), 60:("√3/2","1/2","√3")}
    ang = random.choice([30,45,60])
    fn  = random.choice(["sen","cos","tan"])
    idx = {"sen":0,"cos":1,"tan":2}[fn]
    ans = tbl[ang][idx]
    proc = (f"📝 *Valores especiales de trigonometría:*\n"
            f"```\nÁng | sen   | cos   | tan\n"
            f" 30°| 1/2   | √3/2  | 1/√3\n"
            f" 45°| √2/2  | √2/2  | 1\n"
            f" 60°| √3/2  | 1/2   | √3\n```\n"
            f"{fn}({ang}°) = {ans}\n✅ *Respuesta: {ans}*")
    return {"q": f"¿Cuánto vale {fn}({ang}°)?", "a": ans, "proc": proc,
            "hint": "Memoriza la tabla de valores especiales (30, 45, 60)"}

def _logaritmo(diff_level):
    base = random.choice([2,3,5,10])
    exp_v = random.randint(1, {1:2,2:3,3:4}[diff_level])
    arg = base**exp_v
    proc = (f"📝 *Procedimiento:*\nlog_{base}({arg}) = x\n"
            f"Significa: {base}^x = {arg}\n{base}^{exp_v} = {arg}\n✅ *x = {exp_v}*")
    return {"q": f"Resuelve: log_{base}({arg}) = ?", "a": str(exp_v), "proc": proc,
            "hint": f"¿A qué potencia elevo {base} para obtener {arg}?"}

def _algebra_expresion(diff_level):
    a,b,c,d = [random.randint(1,7) for _ in range(4)]
    expr = sp.expand((a*x+b)*(c*x+d))
    proc = (f"📝 *Producto de binomios (FOIL):*\n"
            f"({a}x+{b})({c}x+{d})\n"
            f"• {a}x·{c}x = {a*c}x²\n"
            f"• {a}x·{d}  = {a*d}x\n"
            f"• {b}·{c}x  = {b*c}x\n"
            f"• {b}·{d}   = {b*d}\n"
            f"= {a*c}x² + {a*d+b*c}x + {b*d}\n✅ *Respuesta: {expr}*")
    return {"q": f"Expande: ({a}x+{b})({c}x+{d})", "a": str(expr), "proc": proc,
            "hint": "Aplica FOIL: Primeros, Externos, Internos, Últimos"}

# ── UNIVERSIDAD ───────────────────────────────────────────────────────────────
def _derivada(diff_level):
    n = random.randint(2, {1:3,2:5,3:7}[diff_level])
    a,b,c = random.randint(1,6), random.randint(1,6), random.randint(1,6)
    f  = a*x**n + b*x**2 + c*x
    df = diff(f, x)
    proc = (f"📝 *Derivación — Regla de la potencia:*\n"
            f"f(x) = {a}x^{n} + {b}x² + {c}x\n\n"
            f"d/dx[xⁿ] = n·xⁿ⁻¹\n\n"
            f"• d/dx[{a}x^{n}] = {a*n}x^{n-1}\n"
            f"• d/dx[{b}x²]   = {2*b}x\n"
            f"• d/dx[{c}x]    = {c}\n\n"
            f"f'(x) = {df}\n✅ *f'(x) = {df}*")
    return {"q": f"Deriva: f(x) = {a}x^{n} + {b}x² + {c}x", "a": str(df),
            "proc": proc, "hint": "Regla de la potencia: d/dx[xⁿ] = n·xⁿ⁻¹"}

def _integral(diff_level):
    n = random.randint(2, {1:3,2:5,3:6}[diff_level])
    a,b = random.randint(1,6), random.randint(1,6)
    f   = a*x**n + b*x
    res = integrate(f, x)
    proc = (f"📝 *Integración — Regla de la potencia:*\n"
            f"∫({a}x^{n} + {b}x) dx\n\n"
            f"∫xⁿ dx = xⁿ⁺¹/(n+1) + C\n\n"
            f"• ∫{a}x^{n} dx = {a}/{n+1}·x^{n+1}\n"
            f"• ∫{b}x dx    = {b}/2·x²\n\n"
            f"= {res} + C\n✅ *Respuesta: {res} + C*")
    return {"q": f"Integra: ∫ ({a}x^{n} + {b}x) dx  (sin la constante C)", "a": str(res),
            "proc": proc, "hint": "∫xⁿ dx = xⁿ⁺¹/(n+1) + C"}

def _matriz_suma(diff_level):
    n = {1:2, 2:2, 3:3}[diff_level]
    A = [[random.randint(1,9) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(1,9) for _ in range(n)] for _ in range(n)]
    C = [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]
    def fmt(M): return " | ".join([" ".join(map(str,r)) for r in M])
    proc = (f"📝 *Suma de matrices elemento a elemento:*\n"
            f"A = [{fmt(A)}]\nB = [{fmt(B)}]\n"
            f"A+B = [{fmt(C)}]\n✅ *Respuesta: [{fmt(C)}]*")
    ans = str(C).replace(" ","")
    return {"q": f"Suma las matrices A=[{fmt(A)}] y B=[{fmt(B)}]\n(Responde en formato [[a,b],[c,d]])",
            "a": ans, "proc": proc, "hint": "Suma los elementos en la misma posición"}

def _edo_separable(diff_level):
    a = random.randint(1,4)
    proc = (f"📝 *Procedimiento — Variables separables:*\n"
            f"dy/dx = {a}xy\n\n"
            f"Paso 1: Separar → dy/y = {a}x dx\n"
            f"Paso 2: Integrar → ln|y| = {a}x²/2 + C\n"
            f"Paso 3: Despejar → y = Ae^({a}x²/2)\n✅ *y = Ae^({a}x²/2)*")
    return {"q": f"Resuelve la EDO: dy/dx = {a}xy  (escribe la solución general)",
            "a": f"Ae^({a}x**2/2)", "proc": proc,
            "hint": "Separa dy/y del lado izquierdo y dx del derecho, luego integra"}

# ── DISPATCHER ────────────────────────────────────────────────────────────────
GENERATORS = {
    "primaria": {
        "suma_resta":    _suma_resta,
        "multiplicacion":_multiplicacion,
        "division":      _division,
        "fracciones":    _fracciones,
        "porcentajes":   _porcentaje,
        "decimales":     lambda d: _suma_resta(d),  # reuse
    },
    "secundaria": {
        "algebra":       _algebra_expresion,
        "ecuaciones":    _ecuacion_lineal,
        "cuadraticas":   _cuadratica,
        "trigonometria": _trigonometria,
        "logaritmos":    _logaritmo,
        "probabilidad":  _porcentaje,   # reuse
    },
    "universidad": {
        "calculo_diferencial":      _derivada,
        "calculo_integral":         _integral,
        "algebra_lineal":           _matriz_suma,
        "ecuaciones_diferenciales": _edo_separable,
    }
}

def generate(level: str, topic: str, difficulty: int = 1) -> dict:
    gen = GENERATORS.get(level, {}).get(topic)
    if gen:
        try:
            ex = gen(difficulty)
            ex.setdefault("alts", [])
            return ex
        except Exception as e:
            pass
    # fallback
    a,b = random.randint(10,99), random.randint(10,99)
    return {"q": f"{a} + {b} = ?", "a": str(a+b),
            "proc": f"✅ *{a} + {b} = {a+b}*", "hint": "Suma los dos números", "alts": []}

def check(user_ans: str, correct: str, alts: list = None) -> bool:
    return _check(user_ans, correct, alts)
