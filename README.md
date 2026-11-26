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

## Adding a lamp

1. Frame its photos (above).
2. Copy `products/03/` to `products/04/` and change the title, `<h1>`, subtitle,
   photo, description and specs. Extra photos go as more `<img>` tags inside
   `.product-images`; they stack and open in the lightbox.
3. Add a `.lamp-item` block for it to the Kolekcija gallery in `home.html`.
4. Add its URL to `sitemap/sitemap.xml`.
