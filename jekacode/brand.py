"""Official Jekacode colours, sampled from the logo PNG.

These hex codes are used in Streamlit, Gradio titles, HTML chat CSS, and notebook headers.
Navy #03045E · Green #16D365
"""

from pathlib import Path

NAVY = "#03045E"
GREEN = "#16D365"
BLACK = "#000000"
WHITE = "#FFFFFF"
LIGHT = "#F4F6FB"
MUTED = "#5B6475"

ROOT = Path(__file__).resolve().parents[1]  # course folder
LOGO = ROOT / "assets" / "jekacode-logo.png"
