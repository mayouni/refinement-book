#!/usr/bin/env python3
"""figures.py — custom explanatory diagrams injected into specific chapters.
Color is permitted inside figures (no yellow). Body prose stays monochrome.
Each value is a complete <figure>…</figure> (the interactive cascade carries its own <script>)."""
import math

# palette
INK="#1a1612"; SOFT="#6b6358"; RULE="#cfc8b4"; PAPER="#ffffff"; BG="#fbf8ee"
ORANGE="#E96A1A"; RED="#B83838"; GREEN="#2F6B3A"; GREEN2="#7FC272"
TEAL="#0f8a7d"; PURPLE="#6e2a86"; SAND="#efe9d6"

SERIF="'EB Garamond',serif"; SANS="'Inter',sans-serif"

# ---------------------------------------------------------------- Ch2 : line -> refinement
FIG_UNIT = f"""<figure>
<svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" aria-label="The line and the refinement">
  <!-- left: the diff -->
  <rect x="20" y="60" width="220" height="170" rx="6" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  <rect x="20" y="60" width="220" height="26" rx="6" fill="{SAND}"/>
  <text x="34" y="78" font-family="{SANS}" font-size="11" font-weight="700" fill="{INK}">loan_pricing.py</text>
  <g font-family="{SANS}" font-size="11">
    <rect x="20" y="100" width="220" height="20" fill="#fbe9e7"/>
    <text x="32" y="114" fill="{RED}">- penalty_cap = 18</text>
    <rect x="20" y="122" width="220" height="20" fill="#e7f3e9"/>
    <text x="32" y="136" fill="{GREEN}">+ penalty_cap = 16</text>
    <text x="32" y="160" fill="{SOFT}">  rate = base + cap</text>
    <text x="32" y="178" fill="{SOFT}">  ...</text>
  </g>
  <text x="130" y="252" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">the line — what changed, as bytes</text>

  <!-- arrow -->
  <g stroke="{INK}" stroke-width="1.6" fill="none">
    <line x1="258" y1="145" x2="318" y2="145"/><path d="M318 145 l-9 -5 l0 10 z" fill="{INK}" stroke="none"/>
  </g>

  <!-- right: the refinement card -->
  <rect x="338" y="56" width="242" height="178" rx="10" fill="{PAPER}" stroke="{INK}" stroke-width="1.3"/>
  <circle cx="368" cy="86" r="6" fill="{RED}"/>
  <text x="384" y="90" font-family="{SANS}" font-size="12" font-weight="700" fill="{INK}">tighten_penalty_cap</text>
  <line x1="354" y1="102" x2="564" y2="102" stroke="{RULE}" stroke-width="1"/>
  <g font-family="{SANS}" font-size="10.5" fill="{INK}">
    <text x="356" y="124"><tspan fill="{SOFT}">intent</tspan>   BCEAO 4.2 · cap 18 → 16</text>
    <text x="356" y="146"><tspan fill="{SOFT}">author</tspan>  amina@sonibank</text>
    <text x="356" y="168"><tspan fill="{SOFT}">cascade</tspan> 14 products · +hooks, reports</text>
    <text x="356" y="190"><tspan fill="{SOFT}">gate</tspan>    <tspan fill="{GREEN}" font-weight="700">tests ✓ · policy ✓</tspan></text>
    <text x="356" y="212"><tspan fill="{SOFT}">inverse</tspan> ↺ pre-computed</text>
  </g>
  <text x="459" y="252" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">the refinement — the change, made governable</text>
</svg>
<figcaption><strong>Fig.</strong> The unit changes. The diff shows which bytes moved; the refinement carries what the change <em>means</em> — its intent, its author, its blast radius, its proof, and its undo.</figcaption>
</figure>"""

