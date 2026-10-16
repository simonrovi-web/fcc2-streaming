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
x.beginPath();var RC=(getComputedStyle(document.body).getPropertyValue('--red2-rgb')||'255,42,42').trim();x.fillStyle='rgba('+RC+','+p.a+')';x.shadowColor='rgb('+RC+')';x.shadowBlur=8;x.arc(p.x,p.y,p.r,0,6.28);x.fill();}requestAnimationFrame(loop)})();}'''
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
function fitAll(){document.querySelectorAll('[data-fit]').forEach(fitEl);var g={};document.querySelectorAll('[data-sync]').forEach(function(e){var k=e.dataset.sync,f=parseFloat(e.style.fontSize)||999;g[k]=Math.min(g[k]||999,f)});document.querySelectorAll('[data-sync]').forEach(function(e){e.style.fontSize=g[e.dataset.sync]+'px'})}
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
 if(d.theme)applyTheme(d.theme);if(m&&window.onData)window.onData(m);document.querySelectorAll('.gym').forEach(function(g){var t=g.querySelector('b');g.classList.toggle('empty',!t||!t.textContent.trim())});fitAll();
 if(big&&PANEL!=='marcador'&&document.getAnimations)document.getAnimations().forEach(function(a){try{a.cancel();a.play()}catch(e){}});
 if(d.clock&&window.onClock&&PANEL==='marcador')window.onClock(d.clock);
 if(d.layout&&window.onLayout&&PANEL==='marcador')window.onLayout(d.layout);
 if(d.mosca&&window.onMosca&&PANEL==='mosca')window.onMosca(d.mosca);
 if(PANEL==='lt'&&window.onLT){window.onLT(d.lt,!!(d.show&&d.show.lt))}
 else if(d.show&&PANEL in d.show){var v=!!d.show[PANEL];document.documentElement.style.transition='opacity .4s';document.documentElement.style.opacity=v?1:0}}
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
VSCSS = """
.half{position:absolute;top:0;bottom:104px;width:1030px}
.half.r{left:0;background:linear-gradient(100deg,rgba(var(--ca-rgb),.62),rgba(var(--ca-rgb),.18) 55%,rgba(var(--ca-rgb),.04));clip-path:polygon(0 0,100% 0,87% 100%,0 100%);animation:inL .8s ease both}
.half.b{right:0;background:linear-gradient(-100deg,rgba(var(--cb-rgb),.62),rgba(var(--cb-rgb),.18) 55%,rgba(var(--cb-rgb),.04));clip-path:polygon(13% 0,100% 0,100% 100%,0 100%);animation:inR .8s ease both}
.edge{position:absolute;top:0;bottom:104px;width:6px;z-index:1;transform-origin:top}
.edge.r{left:1027px;background:var(--ca);box-shadow:0 0 24px var(--ca);transform:skewX(-7.6deg)}
.edge.b{left:887px;background:var(--cb);box-shadow:0 0 24px var(--cb);transform:skewX(-7.6deg)}
.fighter{position:absolute;top:186px;width:640px;display:flex;flex-direction:column;align-items:center;text-align:center;z-index:2}
.fighter.r{left:90px;animation:inL .8s .1s ease both}.fighter.b{right:90px;animation:inR .8s .1s ease both}
.corner{font-family:"Bebas";font-size:30px;letter-spacing:8px;padding:5px 26px 1px;transform:skewX(-14deg);color:#fff;box-shadow:0 6px 18px rgba(0,0,0,.45)}
.corner.r{background:var(--ca)}.corner.b{background:var(--cb)}
.corner span{display:inline-block;transform:skewX(14deg)}
.name{font-family:"Bebas";font-size:124px;line-height:1;padding-top:.06em;letter-spacing:2px;width:640px;padding:0 .14em;box-sizing:border-box;max-height:226px;overflow:hidden;overflow-wrap:break-word;font-style:italic;color:#fff;text-shadow:4px 4px 0 #000,0 10px 34px rgba(0,0,0,.7)}
.namebox{height:232px;width:640px;margin-top:12px;display:flex;align-items:center;justify-content:center}
.gym{display:flex;align-items:center;gap:12px;margin-top:8px;padding:6px 26px 2px 18px;background:rgba(0,0,0,.6);transform:skewX(-14deg);max-width:620px}
.gym>*{transform:skewX(14deg)}
.gym.r{border-bottom:4px solid var(--ca)}.gym.b{border-bottom:4px solid var(--cb)}
.gym svg{width:30px;height:34px;flex:none}
.gym.r svg path{fill:var(--ca)}.gym.b svg path{fill:var(--cb)}
.gym b{font-family:"Bebas";font-size:42px;line-height:1.15;letter-spacing:3px;font-weight:400;color:#fff;white-space:nowrap;overflow:hidden;max-width:540px}
.gym.empty{visibility:hidden}
.nick{font-size:26px;letter-spacing:4px;color:#e6e6e6;margin-top:8px;min-height:32px}
.stats{display:flex;justify-content:center;margin-top:16px;background:rgba(0,0,0,.55);border-top:3px solid rgba(255,255,255,.25)}
.stats div{padding:10px 30px 8px;border-left:1px solid rgba(255,255,255,.15);min-width:130px}
.stats div:first-child{border-left:0}
.stats b{display:block;font-family:"Bebas";font-size:50px;line-height:1.05}
.stats span{font-size:15px;letter-spacing:4px;color:#cfcfcf}
.minilogo{position:absolute;left:50%;top:28px;width:300px;margin-left:-150px;mix-blend-mode:lighten;z-index:3}
.vs{position:absolute;left:50%;top:400px;width:400px;margin:-150px 0 0 -200px;text-align:center;font-family:"Bebas";font-size:290px;line-height:1;font-style:italic;color:#fff;z-index:3;
 text-shadow:5px 5px 0 #000,0 0 50px rgba(var(--red2-rgb),.85),0 0 110px rgba(var(--red2-rgb),.45);animation:vsIn .7s .35s cubic-bezier(.2,1.6,.4,1) both}
@keyframes vsIn{from{opacity:0;transform:scale(2.4)}to{opacity:1;transform:none}}
.info{position:absolute;left:50%;top:716px;width:1100px;margin-left:-550px;text-align:center;z-index:3}
.info .k{display:inline-block;font-family:"Bebas";font-size:66px;line-height:1.1;letter-spacing:10px;background:var(--red);padding:4px 44px 0;transform:skewX(-14deg);box-shadow:0 0 26px rgba(var(--red-rgb),.5)}
.info .k span{display:inline-block;transform:skewX(14deg)}
.info .w{font-family:"Bebas";font-size:60px;line-height:1.1;letter-spacing:6px;margin-top:12px;text-shadow:3px 3px 0 #000}
.info .n{font-family:"Bebas";font-size:40px;line-height:1.1;letter-spacing:8px;color:#e6e6e6;margin-top:2px;text-shadow:2px 2px 0 #000}
"""
def side(cls, corner, pre):
    return f"""<div class="fighter {cls}"><div class="corner {cls}"><span data-k="{pre}corner">{corner}</span></div>
<div class="namebox"><div class="name" data-k="{pre}nombre" data-fit="h" data-max="112" data-min="48" data-sync="vsn">NOMBRE APELLIDO</div></div>
<div class="gym {cls}"><svg viewBox="0 0 24 28"><path d="M12 0l12 4v9c0 7.5-5.2 12.6-12 15C5.2 25.6 0 20.5 0 13V4z"/></svg><b data-k="{pre}gym" data-fit="w" data-max="42" data-min="22">GIMNASIO</b></div>
<div class="nick" data-k="{pre}apodo">"APODO"</div>
<div class="stats"><div><b data-k="{pre}record">0-0-0</b><span>RÉCORD</span></div><div><b data-k="{pre}peso">00 KG</b><span>PESO</span></div><div><b data-k="{pre}edad">00</b><span>EDAD</span></div></div></div>"""
P['FCC2_VS'] = page('FCC 2 VS', VSCSS, f"""<div class="stage">{BG}
<div class="half r"></div><div class="half b"></div>
{side('r','ESQUINA ROJA','r_')}{side('b','ESQUINA AZUL','b_')}
<img class="minilogo" src="{LOGO}">
<div class="vs">VS</div>
<div class="info"><div class="k"><span data-k="disciplina">MMA</span></div><div class="w" data-k="categoria">CATEGORÍA · 3 ROUNDS X 3 MIN</div><div class="n" data-k="numero">COMBATE 1</div></div>
<div class="vig"></div>{BAR}</div>""")

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
<div class="vig"></div>{BAR}</div>''', '''
// si gana la esquina azul (u otra), todo el panel toma el color de esa esquina
var SIDE='r';
function sideVars(){var cs=getComputedStyle(document.documentElement),b=document.body.style;
 ['--red','--red2','--red-dk','--red-rgb','--red2-rgb'].forEach(function(k){b.removeProperty(k)});
 if(SIDE==='r'||SIDE==='d'){var a=hx(cs.getPropertyValue('--ca').trim());if(!a||SIDE==='d')return;var c=a}else{var c=hx(cs.getPropertyValue('--cb').trim());if(!c)return}
 var l=mixc(c,[255,255,255],.22);b.setProperty('--red',css(c));b.setProperty('--red2',css(l));b.setProperty('--red-dk',css(mixc(c,[0,0,0],.45)));b.setProperty('--red-rgb',c.join(','));b.setProperty('--red2-rgb',l.join(','))}
window.onData=function(m){if(m&&m.lado&&m.lado!==SIDE){SIDE=m.lado;document.body.dataset.side=SIDE}sideVars()};
if(Q.get('lado')){SIDE=Q.get('lado');setTimeout(sideVars,50)}''')

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
.bug{position:absolute;left:0;right:0;margin:0 auto;width:max-content;bottom:46px;transform-origin:center bottom;display:flex;flex-direction:column;align-items:center;transition:transform .35s ease}
.bug>*{animation:fadeUp .5s ease both}@keyframes fadeUp{from{opacity:0;translate:0 24px}to{opacity:1;translate:0 0}}
.bug.pos-tc{bottom:auto;top:40px;transform-origin:center top}
.sub{font-family:"Oswald";font-weight:600;font-size:15px;letter-spacing:5px;color:#fff;background:var(--red);padding:3px 16px 2px;margin-bottom:0;text-transform:uppercase;white-space:nowrap}
.sub:empty{display:none}
.bar{display:flex;align-items:stretch;height:60px;background:rgba(46,48,54,.86);box-shadow:0 8px 22px rgba(0,0,0,.45)}
.f{width:430px;display:flex;align-items:center;justify-content:center;gap:14px;padding:0 24px;min-width:0}
.badge{flex:none;min-width:30px;height:30px;padding:0 8px;display:flex;align-items:center;justify-content:center;font-family:"Oswald";font-weight:600;font-size:16px;letter-spacing:1px;color:#fff;border-radius:2px}
.f.l .badge{background:var(--ca)}.f.r .badge{background:var(--cb)}
.badge:empty{min-width:14px;width:14px;height:14px;padding:0}
.nm{min-width:0;max-width:330px;padding-right:4px;font-family:"Oswald";font-weight:600;font-size:30px;line-height:1.3;letter-spacing:3px;color:#fff;white-space:nowrap;overflow:hidden;text-transform:uppercase}
.ctr{display:flex;align-items:center;gap:16px;padding:0 26px;background:rgba(14,14,16,.96);position:relative}
.ctr:before,.ctr:after{content:"";position:absolute;top:14px;bottom:14px;width:6px}
.ctr:before{left:0;background:var(--ca)}.ctr:after{right:0;background:var(--cb)}
.ctr img{height:46px}
.tm{font-family:"Oswald";font-weight:600;font-size:38px;line-height:1;letter-spacing:1px;color:#fff;min-width:96px;text-align:center;font-variant-numeric:tabular-nums}
.tm.low{color:var(--red2);animation:pulse .8s steps(1) infinite}
.pips{display:flex;gap:6px;margin-top:6px}
.pips s{display:block;width:44px;height:5px;background:rgba(40,40,44,.85);box-shadow:0 1px 3px rgba(0,0,0,.5)}
.pips s.on{background:rgba(200,200,205,.9)}
.pips s.cur{background:#fff}
.st{position:absolute;left:50%;top:-26px;transform:translateX(-50%);font-family:"Oswald";font-weight:600;font-size:16px;letter-spacing:4px;color:#f5b301;display:none;text-shadow:0 1px 3px #000}
.pos-tc .st{top:auto;bottom:-30px}
.hidden{display:none}
.help{position:absolute;top:20px;left:20px;font-size:18px;background:rgba(0,0,0,.85);padding:10px 16px;display:none;line-height:1.5}
''', f'''<div class="bug" id="bug">
 <div class="sub" data-k="sub">MMA · CATEGORÍA</div>
 <div class="bar">
  <div class="f l"><div class="badge" data-k="rrec"></div><div class="nm" data-k="rojo" data-fit="w" data-max="30" data-min="18">PELEADOR ROJO</div></div>
  <div class="ctr"><img src="{LOGOA}"><div class="tm" id="tm">3:00</div><div class="st" id="st">PAUSA</div></div>
  <div class="f r"><div class="badge" data-k="brec"></div><div class="nm" data-k="azul" data-fit="w" data-max="30" data-min="18">PELEADOR AZUL</div></div>
 </div>
 <div class="pips" id="pips"></div>
 <div class="hidden"><span data-k="r_corner"></span><span data-k="b_corner"></span><span id="rd">1</span><span id="tot"></span><i id="pb"></i></div>
</div>
<div class="help" id="help">ESPACIO iniciar/pausar · R reiniciar · ← → round · + − 10 s · H ayuda · (lo normal es manejarlo desde CONTROL_EN_VIVO)</div>''', '''
var RL=parseFloat(Q.get('min')||'3')*60,tm=document.getElementById('tm');
var C={round:1,total:3,len:RL,rem:RL,running:false,at:Date.now()};
try{var sc=JSON.parse(localStorage.getItem('fcc2-clock-local')||'null');if(sc)C=sc}catch(e){}
function rem(){return C.running?Math.max(0,C.rem-(Date.now()-C.at)/1000):C.rem}
function setC(o){var r=rem();for(var k in o)C[k]=o[k];if(!('rem' in o))C.rem=r;C.at=Date.now();try{localStorage.setItem('fcc2-clock-local',JSON.stringify(C))}catch(e){}}
window.onLayout=function(l){var g=document.getElementById('bug');if(!g||!l)return;var pos=/^t/.test(l.pos||'')?'tc':'bc';
 g.className='bug pos-'+pos;g.style.transform='scale('+(+l.scale||1)+')';try{localStorage.setItem('fcc2-layout',JSON.stringify(l))}catch(e){}};
try{window.onLayout(JSON.parse(localStorage.getItem('fcc2-layout')||'null'))}catch(e){}
window.onClock=function(c){C={round:c.round,total:c.total||3,len:c.len,rem:c.rem,running:c.running,at:Date.now()};try{localStorage.setItem('fcc2-clock-local',JSON.stringify(C))}catch(e){}};
var lastP='';
function draw(){var r=rem();if(C.running&&r<=0){C.running=false;C.rem=0}var s=Math.ceil(r);
 tm.textContent=Math.floor(s/60)+':'+String(s%60).padStart(2,'0');tm.classList.toggle('low',s<=10&&s>0);
 document.getElementById('st').style.display=(!C.running&&r>0&&r<C.len)?'block':'none';
 var key=C.round+'/'+C.total;if(key!==lastP){lastP=key;var h='';for(var i=1;i<=(C.total||3);i++)h+='<s class="'+(i<C.round?'on':i===C.round?'cur':'')+'"></s>';document.getElementById('pips').innerHTML=h}
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

P['FCC2_Overlay_LowerThird'] = page('FCC 2 Lower Third', r"""
#lt{position:absolute;left:96px;bottom:96px;--c:var(--red);--c-rgb:var(--red-rgb);--cd:var(--red-dk)}
#lt.r{--c:var(--ca);--c-rgb:var(--ca-rgb);--cd:var(--ca-dk)}
#lt.b{--c:var(--cb);--c-rgb:var(--cb-rgb);--cd:var(--cb-dk)}
#lt{visibility:hidden}#lt.in,#lt.out{visibility:visible}
.row1{display:flex;align-items:stretch;height:132px;position:relative}
/* bloque de color con número / esquina */
.slab{position:relative;width:200px;margin-right:-26px;z-index:2;transform:skewX(-14deg);transform-origin:left;
 background:linear-gradient(160deg,rgba(255,255,255,.12),transparent 45%,rgba(0,0,0,.45)),var(--c);box-shadow:0 0 34px rgba(var(--c-rgb),.65),inset 0 0 0 2px rgba(255,255,255,.12);overflow:hidden}
.slab .in{position:absolute;inset:0;transform:skewX(14deg);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.slab small{font-family:"Bebas";font-size:20px;letter-spacing:3px;color:rgba(255,255,255,.85);line-height:1}
.slab b{font-family:"Bebas";font-weight:400;font-size:86px;line-height:.9;color:#fff;text-shadow:3px 3px 0 rgba(0,0,0,.35)}
.slab img{width:150px;filter:drop-shadow(0 4px 10px rgba(0,0,0,.6))}
.slab::after{content:"";position:absolute;top:-20%;bottom:-20%;width:60px;left:-120px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-14deg)}
/* barra principal */
.bar{position:relative;background:linear-gradient(90deg,rgba(6,6,6,.96) 0%,rgba(14,14,14,.94) 70%,rgba(var(--c-rgb),.35) 100%);padding:0 70px 0 64px;display:flex;flex-direction:column;justify-content:center;
 min-width:760px;clip-path:polygon(0 0,100% 0,calc(100% - 34px) 100%,0 100%);overflow:hidden}
.bar::before{content:"";position:absolute;left:0;right:0;top:0;height:4px;background:linear-gradient(90deg,var(--c),rgba(var(--c-rgb),0));transform-origin:left}
.bar::after{content:"";position:absolute;top:0;bottom:0;width:160px;left:-200px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.13),transparent);transform:skewX(-20deg)}
.mask{overflow:hidden;padding-top:6px}
.nm{font-family:"Bebas";font-size:88px;line-height:1;letter-spacing:2px;font-style:italic;color:#fff;white-space:nowrap;padding-right:.12em;text-shadow:3px 3px 0 #000}
.nk{font-family:"Bebas";font-size:30px;letter-spacing:6px;color:rgba(var(--c-rgb),1);filter:brightness(1.5);line-height:1.05;white-space:nowrap}
.nk:empty{display:none}
/* franja de características */
.row2{display:flex;margin-left:150px;margin-top:-2px;position:relative;z-index:1}
.chip{display:flex;flex-direction:column;justify-content:center;background:rgba(0,0,0,.88);border-bottom:3px solid var(--c);padding:8px 26px 6px;margin-right:6px;transform:skewX(-14deg);min-width:120px}
.chip>*{transform:skewX(14deg)}
.chip span{font-size:14px;letter-spacing:4px;color:#9d9d9d;line-height:1.1}
.chip b{font-family:"Bebas";font-weight:400;font-size:34px;letter-spacing:2px;color:#fff;line-height:1.05;white-space:nowrap}
.chip.hl{background:linear-gradient(90deg,transparent,rgba(0,0,0,.4)),var(--c);border-bottom-color:#fff}
.chip.hl span{color:rgba(255,255,255,.8)}
.tagline{position:absolute;left:205px;top:-34px;font-family:"Bebas";font-size:24px;letter-spacing:7px;color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.8);white-space:nowrap}.tagline i{display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--c);box-shadow:0 0 10px var(--c);margin-right:10px;vertical-align:2px;animation:pulse 1.2s ease-in-out infinite}

/* ===== animación de entrada ===== */
#lt.in .slab{animation:slabIn .55s cubic-bezier(.2,.9,.25,1.15) both,breathe2 3s 1.2s ease-in-out infinite}
#lt.in .slab::after{animation:shine 3.8s 1.1s ease-in-out infinite}
#lt.in .slab .in{animation:fadeUp .4s .3s ease both}
#lt.in .bar{animation:barIn .6s .14s cubic-bezier(.7,0,.2,1) both}
#lt.in .bar::before{animation:lineIn .7s .45s ease both}
#lt.in .bar::after{animation:sweep 4.2s .75s ease-in-out infinite}
#lt.in .nm{animation:nameIn .6s .38s cubic-bezier(.2,.9,.2,1) both}
#lt.in .nk{animation:fadeL .5s .62s ease both}
#lt.in .tagline{animation:fadeL .5s .8s ease both}
#lt.in .chip{animation:chipIn .45s var(--d,0s) cubic-bezier(.2,1.25,.4,1) both}
@keyframes slabIn{0%{transform:skewX(-14deg) scaleX(0);filter:brightness(3)}60%{filter:brightness(1.6)}100%{transform:skewX(-14deg) scaleX(1);filter:none}}
@keyframes barIn{from{clip-path:polygon(0 0,0 0,0 100%,0 100%)}to{clip-path:polygon(0 0,100% 0,calc(100% - 34px) 100%,0 100%)}}
@keyframes lineIn{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes nameIn{from{transform:translateY(105%) skewX(-8deg);letter-spacing:22px;opacity:0}to{transform:none;letter-spacing:2px;opacity:1}}
@keyframes fadeL{from{opacity:0;transform:translateX(-40px)}to{opacity:1;transform:none}}
@keyframes fadeUp{from{opacity:0;transform:skewX(14deg) translateY(30px)}to{opacity:1;transform:skewX(14deg)}}
@keyframes chipIn{from{opacity:0;transform:skewX(-14deg) translateY(-34px) scaleY(.4)}to{opacity:1;transform:skewX(-14deg)}}
@keyframes sweep{0%{left:-200px}35%,100%{left:110%}}
@keyframes shine{0%{left:-120px}30%,100%{left:260px}}
@keyframes breathe2{0%,100%{box-shadow:0 0 34px rgba(var(--c-rgb),.65),inset 0 0 0 2px rgba(255,255,255,.12)}50%{box-shadow:0 0 58px rgba(var(--c-rgb),1),inset 0 0 0 2px rgba(255,255,255,.25)}}
/* ===== animación de salida ===== */
#lt.out .chip{animation:chipOut .3s ease both}
#lt.out .nm,#lt.out .nk,#lt.out .tagline{animation:nameOut .3s ease both}
#lt.out .bar{animation:barOut .45s .18s cubic-bezier(.7,0,.3,1) both}
#lt.out .slab{animation:slabOut .4s .42s cubic-bezier(.6,0,.4,1) both}
@keyframes chipOut{to{opacity:0;transform:skewX(-14deg) translateY(-30px)}}
@keyframes nameOut{to{opacity:0;transform:translateY(-60%)}}
@keyframes barOut{from{clip-path:polygon(0 0,100% 0,calc(100% - 34px) 100%,0 100%)}to{clip-path:polygon(0 0,0 0,0 100%,0 100%)}}
@keyframes slabOut{to{transform:skewX(-14deg) scaleX(0);opacity:0}}
""", f"""<div id="lt"><div class="row1"><div class="slab glow"><div class="in" id="slab"></div></div>
<div class="tagline"><i></i><span id="tagline">FCC 2 · FIGHTING CHAMPIONSHIP CHILE</span></div><div class="bar"><div class="mask"><div class="nm" id="nm" data-fit="w" data-max="88" data-min="44">NOMBRE APELLIDO</div></div><div class="nk" id="nk"></div></div></div>
<div class="row2" id="chips"></div></div>
<img id="logoa" src="{LOGOA}" style="display:none">""", r"""
var LTD=null,LTV=false,LTK='';
function e2(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function ltRender(d){var el=document.getElementById('lt'),f=d.modo==='peleador';
 el.classList.remove('r','b');if(f&&(d.esq==='r'||d.esq==='b'))el.classList.add(d.esq);
 document.getElementById('slab').innerHTML=f&&d.num?'<small>'+e2(d.esq==='b'?(d.lbl||'ESQUINA AZUL'):(d.lbl||'ESQUINA ROJA'))+'</small><b>'+e2(d.num)+'</b><small>COMBATE</small>':'<img src="'+document.getElementById('logoa').src+'">';
 var nm=document.getElementById('nm');nm.textContent=d.nombre||'NOMBRE APELLIDO';
 document.getElementById('nk').textContent=f?(d.apodo||''):(d.cargo||'');
 document.getElementById('tagline').textContent=f?'FCC 2 · FIGHTING CHAMPIONSHIP CHILE':'FCC 2 · EN VIVO';
 var ch=[];if(f){if(d.disciplina)ch.push(['DISCIPLINA',d.disciplina,1]);if(d.categoria)ch.push(['CATEGORÍA',d.categoria]);if(d.gym)ch.push(['EQUIPO',d.gym]);if(d.record)ch.push(['RÉCORD',d.record]);if(d.edad)ch.push(['EDAD',/\d$/.test(d.edad)?d.edad+' AÑOS':d.edad]);if(d.peso&&!(d.categoria||'').match(/KG|PESADO/))ch.push(['PESO',d.peso])}
 document.getElementById('chips').innerHTML=ch.map(function(c,i){return '<div class="chip'+(c[2]?' hl':'')+'" style="--d:'+(.62+i*.09)+'s"><span>'+e2(c[0])+'</span><b>'+e2(c[1])+'</b></div>'}).join('');
 var bar=document.querySelector('.bar');bar.style.minWidth=Math.max(760,ch.length*190-80)+'px';fitAll()}
function ltPlay(cls){var el=document.getElementById('lt');el.classList.remove('in','out');void el.offsetWidth;if(cls)el.classList.add(cls)}
window.onLT=function(d,show){if(!d)d={};var k=JSON.stringify(d);
 if(show&&(!LTV||k!==LTK)){var go=function(){LTD=d;LTK=k;ltRender(d);ltPlay('in')};if(LTV){ltPlay('out');setTimeout(go,900)}else go();LTV=true}
 else if(!show&&LTV){LTV=false;ltPlay('out')}
 else if(!show){LTK=k}};
// vista previa sin control: ?demo=1
if(Q.get('demo'))setTimeout(function(){window.onLT({modo:'peleador',esq:Q.get('esq')||'r',num:'7',nombre:'ISABELLA AGUIRRES DÍAZ',apodo:'"LA LEONA"',disciplina:'NOGI',categoria:'59 KG · FEMENINO INFANTIL',gym:'MANZUR BROS',record:'4-1-0',edad:'15'},true)},300);
""", full=False)

P['FCC2_Overlay_Mosca'] = page('FCC 2 Mosca', """
.mosca{position:absolute;right:56px;bottom:56px;display:flex;flex-direction:column;align-items:flex-end;gap:8px;transform-origin:right bottom;transition:opacity .4s,transform .35s}
.mosca.pos-bl{right:auto;left:56px;align-items:flex-start;transform-origin:left bottom}
.mosca.pos-tr{bottom:auto;top:56px;transform-origin:right top}
.mosca.pos-tl{bottom:auto;top:56px;right:auto;left:56px;align-items:flex-start;transform-origin:left top}
.mosca img{width:250px;filter:drop-shadow(0 6px 16px rgba(0,0,0,.8))}
.live{display:flex;align-items:center;gap:10px;background:rgba(0,0,0,.78);border-left:6px solid var(--red2);padding:5px 16px 2px 12px;transform:skewX(-14deg)}
.live>*{transform:skewX(14deg)}
.live i{width:14px;height:14px;border-radius:50%;background:var(--red2);box-shadow:0 0 12px var(--red2);animation:pulse 1.2s ease-in-out infinite}
.live b{font-family:"Bebas";font-size:30px;letter-spacing:5px;color:#fff;font-weight:400}
.msg{font-family:"Bebas";font-size:24px;letter-spacing:4px;color:#fff;background:linear-gradient(90deg,var(--red),var(--red-dk));padding:4px 16px 1px;transform:skewX(-14deg);max-width:520px;white-space:nowrap;overflow:hidden;transition:opacity .5s}
.msg span{display:inline-block;transform:skewX(14deg)}
.msg.off{opacity:0}
.hide{display:none!important}
""", f"""<div class="mosca" id="mosca"><img src="{LOGOA}"><div class="live" id="live"><i></i><b data-k="estado">EN VIVO</b></div><div class="msg" id="msg"><span id="msgt">FCC 2 · FIGHTING CHAMPIONSHIP CHILE</span></div></div>""", """
var MS=['FCC 2 · FIGHTING CHAMPIONSHIP CHILE','BLACK HOUSE · SANTIAGO','AUSPICIA DI PIPINO PIZZA'],mi=0,CFG={pos:'br',scale:1,op:1,live:true,msgs:true};
try{var c0=JSON.parse(localStorage.getItem('fcc2-mosca')||'null');if(c0)CFG=c0}catch(e){}
function applyM(){var m=document.getElementById('mosca');m.className='mosca pos-'+(CFG.pos||'br');var top=/^t/.test(CFG.pos||'br');m.style.top=top?(CFG.avoid==='top'?'190px':''):'';m.style.bottom=!top?(CFG.avoid==='bottom'?'190px':''):'';m.style.transform='scale('+(+CFG.scale||1)+')';m.style.opacity=CFG.op==null?1:CFG.op;
 document.getElementById('live').classList.toggle('hide',!CFG.live);document.getElementById('msg').classList.toggle('hide',!CFG.msgs||!MS.length);
 if(CFG.list&&CFG.list.length)MS=CFG.list}
window.onMosca=function(c){CFG=c;try{localStorage.setItem('fcc2-mosca',JSON.stringify(c))}catch(e){}applyM();if(mi>=MS.length)mi=0;document.getElementById('msgt').textContent=MS[mi]||''};
applyM();document.getElementById('msgt').textContent=MS[0];
setInterval(function(){if(MS.length<2)return;var el=document.getElementById('msg');el.classList.add('off');setTimeout(function(){mi=(mi+1)%MS.length;document.getElementById('msgt').textContent=MS[mi];el.classList.remove('off')},550)},6000);""", full=False)

os.makedirs('out', exist_ok=True)
PID={'FCC2_VS':'vs','FCC2_Ganador':'ganador','FCC2_Overlay_Marcador':'marcador','FCC2_Overlay_LowerThird':'lt','FCC2_Overlay_Replay':'replay','FCC2_Overlay_Mosca':'mosca','FCC2_Pausa':'pausa','FCC2_Final':'final'}
for k, v in P.items():
    open(f'out/{k}.html', 'w').write(v.replace('__PANEL__', PID.get(k,'otro')))
print(list(P))
