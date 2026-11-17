<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>शुभ दीपावली | Shubh Deepavali Celebration</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts for Regal Indian Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rozha+One&family=Yatra+One&family=Poppins:wght@400;600;800&display=swap" rel="stylesheet">
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        /* Custom Fonts */
        .font-hindi {
            font-family: 'Rozha One', 'Yatra One', serif;
        }
        .font-english {
            font-family: 'Poppins', sans-serif;
        }

        /* Root Deepavali Color Palette */
        :root {
            --gold-light: #fff2a3;
            --gold-main: #f59e0b;
            --gold-dark: #b45309;
            --diya-flame: #ff6b00;
        }

        /* Rich Festive Background */
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: radial-gradient(circle at center, #2a0845 0%, #12002b 60%, #050010 100%);
            height: 100vh;
            color: #fff;
            user-select: none;
        }

        /* Rangoli Mandala Overlay Background */
        .mandala-bg {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: min(85vw, 85vh);
            height: min(85vw, 85vh);
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" fill="none" stroke="rgba(245, 158, 11, 0.08)" stroke-width="1.5"><circle cx="250" cy="250" r="230"/><circle cx="250" cy="250" r="190"/><circle cx="250" cy="250" r="150"/><circle cx="250" cy="250" r="100"/><path d="M 250 20 L 250 480 M 20 250 L 480 250 M 87 87 L 413 413 M 87 413 L 413 87"/><circle cx="250" cy="20" r="12"/><circle cx="250" cy="480" r="12"/><circle cx="20" cy="250" r="12"/><circle cx="480" cy="250" r="12"/></svg>');
            background-size: contain;
            background-repeat: no-repeat;
            pointer-events: none;
            animation: rotateMandala 120s linear infinite;
            z-index: 1;
        }

        @keyframes rotateMandala {
            from { transform: translate(-50%, -50%) rotate(0deg); }
            to { transform: translate(-50%, -50%) rotate(360deg); }
        }

        /* Regal Golden Text Styling with Shimmer Glow */
        .regal-gold-text {
            background: linear-gradient(135deg, #fff7ad 0%, #ffa900 30%, #ffd700 50%, #d47a00 80%, #fffbcf 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(255, 180, 0, 0.5), 0 0 40px rgba(255, 120, 0, 0.3);
            animation: goldShimmer 4s ease infinite alternate, textEntrance 2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @keyframes goldShimmer {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        @keyframes textEntrance {
            0% {
                opacity: 0;
                transform: scale(0.7) translateY(40px);
                filter: blur(10px);
            }
            100% {
                opacity: 1;
                transform: scale(1) translateY(0);
                filter: blur(0px);
            }
        }

        .sub-text-entrance {
            animation: subTextEntrance 2s cubic-bezier(0.16, 1, 0.3, 1) 0.5s forwards;
            opacity: 0;
        }

        @keyframes subTextEntrance {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Diya Flame Flicker Effects */
        .flame-container {
            position: relative;
            width: 24px;
            height: 40px;
            margin: 0 auto;
            transform-origin: center bottom;
            animation: flameWobble 2s infinite ease-in-out alternate;
        }

        .flame {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 34px;
            background: linear-gradient(to top, #ff2a00 0%, #ff8c00 40%, #ffee00 80%, #ffffff 100%);
            border-radius: 50% 50% 35% 35% / 80% 80% 35% 35%;
            box-shadow: 0 0 15px #ff5500, 0 0 30px #ffaa00, 0 -10px 20px #ffffaa;
            animation: flameFlicker 0.15s infinite alternate ease-in-out;
        }

        .flame-core {
            position: absolute;
            bottom: 2px;
            left: 50%;
            transform: translateX(-50%);
            width: 8px;
            height: 16px;
            background: #ffffff;
            border-radius: 50% 50% 35% 35% / 80% 80% 35% 35%;
            box-shadow: 0 0 8px #ffffff;
        }

        .flame-glow {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 60px;
            height: 60px;
            background: radial-gradient(circle, rgba(255, 140, 0, 0.4) 0%, rgba(255, 60, 0, 0) 70%);
            border-radius: 50%;
            animation: glowPulse 1.5s infinite alternate ease-in-out;
        }

        @keyframes flameFlicker {
            0% { transform: translateX(-50%) scale(1) rotate(-1deg); }
            100% { transform: translateX(-50%) scale(1.08, 0.95) rotate(1deg); }
        }

        @keyframes flameWobble {
            0% { transform: rotate(-3deg); }
            100% { transform: rotate(3deg); }
        }

        @keyframes glowPulse {
            0% { opacity: 0.7; transform: translate(-50%, -50%) scale(0.9); }
            100% { opacity: 1; opacity: 1; transform: translate(-50%, -50%) scale(1.2); }
        }

        /* SVG Diya Base Styling */
        .diya-svg {
            filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.6));
        }

        /* Interactive Firework Burst Click Hint */
        .click-hint {
            animation: pulseFade 2s infinite;
        }

        @keyframes pulseFade {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 0.9; }
        }

        /* Custom Audio Button Glow */
        .btn-glow {
            box-shadow: 0 0 15px rgba(245, 158, 11, 0.5);
            transition: all 0.3s ease;
        }
        .btn-glow:hover {
            box-shadow: 0 0 25px rgba(245, 158, 11, 0.8);
            transform: scale(1.05);
        }
    </style>
</head>
<body class="relative flex flex-col items-center justify-between min-h-screen">

    <!-- Fireworks & Sparkles Fullscreen Canvas -->
    <canvas id="fireworksCanvas" class="absolute inset-0 w-full h-full z-0 pointer-events-auto cursor-pointer"></canvas>

    <!-- Decorative Mandala Background Overlay -->
    <div class="mandala-bg"></div>

    <!-- Top Hanging Toran Festive Border (SVG Garland) -->
    <div class="relative z-10 w-full flex justify-between items-top px-2 md:px-10 pt-0 pointer-events-none">
        <svg class="w-full h-16 md:h-24 text-amber-500 opacity-80" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <!-- Toran Arch Path -->
            <path d="M0,0 Q150,90 300,0 Q450,90 600,0 Q750,90 900,0 Q1050,90 1200,0" fill="none" stroke="#f59e0b" stroke-width="3"/>
            <!-- Hanging Marigold Flowers & Bells -->
            <g fill="#ff6b00">
                <circle cx="150" cy="45" r="8" />
                <circle cx="450" cy="45" r="8" />
                <circle cx="750" cy="45" r="8" />
                <circle cx="1050" cy="45" r="8" />
            </g>
            <g fill="#ffd700">
                <polygon points="150,55 145,68 155,68" />
                <polygon points="450,55 445,68 455,68" />
                <polygon points="750,55 745,68 755,68" />
                <polygon points="1050,55 1045,68 1055,68" />
            </g>
        </svg>
    </div>

    <!-- Top Action Bar (Sound Control & Wishes Switcher) -->
    <div class="absolute top-4 right-4 z-30 flex items-center space-x-3">
        <button id="soundToggle" class="btn-glow bg-amber-600/80 hover:bg-amber-500 text-white p-3 rounded-full border border-amber-300 backdrop-blur-md flex items-center justify-center transition focus:outline-none" title="Toggle Sound">
            <i id="soundIcon" class="fas fa-volume-mute text-lg w-6 h-6 flex items-center justify-center"></i>
        </button>
        <button id="fireworkTrigger" class="btn-glow bg-amber-500/80 hover:bg-amber-400 text-amber-950 font-semibold px-4 py-2 rounded-full border border-amber-200 backdrop-blur-md text-sm transition hidden md:block">
            <i class="fas fa-magic mr-2"></i>आतिशबाज़ी जलाएं
        </button>
    </div>

    <!-- Center Content: Shubh Deepavali Greeting -->
    <main class="relative z-10 flex flex-col items-center justify-center my-auto text-center px-4 pointer-events-none">
        
        <!-- Decorative Top Crest Icon -->
        <div class="mb-2 text-amber-400 opacity-90 animate-bounce">
            <svg class="w-12 h-12 md:w-16 md:h-16 mx-auto" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2L14.5 9.5L22 12L14.5 14.5L12 22L9.5 14.5L2 12L9.5 9.5L12 2Z"/>
            </svg>
        </div>

        <!-- Main Hindi Typography -->
        <h1 class="font-hindi regal-gold-text text-5xl sm:text-7xl md:text-8xl lg:text-9xl font-bold tracking-wide leading-tight py-2">
            शुभ दीपावली
        </h1>

        <!-- Subheading in Hindi & English -->
        <div class="sub-text-entrance mt-3 space-y-2">
            <p class="font-hindi text-amber-200 text-xl sm:text-2xl md:text-3xl font-medium tracking-wider drop-shadow-md">
                आपको और आपके परिवार को रोशनी के पर्व की हार्दिक शुभकामनाएं
            </p>
            <p class="font-english text-amber-400/90 text-sm sm:text-base md:text-lg tracking-widest uppercase font-semibold">
                May the divine light of Diwali bring peace, prosperity & happiness
            </p>
        </div>

        <!-- Tap anywhere hint -->
        <p class="click-hint font-english text-xs md:text-sm text-amber-300/70 mt-6 tracking-wide">
            <i class="fas fa-hand-pointer mr-1"></i> Screen par kahin bhi click karein patakho ke liye
        </p>
    </main>

    <!-- Side Floating Diyas framing the central greeting -->
    <div class="absolute top-1/2 left-4 md:left-12 -translate-y-1/2 z-10 hidden sm:flex flex-col items-center space-y-12 pointer-events-none">
        <!-- Left Upper Diya -->
        <div class="transform -rotate-12 scale-90">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-16 h-10" viewBox="0 0 100 60">
                <path d="M10,20 Q50,60 90,20 Q50,25 10,20 Z" fill="#b45309" stroke="#ffd700" stroke-width="2"/>
                <path d="M20,22 Q50,45 80,22" fill="none" stroke="#f59e0b" stroke-width="2"/>
            </svg>
        </div>
        <!-- Left Lower Diya -->
        <div class="transform rotate-6 scale-110">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-20 h-12" viewBox="0 0 100 60">
                <path d="M10,20 Q50,60 90,20 Q50,25 10,20 Z" fill="#9a3412" stroke="#ffd700" stroke-width="2"/>
                <path d="M20,22 Q50,45 80,22" fill="none" stroke="#f59e0b" stroke-width="2"/>
            </svg>
        </div>
    </div>

    <div class="absolute top-1/2 right-4 md:right-12 -translate-y-1/2 z-10 hidden sm:flex flex-col items-center space-y-12 pointer-events-none">
        <!-- Right Upper Diya -->
        <div class="transform rotate-12 scale-90">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-16 h-10" viewBox="0 0 100 60">
                <path d="M10,20 Q50,60 90,20 Q50,25 10,20 Z" fill="#b45309" stroke="#ffd700" stroke-width="2"/>
                <path d="M20,22 Q50,45 80,22" fill="none" stroke="#f59e0b" stroke-width="2"/>
            </svg>
        </div>
        <!-- Right Lower Diya -->
        <div class="transform -rotate-6 scale-110">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-20 h-12" viewBox="0 0 100 60">
                <path d="M10,20 Q50,60 90,20 Q50,25 10,20 Z" fill="#9a3412" stroke="#ffd700" stroke-width="2"/>
                <path d="M20,22 Q50,45 80,22" fill="none" stroke="#f59e0b" stroke-width="2"/>
            </svg>
        </div>
    </div>

    <!-- Bottom Row Array of Illuminated Diyas -->
    <footer class="relative z-20 w-full pb-4 pt-6 px-4 flex justify-around items-end max-w-6xl mx-auto pointer-events-none">
        <!-- Diya Item 1 -->
        <div class="flex flex-col items-center">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-16 sm:w-20 md:w-24 h-10 sm:h-12" viewBox="0 0 100 60">
                <path d="M5,15 Q50,60 95,15 Q50,25 5,15 Z" fill="#7c2d12" stroke="#ffd700" stroke-width="2"/>
                <path d="M15,18 Q50,45 85,18" fill="none" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="50" cy="35" r="4" fill="#ffd700"/>
            </svg>
        </div>

        <!-- Diya Item 2 -->
        <div class="flex flex-col items-center">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-20 sm:w-24 md:w-28 h-12 sm:h-14" viewBox="0 0 100 60">
                <path d="M5,15 Q50,60 95,15 Q50,25 5,15 Z" fill="#9a3412" stroke="#ffd700" stroke-width="2"/>
                <path d="M15,18 Q50,45 85,18" fill="none" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="50" cy="35" r="5" fill="#ffd700"/>
            </svg>
        </div>

        <!-- Grand Center Diya -->
        <div class="flex flex-col items-center transform scale-110 sm:scale-125 -translate-y-2">
            <div class="flame-container" style="width:30px; height:48px;">
                <div class="flame-glow" style="width:80px; height:80px;"></div>
                <div class="flame" style="width:26px; height:42px;"></div>
                <div class="flame-core" style="width:10px; height:20px;"></div>
            </div>
            <svg class="diya-svg w-24 sm:w-28 md:w-36 h-14 sm:h-16" viewBox="0 0 100 60">
                <!-- Outer Bowl -->
                <path d="M0,10 Q50,65 100,10 Q50,22 0,10 Z" fill="#b45309" stroke="#ffe066" stroke-width="2.5"/>
                <!-- Inner Gold Rim -->
                <path d="M10,14 Q50,48 90,14" fill="none" stroke="#ffd700" stroke-width="2.5"/>
                <!-- Traditional Ornaments -->
                <circle cx="50" cy="38" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="1"/>
                <circle cx="30" cy="30" r="4" fill="#ff4500"/>
                <circle cx="70" cy="30" r="4" fill="#ff4500"/>
            </svg>
        </div>

        <!-- Diya Item 4 -->
        <div class="flex flex-col items-center">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-20 sm:w-24 md:w-28 h-12 sm:h-14" viewBox="0 0 100 60">
                <path d="M5,15 Q50,60 95,15 Q50,25 5,15 Z" fill="#9a3412" stroke="#ffd700" stroke-width="2"/>
                <path d="M15,18 Q50,45 85,18" fill="none" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="50" cy="35" r="5" fill="#ffd700"/>
            </svg>
        </div>

        <!-- Diya Item 5 -->
        <div class="flex flex-col items-center">
            <div class="flame-container">
                <div class="flame-glow"></div>
                <div class="flame"></div>
                <div class="flame-core"></div>
            </div>
            <svg class="diya-svg w-16 sm:w-20 md:w-24 h-10 sm:h-12" viewBox="0 0 100 60">
                <path d="M5,15 Q50,60 95,15 Q50,25 5,15 Z" fill="#7c2d12" stroke="#ffd700" stroke-width="2"/>
                <path d="M15,18 Q50,45 85,18" fill="none" stroke="#f59e0b" stroke-width="2"/>
                <circle cx="50" cy="35" r="4" fill="#ffd700"/>
            </svg>
        </div>
    </footer>

    <!-- JavaScript Logic: Canvas Fireworks & Web Audio Synthesizer -->
    <script>
        // Setup Canvas for High Performance Particle System
        const canvas = document.getElementById('fireworksCanvas');
        const ctx = canvas.getContext('2d');

        let width, height;
        function resizeCanvas() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        // Color Palettes for Festive Fireworks (Gold, Crimson, Emerald, Magenta, Cyan)
        const colorPalettes = [
            ['#ff416c', '#ff4b2b', '#ffd700', '#ffffff'],
            ['#f59e0b', '#fbbf24', '#d97706', '#fffbeb'],
            ['#00f2fe', '#4facfe', '#ffffff', '#00c6ff'],
            ['#b3ff00', '#38ef7d', '#11998e', '#ffffff'],
            ['#ff007f', '#ff758c', '#ff7eb3', '#ffffff']
        ];

        // Particle Class
        class Particle {
            constructor(x, y, color, velocityX, velocityY, friction, gravity, decay) {
                this.x = x;
                this.y = y;
                this.color = color;
                this.vx = velocityX;
                this.vy = velocityY;
                this.friction = friction || 0.96;
                this.gravity = gravity || 0.15;
                this.alpha = 1;
                this.decay = decay || (Math.random() * 0.015 + 0.01);
                this.size = Math.random() * 3 + 1.5;
            }

            update() {
                this.vx *= this.friction;
                this.vy *= this.friction;
                this.vy += this.gravity;
                this.x += this.vx;
                this.y += this.vy;
                this.alpha -= this.decay;
            }

            draw(ctx) {
                ctx.save();
                ctx.globalAlpha = Math.max(this.alpha, 0);
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = this.color;
                ctx.fill();
                ctx.restore();
            }
        }

        // Rocket Class (Ascending Firework)
        class Rocket {
            constructor(startX, startY, targetX, targetY) {
                this.x = startX;
                this.y = startY;
                this.targetX = targetX;
                this.targetY = targetY;
                this.distanceToTarget = Math.hypot(targetX - startX, targetY - startY);
                this.distanceTraveled = 0;
                this.coordinates = [];
                this.coordinateCount = 3;
                
                while (this.coordinateCount--) {
                    this.coordinates.push([this.x, this.y]);
                }
                
                this.angle = Math.atan2(targetY - startY, targetX - startX);
                this.speed = Math.random() * 3 + 7;
                this.friction = 0.99;
                this.brightness = Math.random() * 50 + 50;
            }

            update(index, rocketsArray, particlesArray) {
                this.coordinates.pop();
                this.coordinates.unshift([this.x, this.y]);

                this.speed *= this.friction;
                const vx = Math.cos(this.angle) * this.speed;
                const vy = Math.sin(this.angle) * this.speed;

                this.distanceTraveled = Math.hypot(this.x - (this.x + vx), this.y - (this.y + vy));
                this.x += vx;
                this.y += vy;

                // Check if target is reached or rocket slows down
                if (this.y <= this.targetY || Math.abs(this.x - this.targetX) < 10) {
                    createExplosion(this.targetX, this.targetY, particlesArray);
                    rocketsArray.splice(index, 1);
                    playFireworkSound();
                }
            }

            draw(ctx) {
                ctx.beginPath();
                ctx.moveTo(this.coordinates[this.coordinates.length - 1][0], this.coordinates[this.coordinates.length - 1][1]);
                ctx.lineTo(this.x, this.y);
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 2;
                ctx.stroke();
            }
        }

        const rockets = [];
        const particles = [];

        function createExplosion(x, y, particlesArray) {
            const particleCount = Math.floor(Math.random() * 60) + 80;
            const palette = colorPalettes[Math.floor(Math.random() * colorPalettes.length)];

            for (let i = 0; i < particleCount; i++) {
                const angle = Math.random() * Math.PI * 2;
                const speed = Math.random() * 8 + 1;
                const vx = Math.cos(angle) * speed;
                const vy = Math.sin(angle) * speed;
                const color = palette[Math.floor(Math.random() * palette.length)];
                particlesArray.push(new Particle(x, y, color, vx, vy));
            }
        }

        // Background Sparkles (Ambient Floating Lights)
        const ambientSparks = [];
        for (let i = 0; i < 40; i++) {
            ambientSparks.push({
                x: Math.random() * window.innerWidth,
                y: Math.random() * window.innerHeight,
                size: Math.random() * 2 + 0.5,
                alpha: Math.random(),
                speed: Math.random() * 0.5 + 0.2
            });
        }

        function drawAmbientSparks() {
            ambientSparks.forEach(spark => {
                spark.y -= spark.speed;
                if (spark.y < 0) spark.y = height;
                spark.alpha += (Math.random() - 0.5) * 0.05;
                spark.alpha = Math.max(0.1, Math.min(0.8, spark.alpha));

                ctx.save();
                ctx.globalAlpha = spark.alpha;
                ctx.fillStyle = '#ffd700';
                ctx.beginPath();
                ctx.arc(spark.x, spark.y, spark.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            });
        }

        // Animation Loop
        function animate() {
            requestAnimationFrame(animate);

            // Semi-transparent clearing for trail effect
            ctx.globalCompositeOperation = 'destination-out';
            ctx.fillStyle = 'rgba(0, 0, 0, 0.25)';
            ctx.fillRect(0, 0, width, height);

            ctx.globalCompositeOperation = 'lighter';

            // Draw ambient particles
            drawAmbientSparks();

            // Rockets loop
            let i = rockets.length;
            while (i--) {
                rockets[i].draw(ctx);
                rockets[i].update(i, rockets, particles);
            }

            // Particles loop
            let j = particles.length;
            while (j--) {
                particles[j].draw(ctx);
                particles[j].update();
                if (particles[j].alpha <= 0) {
                    particles.splice(j, 1);
                }
            }
        }

        // Launch Automatic Background Fireworks periodically
        function launchAutoFirework() {
            const startX = width * 0.1 + Math.random() * (width * 0.8);
            const startY = height;
            const targetX = width * 0.1 + Math.random() * (width * 0.8);
            const targetY = height * 0.1 + Math.random() * (height * 0.4);

            rockets.push(new Rocket(startX, startY, targetX, targetY));
        }

        setInterval(launchAutoFirework, 1200);

        // User Click / Tap to Launch Firework Burst
        window.addEventListener('click', (e) => {
            // Ignore click if clicking audio buttons
            if (e.target.closest('#soundToggle') || e.target.closest('#fireworkTrigger')) return;

            const startX = width / 2;
            const startY = height;
            const targetX = e.clientX;
            const targetY = e.clientY;

            rockets.push(new Rocket(startX, startY, targetX, targetY));
        });

        document.getElementById('fireworkTrigger').addEventListener('click', () => {
            for (let k = 0; k < 4; k++) {
                setTimeout(launchAutoFirework, k * 200);
            }
        });

        // Web Audio API Synthesizer for Firework Pops & Ambient Chimes (No external MP3 required)
        let audioCtx = null;
        let soundEnabled = false;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        function playFireworkSound() {
            if (!soundEnabled || !audioCtx) return;

            try {
                // White noise burst for firework pop
                const bufferSize = audioCtx.sampleRate * 0.3;
                const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                const output = buffer.getChannelData(0);

                for (let i = 0; i < bufferSize; i++) {
                    output[i] = Math.random() * 2 - 1;
                }

                const whiteNoise = audioCtx.createBufferSource();
                whiteNoise.buffer = buffer;

                const filter = audioCtx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(800, audioCtx.currentTime);
                filter.frequency.exponentialRampToValueAtTime(50, audioCtx.currentTime + 0.3);

                const gainNode = audioCtx.createGain();
                gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);

                whiteNoise.connect(filter);
                filter.connect(gainNode);
                gainNode.connect(audioCtx.destination);

                whiteNoise.start();
            } catch (err) {
                console.log('Audio playback error:', err);
            }
        }

        // Sound Toggle Button Handler
        const soundBtn = document.getElementById('soundToggle');
        const soundIcon = document.getElementById('soundIcon');

        soundBtn.addEventListener('click', () => {
            initAudio();
            if (audioCtx && audioCtx.state === 'suspended') {
                audioCtx.resume();
            }

            soundEnabled = !soundEnabled;

            if (soundEnabled) {
                soundIcon.className = 'fas fa-volume-up text-lg w-6 h-6 flex items-center justify-center text-amber-200';
                soundBtn.classList.add('bg-amber-500');
                // Play test festive chime
                playChimeSound();
            } else {
                soundIcon.className = 'fas fa-volume-mute text-lg w-6 h-6 flex items-center justify-center';
                soundBtn.classList.remove('bg-amber-500');
            }
        });

        function playChimeSound() {
            if (!audioCtx) return;
            const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
            notes.forEach((freq, idx) => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime + idx * 0.1);

                gain.gain.setValueAtTime(0.1, audioCtx.currentTime + idx * 0.1);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + idx * 0.1 + 0.8);

                osc.connect(gain);
                gain.connect(audioCtx.destination);

                osc.start(audioCtx.currentTime + idx * 0.1);
                osc.stop(audioCtx.currentTime + idx * 0.1 + 0.8);
            });
        }

        // Start Animation Loop on Load
        window.onload = () => {
            animate();
            // Fire initial burst batch
            setTimeout(() => {
                launchAutoFirework();
                setTimeout(launchAutoFirework, 300);
            }, 600);
        };
    </script>
</body>
</html>
