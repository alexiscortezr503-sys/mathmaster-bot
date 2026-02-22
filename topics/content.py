"""Contenido matemático completo para todos los niveles"""

CONTENT = {

# ══════════════════ PRIMARIA ══════════════════════════════════════════════════

"primaria_suma_resta": """➕ *SUMA Y RESTA*

━━━━━━━━━━━━━━━━━━━━
📖 *Suma — Juntar cantidades*
```
  347
+ 256
─────
  603
```
• Unidades: 7+6=13 → escribo 3, llevo 1
• Decenas: 4+5+1=10 → escribo 0, llevo 1
• Centenas: 3+2+1=6 ✅

📖 *Resta con préstamo*
```
  523
- 287
─────
  236
```
• 3-7 no se puede → pido prestado → 13-7=6
• 12-1-8=3 → 5-1-2=2 ✅

💡 *Verificación:* 236+287=523 ✅""",

"primaria_multiplicacion": """✖️ *MULTIPLICACIÓN*

━━━━━━━━━━━━━━━━━━━━
📖 *Multiplicar = sumar varias veces*
5×3 = 5+5+5 = 15

*Multiplicación de 2 cifras:*
```
   47
×  36
─────
  282  ← 47×6
+1410  ← 47×30
─────
 1692 ✅
```
💡 *Tablas del 1 al 12:* ¡La base de todo!""",

"primaria_division": """➗ *DIVISIÓN*

━━━━━━━━━━━━━━━━━━━━
Dividendo ÷ Divisor = Cociente (Resto)

*Ejemplo: 847 ÷ 4*
```
847 ÷ 4 = 211  Resto: 3
```
*Verificación:* 211×4+3 = 847 ✅

💡 *Divisibilidad:*
• ÷2: termina en par
• ÷3: suma de dígitos ÷3
• ÷5: termina en 0 o 5
• ÷10: termina en 0""",

"primaria_fracciones": """½ *FRACCIONES*

━━━━━━━━━━━━━━━━━━━━
*Suma — diferente denominador:*
```
1/3 + 1/4 → MCM=12
= 4/12 + 3/12 = 7/12 ✅
```
*Multiplicación:*
```
2/3 × 3/4 = 6/12 = 1/2 ✅
```
*División (multiplica por recíproco):*
```
2/3 ÷ 4/5 = 2/3 × 5/4 = 10/12 = 5/6 ✅
```""",

"primaria_porcentajes": """📊 *PORCENTAJES*

━━━━━━━━━━━━━━━━━━━━
X% de N = (X × N) / 100

*Ejemplo:* 30% de 200
= (30×200)/100 = 60 ✅

*Truco:*
• 50% → divide entre 2
• 25% → divide entre 4
• 10% → mueve el punto decimal
• 1%  → divide entre 100""",

"primaria_decimales": """🔢 *DECIMALES*

━━━━━━━━━━━━━━━━━━━━
*Suma:* alinea los puntos decimales
```
  12.35
+  4.80
──────
  17.15 ✅
```
*Multiplicación:*
```
2.5 × 1.2 = 3.00
(25×12=300, 2 decimales) ✅
```
*División:* convierte el divisor a entero multiplicando ambos por 10, 100...""",

"primaria_geometria_basica": """📐 *GEOMETRÍA BÁSICA*

━━━━━━━━━━━━━━━━━━━━
*Perímetro* = suma de todos los lados

*Cuadrado:* P = 4×lado | A = lado²
*Rectángulo:* P = 2(largo+ancho) | A = largo×ancho
*Triángulo:* P = a+b+c | A = base×altura/2
*Círculo:* C = 2πr | A = πr²  (π≈3.1416)

*Ejemplo:* Rectángulo 8×5
P = 2(8+5) = 26 cm
A = 8×5 = 40 cm² ✅""",

"primaria_problemas_logica": """🧩 *PROBLEMAS DE LÓGICA*

━━━━━━━━━━━━━━━━━━━━
*Pasos para resolver un problema:*
1. Lee con atención
2. Identifica los datos
3. Identifica lo que piden
4. Elige la operación
5. Resuelve y verifica

*Ejemplo:*
María tiene 24 canicas. Le da 1/3 a su hermano.
¿Cuántas le quedan?

Datos: 24 canicas, da 1/3
1/3 de 24 = 8 (las que da)
24 - 8 = 16 ✅

*María se queda con 16 canicas*""",

# ══════════════════ SECUNDARIA ════════════════════════════════════════════════

"secundaria_algebra": """📊 *ÁLGEBRA*

━━━━━━━━━━━━━━━━━━━━
*Simplificación:*
3x + 5y - 2x + y = x + 6y ✅

*Productos notables:*
```
(a+b)² = a² + 2ab + b²
(a-b)² = a² - 2ab + b²
(a+b)(a-b) = a² - b²
```
*FOIL:* (2x+3)(x+4)
= 2x²+8x+3x+12 = 2x²+11x+12 ✅

*Factorización:*
x²+5x+6 = (x+2)(x+3) ✅""",

"secundaria_ecuaciones": """⚖️ *ECUACIONES*

━━━━━━━━━━━━━━━━━━━━
*1° grado:*
3x-7=2x+5 → x=12 ✅

*Sistema 2×2:*
```
2x+y=7  ...(1)
x-y=2   ...(2)
```
Suma: 3x=9 → x=3
(2): 3-y=2 → y=1 ✅

*Método de sustitución:*
De (2): x=y+2
En (1): 2(y+2)+y=7 → 3y=3 → y=1 ✅""",

"secundaria_cuadraticas": """📐 *ECUACIONES CUADRÁTICAS*

━━━━━━━━━━━━━━━━━━━━
*Fórmula general:*
x = (-b ± √(b²-4ac)) / 2a

*Discriminante:*
• b²-4ac > 0 → 2 soluciones reales
• b²-4ac = 0 → 1 solución real
• b²-4ac < 0 → sin soluciones reales

*Ejemplo:* x²-5x+6=0
x = (5±√1)/2 → x=3, x=2 ✅

*Completar cuadrado:*
x²+6x+5=0
(x+3)²=4 → x=-1, x=-5 ✅""",

"secundaria_trigonometria": """📐 *TRIGONOMETRÍA*

━━━━━━━━━━━━━━━━━━━━
*SOH-CAH-TOA:*
```
sen(θ) = Opuesto/Hipotenusa
cos(θ) = Adyacente/Hipotenusa
tan(θ) = Opuesto/Adyacente
```
*Tabla especial:*
```
Áng | sen   | cos   | tan
30° | 1/2   | √3/2  | 1/√3
45° | √2/2  | √2/2  | 1
60° | √3/2  | 1/2   | √3
```
*Identidades:*
sen²θ + cos²θ = 1
tan(θ) = sen(θ)/cos(θ)""",

"secundaria_logaritmos": """🔢 *LOGARITMOS*

━━━━━━━━━━━━━━━━━━━━
log_b(x)=y ⟺ bʸ=x

*Propiedades:*
```
log(a·b) = log(a)+log(b)
log(a/b) = log(a)-log(b)
log(aⁿ)  = n·log(a)
log_b(b) = 1
log_b(1) = 0
```
*Ejemplo:* log₂(8)=3 porque 2³=8 ✅
*Cambio de base:* log_b(x) = ln(x)/ln(b)""",

"secundaria_probabilidad": """🎲 *PROBABILIDAD*

━━━━━━━━━━━━━━━━━━━━
P(A) = casos favorables / casos totales

*Reglas:*
• 0 ≤ P(A) ≤ 1
• P(A) + P(A') = 1
• P(A∪B) = P(A)+P(B)-P(A∩B)
• P(A∩B) = P(A)·P(B) si son independientes

*Ejemplo:* Dado de 6 caras, P(par)
= {2,4,6}/6 = 3/6 = 1/2 ✅

*Permutaciones:* nPr = n!/(n-r)!
*Combinaciones:* nCr = n!/(r!(n-r)!)""",

"secundaria_funciones": """📈 *FUNCIONES*

━━━━━━━━━━━━━━━━━━━━
f: A→B  asigna a cada x un único y

*Tipos principales:*
• Lineal: f(x)=mx+b (línea recta)
• Cuadrática: f(x)=ax²+bx+c (parábola)
• Exponencial: f(x)=aˣ
• Logarítmica: f(x)=log(x)

*Dominio y rango:*
f(x)=√x → Dominio: x≥0, Rango: y≥0

*Composición:* (f∘g)(x) = f(g(x))
*Inversa:* despeja x en términos de y""",

"secundaria_geometria_analitica": """🔷 *GEOMETRÍA ANALÍTICA*

━━━━━━━━━━━━━━━━━━━━
*Distancia entre dos puntos:*
d = √((x₂-x₁)²+(y₂-y₁)²)

*Punto medio:*
M = ((x₁+x₂)/2, (y₁+y₂)/2)

*Ecuación de la recta:*
• Pendiente-intercepto: y=mx+b
• Dos puntos: m=(y₂-y₁)/(x₂-x₁)

*Circunferencia:* (x-h)²+(y-k)²=r²
*Parábola:* y=a(x-h)²+k (vértice h,k)
*Elipse:* x²/a²+y²/b²=1""",

"secundaria_numeros_complejos": """🔢 *NÚMEROS COMPLEJOS*

━━━━━━━━━━━━━━━━━━━━
z = a + bi  donde i=√(-1), i²=-1

*Operaciones:*
```
Suma: (a+bi)+(c+di) = (a+c)+(b+d)i
Mult: (a+bi)(c+di) = (ac-bd)+(ad+bc)i
```
*Módulo:* |z| = √(a²+b²)
*Conjugado:* z̄ = a-bi
*División:* z₁/z₂ = z₁·z̄₂/|z₂|²

*Forma polar:* z = r(cosθ+isenθ)
*Fórmula de Euler:* eⁱᶿ = cosθ+isenθ
*De Moivre:* zⁿ = rⁿ(cos(nθ)+isen(nθ))""",

"secundaria_estadistica": """📊 *ESTADÍSTICA*

━━━━━━━━━━━━━━━━━━━━
*Medidas de tendencia central:*
Datos: {2, 4, 4, 6, 8}

• *Media:* (2+4+4+6+8)/5 = 4.8
• *Mediana:* valor central = 4
• *Moda:* valor más frecuente = 4

*Medidas de dispersión:*
• *Rango:* máx-mín = 8-2 = 6
• *Varianza:* promedio de (xᵢ-x̄)²
• *Desv. estándar:* σ = √varianza

*Regla empírica (distribución normal):*
• 68% datos entre μ±σ
• 95% datos entre μ±2σ
• 99.7% datos entre μ±3σ""",

# ══════════════════ UNIVERSIDAD ══════════════════════════════════════════════

"universidad_calculo_diferencial": """∂ *CÁLCULO DIFERENCIAL*

━━━━━━━━━━━━━━━━━━━━
*Reglas de derivación:*
```
d/dx[xⁿ]    = n·xⁿ⁻¹
d/dx[eˣ]    = eˣ
d/dx[ln x]  = 1/x
d/dx[sen x] = cos x
d/dx[cos x] = -sen x
```
*Cadena:* [f(g(x))]' = f'(g(x))·g'(x)
*Producto:* (fg)' = f'g+fg'
*Cociente:* (f/g)' = (f'g-fg')/g²

*Ejemplo cadena:*
f(x)=(3x²+2)⁵
f'(x)=30x(3x²+2)⁴ ✅""",

"universidad_calculo_integral": """∫ *CÁLCULO INTEGRAL*

━━━━━━━━━━━━━━━━━━━━
*Reglas:*
```
∫xⁿ dx    = xⁿ⁺¹/(n+1)+C
∫eˣ dx    = eˣ+C
∫1/x dx   = ln|x|+C
∫sen x dx = -cos x+C
∫cos x dx = sen x+C
```
*Integral definida:*
∫₀²(x²+1)dx = [x³/3+x]₀² = 14/3 ✅

*Técnicas:*
• Sustitución u
• Integración por partes: ∫u dv = uv-∫v du
• Fracciones parciales""",

"universidad_calculo_multivariable": """🌐 *CÁLCULO MULTIVARIABLE*

━━━━━━━━━━━━━━━━━━━━
*Derivadas parciales:*
f(x,y)=x²y+3xy²
∂f/∂x = 2xy+3y²
∂f/∂y = x²+6xy

*Gradiente:* ∇f = (∂f/∂x, ∂f/∂y)

*Regla de la cadena:*
dz/dt = ∂z/∂x·dx/dt + ∂z/∂y·dy/dt

*Integrales dobles:*
∬f(x,y)dA = ∫∫f(x,y)dx dy

*Teorema de Green, Stokes, Divergencia*
*Multiplicadores de Lagrange para optimización*""",

"universidad_algebra_lineal": """🔢 *ÁLGEBRA LINEAL*

━━━━━━━━━━━━━━━━━━━━
*Multiplicación de matrices:*
```
[1 2]×[5 6] = [19 22]
[3 4] [7 8]   [43 50]
```
*Determinante 2×2:* ad-bc
*Determinante 3×3:* expansión por cofactores

*Inversa:* A·A⁻¹=I
*Eigenvalores:* det(A-λI)=0
*Sistema Ax=b:* Gauss-Jordan

*Espacios vectoriales:*
• Base, dimensión, rango
• Transformaciones lineales
• Diagonalización""",

"universidad_ecuaciones_diferenciales": """📉 *ECUACIONES DIFERENCIALES*

━━━━━━━━━━━━━━━━━━━━
*Variables separables:*
dy/dx=2xy → y=Ae^(x²) ✅

*EDO lineal 1° orden:*
dy/dx+2y=4 → y=2+Ce^(-2x) ✅

*EDO 2° orden homogénea:*
y''-5y'+6y=0
r²-5r+6=0 → r=2,3
y=C₁e^(2x)+C₂e^(3x) ✅

*Transformada de Laplace:*
L{f(t)} = ∫₀^∞ e^(-st)f(t)dt
L{1}=1/s | L{eᵃᵗ}=1/(s-a)
L{y'}=sY-y(0)""",

"universidad_estadistica_inferencial": """📊 *ESTADÍSTICA INFERENCIAL*

━━━━━━━━━━━━━━━━━━━━
*Distribuciones:*
• Normal: N(μ,σ²)
• t-Student: muestras pequeñas
• Chi-cuadrado: prueba de bondad
• F de Fisher: ANOVA

*Intervalos de confianza:*
IC = x̄ ± z·(σ/√n)

*Prueba de hipótesis:*
1. H₀ y H₁
2. Nivel de significancia α
3. Estadístico de prueba
4. Región de rechazo
5. Conclusión

*Regresión lineal:* ŷ = β₀+β₁x
*Correlación:* r = Σ(x-x̄)(y-ȳ)/√[...]""",

"universidad_analisis_real": """🔬 *ANÁLISIS REAL*

━━━━━━━━━━━━━━━━━━━━
*Sucesiones y límites:*
lim(n→∞) 1/n = 0

*Criterios de convergencia:*
• Razón (D'Alembert): lim|aₙ₊₁/aₙ|
• Raíz (Cauchy): lim|aₙ|^(1/n)
• Integral de Cauchy

*Continuidad:* f continua en x₀ si
lim(x→x₀)f(x) = f(x₀)

*Teoremas fundamentales:*
• Bolzano-Weierstrass
• Heine-Cantor
• Teorema del valor medio
• Teorema de Taylor""",

"universidad_matematica_discreta": """💻 *MATEMÁTICA DISCRETA*

━━━━━━━━━━━━━━━━━━━━
*Lógica proposicional:*
• ∧ (and) | ∨ (or) | ¬ (not)
• → (implica) | ↔ (bicondicional)

*Teoría de conjuntos:*
A∪B, A∩B, A-B, Aᶜ, A×B

*Teoría de grafos:*
• Grafo: G=(V,E)
• Grado, camino, ciclo
• Árbol, árbol generador mínimo
• Dijkstra, Floyd-Warshall

*Inducción matemática:*
1. Base: P(1) verdadero
2. Paso: P(k)→P(k+1)
3. Conclusión: P(n) para todo n

*Combinatoria:* permutaciones, combinaciones, principio de inclusión-exclusión""",

# ══════════════════ AVANZADO ══════════════════════════════════════════════════

"avanzado_teoria_numeros": """🔢 *TEORÍA DE NÚMEROS*

━━━━━━━━━━━━━━━━━━━━
*Divisibilidad y primos:*
• Teorema fundamental: todo n>1 = producto de primos
• Criba de Eratóstenes
• MCD, MCM: algoritmo de Euclides

*Congruencias:*
a ≡ b (mod n) ⟺ n|(a-b)
*Pequeño Teorema de Fermat:*
aᵖ ≡ a (mod p), p primo

*Funciones:*
• φ(n) de Euler: números coprimos con n
• d(n): cantidad de divisores
• σ(n): suma de divisores

*Teorema Chino del Resto:*
Sistema de congruencias con módulos coprimos""",

"avanzado_algebra_abstracta": """⚛️ *ÁLGEBRA ABSTRACTA*

━━━━━━━━━━━━━━━━━━━━
*Grupos:*
(G,·) con clausura, asociatividad,
identidad e, inverso a⁻¹

*Subgrupos, orden, índice*
*Teorema de Lagrange:* |H| divide |G|
*Grupos cíclicos:* G=⟨g⟩

*Anillos y campos:*
• Anillo: grupo abeliano + multiplicación
• Campo: anillo con inversos multiplicativos

*Homomorfismos e isomorfismos*
*Núcleo e imagen*
*Teoremas de isomorfismo*""",

"avanzado_analisis_complejo": """🔬 *ANÁLISIS COMPLEJO*

━━━━━━━━━━━━━━━━━━━━
*Funciones analíticas:*
Ecuaciones de Cauchy-Riemann:
∂u/∂x = ∂v/∂y | ∂u/∂y = -∂v/∂x

*Integral de contorno:*
∮_C f(z)dz

*Teorema de Cauchy:*
Si f analítica en D: ∮f(z)dz=0

*Teorema de los residuos:*
∮f(z)dz = 2πi·Σ Res(f,zₖ)

*Series de Laurent:*
f(z) = Σ aₙ(z-z₀)ⁿ (n de -∞ a ∞)

*Transformada de Fourier y Z*""",

"avanzado_edp": """🌊 *ECUACIONES EN DERIVADAS PARCIALES*

━━━━━━━━━━━━━━━━━━━━
*Clasificación:*
• Elíptica: ∇²u=0 (Laplace)
• Parabólica: ∂u/∂t=α∇²u (calor)
• Hiperbólica: ∂²u/∂t²=c²∇²u (onda)

*Ec. de calor:* ∂u/∂t = α∂²u/∂x²
Solución: separación de variables

*Ec. de onda:* ∂²u/∂t² = c²∂²u/∂x²
Solución: d'Alembert

*Ec. de Laplace:* ∇²u=0
Solución: funciones armónicas

*Métodos:* Separación de variables,
Transformadas, Diferencias finitas""",

"avanzado_topologia": """🔷 *TOPOLOGÍA*

━━━━━━━━━━━━━━━━━━━━
*Espacios topológicos:*
(X,τ): conjuntos abiertos con
∅,X∈τ | uniones e intersecciones finitas ∈τ

*Continuidad topológica:*
f continua ⟺ preimagen de abierto es abierto

*Propiedades:*
• Hausdorff (T₂): puntos separables
• Compacto: toda cubierta tiene subcubierta finita
• Conexo: no se puede partir en dos abiertos

*Homeomorfismo:* biyección continua con
inversa continua

*Homotopía y grupo fundamental π₁(X)*
*Superficies: esfera, toro, banda de Möbius*""",

"avanzado_geometria_diferencial": """📐 *GEOMETRÍA DIFERENCIAL*

━━━━━━━━━━━━━━━━━━━━
*Curvas en ℝ³:*
• Vector tangente: T = r'/|r'|
• Curvatura: κ = |T'|/|r'|
• Torsión: τ = -(N'·B)/|r'|
• Fórmulas de Frenet-Serret

*Superficies:*
• Primera forma fundamental
• Segunda forma fundamental
• Curvatura gaussiana: K = κ₁κ₂
• Curvatura media: H = (κ₁+κ₂)/2

*Teorema Egregium de Gauss:*
K es invariante bajo isometría

*Geodésicas: curvas de longitud mínima*
*Teorema de Gauss-Bonnet*""",
}

def get(level: str, topic: str) -> str | None:
    return CONTENT.get(f"{level}_{topic}")
