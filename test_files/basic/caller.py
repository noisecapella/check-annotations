# Note: if we just say sub.callee this won't work
from sub.callee import f
import sub.callee

z = f("xyz")
g = sub.callee.f(3)

print(g)