# ---------------------------------------------------------------- Ch3 : tree -> graph
FIG_GRAPH = f"""<figure>
<svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" aria-label="A tree of files versus a typed graph">
  <!-- left: file tree -->
  <g font-family="{SANS}" font-size="12" fill="{INK}">
    <text x="28" y="60">📁 lending/</text>
    <text x="50" y="84" fill="{SOFT}">pricing.py</text>
    <text x="50" y="106" fill="{SOFT}">risk.py</text>
    <text x="50" y="128" fill="{SOFT}">policy.py</text>
    <text x="28" y="152">📁 tests/</text>
    <text x="50" y="174" fill="{SOFT}">test_pricing.py</text>
  </g>
  <text x="120" y="214" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">a tree of files</text>
  <text x="120" y="232" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">— where text lives</text>

  <g stroke="{INK}" stroke-width="1.6" fill="none">
    <line x1="232" y1="120" x2="292" y2="120"/><path d="M292 120 l-9 -5 l0 10 z" fill="{INK}" stroke="none"/>
  </g>

  <!-- right: typed graph -->
  <g stroke="{SOFT}" stroke-width="1.1" fill="none" opacity="0.7">
    <line x1="430" y1="70" x2="370" y2="130"/>
    <line x1="430" y1="70" x2="500" y2="120"/>
    <line x1="370" y1="130" x2="430" y2="185"/>
    <line x1="500" y1="120" x2="430" y2="185"/>
  </g>
  <line x1="430" y1="70" x2="430" y2="185" stroke="{PURPLE}" stroke-width="1.4" stroke-dasharray="4 3"/>
  <circle cx="430" cy="70" r="13" fill="{GREEN}"/><text x="430" y="74" text-anchor="middle" font-family="{SANS}" font-size="9" fill="#fff">fn</text>
  <rect x="357" y="118" width="26" height="24" rx="4" fill="{TEAL}"/><text x="370" y="134" text-anchor="middle" font-family="{SANS}" font-size="9" fill="#fff">type</text>
  <path d="M500 106 l14 14 l-14 14 l-14 -14 z" fill="{ORANGE}"/><text x="500" y="124" text-anchor="middle" font-family="{SANS}" font-size="8.5" fill="#fff">policy</text>
  <circle cx="430" cy="185" r="13" fill="{PURPLE}"/><text x="430" y="189" text-anchor="middle" font-family="{SANS}" font-size="8" fill="#fff">req</text>
  <text x="372" y="172" font-family="{SANS}" font-size="9" font-style="italic" fill="{PURPLE}">satisfies</text>
  <text x="475" y="214" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">a typed graph</text>
  <text x="475" y="232" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">— how the parts relate</text>
</svg>
<figcaption><strong>Fig.</strong> The same codebase, two representations. The tree shows where text lives; the graph shows how the parts relate — calls, depends-on, and the dashed <em>satisfies</em> edge that ties code to the requirement it serves.</figcaption>
</figure>"""

# ---------------------------------------------------------------- Ch4 : the four-stage compiler / the gate
def _stage(x, label):
    return (f'<rect x="{x}" y="74" width="96" height="52" rx="7" fill="{PAPER}" stroke="{INK}" stroke-width="1.1"/>'
            f'<text x="{x+48}" y="104" text-anchor="middle" font-family="{SANS}" font-size="10.5" font-weight="600" fill="{INK}">{label}</text>')
def _arrow(x):
    return f'<line x1="{x}" y1="100" x2="{x+14}" y2="100" stroke="{INK}" stroke-width="1.4"/><path d="M{x+14} 100 l-8 -4 l0 8 z" fill="{INK}"/>'
FIG_GATE = f"""<figure>
<svg viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" aria-label="The four-stage refinement compiler and the gate">
  <text x="14" y="58" font-family="{SANS}" font-size="10" font-weight="700" letter-spacing="0.06em" fill="{SOFT}">PROPOSAL</text>
  <line x1="14" y1="100" x2="40" y2="100" stroke="{INK}" stroke-width="1.4"/><path d="M40 100 l-8 -4 l0 8 z" fill="{INK}"/>
  {_stage(44,'structural')}{_arrow(140)}
  {_stage(158,'constraints')}{_arrow(254)}
  {_stage(272,'derivations')}{_arrow(368)}
  {_stage(386,'governance')}{_arrow(482)}
  <!-- gate diamond -->
  <path d="M530 100 l22 -22 l22 22 l-22 22 z" fill="{ORANGE}"/>
  <text x="552" y="104" text-anchor="middle" font-family="{SANS}" font-size="10" font-weight="700" fill="#fff">gate</text>
  <!-- outcomes -->
  <g stroke="{INK}" stroke-width="1.3" fill="none">
    <path d="M552 122 L552 160"/><path d="M552 160 l-4 -8 l8 0 z" fill="{INK}" stroke="none"/>
  </g>
  <text x="552" y="178" text-anchor="middle" font-family="{SANS}" font-size="11" font-weight="700" fill="{GREEN}">commit ✓</text>
  <text x="552" y="194" text-anchor="middle" font-family="{SANS}" font-size="9" fill="{SOFT}">or refuse ✗</text>
  <!-- audit -->
  <line x1="300" y1="160" x2="552" y2="160" stroke="{RULE}" stroke-width="1" stroke-dasharray="3 3"/>
  <rect x="44" y="146" width="256" height="28" rx="6" fill="{SAND}" stroke="{RULE}"/>
  <text x="172" y="164" text-anchor="middle" font-family="{SERIF}" font-size="12.5" font-style="italic" fill="{INK}">every verdict enters the audit chain</text>
  <text x="172" y="214" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">what cannot be validated cannot land</text>
</svg>
<figcaption><strong>Fig.</strong> Every refinement runs the same four stages before it can land. The gate is deterministic — what cannot be validated cannot commit — and either way the verdict enters the audit chain.</figcaption>
</figure>"""

