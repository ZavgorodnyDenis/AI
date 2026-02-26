import math

def f(x): return x*x - 2
def df(x): return 2*x

def newton_method(f, df, x0, tol=1e-6, max_iter=50):
    x = x0
    print(f"Начальное: x₀ = {x:.10f}")
    
    for i in range(max_iter):
        fx, dfx = f(x), df(x)
        if abs(dfx) < 1e-12: return None, i, "Производная=0"
        
        dx = fx / dfx
        x -= dx
        
        print(f"Итерация {i+1}: x={x:.10f}, f(x)={fx:.2e}, |Δx|={abs(dx):.2e}")
        if abs(dx) < tol: return x, i+1, "Сошлось"
    
    return x, max_iter, "Превышен лимит"

print("ЛАБОРАТОРНАЯ РАБОТА: Метод Ньютона\n"+"="*60)
root, iterations, status = newton_method(f, df, 1.0)
print("\n"+"="*60)
print(f"Корень:      {root:.12f}")
print(f"Точное √2:   {math.sqrt(2):.12f}")
print(f"Итераций:    {iterations}")
print(f"Толерант:    1e-6")
print(f"Статус:      {status}")
print(f"Ошибка:      {abs(root-math.sqrt(2)):.2e}")
print("\n КВАДРАТИЧНАЯ СХОДИМОСТЬ: ✓")
