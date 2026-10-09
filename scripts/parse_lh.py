import json

with open('lighthouse_mobile.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('=== SCORES ===')
for k, v in d['categories'].items():
    print(f"{k.upper()}: {v['score'] * 100:.1f}")

print('\n=== AUDITS COM SCORE < 0.9 ===')
for k, v in d['audits'].items():
    score = v.get('score')
    if score is not None and score < 0.9:
        print(f"[{k}] (score: {score}) {v.get('title')}: {v.get('displayValue', '')}")

print('\n=== METRICAS PERFORMANCE ===')
for m in ['first-contentful-paint', 'largest-contentful-paint', 'total-blocking-time', 'cumulative-layout-shift', 'speed-index']:
    item = d['audits'].get(m, {})
    print(f"{m}: {item.get('displayValue')} (score: {item.get('score')})")
