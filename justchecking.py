# birthday.py
import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="🎉 Happy Birthday", page_icon="🎈", layout="centered")

# ----- Change Streamlit page title -----
st.title("You are finally 22 oldie 🎉")

# ----- Funny subtitle -----
st.markdown(
    "<h3 style='text-align: center; color: #e91e63;'>Level 22 of rizzing up 💯 | Level 10 gyatt 🍑</h3>",
    unsafe_allow_html=True
)

# ----- Fixed name -----
name = "Pookie"

# ----- Working GIF -----
cake_image = "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"

# ----- Celebration HTML/JS -----
html_code = f"""
<div style="text-align:center; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;">
  <h2 style="font-size:32px; margin-bottom:6px; color:white;">🎂 Happy Birthday, {name}! 🎂</h2>
  <div id="celebration" style="margin-top:20px;">
    <img src="{cake_image}" alt="cake" style="max-width:320px; border-radius:8px; box-shadow: 0 6px 18px rgba(0,0,0,0.15);" />
  </div>
  <p id="msg" style="color: #ddd; margin-top:8px;">Surprise! 🎉</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
// burst confetti repeatedly a few times
let bursts = 0;
const ci = setInterval(function(){{
  confetti({{ particleCount: 200, spread: 140, origin: {{ x: Math.random(), y: Math.random()*0.6 }} }});
  bursts += 1;
  if(bursts > 12) clearInterval(ci);
}}, 400);
</script>
"""

html(html_code, height=520)

# ----- Python balloons for extra effect -----
st.balloons()
st.success(f"🎉 Happy Birthday, {name}! 🎉")


