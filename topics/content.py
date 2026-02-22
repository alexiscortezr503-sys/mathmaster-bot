"""Contenido educativo completo para todos los niveles y temas"""

CONTENT = {

# ══════════════════════ PRIMARIA ══════════════════════════════════════════════

"primaria_suma_resta": """➕ *SUMA Y RESTA*

━━━━━━━━━━━━━━━━━━━━
📖 *Suma — Juntar cantidades*

```
  347
+ 256
─────
```
• Unidades: 7+6=13 → escribo 3, llevo 1
• Decenas:  4+5+1=10 → escribo 0, llevo 1
• Centenas: 3+2+1=6
```
  347
+ 256
─────
  603  ✅
```

━━━━━━━━━━━━━━━━━━━━
📖 *Resta — Quitar una cantidad*

```
  523
- 287
─────
```
• 3-7 no se puede → pido prestado → 13-7=6
• 2-1-8 no se puede → pido prestado → 12-1-8=3
• 5-1-2=2
```
  523
- 287
─────
  236  ✅
```
💡 *Verificación:* 236 + 287 = 523 ✅""",

"primaria_multiplicacion": """✖️ *MULTIPLICACIÓN*

━━━━━━━━━━━━━━━━━━━━
📖 *Multiplicar = sumar varias veces*
5 × 3 = 5+5+5 = 15

*Multiplicación de 2 cifras:*
```
   47
×  36
─────
  282   ← 47×6
+1410   ← 47×30
─────
 1692  ✅
```

*Pasos:*
1. Multiplica por las unidades (6): 47×6=282
2. Multiplica por las decenas (3), agrega un 0: 47×3=141 → 1410
3. Suma los resultados parciales

💡 *Tip:* ¡Aprende las tablas del 1 al 12!""",

"primaria_division": """➗ *DIVISIÓN*

━━━━━━━━━━━━━━━━━━━━
📖 *Dividir = repartir en partes iguales*

*Partes de la división:*
• Dividendo ÷ Divisor = Cociente (Resto)

*Ejemplo: 847 ÷ 4*
```
847 ÷ 4 = 211  (Resto: 3)

8 ÷ 4 = 2  → bajo el 4
04 ÷ 4 = 1 → bajo el 7
07 ÷ 4 = 1 → resto 3
```
*Verificación:* 211 × 4 + 3 = 847 ✅

━━━━━━━━━━━━━━━━━━━━
💡 *Reglas de divisibilidad:*
• ÷2: termina en número par
• ÷3: suma de dígitos divisible por 3
• ÷5: termina en 0 o 5
• ÷10: termina en 0""",

"primaria_fracciones": """½ *FRACCIONES*

━━━━━━━━━━━━━━━━━━━━
📖 *Partes de una fracción:*
• Numerador (arriba): partes que tienes
• Denominador (abajo): partes totales

*Suma — mismo denominador:*
2/5 + 1/5 = 3/5

*Suma — diferente denominador:*
```
1/3 + 1/4
MCM(3,4) = 12
= 4/12 + 3/12 = 7/12  ✅
```

*Multiplicación:*
```
2/3 × 3/4 = 6/12 = 1/2  ✅
```

*División (multiplica por el recíproco):*
```
2/3 ÷ 4/5 = 2/3 × 5/4 = 10/12 = 5/6  ✅
```

💡 *Para simplificar:* divide numerador y denominador por su MCD""",

"primaria_porcentajes": """📊 *PORCENTAJES*

━━━━━━━━━━━━━━━━━━━━
📖 *Porcentaje = "por cada 100"*
25% = 25/100 = 0.25

*Fórmula básica:*
X% de N = (X × N) / 100

*Ejemplo 1:* ¿Cuánto es el 30% de 200?
= (30 × 200) / 100 = 60 ✅

*Ejemplo 2:* Un artículo costaba $80 y tiene 15% de descuento.
• Descuento = 15% × 80 = $12
• Precio final = 80 - 12 = $68 ✅

*Porcentajes especiales fáciles:*
• 50% → divide entre 2
• 25% → divide entre 4
• 10% → mueve el punto decimal un lugar
• 1%  → divide entre 100""",

# ══════════════════════ SECUNDARIA ════════════════════════════════════════════

"secundaria_algebra": """📊 *ÁLGEBRA*

━━━━━━━━━━━━━━━━━━━━
📖 *Expresiones algebraicas*
• Variable: letra que representa un número (x, y, n)
• Término: 3x, -5y², 7
• Coeficiente: número que multiplica la variable

*Simplificación:*
```
3x + 5y - 2x + y
= (3x-2x) + (5y+y)
= x + 6y  ✅
```

━━━━━━━━━━━━━━━━━━━━
*Productos notables:*
```
(a+b)² = a² + 2ab + b²
(a-b)² = a² - 2ab + b²
(a+b)(a-b) = a² - b²
```

*Ejemplo:* (x+3)²
= x² + 2(x)(3) + 3² = x² + 6x + 9 ✅

*FOIL — Binomios:*
(2x+3)(x+4)
= 2x²+8x+3x+12 = 2x²+11x+12 ✅""",

"secundaria_ecuaciones": """⚖️ *ECUACIONES*

━━━━━━━━━━━━━━━━━━━━
📖 *Ecuación de 1° grado:*
```
3x - 7 = 2x + 5
3x - 2x = 5 + 7
x = 12  ✅
```
Verificación: 3(12)-7 = 29 = 2(12)+5 ✅

━━━━━━━━━━━━━━━━━━━━
📖 *Sistemas de ecuaciones:*
```
2x + y = 7   ...(1)
x - y = 2    ...(2)
```
Suma (1)+(2): 3x = 9 → x = 3
Sustituye: 3 - y = 2 → y = 1
Solución: x=3, y=1 ✅""",

"secundaria_cuadraticas": """📐 *ECUACIONES CUADRÁTICAS*

━━━━━━━━━━━━━━━━━━━━
*Fórmula general:*
ax² + bx + c = 0
x = (-b ± √(b²-4ac)) / 2a

*Discriminante (b²-4ac):*
• > 0: dos soluciones reales
• = 0: una solución real
• < 0: sin soluciones reales

*Ejemplo:* x² - 5x + 6 = 0
a=1, b=-5, c=6
```
x = (5 ± √(25-24)) / 2
x = (5 ± 1) / 2
x₁ = 3,  x₂ = 2  ✅
```

*Factorización:* (x-3)(x-2) = 0 ✅

*Completar el cuadrado:*
x² + 6x + 5 = 0
(x+3)² - 9 + 5 = 0
(x+3)² = 4
x+3 = ±2 → x=-1, x=-5 ✅""",

"secundaria_trigonometria": """📐 *TRIGONOMETRÍA*

━━━━━━━━━━━━━━━━━━━━
*Razones trigonométricas — SOH-CAH-TOA:*
```
sen(θ) = Opuesto / Hipotenusa
cos(θ) = Adyacente / Hipotenusa
tan(θ) = Opuesto / Adyacente
```

*Tabla de valores especiales:*
```
Ángulo | sen   | cos   | tan
  0°   |  0    |  1    |  0
 30°   | 1/2   | √3/2  | 1/√3
 45°   | √2/2  | √2/2  |  1
 60°   | √3/2  | 1/2   |  √3
 90°   |  1    |  0    |  ∞
```

*Identidades fundamentales:*
• sen²θ + cos²θ = 1
• tan(θ) = sen(θ)/cos(θ)

*Ejemplo:* Edificio con sombra de 10m a 60°
tan(60°) = altura/10 → altura = 10√3 ≈ 17.32m ✅""",

"secundaria_logaritmos": """🔢 *LOGARITMOS Y EXPONENCIALES*

━━━━━━━━━━━━━━━━━━━━
*Definición:*
log_b(x) = y  ⟺  b^y = x

*Propiedades:*
```
log(a·b)  = log(a) + log(b)
log(a/b)  = log(a) - log(b)
log(aⁿ)   = n·log(a)
log_b(b)  = 1
log_b(1)  = 0
```

*Ejemplos:*
log₂(8) = 3  porque 2³=8 ✅
log₁₀(1000) = 3 porque 10³=1000 ✅

*Cambio de base:*
log_b(x) = ln(x)/ln(b) = log(x)/log(b)

*Ecuación exponencial:*
2^x = 32
x = log₂(32) = 5 ✅""",

# ══════════════════════ UNIVERSIDAD ═══════════════════════════════════════════

"universidad_calculo_diferencial": """∂ *CÁLCULO DIFERENCIAL*

━━━━━━━━━━━━━━━━━━━━
*La Derivada — tasa de cambio instantánea*
f'(x) = lim[h→0] (f(x+h)-f(x))/h

*Reglas principales:*
```
d/dx[xⁿ]    = n·xⁿ⁻¹    (potencia)
d/dx[k]     = 0          (constante)
d/dx[eˣ]    = eˣ
d/dx[ln x]  = 1/x
d/dx[sen x] = cos x
d/dx[cos x] = -sen x
```

*Regla del producto:* (fg)' = f'g + fg'
*Regla del cociente:* (f/g)' = (f'g-fg')/g²
*Regla de la cadena:* [f(g(x))]' = f'(g(x))·g'(x)

*Ejemplo — Cadena:*
f(x) = (3x²+2)⁵
f'(x) = 5(3x²+2)⁴ · 6x = 30x(3x²+2)⁴ ✅

*Puntos críticos:* donde f'(x)=0 o no existe""",

"universidad_calculo_integral": """∫ *CÁLCULO INTEGRAL*

━━━━━━━━━━━━━━━━━━━━
*Reglas de integración:*
```
∫ xⁿ dx      = xⁿ⁺¹/(n+1) + C
∫ eˣ dx      = eˣ + C
∫ 1/x dx     = ln|x| + C
∫ sen x dx   = -cos x + C
∫ cos x dx   =  sen x + C
∫ k dx       = kx + C
```

*Ejemplo — indefinida:*
∫(3x²+4x-5)dx = x³+2x²-5x+C ✅

*Integral definida — Teorema Fundamental:*
∫ₐᵇ f(x)dx = F(b) - F(a)

*Ejemplo:* ∫₀² (x²+1)dx
= [x³/3 + x]₀²
= (8/3+2) - 0 = 14/3 ≈ 4.67 ✅

*Sustitución u:*
∫ 2x(x²+1)³ dx → u=x²+1, du=2x dx
= ∫ u³ du = u⁴/4 + C = (x²+1)⁴/4 + C ✅""",

"universidad_algebra_lineal": """🔢 *ÁLGEBRA LINEAL*

━━━━━━━━━━━━━━━━━━━━
*Suma de matrices:* elemento a elemento
*Multiplicación:* fila × columna

*Ejemplo multiplicación 2×2:*
```
[1 2] × [5 6] = [19 22]
[3 4]   [7 8]   [43 50]
```
• (1·5+2·7)=19, (1·6+2·8)=22
• (3·5+4·7)=43, (3·6+4·8)=50

*Determinante 2×2:*
det[a b] = ad - bc
   [c d]

*Inversa 2×2:*
A⁻¹ = (1/det(A)) · [d -b; -c a]

*Eliminación de Gauss:*
Transforma la matriz aumentada a forma escalonada
→ sustitución hacia atrás para encontrar solución""",

"universidad_ecuaciones_diferenciales": """📉 *ECUACIONES DIFERENCIALES*

━━━━━━━━━━━━━━━━━━━━
*Variables separables:*
dy/dx = g(x)·h(y)
→ dy/h(y) = g(x)dx → integrar ambos lados

*Ejemplo:* dy/dx = 2xy
dy/y = 2x dx
ln|y| = x² + C
y = Ae^(x²) ✅

━━━━━━━━━━━━━━━━━━━━
*EDO lineal de 1° orden:*
dy/dx + P(x)y = Q(x)
Factor integrante: μ = e^(∫P dx)

*Ejemplo:* dy/dx + 2y = 4
μ = e^(2x)
e^(2x)y = ∫4e^(2x)dx = 2e^(2x)+C
y = 2 + Ce^(-2x) ✅

*EDO de 2° orden homogénea:*
y''-5y'+6y=0 → r²-5r+6=0
(r-2)(r-3)=0 → r=2,3
y = C₁e^(2x)+C₂e^(3x) ✅""",
}

def get(level: str, topic: str) -> str | None:
    return CONTENT.get(f"{level}_{topic}")