# ---------------------------------------------------------------- Ch5 : INTERACTIVE cascade
def _cascade():
    cx, cy = 300, 205
    n1, r1 = 14, 122
    e1=[]; no1=[]
    for k in range(n1):
        a = -math.pi/2 + 2*math.pi*k/n1
        x = cx + r1*math.cos(a); y = cy + r1*math.sin(a)
        e1.append(f'<line class="ci-edge ci-e1" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GREEN}" stroke-width="1"/>')
        no1.append(f'<circle class="ci-node ci-n1" cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{GREEN}"/>')
    n2, r2 = 10, 182
    e2=[]; no2=[]
    for j in range(n2):
        a = -math.pi/2 + 2*math.pi*(j+0.5)/n2
        x1 = cx + r1*math.cos(a); y1 = cy + r1*math.sin(a)
        x = cx + r2*math.cos(a); y = cy + r2*math.sin(a)
        e2.append(f'<line class="ci-edge ci-e2" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GREEN2}" stroke-width="0.9"/>')
        no2.append(f'<circle class="ci-node ci-n2" cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{GREEN2}"/>')
    return f"""<figure>
<svg id="casc-int" viewBox="0 0 600 430" xmlns="http://www.w3.org/2000/svg" aria-label="Interactive cascade of a penalty-cap change">
  {''.join(e1)}
  {''.join(e2)}
  {''.join(no1)}
  {''.join(no2)}
  <circle cx="{cx}" cy="{cy}" r="34" fill="{RED}"/>
  <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="{SANS}" font-size="12" font-weight="700" fill="#fff">penalty_cap</text>
  <text x="{cx}" y="{cy+14}" text-anchor="middle" font-family="{SANS}" font-size="11" fill="#fff">18% → 16%</text>
  <text x="24" y="34" font-family="{SANS}" font-size="13" font-weight="700" fill="{INK}">revalidated: <tspan id="casc-count" fill="{GREEN}">0</tspan></text>
  <text id="casc-note" x="300" y="416" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}" opacity="0">4 downstream nodes did not change — early cutoff stops the cascade there.</text>
</svg>
<figcaption><span class="fig-hint">▶ Click the diagram to watch the cascade propagate.</span> &nbsp;A single penalty-cap change forces fourteen products to revalidate, then ripples outward — until a revalidated node's verdict comes back unchanged, where the cascade stops. <button class="ci-replay" id="casc-replay">Replay ↺</button></figcaption>
</figure>
<script>
(function(){{
  var svg=document.getElementById('casc-int'); if(!svg) return;
  var e1=svg.querySelectorAll('.ci-e1'), n1=svg.querySelectorAll('.ci-n1'),
      e2=svg.querySelectorAll('.ci-e2'), n2=svg.querySelectorAll('.ci-n2'),
      cnt=document.getElementById('casc-count'), note=document.getElementById('casc-note');
  var timers=[], played=false;
  function reset(){{ timers.forEach(clearTimeout); timers=[];
    Array.prototype.forEach.call(svg.querySelectorAll('.ci-lit'),function(el){{el.classList.remove('ci-lit');}});
    cnt.textContent='0'; note.setAttribute('opacity','0'); }}
  function play(){{ reset();
    for(var k=0;k<n1.length;k++){{ (function(k){{
      timers.push(setTimeout(function(){{ e1[k].classList.add('ci-lit'); n1[k].classList.add('ci-lit'); cnt.textContent=String(k+1); }}, 140+k*70));
    }})(k); }}
    var base=140+n1.length*70+220, cut=6;
    for(var j=0;j<cut;j++){{ (function(j){{
      timers.push(setTimeout(function(){{ e2[j].classList.add('ci-lit'); n2[j].classList.add('ci-lit'); }}, base+j*95));
    }})(j); }}
    timers.push(setTimeout(function(){{ note.setAttribute('opacity','1'); }}, base+cut*95+260));
  }}
  svg.addEventListener('click', play);
  var rb=document.getElementById('casc-replay'); if(rb) rb.addEventListener('click', function(e){{ e.preventDefault(); play(); }});
  // autoplay once when first scrolled into view
  if('IntersectionObserver' in window){{
    var io=new IntersectionObserver(function(es){{ es.forEach(function(en){{ if(en.isIntersecting && !played){{ played=true; play(); }} }}); }}, {{threshold:0.4}});
    io.observe(svg);
  }} else {{ setTimeout(play, 800); }}
}})();
</script>"""
FIG_CASCADE = _cascade()

