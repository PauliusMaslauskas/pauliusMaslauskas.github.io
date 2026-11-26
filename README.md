Gloto akis portfolio page.

## Product photos

Every lamp photo follows one standard so the collection lines up:

- 1200 × 1600 px (3:4 portrait), transparent PNG
- lamp centred, 80% of the frame tall, standing on a floor line 10% from the bottom
- named `img/product/lamp_NN.png`, extra shots `lamp_NN_2.png`, `lamp_NN_3.png`, …

You don't have to export to the standard by hand. Cut the lamp out (transparent
background), name the file, and run:

```sh
pip3 install pillow                                   # once
python3 tools/frame_photos.py ~/Desktop/lamp_04.png ~/Desktop/lamp_04_2.png
```

The framed photos land in `img/product/`.

## Adding a piece

Pieces are numbered Modelis 01, 02, 03 … with no separate names.

1. Frame its photos (above): `lamp_NN.png`, `lamp_NN_2.png`, …
2. Copy `products/_template/` to `products/NN/` and replace every `XX` with the number.
   Fill in height and weight, keep the one `Maitinimas` line that fits, and set the care
   section to `data-power="12v"` or `"220v"`. That shows the matching care-card text,
   which lives in `js/care.js`. Extra photos go as more `<img>` tags inside
   `.product-images`; they stack and open in the lightbox.
   (Folders starting with `_` are not published, so the template never goes live.)
3. Add a card for it to the Kolekcija gallery in `home.html`:
   ```html
   <a href="products/NN/" class="lamp-item">
       <div class="lamp-img">
           <img src="img/product/lamp_NN.png" alt="Modelis NN">
       </div>
       <div class="lamp-info">
           <h3>Modelis NN —</h3>
           <p>— cm · — kg</p>
       </div>
   </a>
   ```
4. Add `https://glostoakis.lt/products/NN/` to `sitemap/sitemap.xml`.
