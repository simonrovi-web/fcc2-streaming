import base64, os
B = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
F = 'node_modules/@fontsource/'
FONTS = f'''@font-face{{font-family:"Bebas";src:url(data:font/woff2;base64,{B(F+'bebas-neue/files/bebas-neue-latin-400-normal.woff2')}) format("woff2");}}
@font-face{{font-family:"Oswald";font-weight:400;src:url(data:font/woff2;base64,{B(F+'oswald/files/oswald-latin-400-normal.woff2')}) format("woff2");}}
@font-face{{font-family:"Oswald";font-weight:600;src:url(data:font/woff2;base64,{B(F+'oswald/files/oswald-latin-600-normal.woff2')}) format("woff2");}}'''
LOGO = 'data:image/png;base64,' + B('logo.png')
LOGOA = 'data:image/png;base64,' + B('logo_alpha.png')

BASE = '''
:root{--red:#e3121b;--red2:#ff2a2a;--red-dk:var(--red-dk);--red-rgb:227,18,27;--red2-rgb:255,42,42;--blue:#1f5fff;--ca:#e3121b;--ca-rgb:227,18,27;--ca-dk:var(--red-dk);--cb:#1f5fff;--cb-rgb:31,95,255;--cb-dk:var(--cb-dk);--ink:#f3f3f3;--mute:#9a9a9a;--bg:#060606;}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;color:var(--ink);font-family:"Oswald",sans-serif}
.bebas{font-family:"Bebas"}
[contenteditable]{outline:none}
[contenteditable]:focus{box-shadow:0 0 0 2px rgba(255,255,255,.4)}
@keyframes pulse{50%{opacity:.25}}
@keyframes sway{50%{transform:rotate(-14deg)}}
@keyframes sway2{50%{transform:rotate(14deg)}}
@keyframes breathe{50%{transform:translateX(-50%) scale(1.025)}}
@keyframes inUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}
@keyframes inL{from{opacity:0;transform:translateX(-120px)}to{opacity:1;transform:none}}
@keyframes inR{from{opacity:0;transform:translateX(120px)}to{opacity:1;transform:none}}
'''
FULL = '''
body{background:var(--bg)}
.stage{position:relative;width:1920px;height:1080px;overflow:hidden;
  background:radial-gradient(900px 520px at 50% 34%, rgba(var(--red-rgb),.28), transparent 70%),
   radial-gradient(700px 420px at 0% 100%, rgba(var(--red-rgb),.22), transparent 70%),
   radial-gradient(700px 420px at 100% 100%, rgba(var(--red-rgb),.22), transparent 70%),linear-gradient(#0b0b0b,#030303);}
.grid{position:absolute;inset:0;opacity:.07;background:repeating-linear-gradient(45deg,#fff 0 1px,transparent 1px 34px),repeating-linear-gradient(-45deg,#fff 0 1px,transparent 1px 34px);
  -webkit-mask:radial-gradient(ellipse at 50% 40%,transparent 30%,#000 80%)}
.beam{position:absolute;top:-200px;width:520px;height:1300px;background:linear-gradient(rgba(255,255,255,.10),transparent 70%);filter:blur(30px);transform-origin:top center}
.beam.l{left:120px;transform:rotate(-22deg);animation:sway 9s ease-in-out infinite}
.beam.r{right:120px;transform:rotate(22deg);animation:sway2 9s ease-in-out infinite}
canvas#fx{position:absolute;inset:0}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.75));pointer-events:none}
.tag{position:absolute;top:66px;left:64px;display:flex;align-items:center;gap:14px;font-family:"Bebas";font-size:40px;letter-spacing:3px;z-index:3}
.tag .dot{width:16px;height:16px;border-radius:50%;background:var(--red2);box-shadow:0 0 14px var(--red2);animation:pulse 1.4s ease-in-out infinite}
.tag small{display:block;font-family:"Oswald";font-size:20px;letter-spacing:4px;color:var(--mute)}
.date{position:absolute;top:56px;right:64px;border:3px solid var(--red);padding:14px 22px 12px;text-align:center;background:rgba(0,0,0,.55);z-index:3}
.date b{display:block;font-family:"Bebas";font-size:84px;line-height:.85;color:var(--red2)}
.date span{display:block;font-family:"Bebas";font-size:44px;line-height:1;letter-spacing:2px}
.date i{display:block;font-style:normal;font-family:"Bebas";font-size:40px;line-height:1;color:var(--red2)}
.logo{position:absolute;left:50%;transform:translateX(-50%);mix-blend-mode:lighten;animation:breathe 6s ease-in-out infinite}
.kicker{display:inline-block;font-family:"Bebas";font-size:46px;letter-spacing:10px;padding:4px 36px 0;background:var(--red);transform:skew(-12deg);box-shadow:0 0 30px rgba(var(--red-rgb),.5)}
.kicker>span{display:inline-block;transform:skew(12deg)}
.disc{font-family:"Bebas";font-size:38px;letter-spacing:8px;color:#ddd}
.disc em{font-style:normal;color:var(--red2);margin:0 18px}
.bar{position:absolute;left:0;right:0;bottom:0;height:104px;display:flex;background:linear-gradient(90deg,rgba(0,0,0,.92),rgba(18,0,0,.92));border-top:3px solid var(--red);z-index:3}
.cell{flex:1;display:flex;align-items:center;gap:18px;padding:0 34px;border-right:1px solid rgba(255,255,255,.12)}
.cell:last-child{border-right:0}
.cell svg{flex:none;width:44px;height:44px;stroke:var(--red2);fill:none;stroke-width:2}
.cell .t{font-family:"Bebas";font-size:34px;line-height:1;letter-spacing:1px}
.cell .s{font-size:18px;color:var(--mute);letter-spacing:1px;margin-top:3px}
.cell.sp{flex:1.1;background:rgba(var(--red-rgb),.12)}
.cell.sp .t{color:var(--red2);font-size:40px}
'''
BG = '<div class="beam l"></div><div class="beam r"></div><div class="grid"></div><canvas id="fx" width="1920" height="1080"></canvas>'
TAG = '<div class="tag"><div class="dot"></div><div>TRANSMISIÓN OFICIAL<small>FCC 2 · PASSLINE</small></div></div>'
DATE = '<div class="date"><b>17</b><span>OCT</span><i>2026</i></div>'
I_CAL = '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>'
I_PIN = '<svg viewBox="0 0 24 24"><path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
I_PLAY = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8.5l6 3.5-6 3.5z"/></svg>'
I_YT = '<svg viewBox="0 0 24 24"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9l5 3-5 3z"/></svg>'
I_TIX = '<svg viewBox="0 0 24 24"><path d="M3 8a2 2 0 0 0 0 4v0a2 2 0 0 1 0 4v2h18v-2a2 2 0 0 1 0-4 2 2 0 0 0 0-4V6H3z"/><path d="M14 6v12" stroke-dasharray="2 2"/></svg>'
BAR = f'''<div class="bar">
<div class="cell">{I_CAL}<div><div class="t">17 DE OCTUBRE 2026</div><div class="s">INICIO TRANSMISIÓN 13:00 HRS</div></div></div>
<div class="cell" style="flex:1.35">{I_PIN}<div><div class="t">BLACK HOUSE</div><div class="s">GENERAL JOFRÉ 254 · SANTIAGO CENTRO</div></div></div>
<div class="cell">{I_PLAY}<div><div class="t">27 COMBATES</div><div class="s">EN VIVO DESDE CUALQUIER DISPOSITIVO</div></div></div>
<div class="cell sp"><div><div class="s">AUSPICIADOR OFICIAL</div><div class="t">DI PIPINO PIZZA</div></div></div></div>'''
SPARKS = '''var c=document.getElementById('fx');if(c){var x=c.getContext('2d'),P=[];
function spawn(a){return{x:Math.random()*1920,y:a?Math.random()*1080:1090,v:.3+Math.random()*1.1,r:.6+Math.random()*2.2,a:.2+Math.random()*.6,w:Math.random()*6.28}}
for(var i=0;i<70;i++)P.push(spawn(true));
(function loop(){x.clearRect(0,0,1920,1080);for(var i=0;i<P.length;i++){var p=P[i];p.y-=p.v;p.w+=.02;p.x+=Math.sin(p.w)*.4;if(p.y<-10)P[i]=p=spawn(false);
x.beginPath();var RC=(getComputedStyle(document.documentElement).getPropertyValue('--red2-rgb')||'255,42,42').trim();x.fillStyle='rgba('+RC+','+p.a+')';x.shadowColor='rgb('+RC+')';x.shadowBlur=8;x.arc(p.x,p.y,p.r,0,6.28);x.fill();}requestAnimationFrame(loop)})();}'''
# Editable text: click in OBS "Interactuar" to edit; saved per file in localStorage. ?param=value also works.
EDIT = '''var Q=new URLSearchParams(location.search),KEY='fcc2:'+location.pathname.split('/').pop();
function st(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){return{}}}
function save(o){try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}}
document.querySelectorAll('[data-k]').forEach(function(el){var k=el.dataset.k,s=st();
 if(Q.get(k))el.textContent=Q.get(k);else if(s[k])el.textContent=s[k];
 el.setAttribute('contenteditable','true');el.spellcheck=false;
 el.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();el.blur()}});
 el.addEventListener('blur',function(){var o=st();o[k]=el.textContent.trim();save(o);if(window.fitAll)fitAll()});});'''