# ---------------------------------------------------------------- Ch6 : access || change governance (Zero Trust)
def _loop(y, tag, tagc, a, b, c, d, dc):
    return f"""
  <text x="20" y="{y-30}" font-family="{SANS}" font-size="10" font-weight="700" letter-spacing="0.05em" fill="{tagc}">{tag}</text>
  <rect x="20"  y="{y-20}" width="116" height="40" rx="7" fill="{PAPER}" stroke="{INK}" stroke-width="1"/><text x="78"  y="{y+4}" text-anchor="middle" font-family="{SANS}" font-size="10.5" fill="{INK}">{a}</text>
  <rect x="166" y="{y-20}" width="116" height="40" rx="7" fill="{PAPER}" stroke="{INK}" stroke-width="1"/><text x="224" y="{y+4}" text-anchor="middle" font-family="{SANS}" font-size="10.5" fill="{INK}">{b}</text>
  <rect x="312" y="{y-20}" width="128" height="40" rx="7" fill="{PAPER}" stroke="{INK}" stroke-width="1"/><text x="376" y="{y+4}" text-anchor="middle" font-family="{SANS}" font-size="10.5" font-weight="700" fill="{dc}">{c}</text>
  <rect x="470" y="{y-20}" width="110" height="40" rx="7" fill="{SAND}" stroke="{RULE}" stroke-width="1"/><text x="525" y="{y+4}" text-anchor="middle" font-family="{SANS}" font-size="10.5" fill="{INK}">{d}</text>
  <g stroke="{INK}" stroke-width="1.3" fill="{INK}">
    <line x1="138" y1="{y}" x2="162" y2="{y}"/><path d="M162 {y} l-7 -4 l0 8 z"/>
    <line x1="284" y1="{y}" x2="308" y2="{y}"/><path d="M308 {y} l-7 -4 l0 8 z"/>
    <line x1="442" y1="{y}" x2="466" y2="{y}"/><path d="M466 {y} l-7 -4 l0 8 z"/>
  </g>"""
FIG_ZT = f"""<figure>
<svg viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" aria-label="Zero Trust governs access; Refine governs change — the same control pattern">
  {_loop(70,  'ZERO TRUST · governs ACCESS', TEAL, 'actor', 'policy engine', 'allow / deny', 'log', TEAL)}
  {_loop(180, 'REFINE · governs CHANGE', GREEN, 'authority', 'compiler', 'commit / refuse', 'audit chain', GREEN)}
  <text x="300" y="128" text-anchor="middle" font-family="{SERIF}" font-size="13" font-style="italic" fill="{SOFT}">same control pattern — different object</text>
</svg>
<figcaption><strong>Fig.</strong> The same loop, pointed at two different objects. Zero Trust governs what an actor may <em>reach</em> at runtime; Refine governs whether a change may <em>land</em>. Refinement-oriented programming extends Zero Trust from access to change.</figcaption>
</figure>"""

