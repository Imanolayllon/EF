import time
from caida_huevos_fb import caida_huevos_fb
from caida_huevos_pd import caida_huevos_pd
 
HUEVOS = 3
casos = [5, 10, 12, 14, 16, 18, 20, 22]
 
print(f"{'Pisos':>5} | {'Result':>6} | {'Oper. FB':>14} | {'Oper. PD':>8} | "
      f"{'Mem. PD':>8} | {'Reduc. oper.':>12} | {'FB (ms)':>10} | {'PD (ms)':>8}")
print("-" * 92)
 
for n in casos:
    t0 = time.perf_counter()
    r_fb, op_fb = caida_huevos_fb(HUEVOS, n)
    t1 = time.perf_counter()
    r_pd, op_pd, mem_pd, _ = caida_huevos_pd(HUEVOS, n)
    t2 = time.perf_counter()
 
    ms_fb = (t1 - t0) * 1000
    ms_pd = (t2 - t1) * 1000
    reduc = op_fb / op_pd if op_pd else float('inf')
    ok = "OK" if r_fb == r_pd else "DIFF!"
 
    print(f"{n:>5} | {r_fb:>3} {ok:>2} | {op_fb:>14,} | {op_pd:>8,} | "
          f"{mem_pd:>8,} | {reduc:>10,.0f}x | {ms_fb:>10.3f} | {ms_pd:>8.4f}")
 
print("-" * 92)
print("Oper. = cantidad de operaciones fundamentales (evaluaciones de un piso).")
print("Mem. PD = celdas de la tabla pd (memoria adicional que gasta la PD).")
print("La FB no usa tabla, pero paga con una cantidad EXPONENCIAL de operaciones.")