LIVE = r"""

// ---- ajuste automático de nombres largos ----
function fitEl(el){var mx=+el.dataset.max,mn=+el.dataset.min||20,f=mx;el.style.fontSize=f+'px';
 var mh=parseFloat(getComputedStyle(el).maxHeight)||1e9;var over=el.dataset.fit==='h'?function(){return el.scrollHeight>mh+4||el.scrollWidth>el.clientWidth+2}:function(){return el.scrollWidth>el.clientWidth+1};
 while(over()&&f>mn){f-=2;el.style.fontSize=f+'px'}}
function fitAll(){document.querySelectorAll('[data-fit]').forEach(fitEl)}
// ---- colores editables desde el control ----
function hx(h){h=(h||'').replace('#','');if(h.length===3)h=h.split('').map(function(c){return c+c}).join('');var n=parseInt(h,16);return isNaN(n)?null:[n>>16&255,n>>8&255,n&255]}
function mixc(c,t,a){return c.map(function(v,i){return Math.round(v+(t[i]-v)*a)})}
function css(c){return '#'+c.map(function(v){return ('0'+v.toString(16)).slice(-2)}).join('')}
function applyTheme(t){if(!t)return;var r=document.documentElement.style;
 var m=hx(t.main);if(m){r.setProperty('--red',css(m));r.setProperty('--red2',css(mixc(m,[255,255,255],.18)));r.setProperty('--red-dk',css(mixc(m,[0,0,0],.45)));r.setProperty('--red-rgb',m.join(','));r.setProperty('--red2-rgb',mixc(m,[255,255,255],.18).join(','))}
 var a=hx(t.a);if(a){r.setProperty('--ca',css(a));r.setProperty('--ca-rgb',a.join(','));r.setProperty('--ca-dk',css(mixc(a,[0,0,0],.45)))}
 var b=hx(t.b);if(b){r.setProperty('--cb',css(b));r.setProperty('--blue',css(b));r.setProperty('--cb-rgb',b.join(','));r.setProperty('--cb-dk',css(mixc(b,[0,0,0],.45)))}
 try{localStorage.setItem('fcc2-theme',JSON.stringify(t))}catch(e){}}
try{applyTheme(JSON.parse(localStorage.getItem('fcc2-theme')||'null'))}catch(e){}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitAll);setTimeout(fitAll,300);
// ---- CONTROL EN VIVO: recibe datos de CONTROL_EN_VIVO (OBS WebSocket, BroadcastChannel o localStorage) ----
var LAST=0;
function applyLive(d){if(!d||!d.ts||d.ts<LAST)return;LAST=d.ts;var m=d[PANEL],big=false;
 if(m)for(var k in m){var el=document.querySelector('[data-k="'+k+'"]');if(el&&document.activeElement!==el&&m[k]!=null&&el.textContent!==String(m[k])){if(/nombre$|^rojo$|^azul$/.test(k))big=true;el.textContent=m[k]}}
 if(d.theme)applyTheme(d.theme);fitAll();
 if(big&&PANEL!=='marcador'&&document.getAnimations)document.getAnimations().forEach(function(a){try{a.cancel();a.play()}catch(e){}});
 if(d.clock&&window.onClock&&PANEL==='marcador')window.onClock(d.clock);
 if(d.show&&PANEL in d.show){var v=!!d.show[PANEL];document.documentElement.style.transition='opacity .4s';document.documentElement.style.opacity=v?1:0}}
window.addEventListener('fcc2',function(e){applyLive(e.detail)});
try{new BroadcastChannel('fcc2').onmessage=function(e){applyLive(e.data)}}catch(e){}
window.addEventListener('storage',function(e){if(e.key==='fcc2-live')try{applyLive(JSON.parse(e.newValue))}catch(x){}});
try{var L0=JSON.parse(localStorage.getItem('fcc2-live')||'null');if(L0){delete L0.clock;applyLive(L0)}}catch(e){}
"""
def page(title, css, body, js='', full=True):
    return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><title>{title}</title>