# ---------------------------------------------------------------- Ch8 : the Refine IDE, cascade facet (illustration)
FIG_IDE = f"""<figure>
<svg viewBox="0 0 600 330" xmlns="http://www.w3.org/2000/svg" aria-label="Illustration of the Refine IDE Cascade facet">
  <rect x="12" y="12" width="576" height="306" rx="10" fill="#eef0ec" stroke="{RULE}" stroke-width="1"/>
  <!-- ribbon / facet tabs -->
  <rect x="12" y="12" width="576" height="34" rx="10" fill="{PAPER}"/>
  <rect x="12" y="38" width="576" height="8" fill="{PAPER}"/>
  <g font-family="{SANS}" font-size="11" fill="{SOFT}">
    <text x="34" y="34">Code</text><text x="86" y="34">RFN</text>
    <rect x="128" y="18" width="64" height="22" rx="5" fill="{GREEN}"/><text x="160" y="34" text-anchor="middle" fill="#fff" font-weight="700">Cascade</text>
    <text x="212" y="34">Tests</text><text x="266" y="34">Graph</text>
  </g>
  <!-- left rail -->
  <rect x="12" y="46" width="92" height="272" fill="#f5f3ee"/>
  <g font-family="{SANS}" font-size="9.5" fill="{SOFT}">
    <text x="24" y="74">Visualize</text><text x="24" y="96">Analyze</text><text x="24" y="118">Compare</text>
  </g>
  <!-- workspace: chain-of-impact -->
  <text x="120" y="72" font-family="{SERIF}" font-size="12" font-style="italic" fill="{SOFT}">tighten_penalty_cap — chain of impact</text>
  <!-- target -->
  <circle cx="150" cy="150" r="22" fill="{RED}"/><text x="150" y="154" text-anchor="middle" font-family="{SANS}" font-size="8.5" fill="#fff">penalty_cap</text>
  <!-- tier 1 -->
  <g stroke="{GREEN}" stroke-width="1.2" fill="none">
    <line x1="172" y1="142" x2="262" y2="110"/><line x1="172" y1="150" x2="262" y2="170"/><line x1="172" y1="158" x2="262" y2="226"/>
  </g>
  <g fill="{PAPER}" stroke="{GREEN}" stroke-width="1.4">
    <rect x="262" y="96"  width="92" height="30" rx="6"/><rect x="262" y="156" width="92" height="30" rx="6"/><rect x="262" y="212" width="92" height="30" rx="6"/>
  </g>
  <g font-family="{SANS}" font-size="9" fill="{INK}">
    <text x="308" y="115" text-anchor="middle">loan_pricing</text><text x="308" y="175" text-anchor="middle">risk_assess</text><text x="308" y="231" text-anchor="middle">contract_tpl</text>
  </g>
  <!-- tier 2 -->
  <g stroke="{GREEN2}" stroke-width="1" fill="none">
    <line x1="354" y1="111" x2="438" y2="111"/><line x1="354" y1="171" x2="438" y2="150"/><line x1="354" y1="171" x2="438" y2="210"/>
  </g>
  <g fill="{PAPER}" stroke="{GREEN2}" stroke-width="1.2">
    <rect x="438" y="98"  width="84" height="26" rx="5"/><rect x="438" y="137" width="84" height="26" rx="5"/><rect x="438" y="197" width="84" height="26" rx="5"/>
  </g>
  <g font-family="{SANS}" font-size="8.5" fill="{SOFT}">
    <text x="480" y="114" text-anchor="middle">test_pricing</text><text x="480" y="153" text-anchor="middle">risk_report</text><text x="480" y="213" text-anchor="middle">q3_filing</text>
  </g>
  <!-- gate chips -->
  <rect x="438" y="250" width="54" height="20" rx="10" fill="{GREEN}"/><text x="465" y="264" text-anchor="middle" font-family="{SANS}" font-size="9" fill="#fff">gate ✓</text>
  <rect x="500" y="250" width="74" height="20" rx="10" fill="{SAND}" stroke="{RULE}"/><text x="537" y="264" text-anchor="middle" font-family="{SANS}" font-size="9" fill="{SOFT}">policy ✓</text>
</svg>
<figcaption><strong>Fig.</strong> The Refine IDE's Cascade facet — the chain-of-impact view a reviewer reads in place of the diff, with the target change at left and its consequences flowing rightward through gates. <em>(An illustration of the working prototype, not a screenshot.)</em></figcaption>
</figure>"""

FIGURES = {
    "ch2-the-unit-changed": FIG_UNIT,
    "ch3-the-codebase-as-a-graph": FIG_GRAPH,
    "ch4-the-compiler-that-revalidates": FIG_GATE,
    "ch5-the-cascade-as-a-working-surface": FIG_CASCADE,
    "ch6-authorities-attribution-audit": FIG_ZT,
    "ch8-five-surfaces-one-engine": FIG_IDE,
}
