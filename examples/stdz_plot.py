from co2stdz import *
from pylab import *

style.use('mydefault.mplstyle')

DELTA_SLOPE = 0.92
DELTA_OF_WG = -15

f = lambda x: ((1 + x/1000) / (1 + DELTA_OF_WG/1000) - 1) * DELTA_SLOPE * 1000

fig = figure(figsize = (3.5, 3.5))
subplots_adjust(.2, .17, .95, .92)

scolor = (0,.2,1)
wgcolor = (0.9,0,0)

X = array([-34, 24])
x1, x2 = X
x0 = (x1 + x2)/2
h = x2 - x1
Y = f(X)
plot(X, Y, '-', lw = 1, color = scolor)

# X = linspace(-30, 10, 5)
# Y = ((1 + X/1000) / (1 + DELTA_OF_WG/1000) - 1) * DELTA_SLOPE * 1000
# plot(X, Y, 'wo', mec = 'r', mew = 1)

plot([DELTA_OF_WG]*2, [0, -1000], '-', dashes = (3,3), lw = 0.8, color = wgcolor)
plot([DELTA_OF_WG, -1000], [0, 0], '-', dashes = (3,3), lw = 0.8, color = wgcolor)

plot(DELTA_OF_WG, 0, 'wo', mec = wgcolor, mew = 1)
text(DELTA_OF_WG + 2, 0, f'working ref gas\n($δ^{{13}}C_{{VPDB}} = {str(DELTA_OF_WG)}$ ‰)', color = wgcolor, size = 11, va = 'top', ha = 'left')
text(0, f(0), f'slope ƒ = {str(DELTA_SLOPE)}\n', color = scolor, size = 11, va = 'center', ha = 'center', rotation = atan(DELTA_SLOPE)/pi*180, linespacing = 2)

axis([x1, x2, f(x0)-h/2, f(x0)+h/2])
xlabel('True $δ^{13}C$   [‰ vs VPDB]')
ylabel('Measured $δ_{636}$   [‰ vs WG]')
savefig('stdz_plot.png', dpi = 120)
close(fig)