<style>{FONTS}{BASE}{FULL if full else 'html,body{background:transparent}'}{css}</style></head>
<body>{body}
<script>var PANEL='__PANEL__';{EDIT}{SPARKS if full else ''}{js}{LIVE}</script></body></html>'''

P = {}

# ---------- FINAL ----------
P['FCC2_Final'] = page('FCC 2 Final', '''
.center{position:absolute;left:0;right:0;top:500px;text-align:center}
.big{font-family:"Bebas";font-size:170px;line-height:.9;letter-spacing:4px;margin-top:22px;text-shadow:0 0 40px rgba(var(--red2-rgb),.35);animation:inUp 1s ease both}
.big em{font-style:normal;color:var(--red2)}
.sub{font-size:30px;letter-spacing:6px;color:#cfcfcf;margin-top:10px}
.ctas{display:flex;justify-content:center;gap:40px;margin-top:40px}
.cta{display:flex;align-items:center;gap:16px;padding:16px 30px;border:2px solid var(--red);background:rgba(0,0,0,.5)}
.cta svg{width:46px;height:46px;stroke:var(--red2);fill:none;stroke-width:2}
.cta b{display:block;font-family:"Bebas";font-size:34px;letter-spacing:2px;line-height:1}
.cta span{font-size:17px;color:var(--mute);letter-spacing:2px}
''', f'''<div class="stage">{BG}{TAG}{DATE}
<img class="logo" src="{LOGO}" style="top:40px;width:640px">
<div class="center"><div class="kicker"><span data-k="kicker">FIN DE LA TRANSMISIÓN</span></div>
<div class="big">GRACIAS POR <em>ACOMPAÑARNOS</em></div>
<div class="sub" data-k="sub">NOS VEMOS EN LA PRÓXIMA FECHA DE FCC</div>
<div class="ctas">
<div class="cta">{I_YT}<div><b>SUSCRÍBETE EN YOUTUBE</b><span>FIGHTING CHAMPIONSHIP CHILE</span></div></div>
<div class="cta"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg><div><b>SÍGUENOS</b><span>@FCCHILE_</span></div></div>
</div></div><div class="vig"></div>{BAR}</div>''')

# ---------- PAUSA ----------
P['FCC2_Pausa'] = page('FCC 2 Pausa', '''
.center{position:absolute;left:0;right:0;top:500px;text-align:center}
.big{font-family:"Bebas";font-size:170px;line-height:.9;letter-spacing:6px;margin-top:20px;text-shadow:0 0 40px rgba(var(--red2-rgb),.35)}
.clock{font-family:"Bebas";font-size:84px;color:var(--red2);letter-spacing:6px;margin-top:6px}
.disc{margin-top:16px}
''', f'''<div class="stage">{BG}{TAG}{DATE}
<img class="logo" src="{LOGO}" style="top:30px;width:680px">
<div class="center"><div class="kicker"><span data-k="kicker">PAUSA</span></div>
<div class="big" data-k="titulo">VOLVEMOS EN BREVE</div>
<div class="clock" id="clock"></div>
<div class="disc">NOGI<em>●</em>BOXEO<em>●</em>KICKBOXING<em>●</em>MMA</div></div>
<div class="vig"></div>{BAR}</div>''', '''
// ?min=5 muestra una cuenta regresiva de 5 minutos desde que la escena se activa
var mins=parseFloat(Q.get('min')||'0'),end=Date.now()+mins*60000,ck=document.getElementById('clock');
function t(){if(!mins){ck.style.display='none';return}var d=Math.max(0,Math.round((end-Date.now())/1000));
ck.textContent=String(Math.floor(d/60)).padStart(2,'0')+':'+String(d%60).padStart(2,'0');}
t();setInterval(t,250);''')

# ---------- VS ----------
VSCSS = '''
.side{position:absolute;top:0;bottom:104px;width:960px;display:flex;flex-direction:column;justify-content:center;padding:0 90px}
.side.r{left:0;background:linear-gradient(100deg,rgba(var(--ca-rgb),.55),rgba(var(--ca-rgb),.08) 70%,transparent);clip-path:polygon(0 0,100% 0,86% 100%,0 100%);animation:inL .8s ease both}
.side.b{right:0;align-items:flex-end;text-align:right;background:linear-gradient(-100deg,rgba(var(--cb-rgb),.55),rgba(var(--cb-rgb),.08) 70%,transparent);clip-path:polygon(14% 0,100% 0,100% 100%,0 100%);animation:inR .8s ease both}
.corner{font-family:"Bebas";font-size:34px;letter-spacing:8px;opacity:.85}
.name{font-family:"Bebas";font-size:150px;line-height:1;padding-top:.06em;letter-spacing:2px;width:600px;max-height:290px;overflow:hidden;overflow-wrap:break-word;margin-top:4px;text-shadow:0 6px 30px rgba(0,0,0,.6)}
.nick{font-size:30px;letter-spacing:4px;color:#ddd;margin-top:14px}
.stats{display:flex;gap:34px;margin-top:34px}
.stats div{border-top:3px solid rgba(255,255,255,.5);padding-top:8px}
.stats b{display:block;font-family:"Bebas";font-size:52px;line-height:1}
.stats span{font-size:16px;letter-spacing:4px;color:#cfcfcf}
.vs{position:absolute;left:50%;top:400px;transform:translate(-50%,-50%);font-family:"Bebas";font-size:260px;line-height:1;color:#fff;text-shadow:0 0 60px rgba(var(--red2-rgb),.7),0 0 6px #000;z-index:2;animation:inUp 1s .3s ease both}
.minilogo{position:absolute;left:50%;top:40px;width:330px;transform:translateX(-50%);mix-blend-mode:lighten;z-index:2}
.info{position:absolute;left:50%;top:700px;transform:translateX(-50%);text-align:center;z-index:2;white-space:nowrap}
.info .k{font-family:"Bebas";font-size:44px;letter-spacing:6px;background:var(--red);padding:4px 30px 0;display:inline-block}
.info .w{font-family:"Bebas";font-size:40px;letter-spacing:4px;margin-top:14px}
.info .n{font-size:22px;letter-spacing:6px;color:var(--mute);margin-top:6px}
'''
def side(cls, corner, pre):
    return f'''<div class="side {cls}"><div class="corner" data-k="{pre}corner">{corner}</div>
<div class="name" data-k="{pre}nombre" data-fit="h" data-max="150" data-min="56">NOMBRE APELLIDO</div>
<div class="nick" data-k="{pre}apodo">"APODO" · ACADEMIA</div>
<div class="stats"><div><b data-k="{pre}record">0-0-0</b><span>RÉCORD</span></div><div><b data-k="{pre}peso">00 KG</b><span>PESO</span></div><div><b data-k="{pre}edad">00</b><span>EDAD</span></div></div></div>'''
P['FCC2_VS'] = page('FCC 2 VS', VSCSS, f'''<div class="stage">{BG}
{side('r','ESQUINA ROJA','r_')}{side('b','ESQUINA AZUL','b_')}
<img class="minilogo" src="{LOGO}">
<div class="vs">VS</div>
<div class="info"><div class="k" data-k="disciplina">MMA</div><div class="w" data-k="categoria">CATEGORÍA · 3 ROUNDS X 3 MIN</div><div class="n" data-k="numero">COMBATE 1 DE 27</div></div>
<div class="vig"></div>{BAR}</div>''')

# ---------- GANADOR ----------
P['FCC2_Ganador'] = page('FCC 2 Ganador', '''
.center{position:absolute;left:0;right:0;top:420px;text-align:center}
.kicker{font-size:60px;letter-spacing:16px}
.name{font-family:"Bebas";font-size:220px;line-height:1.08;padding-top:.04em;margin:16px auto 0;width:1760px;white-space:nowrap;overflow:hidden;letter-spacing:4px;text-shadow:0 0 60px rgba(var(--red2-rgb),.5);animation:inUp 1s ease both}
.row{display:flex;justify-content:center;gap:0;margin-top:30px}
.row div{padding:6px 40px;border-left:2px solid rgba(255,255,255,.2)}
.row div:first-child{border-left:0}
.row b{display:block;font-family:"Bebas";font-size:60px;line-height:1;color:var(--red2)}
.row span{font-size:18px;letter-spacing:6px;color:var(--mute)}
.corner{font-family:"Bebas";font-size:36px;letter-spacing:8px;margin-top:6px}
.belt{position:absolute;left:50%;top:300px;transform:translateX(-50%);width:1500px;height:3px;background:linear-gradient(90deg,transparent,var(--red2),transparent)}
''', f'''<div class="stage">{BG}{TAG}{DATE}
<img class="logo" src="{LOGO}" style="top:30px;width:420px">
<div class="belt"></div>
<div class="center"><div class="kicker"><span>GANADOR</span></div>
<div class="name" data-k="nombre" data-fit="w" data-max="220" data-min="80">NOMBRE APELLIDO</div>
<div class="corner" data-k="esquina">ESQUINA ROJA</div>
<div class="row"><div><b data-k="metodo">KO / TKO</b><span>MÉTODO</span></div><div><b data-k="round">ROUND 2</b><span>ROUND</span></div><div><b data-k="tiempo">1:45</b><span>TIEMPO</span></div><div><b data-k="disciplina">MMA</b><span>DISCIPLINA</span></div></div></div>
<div class="vig"></div>{BAR}</div>''')

# ---------- AUSPICIADOR ----------
P['FCC2_Auspiciador'] = page('FCC 2 Auspiciador', '''
.center{position:absolute;left:0;right:0;top:330px;text-align:center}
.brand{font-family:"Bebas";font-size:260px;line-height:.85;letter-spacing:6px;margin-top:30px;animation:inUp 1s ease both}
.brand em{font-style:normal;color:var(--red2)}
.las{font-family:"Bebas";font-size:56px;letter-spacing:22px;color:#ddd}
.flag{width:300px;height:8px;margin:22px auto 0;background:linear-gradient(90deg,#1f9e4a 33%,#fff 33% 66%,var(--red) 66%)}
.slogan{font-family:"Bebas";font-size:54px;letter-spacing:4px;margin-top:30px}
.slogan em{font-style:normal;color:var(--red2)}
.handles{display:flex;justify-content:center;gap:50px;margin-top:30px;font-size:28px;letter-spacing:2px;color:#ddd}
.handles b{color:var(--red2);font-weight:600;margin-right:10px}
''', f'''<div class="stage">{BG}{TAG}{DATE}
<img class="logo" src="{LOGO}" style="top:40px;width:420px">
<div class="center"><div class="kicker"><span>AUSPICIADOR OFICIAL FCC 2</span></div>
<div class="brand">DI <em>PIPINO</em></div>
<div class="las">LAS FAMOSAS · ITALIAN PIZZA</div>
<div class="flag"></div>
<div class="slogan">LOS GRANDES COMBATES SE DISFRUTAN CON EL MEJOR <em>SABOR</em></div>
<div class="handles"><div><b>IG</b>@dipipino</div><div><b>WSP</b>+569 52876205</div><div><b>TIKTOK</b>dipipinopizza</div></div></div>
<div class="vig"></div>{BAR}</div>''')

# ---------- OVERLAYS (fondo transparente) ----------
P['FCC2_Overlay_Marcador'] = page('FCC 2 Marcador', '''
.bug{position:absolute;left:60px;bottom:60px;display:flex;align-items:stretch;filter:drop-shadow(0 14px 34px rgba(0,0,0,.7));animation:inL .6s ease both}
.lg{width:170px;background:linear-gradient(#141414,#050505);display:flex;align-items:center;justify-content:center;border-right:4px solid var(--red)}
.lg img{width:150px}
.names{display:flex;flex-direction:column;width:600px}
.top{background:linear-gradient(90deg,var(--red),var(--red-dk));font-family:"Bebas";font-size:26px;letter-spacing:6px;padding:5px 18px 1px;color:#fff;white-space:nowrap;overflow:hidden}
.fr{display:flex;align-items:center;height:66px;background:rgba(10,10,10,.94);border-top:1px solid rgba(255,255,255,.07)}
.chip{width:14px;align-self:stretch;background:var(--ca)}
.chip.b{background:var(--cb)}
.nm{flex:1;font-family:"Bebas";font-size:50px;line-height:1.15;padding:4px 18px 0;white-space:nowrap;overflow:hidden;color:#fff;min-width:0}
.rec{font-size:20px;color:#bdbdbd;padding-right:18px;letter-spacing:1px;white-space:nowrap}
.clk{width:240px;background:#050505;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;border-left:1px solid rgba(255,255,255,.08)}
.clk .rd{font-family:"Bebas";font-size:28px;letter-spacing:5px;color:#b5b5b5;line-height:1}
.clk .rd b{color:#fff;font-weight:400}
.clk .tm{font-family:"Bebas";font-size:92px;line-height:.88;color:#fff;font-variant-numeric:tabular-nums}
.clk .tm.low{color:var(--red2);animation:pulse 1s steps(1) infinite}
.clk .st{position:absolute;top:8px;right:10px;font-size:13px;letter-spacing:3px;color:var(--warn,#f5b301);display:none}
.clk .pb{position:absolute;left:0;bottom:0;height:7px;background:linear-gradient(90deg,var(--red-dk),var(--red2));box-shadow:0 0 12px var(--red2)}
.help{position:absolute;top:20px;left:20px;font-size:18px;background:rgba(0,0,0,.85);padding:10px 16px;display:none;line-height:1.5}
''', f'''<div class="bug" id="bug">
<div class="lg"><img src="{LOGOA}"></div>
<div class="names"><div class="top" data-k="sub">MMA · CATEGORÍA</div>
<div class="fr"><div class="chip"></div><div class="nm" data-k="rojo" data-fit="w" data-max="50" data-min="24">PELEADOR ROJO</div><div class="rec" data-k="rrec"></div></div>
<div class="fr"><div class="chip b"></div><div class="nm" data-k="azul" data-fit="w" data-max="50" data-min="24">PELEADOR AZUL</div><div class="rec" data-k="brec"></div></div></div>
<div class="clk"><div class="st" id="st">PAUSA</div><div class="rd">ROUND <b id="rd">1</b><span id="tot"> / 3</span></div><div class="tm" id="tm">3:00</div><div class="pb" id="pb"></div></div>
</div>
<div class="help" id="help">ESPACIO iniciar/pausar · R reiniciar · ← → round · + − 10 s · H ayuda · (lo normal es manejarlo desde CONTROL_EN_VIVO)</div>''', '''
var RL=parseFloat(Q.get('min')||'3')*60,tm=document.getElementById('tm');
var C={round:1,total:3,len:RL,rem:RL,running:false,at:Date.now()};
try{var sc=JSON.parse(localStorage.getItem('fcc2-clock-local')||'null');if(sc)C=sc}catch(e){}
function rem(){return C.running?Math.max(0,C.rem-(Date.now()-C.at)/1000):C.rem}
function setC(o){var r=rem();for(var k in o)C[k]=o[k];if(!('rem' in o))C.rem=r;C.at=Date.now();try{localStorage.setItem('fcc2-clock-local',JSON.stringify(C))}catch(e){}}
window.onClock=function(c){C={round:c.round,total:c.total||3,len:c.len,rem:c.rem,running:c.running,at:Date.now()};try{localStorage.setItem('fcc2-clock-local',JSON.stringify(C))}catch(e){}};
function draw(){var r=rem();if(C.running&&r<=0){C.running=false;C.rem=0}var s=Math.ceil(r);
 tm.textContent=Math.floor(s/60)+':'+String(s%60).padStart(2,'0');tm.classList.toggle('low',s<=10&&s>0);
 document.getElementById('rd').textContent=C.round;document.getElementById('tot').textContent=C.total?' / '+C.total:'';
 document.getElementById('pb').style.width=(C.len?Math.max(0,Math.min(100,100*r/C.len)):0)+'%';
 document.getElementById('st').style.display=(!C.running&&r>0&&r<C.len)?'block':'none';
 requestAnimationFrame(draw)}
requestAnimationFrame(draw);
document.addEventListener('keydown',function(e){if(document.activeElement&&document.activeElement.isContentEditable)return;
 var k=e.key;if(k===' '){setC({running:!C.running});e.preventDefault()}else if(k==='r'||k==='R'){setC({running:false,rem:C.len})}
 else if(k==='ArrowRight'){setC({round:C.round+1,running:false,rem:C.len})}else if(k==='ArrowLeft'){setC({round:Math.max(1,C.round-1)})}
 else if(k==='+'||k==='='){setC({rem:rem()+10})}else if(k==='-'){setC({rem:Math.max(0,rem()-10)})}
 else if(k==='h'||k==='H'){var h=document.getElementById('help');h.style.display=h.style.display==='block'?'none':'block'}});''', full=False)

P['FCC2_Overlay_Replay'] = page('FCC 2 Replay', '''
.frame{position:absolute;inset:0;border:6px solid var(--red);box-shadow:inset 0 0 60px rgba(var(--red-rgb),.35)}
.bug{position:absolute;top:44px;left:44px;display:flex;align-items:center;gap:16px;background:rgba(0,0,0,.82);padding:10px 30px 6px 20px;border-left:8px solid var(--red2);font-family:"Bebas";font-size:60px;letter-spacing:8px;animation:inL .5s ease both}
.bug i{width:22px;height:22px;border-radius:50%;background:var(--red2);box-shadow:0 0 16px var(--red2);animation:pulse 1s steps(1) infinite}
.lg{position:absolute;bottom:30px;right:40px;width:240px}
''', f'''<div class="frame"></div><div class="bug"><i></i><span data-k="texto">REPETICIÓN</span></div><img class="lg" src="{LOGOA}">''', full=False)

P['FCC2_Overlay_LowerThird'] = page('FCC 2 Lower Third', '''
.lt{position:absolute;left:90px;bottom:110px;display:flex;align-items:stretch;animation:inL .7s ease both}
.lt .accent{width:14px;background:var(--red2)}
.lt .box{background:linear-gradient(90deg,rgba(8,8,8,.95),rgba(20,0,0,.9));padding:14px 40px 12px 26px;min-width:620px}
.lt .n{font-family:"Bebas";font-size:66px;line-height:1.1;padding-top:.04em;letter-spacing:2px;max-width:1100px;white-space:nowrap;overflow:hidden}
.lt .c{font-size:24px;letter-spacing:5px;color:#cfcfcf;margin-top:4px}
.lt .c b{color:var(--red2);font-weight:600}
.lt img{width:150px;margin-left:-6px;align-self:center}
''', f'''<div class="lt"><div class="accent"></div><div class="box"><div class="n" data-k="nombre" data-fit="w" data-max="66" data-min="30">NOMBRE APELLIDO</div><div class="c"><b>FCC 2</b> · <span data-k="cargo">COMENTARISTA</span></div></div><img src="{LOGOA}"></div>''', full=False)

os.makedirs('out', exist_ok=True)
PID={'FCC2_VS':'vs','FCC2_Ganador':'ganador','FCC2_Overlay_Marcador':'marcador','FCC2_Overlay_LowerThird':'lt','FCC2_Overlay_Replay':'replay','FCC2_Pausa':'pausa','FCC2_Final':'final'}
for k, v in P.items():
    open(f'out/{k}.html', 'w').write(v.replace('__PANEL__', PID.get(k,'otro')))
print(list(P))
