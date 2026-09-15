from pathlib import Path
p=Path('/mnt/data/site_work/bhavya_top/index.html')
s=p.read_text()
# Remove moving ticker and replace with a static proof ribbon
start=s.index('<section class="ticker">')
end=s.index('</section>', start)+10
ribbon='''<section class="proof-ribbon"><div class="container proof-inner"><span><b>10</b> projects</span><i>·</i><span><b>4</b> flagship case studies</span><i>·</i><span><b>2</b> live Excel models</span><i>·</i><span><b>6</b> validation-led studies</span><i>·</i><span>Last updated <b>Sep 2026</b></span></div></section>'''
s=s[:start]+ribbon+s[end:]
# Replace role switch with stronger lens UI
old='<div class="role-switch" aria-label="Portfolio lens"><button class="role active" data-role="all">All work</button><button class="role" data-role="ib">IB / Valuation</button><button class="role" data-role="risk">Risk</button><button class="role" data-role="quant">Quant</button><button class="role" data-role="data">Data / AI</button></div>'
new='''<div class="lens-label mono">VIEW THE WORK THROUGH A HIRING LENS</div><div class="role-switch" aria-label="Portfolio lens"><button class="role active" data-role="all">Full library</button><button class="role" data-role="ib">IB / Valuation</button><button class="role" data-role="risk">Risk</button><button class="role" data-role="quant">Quant</button><button class="role" data-role="data">Data / AI</button></div><div class="lens-note" id="lensNote">Showing the full body of work. For a specific application, use a role lens to change what a recruiter sees first.</div>'''
s=s.replace(old,new)
# Change work header text
s=s.replace('Ten builds across deals, risk, quantitative research and data systems. Each flagship points to the underlying model, case study or repository.','A compact research library built for inspection. Start with the work most relevant to the role, then drill into the underlying model, case study or repository.')
# Insert evidence standard after research callout
needle='</div>\n</section>\n\n<section id="method"'
insert='''</div><div class="evidence-standard"><div><span class="mono">EVIDENCE STANDARD</span><h3>Every strong claim should have somewhere to go.</h3></div><div class="evidence-flow"><span>CLAIM</span><b>→</b><span>METHOD</span><b>→</b><span>OUTPUT</span><b>→</b><span>CHECK</span><b>→</b><span>LIMITATION</span></div><p>On the flagship projects, the homepage is only the index. The case study is where the assumptions, calculations, validation and caveats should be inspected.</p></div>\n</div>\n</section>\n\n<section id="method"'''
s=s.replace(needle,insert,1)
# Add credibility footer CTA before closing main
needle='</section>\n</main>\n<footer'
cta='''</section>\n<section class="closing container"><div><div class="eyebrow">07 / The short version</div><h2>Strongest signal:<br><em>the work is inspectable.</em></h2></div><div class="closing-copy"><p>I am not trying to make every project look equally impressive. The point is to make the strongest work easy to verify — and the limitations hard to miss.</p><div class="closing-actions"><a class="button primary" href="#work">Review the library ↑</a><a class="button secondary" href="https://github.com/BhavyaSatija54" target="_blank" rel="noreferrer">Open GitHub ↗</a></div></div></div></section>\n</main>\n<footer'''
s=s.replace(needle,cta,1)
# Replace JS role logic
old_js="""const roles=[...document.querySelectorAll('.role')]; const rows=[...document.querySelectorAll('.coverage-row')];
roles.forEach(btn=>btn.addEventListener('click',()=>{roles.forEach(x=>x.classList.remove('active'));btn.classList.add('active');const r=btn.dataset.role;rows.forEach(row=>row.hidden=!(r==='all'||row.dataset.cat===r));document.querySelectorAll('.coverage-category').forEach(cat=>cat.hidden=false);window.dispatchEvent(new Event('scroll'))}));"""
new_js="""const roles=[...document.querySelectorAll('.role')]; const rows=[...document.querySelectorAll('.coverage-row')]; const cats=[...document.querySelectorAll('.coverage-category')]; const lensNote=document.getElementById('lensNote');
const lensCopy={all:'Showing the full body of work. For a specific application, use a role lens to change what a recruiter sees first.',ib:'IB lens: valuation, M&A and transaction work are foregrounded. Quant/risk work remains available as supporting evidence.',risk:'Risk lens: market risk, credit risk and model validation are foregrounded. Deal work remains available as context.',quant:'Quant lens: systematic research, derivatives and market microstructure are foregrounded. Risk engineering remains supporting evidence.',data:'Data / AI lens: research infrastructure, data engineering and ML systems are foregrounded. Finance context remains visible.'};
function applyLens(r){rows.forEach(row=>row.hidden=!(r==='all'||row.dataset.cat===r)); cats.forEach(cat=>{const next=cat.nextElementSibling; let visible=false; let el=next; while(el && !el.classList.contains('coverage-category')){if(el.classList.contains('coverage-row')&&!el.hidden) visible=true;el=el.nextElementSibling;} cat.hidden=!visible;}); if(lensNote) lensNote.textContent=lensCopy[r]||lensCopy.all; window.dispatchEvent(new Event('scroll'));}
roles.forEach(btn=>btn.addEventListener('click',()=>{roles.forEach(x=>x.classList.remove('active'));btn.classList.add('active');applyLens(btn.dataset.role)}));"""
s=s.replace(old_js,new_js)
p.write_text(s)
