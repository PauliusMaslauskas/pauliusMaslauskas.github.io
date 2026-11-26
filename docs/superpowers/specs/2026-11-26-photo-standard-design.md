# Product photo standard: design

**Why:** the first drop goes live on 2026-11-27. The lamp photos came in different
shapes and framings (2:3 and 3:4, lamps 74–81% of the frame, off-centre), so the
homepage collection looked uneven. New photos need to drop in looking consistent
without careful hand-exporting.

**Goals:** one photo standard; new photos framed to it automatically; the homepage
collection lines up. **Non-goals:** redesigning any page, launch-day switch from the
coming-soon page, new product pages. **Anti-goal:** anything that makes adding a
photo on launch day slower.

## Standard

1200 × 1600 (3:4), transparent PNG. Lamp centred, 80% of frame height (max 90% of
width), floor line 10% from the bottom. Files `img/product/lamp_NN.png`, extra shots
`lamp_NN_2.png`, …

## Approaches

- **A. Standard + framing script (picked).** `tools/frame_photos.py` finds the lamp
  through the transparent background, scales and positions it. Photos don't need
  precise export; consistent by construction.
- **B. Standard only, exported by hand.** Less to build, but every photo has to be
  exported exactly right, under launch-day time pressure.

User approved the mockups (photo standard, homepage before/after, product page
with stacked shots) and said "standardise"; A was the stated recommendation.

## Changes

- `tools/frame_photos.py` (Pillow), refuses photos without a transparent background.
- Re-frame the three existing photos, renamed `lamp_1_color.png` → `lamp_01.png` etc.
- `css/home-styles.css`: `.lamp-img` takes `aspect-ratio: 3/4` instead of a fixed
  320 px / 220 px height. Phones (≤420 px, single column) keep the existing 280 px height.
- Product pages: no layout change; they already stack multiple photos with the lightbox.
- README: how to frame photos and add a lamp.
