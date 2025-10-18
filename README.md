<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CONCRETE LAMPS — Industrial Lighting</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: #ffffff;
            color: #1a1a1a;
            font-family: 'Courier New', monospace;
            line-height: 1.6;
            padding: 20px;
            max-width: 900px;
            margin: 0 auto;
        }
        
        h1 {
            font-size: 2.5em;
            font-weight: normal;
            margin-bottom: 10px;
            letter-spacing: 2px;
        }
        
        h2 {
            font-size: 1.5em;
            font-weight: normal;
            margin: 40px 0 20px 0;
            text-transform: uppercase;
            letter-spacing: 3px;
        }
        
        p {
            margin-bottom: 15px;
            font-size: 1em;
        }
        
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 30px 0;
        }
        
        .lamp-item {
            border: 1px solid #1a1a1a;
            padding: 0;
        }
        
        .lamp-img {
            width: 100%;
            height: 300px;
            background: #f5f5f5;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 1px solid #1a1a1a;
        }
        
        .lamp-info {
            padding: 15px;
        }
        
        .lamp-info h3 {
            font-weight: normal;
            margin-bottom: 10px;
            font-size: 1.1em;
        }
        
        hr {
            border: none;
            border-top: 1px solid #1a1a1a;
            margin: 40px 0;
        }
        
        .contact {
            margin-top: 40px;
        }
        
        a {
            color: #1a1a1a;
        }
        
        footer {
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid #1a1a1a;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <header>
        <h1>CONCRETE LAMPS</h1>
        <p>Industrial lighting. Raw materials. No compromise.</p>
    </header>

    <hr>

    <section>
        <h2>Philosophy</h2>
        <p>Each lamp is cast from concrete, left unpolished and unrefined. The material speaks for itself—heavy, permanent, industrial. These are not decorative objects. They are functional tools that embrace their weight and texture.</p>
        <p>Every surface irregularity, air bubble, and rough edge is intentional. This is concrete in its truest form.</p>
    </section>

    <hr>

    <section>
        <h2>Collection</h2>
        <div class="gallery">
            <div class="lamp-item">
                <div class="lamp-img">[LAMP_01]</div>
                <div class="lamp-info">
                    <h3>Model 01 — Table</h3>
                    <p>Height: 45cm</p>
                    <p>Base: 15x15cm</p>
                    <p>Weight: 8kg</p>
                </div>
            </div>
            
            <div class="lamp-item">
                <div class="lamp-img">[LAMP_02]</div>
                <div class="lamp-info">
                    <h3>Model 02 — Floor</h3>
                    <p>Height: 120cm</p>
                    <p>Base: 20x20cm</p>
                    <p>Weight: 18kg</p>
                </div>
            </div>
            
            <div class="lamp-item">
                <div class="lamp-img">[LAMP_03]</div>
                <div class="lamp-info">
                    <h3>Model 03 — Pendant</h3>
                    <p>Height: 30cm</p>
                    <p>Diameter: 18cm</p>
                    <p>Weight: 5kg</p>
                </div>
            </div>
            
            <div class="lamp-item">
                <div class="lamp-img">[LAMP_04]</div>
                <div class="lamp-info">
                    <h3>Model 04 — Wall</h3>
                    <p>Height: 25cm</p>
                    <p>Depth: 12cm</p>
                    <p>Weight: 4kg</p>
                </div>
            </div>
        </div>
    </section>

    <hr>

    <section>
        <h2>Materials</h2>
        <p>— Portland cement</p>
        <p>— Aggregate stone</p>
        <p>— Steel reinforcement</p>
        <p>— Cotton-wrapped electrical cord</p>
        <p>— Edison bulb fittings</p>
    </section>

    <hr>

    <section class="contact">
        <h2>Contact</h2>
        <p><a href="mailto:lamps@example.com">lamps@example.com</a></p>
        <p><a href="tel:+1234567890">+123 456 7890</a></p>
        <p>Based in [Your City]</p>
    </section>

    <footer>
        <p>© 2025 Concrete Lamps. All pieces handmade to order.</p>
    </footer>
</body>
</html>
