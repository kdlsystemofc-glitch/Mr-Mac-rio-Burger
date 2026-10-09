with open("site/torn_top.txt", "r") as f:
    top_p = f.read().strip()
with open("site/torn_bot.txt", "r") as f:
    bot_p = f.read().strip()

with open("site/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace torn-paper-top SVG
top_old_start = html.find('<div class="torn-paper torn-paper-top"')
top_old_end = html.find('</div>', top_old_start) + len('</div>')

top_new = f'''<div class="torn-paper torn-paper-top" aria-hidden="true">
        <svg viewBox="0 0 1440 36" preserveAspectRatio="none" class="torn-svg">
          <path d="{top_p}" fill="#f2e9e2" />
        </svg>
      </div>'''

html = html[:top_old_start] + top_new + html[top_old_end:]

# Replace torn-paper-bottom SVG
bot_old_start = html.find('<div class="torn-paper torn-paper-bottom"')
bot_old_end = html.find('</div>', bot_old_start) + len('</div>')

bot_new = f'''<div class="torn-paper torn-paper-bottom" aria-hidden="true">
        <svg viewBox="0 0 1440 36" preserveAspectRatio="none" class="torn-svg">
          <path d="{bot_p}" fill="#f2e9e2" />
        </svg>
      </div>'''

html = html[:bot_old_start] + bot_new + html[bot_old_end:]

with open("site/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully!")
