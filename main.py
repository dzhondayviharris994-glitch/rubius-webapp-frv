from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path

app = FastAPI(title="Forverunu's Corp Website")

# Создаем временное хранилище для HTML
pages = {
    "index": """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Главная</title>
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    color: #fff;
    background: #0a0a0a;
  }

  .video-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -1;
  }

  .video-background video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.4;
    filter: brightness(0.7);
  }

  .content {
    position: relative;
    z-index: 1;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 60px 40px;
    text-align: center;
    background: radial-gradient(ellipse at center, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.8) 100%);
  }

  .logo {
    font-size: 4.5rem;
    font-weight: 300;
    margin-bottom: 10px;
    letter-spacing: 3px;
    background: linear-gradient(135deg, #fff 0%, #aaa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
  }

  .subtitle {
    font-size: 1.3rem;
    margin-bottom: 50px;
    color: #ccc;
    font-weight: 300;
    letter-spacing: 1px;
  }

  .welcome-text {
    font-size: 1.1rem;
    margin-bottom: 60px;
    max-width: 500px;
    line-height: 1.6;
    color: #aaa;
  }

  .buttons {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    max-width: 600px;
    width: 100%;
  }

  .btn {
    padding: 18px 25px;
    font-size: 1.1rem;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    background: rgba(255, 255, 255, 0.1);
    color: #fff;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.4s ease;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }

  .btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.7s ease;
  }

  .btn:hover {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.2);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }

  .btn:hover::before {
    left: 100%;
  }

  .accent {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: 1px solid rgba(255,255,255,0.2);
  }

  .accent:hover {
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
  }

  /* Анимации */
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .fade-in {
    animation: fadeInUp 1s ease forwards;
  }

  .delay-1 { animation-delay: 0.2s; opacity: 0; }
  .delay-2 { animation-delay: 0.4s; opacity: 0; }
  .delay-3 { animation-delay: 0.6s; opacity: 0; }
  .delay-4 { animation-delay: 0.8s; opacity: 0; }

  /* Мобильная адаптация */
  @media (max-width: 768px) {
    .content {
      padding: 40px 20px;
    }

    .logo {
      font-size: 2.5rem;
    }

    .buttons {
      grid-template-columns: 1fr;
    }

    .btn {
      padding: 16px 20px;
    }
  }
</style>
</head>
<body>

<div class="video-background">
  <video autoplay muted loop playsinline>
    <source src="https://www.w3schools.com/howto/rain.mp4" type="video/mp4" />
  </video>
</div>

<div class="content">
  <h1 class="logo fade-in">FORVERUNU'S CORP</h1>
  <p class="subtitle fade-in delay-1">Добро пожаловать в мой мир</p>
  <p class="welcome-text fade-in delay-2">Исследуйте мои проекты, интересы и творческие работы через эту интерактивную платформу</p>

  <div class="buttons">
    <a href="/games" class="btn fade-in delay-1">Мои игры</a>
    <a href="/viewed" class="btn fade-in delay-2">Просмотренные тайтлы</a>
    <a href="/aboutme" class="btn accent fade-in delay-3">Про меня</a>
    <a href="/myuniverse" class="btn fade-in delay-4">Моя вселенная</a>
  </div>
</div>

</body>
</html>""",
    "games": """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Игровая коллекция</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  :root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --bg-dark: #0f0f23;
    --bg-card: #1a1b2e;
    --bg-card-hover: #23243d;
    --text-light: #e2e8f0;
    --text-muted: #94a3b8;
    --accent: #8b5cf6;
    --gradient: linear-gradient(135deg, #6366f1, #8b5cf6);
  }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg-dark);
    color: var(--text-light);
    min-height: 100vh;
    padding: 20px;
    line-height: 1.6;
  }

  .container {
    max-width: 1400px;
    margin: 0 auto;
  }

  .header {
    text-align: center;
    margin-bottom: 40px;
    padding: 40px 20px;
    background: rgba(255,255,255,0.02);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.05);
  }

  .site-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 10px;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
  }

  .subtitle {
    font-size: 1.2rem;
    color: var(--text-muted);
    margin-bottom: 30px;
    font-weight: 400;
  }

  .navigation {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .nav-btn {
    padding: 12px 24px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    color: var(--text-light);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
  }

  .nav-btn:hover {
    background: rgba(255,255,255,0.1);
    border-color: var(--primary);
    transform: translateY(-2px);
  }

  .nav-btn.active {
    background: var(--gradient);
    border-color: transparent;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
  }

  .content-section {
    display: none;
    animation: fadeIn 0.5s ease;
  }

  .content-section.active {
    display: block;
  }

  .stats-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    padding: 20px;
    background: rgba(255,255,255,0.02);
    border-radius: 15px;
  }

  .total-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    margin-bottom: 30px;
  }

  .stat-card {
    background: var(--bg-card);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all 0.3s ease;
  }

  .stat-card:hover {
    transform: translateY(-3px);
    border-color: var(--primary);
  }

  .stat-number {
    font-size: 2rem;
    font-weight: 700;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
  }

  .stat-label {
    color: var(--text-muted);
    font-size: 0.9rem;
  }

  .games-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
  }

  .game-card {
    background: var(--bg-card);
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.3s ease;
    border: 1px solid rgba(255,255,255,0.05);
    position: relative;
  }

  .game-card:hover {
    transform: translateY(-5px);
    background: var(--bg-card-hover);
    border-color: var(--primary);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  }

  .game-badge {
    position: absolute;
    top: 12px;
    right: 12px;
    background: var(--gradient);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    z-index: 2;
  }

  .game-cover {
    width: 100%;
    height: 160px;
    object-fit: cover;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }

  .game-info {
    padding: 20px;
  }

  .game-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 10px;
    color: var(--text-light);
  }

  .game-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    font-size: 0.9rem;
  }

  .game-time {
    color: var(--primary);
    font-weight: 600;
  }

  .game-price {
    color: #10b981;
    font-weight: 600;
  }

  .game-last-played {
    color: var(--text-muted);
    font-size: 0.85rem;
    margin-top: 5px;
  }

  .progress-bar {
    width: 100%;
    height: 4px;
    background: rgba(255,255,255,0.1);
    border-radius: 2px;
    margin-top: 10px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    background: var(--gradient);
    border-radius: 2px;
    transition: width 0.3s ease;
  }

  .wishlist-header {
    text-align: center;
    margin-bottom: 30px;
  }

  .steam-trade {
    display: inline-block;
    padding: 12px 24px;
    background: var(--gradient);
    color: white;
    text-decoration: none;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease;
    margin-bottom: 30px;
  }

  .steam-trade:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .category-filters {
    display: flex;
    gap: 10px;
    margin-bottom: 25px;
    flex-wrap: wrap;
  }

  .filter-btn {
    padding: 8px 16px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    color: var(--text-light);
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .filter-btn.active {
    background: var(--gradient);
    border-color: transparent;
  }

  @media (max-width: 768px) {
    .site-title {
      font-size: 2rem;
    }

    .games-grid {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 15px;
    }

    .stats-header {
      flex-direction: column;
      gap: 15px;
      text-align: center;
    }

    .total-stats {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 480px) {
    body {
      padding: 10px;
    }

    .games-grid {
      grid-template-columns: 1fr;
    }

    .total-stats {
      grid-template-columns: 1fr;
    }

    .site-title {
      font-size: 1.8rem;
    }
  }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1 class="site-title">ИГРОВАЯ КОЛЛЕКЦИЯ</h1>
    <p class="subtitle">Мои достижения, статистика и желаемые игры</p>
    <div class="navigation">
      <a href="/" class="nav-btn">Главная</a>
      <button class="nav-btn active" data-tab="stats">Моя статистика</button>
      <button class="nav-btn" data-tab="wishlist">Список желаемого</button>
    </div>
  </div>

  <div id="stats" class="content-section active">
    <div class="stats-header">
      <h2>Обзор игровой активности</h2>
      <div class="category-filters">
        <button class="filter-btn active" data-filter="all">Все игры</button>
        <button class="filter-btn" data-filter="favorite">Фавориты</button>
        <button class="filter-btn" data-filter="recent">Недавние</button>
      </div>
    </div>

    <div class="total-stats">
      <div class="stat-card">
        <div class="stat-number" id="totalGames">0</div>
        <div class="stat-label">Всего игр</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="totalHours">0</div>
        <div class="stat-label">Часов в играх</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="favoriteGames">0</div>
        <div class="stat-label">Фаворитов</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" id="activeGames">0</div>
        <div class="stat-label">Активных игр</div>
      </div>
    </div>

    <div class="games-grid" id="gamesGrid"></div>
  </div>

  <div id="wishlist" class="content-section">
    <div class="wishlist-header">
      <a href="https://steamcommunity.com/tradeoffer/new/?partner=1300548007&token=vN1Bv-u2" target="_blank" class="steam-trade">
        Предложить обмен в Steam
      </a>
      <h2>Игры, которые я хочу получить</h2>
    </div>
    <div class="games-grid" id="wishlistGrid"></div>
  </div>
</div>

<script>
  // Оригинальный список игр с вашими данными
 const games = [
    {
      title: "CS2",
      image: "https://avatars.mds.yandex.net/i?id=31d8b17862c72acfcb22c0eb4d7015994d15df90-4012546-images-thumbs&n=13",
      time: 104.3,
      lastLaunch: "04.11.2025",
      favorite: true
    },
    {
      title: "R.E.P.O.",
      image: "https://avatars.mds.yandex.net/i?id=63b76af9dbe9be4965977b568c4b71e0364da6a3-11623870-images-thumbs&n=13",
      time: 132.5,
      lastLaunch: "03.11.2025",
      favorite: true
    },
    {
      title: "Cuphead",
      image: "https://avatars.mds.yandex.net/i?id=6dcce95b3805e8cae27b2ab35753e7d185db3895-12721850-images-thumbs&n=13",
      time: 112.9,
      lastLaunch: "28.05.2025",
      favorite: true
    },
    {
      title: "Doki Doki Literature Club",
      image: "https://avatars.mds.yandex.net/i?id=d51d1984498a54d9bafdae1a9f097fcc9e419fa3-5258850-images-thumbs&n=13",
      time: 80.9,
      lastLaunch: "05.01.2025",
      favorite: true
    },
    {
      title: "Little Nightmares 2",
      image: "https://yandex-images.clstorage.net/9vl8K4F01/d3c6ae_l41/4lyiNrY7P3zZnMQpNeea7fvAHZrZwwOQAmC04f2KGkKXFki8dwSZ9F6dHBJwSxInUVhrvzX_3PbV-oIm0LNHZfAJ43rweygpitfbfT3kn-_mnV6LxZkHzRgi6L7sgkcexBcu2lN84pIl-zQ0XWcJdloNPvIvvM2Que2nVIWnKyX4VLk6jiFZRfeOojsD-5zt67gxi-urDfwCVMW--eNLd5BgGddQXPq7O_sUFER8CEd9JBT_RJngp6CEp1Cshwk81X6PL4YZdVrugoMzGMGn2u2ZIKnclgLdIGjCmP3JeHaBVwjNe0jjoCnPKxxBUR5wTiUj-XuDwrufgoZOqpMIO_xKuAa-Lnxo05enNS36tdjQhwez2KYIxA1N2JLZz29QuHQ_3XtZzYEl4Acwd2IheVY9DeZYoN-3nIy0UoWwJifZcpoktxh2cP6-jB4544b66pw2l9e4OOwvS_-9yPRac5JHM_JBU9i6Ld8YNHd-F3x_Lxz9bL3znpKJt36ZpSQ523qwE6ELWXPogrA4Ed6L2ei0HK3rniD2A3P8g_jeZ3Ksfh_wW2jZmwHaCjBGcCFhQj8O43i_y66nhI5nnbodBv5IviKHIXxT2qyQFSb8pvzPghKs5JgT7BJV6rjQzH5pu1cg5HxU0qAw6z4qUUgSfnceGetxq--KgKmmbIupIRvsTbIFtxpFZOWMsxIgx4fO9ZgclOeYE-4dQ8yf1NVgW5FdI9dhT_ivHM4sGXZBIlx4ER3LR6HbgJKYrEunqxk25Hi5DpcmQ1_wqpo0NvC35c6iG6_uuTroJlf_mMz1aHWMfhzNd1T6igPOBBhDfj1EYBMyyESN1qKuvJVMg6E6B8dutTWQAktj7Z2iPSztn-3GnBe76oAC6QRPxpD10m97gmc71nNZ7JkCwCkJUFsGZngxLN1WnsC6taGCVqqDIS3Zb7wSlDlld_W5pwAdxJLH0Zsdrei2M-EBReeJ6uA",
      time: 28.3,
      lastLaunch: "17.07.2025",
      favorite: false
    },
    {
      title: "Soundpad",
      image: "https://avatars.mds.yandex.net/i?id=5ce3ee51f30048ecb75c63958faa99b09e9c05a7-13469218-images-thumbs&n=13",
      time: 24.9,
      lastLaunch: "02.11.2025",
      favorite: false
    },
    {
      title: "The Forest",
      image: "https://avatars.mds.yandex.net/i?id=7d16e0bc9ccb40001c742bf17e0b64a5242e9843-8981816-images-thumbs&n=13",
      time: 21.5,
      lastLaunch: "19.10.2025",
      favorite: false
    },
    {
      title: "The Binding of Isaac",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/113200/header.jpg?t=1643480517",
      time: 11.4,
      lastLaunch: "30.10.2025",
      favorite: false
    },
    {
      title: "Metro 2033 Redux",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/286690/header.jpg?t=1741110084",
      time: 10.3,
      lastLaunch: "03.05.2025",
      favorite: false
    },
    {
      title: "Selene ~Apoptosis~",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1398210/header.jpg?t=1744545547",
      time: 9,
      lastLaunch: "02.05.2025",
      favorite: false
    },
    {
      title: "Euro Truck Simulator 2",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/227300/9a81dc3126c56637297b654f9dcac057cfd79b77/header.jpg?t=1762506977",
      time: 9,
      lastLaunch: "27.10.2025",
      favorite: true
    },
    {
      title: "No, I'm not a Human",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/3180070/fadebc14211b17b5a6603926612ead9294cad9ce/header.jpg?t=1761654689",
      time: 8.9,
      lastLaunch: "28.09.2025",
      favorite: false
    },
    {
      title: "Undertale",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/391540/header.jpg?t=1757349115",
      time: 8.4,
      lastLaunch: "04.01.2025",
      favorite: false
    },
    {
      title: "MiSide",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/2527500/header.jpg?t=1761879413",
      time: 7.3,
      lastLaunch: "28.05.2025",
      favorite: false
    },
    {
      title: "Plague Inc: Evolved",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/246620/header.jpg?t=1762364180",
      time: 5.4,
      lastLaunch: "22.03.2025",
      favorite: false
    },
    {
      title: "Goose Goose Duck",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1568590/header.jpg?t=1750955551",
      time: 5,
      lastLaunch: "10.05.2025",
      favorite: false
    },
    {
      title: "POSTAL 2",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/223470/header_russian.jpg?t=1726251082",
      time: 4.3,
      lastLaunch: "14.07.2025",
      favorite: false
    },
    {
      title: "Buckshot Roulette",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/2835570/header.jpg?t=1762442355",
      time: 3.4,
      lastLaunch: "30.03.2025",
      favorite: false
    },
    {
      title: "Detroit: Become Human",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1222140/header.jpg?t=1667468479",
      time: 2.8,
      lastLaunch: "22.03.2025",
      favorite: false
    },
    {
      title: "SCP: Secret Laboratory",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/700330/ef0c2c19cbd56f534b9378dee066f23279a29275/header.jpg?t=1763161281",
      time: 2.6,
      lastLaunch: "27.05.2025",
      favorite: false
    },
    {
      title: "The NOexistenceN of you AND me",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/2873080/header.jpg?t=1758591398",
      time: 1.72,
      lastLaunch: "27.05.2025",
      favorite: false
    },
    {
      title: "Left 4 Dead",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/500/header.jpg?t=1745368560",
      time: 1.48,
      lastLaunch: "28.05.2025",
      favorite: false
    },
    {
      title: "House Flipper",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/613100/header_russian.jpg?t=1763159723",
      time: 1.33,
      lastLaunch: "19.07.2025",
      favorite: false
    },
    {
      title: "Everlasting Summer",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/331470/header_russian.jpg?t=1741850740",
      time: 1.3,
      lastLaunch: "25.08.2025",
      favorite: false
    },
    {
      title: "Left 4 Dead 2",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/550/header.jpg?t=1745368562",
      time: 1.22,
      lastLaunch: "10.06.2025",
      favorite: false
    },
    {
      title: "Hatred",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/341940/header.jpg?t=1727965684",
      time: 1.03,
      lastLaunch: "28.10.2025",
      favorite: false
    },
    {
      title: "Eraser",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1819570/header.jpg?t=1640571341",
      time: 0.98,
      lastLaunch: "29.08.2025",
      favorite: false
    },
    {
      title: "Strinova",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1282270/9f2316553893c46fadf63fa27df1d2d0d3383f8f/header.jpg?t=1761717145",
      time: 0.666667,
      lastLaunch: "06.01.2025",
      favorite: false
    },
    {
      title: "Ваша мать",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/3399950/header_russian.jpg?t=1757872666",
      time: 0.633333,
      lastLaunch: "25.08.2025",
      favorite: false
    },
    {
      title: "City Car Driving",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/493490/header.jpg?t=1698810885",
      time: 0.616667,
      lastLaunch: "27.05.2025",
      favorite: false
    },
    {
      title: "Liar`s Bar",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/3097560/779fd888bc6ac673dd75254aad814b7e8a47ce7a/header.jpg?t=1750969308",
      time: 0.6,
      lastLaunch: "28.05.2025",
      favorite: false
    },
    {
      title: "Tiny Bunny",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1421250/header.jpg?t=1762968763",
      time: 0.5,
      lastLaunch: "19.07.2025",
      favorite: true
    },
    {
      title: "Project Zomboid",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/108600/header.jpg?t=1762369969",
      time: 0.4,
      lastLaunch: "22.03.2025",
      favorite: false
    },
    {
      title: "你的老婆",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/3339420/fe3293227391e65cbcb47bf0ced6aa0f4fd28bf0/header.jpg?t=1763386146",
      time: 0.033333,
      lastLaunch: "08.02.2025",
      favorite: false
    },
    {
      title: "Heavy Rain",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/960910/header.jpg?t=1675271942",
      time: 0,
      lastLaunch: "-",
      favorite: false
    },
    {
      title: "Portal",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/400/header.jpg?t=1745368554",
      time: 0.25,
      lastLaunch: "03.06.2025",
      favorite: false
    },
    {
      title: "Portal 2",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/620/header.jpg?t=1745363004",
      time: 0.066667,
      lastLaunch: "19.07.2025",
      favorite: false
    },
    {
      title: "Outlast 2",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/414700/header.jpg?t=1618944453",
      time: 0.0000000002673,
      lastLaunch: "-",
      favorite: false
    },
    {
      title: "Pic-Me!",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/3265280/header.jpg?t=1761043872",
      time: 0.07333299903,
      lastLaunch: "-",
      favorite: false
    },
    {
      title: "PUBG: BATTLEGROUNDS",
      image: "https://avatars.mds.yandex.net/i?id=5681603cdc0a5efcedc837185a80dcf63352071b-5709069-images-thumbs&n=13",
      time: 0.000000000703,
      lastLaunch: "16.08.2024",
      favorite: false
    },
     {
      title: "Wallpaper Engine",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/431960/header.jpg?t=1739211362",
      time: 17.4,
      lastLaunch: "16.11.2025",
      favorite: true
    },
    {
      title: "Станция Сайхате",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/3079280/header_russian.jpg?t=1754553538",
      time: 17.3,
      lastLaunch: "16.09.2025",
      favorite: false
    },
    {
      title: "Phasmophobia",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/739630/c227a2855aba60f3657bc0c3a46515b8c41fb2b6/header.jpg?t=1763980860",
      time: 13.3,
      lastLaunch: "24.03.2025",
      favorite: false
    }
  ];

  // Оригинальный список желаемых игр
  const wishlist = [
    {
      title: "Teardown",
      image: "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1167630/ss_dc08bfb0b8b381bc580d2599ad24462af4690a20.jpg?t=1760518638",
      price: "1399 руб"
    },
    {
      title: "Garry's Mod",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/4000/header.jpg?t=1745368554",
      price: "750 руб"
    },
    {
      title: "Little Nightmares III",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1392860/header.jpg?t=1762353803",
      price: "2849 руб"
    },
    {
      title: "WorldBox - God Simulator",
      image: "https://shared.fastly.steamstatic.com/store_item_assets//steam/apps/1206560/header.jpg?t=1762353803",
      price: "710 руб"
    },
    {
      title: "BeamNG.drive",
      image: "https://avatars.mds.yandex.net/i?id=d762ec2b049fbd037963dbce962f27de58c5f1ce-5235013-images-thumbs&n=13",
      price: "880 руб"
    },
    {
      title: "Rust",
      image: "https://avatars.mds.yandex.net/i?id=acfcbd481f14cc3eff0d1b50a26b89bd497a4dc8-5342977-images-thumbs&n=13",
      price: "1399 руб"
    },
    {
      title: "Dispatch",
      image: "https://shared.fastly.steamstatic.com//store_item_assets/steam/apps/2592160/header.jpg?t=1763398023",
      price: "1100 руб"
    }
  ];

  // Сортировка игр по времени
  games.sort((a, b) => b.time - a.time);

  const gamesGrid = document.getElementById('gamesGrid');
  const wishlistGrid = document.getElementById('wishlistGrid');
  const navBtns = document.querySelectorAll('.nav-btn');
  const filterBtns = document.querySelectorAll('.filter-btn');

  // Функция для обновления статистики
  function updateStats() {
    const totalGames = games.length;
    const totalHours = games.reduce((sum, game) => sum + game.time, 0);
    const favoriteGames = games.filter(game => game.favorite).length;
    const activeGames = games.filter(game => game.time > 0).length;

    document.getElementById('totalGames').textContent = totalGames;
    document.getElementById('totalHours').textContent = totalHours;
    document.getElementById('favoriteGames').textContent = favoriteGames;
    document.getElementById('activeGames').textContent = activeGames;
  }

  // Рендер игр
  function renderGames(filter = 'all') {
    gamesGrid.innerHTML = '';

    let filteredGames = games;

    if (filter === 'favorite') {
      filteredGames = games.filter(game => game.favorite);
    } else if (filter === 'recent') {
      // Показываем игры, в которые играли в последнее время (за последние 30 дней)
      const thirtyDaysAgo = new Date();
      thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30);

      filteredGames = games.filter(game => {
        if (game.lastLaunch === '-' || !game.lastLaunch) return false;

        const launchDate = new Date(game.lastLaunch.split('.').reverse().join('-'));
        return launchDate >= thirtyDaysAgo;
      });
    }

    filteredGames.forEach(game => {
      const progressWidth = Math.min((game.time / 150) * 100, 100);

      const card = document.createElement('div');
      card.className = 'game-card';
      card.innerHTML = `
        ${game.favorite ? '<div class="game-badge">Фаворит</div>' : ''}
        <img class="game-cover" src="${game.image}" alt="${game.title}" loading="lazy">
        <div class="game-info">
          <h3 class="game-title">${game.title}</h3>
          <div class="game-meta">
            <span class="game-time">${game.time} ч</span>
          </div>
          <div class="progress-bar">
            <div class="progress-fill" style="width: ${progressWidth}%"></div>
          </div>
          <div class="game-last-played">Последний запуск: ${game.lastLaunch}</div>
        </div>
      `;

      gamesGrid.appendChild(card);
    });
  }

  // Рендер вишлиста
  function renderWishlist() {
    wishlistGrid.innerHTML = '';

    wishlist.forEach(game => {
      const card = document.createElement('div');
      card.className = 'game-card';
      card.innerHTML = `
        <img class="game-cover" src="${game.image}" alt="${game.title}" loading="lazy">
        <div class="game-info">
          <h3 class="game-title">${game.title}</h3>
          <div class="game-meta">
            <span class="game-price">${game.price}</span>
          </div>
        </div>
      `;
      wishlistGrid.appendChild(card);
    });
  }

  // Переключение табов
  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      if (btn.dataset.tab) {
        navBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        document.querySelectorAll('.content-section').forEach(section => {
          section.classList.remove('active');
        });
        document.getElementById(btn.dataset.tab).classList.add('active');

        if (btn.dataset.tab === 'wishlist') {
          renderWishlist();
        }
      }
    });
  });

  // Фильтрация игр
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderGames(btn.dataset.filter);
    });
  });

  // Инициализация
  updateStats();
  renderGames();
</script>
</body>
</html>""",
    "viewed": """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Просмотренные тайтлы</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  :root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --bg-dark: #0f0f23;
    --bg-card: #1a1b2e;
    --bg-card-hover: #23243d;
    --text-light: #e2e8f0;
    --text-muted: #94a3b8;
    --accent: #8b5cf6;
    --gradient: linear-gradient(135deg, #6366f1, #8b5cf6);
    --admin: #ef4444;
  }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg-dark);
    color: var(--text-light);
    min-height: 100vh;
    line-height: 1.6;
  }

  .container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
  }

  .header {
    text-align: center;
    margin-bottom: 40px;
    padding: 60px 20px;
    background: rgba(255,255,255,0.02);
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.05);
    animation: fadeIn 0.8s ease;
  }

  .site-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 15px;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
  }

  .subtitle {
    font-size: 1.3rem;
    color: var(--text-muted);
    font-weight: 400;
  }

  /* Стили для поисковой строки */
  .search-container {
    margin: 30px 0;
    display: flex;
    justify-content: center;
    animation: fadeIn 0.8s ease 0.2s both;
  }

  .search-box {
    position: relative;
    width: 100%;
    max-width: 600px;
  }

  .search-input {
    width: 100%;
    padding: 18px 50px 18px 25px;
    font-size: 1.1rem;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    color: var(--text-light);
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
  }

  .search-input:focus {
    outline: none;
    border-color: var(--primary);
    background: rgba(255,255,255,0.08);
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
    transform: translateY(-2px);
  }

  .search-input::placeholder {
    color: var(--text-muted);
  }

  .search-icon {
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-muted);
    transition: color 0.3s ease;
  }

  .search-input:focus + .search-icon {
    color: var(--primary);
  }

  .search-results {
    margin-top: 10px;
    color: var(--text-muted);
    font-size: 0.9rem;
    text-align: center;
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .search-results.show {
    opacity: 1;
  }

  .category-tabs {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-bottom: 40px;
    flex-wrap: wrap;
  }

  .category-tab {
    padding: 15px 30px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    color: var(--text-light);
    font-weight: 500;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    cursor: pointer;
    font-size: 1.1rem;
  }

  .category-tab:hover {
    background: rgba(255,255,255,0.1);
    border-color: var(--primary);
    transform: translateY(-2px);
  }

  .category-tab.active {
    background: var(--gradient);
    border-color: transparent;
    box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
  }

  .content-section {
    display: none;
    animation: fadeInUp 0.5s ease;
  }

  .content-section.active {
    display: block;
  }

  .titles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
  }

  .title-card {
    background: var(--bg-card);
    border-radius: 16px;
    padding: 25px;
    transition: all 0.3s ease;
    border: 1px solid rgba(255,255,255,0.05);
    text-decoration: none;
    color: var(--text-light);
    position: relative;
    overflow: hidden;
  }

  .title-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
    transition: left 0.7s ease;
  }

  .title-card:hover {
    background: var(--bg-card-hover);
    border-color: var(--primary);
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  }

  .title-card:hover::before {
    left: 100%;
  }

  .title-name {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 8px;
    line-height: 1.4;
  }

  .title-status {
    font-size: 0.9rem;
    color: var(--text-muted);
    font-weight: 500;
  }

  .status-soon {
    color: #f59e0b;
  }

  .home-link {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 15px 30px;
    background: var(--gradient);
    color: white;
    text-decoration: none;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    margin-bottom: 30px;
  }

  .home-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
  }

  /* Кнопка администрации */
  .admin-button-container {
    text-align: center;
    margin: 20px 0;
    display: none;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease;
  }

  .admin-button-container.show {
    display: block;
    opacity: 1;
    transform: translateY(0);
  }

  .admin-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    padding: 16px 36px;
    background: linear-gradient(135deg, var(--admin), #dc2626);
    color: white;
    text-decoration: none;
    border-radius: 12px;
    font-weight: 700;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    border: 2px solid rgba(239, 68, 68, 0.3);
    box-shadow: 0 6px 20px rgba(239, 68, 68, 0.3);
    width: auto;
  }

  .admin-button:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 10px 25px rgba(239, 68, 68, 0.4);
    background: linear-gradient(135deg, #dc2626, var(--admin));
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(-30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .section-header {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 30px;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
  }

  /* Анимации для карточек при фильтрации */
  .title-card.hidden {
    display: none;
  }

  .title-card.visible {
    animation: cardAppear 0.4s ease;
  }

  @keyframes cardAppear {
    from {
      opacity: 0;
      transform: scale(0.9) translateY(10px);
    }
    to {
      opacity: 1;
      transform: scale(1) translateY(0);
    }
  }

  @media (max-width: 768px) {
    .container {
      padding: 15px;
    }

    .header {
      padding: 40px 20px;
      margin-bottom: 30px;
    }

    .site-title {
      font-size: 2.2rem;
    }

    .subtitle {
      font-size: 1.1rem;
    }

    .search-input {
      padding: 15px 45px 15px 20px;
      font-size: 1rem;
    }

    .category-tabs {
      gap: 10px;
      margin-bottom: 30px;
    }

    .category-tab {
      padding: 12px 20px;
      font-size: 1rem;
      flex: 1;
      min-width: 140px;
      text-align: center;
    }

    .titles-grid {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 15px;
    }

    .title-card {
      padding: 20px;
    }

    .title-name {
      font-size: 1.1rem;
    }

    .section-header {
      font-size: 1.6rem;
    }

    .admin-button {
      padding: 14px 28px;
      font-size: 1rem;
    }
  }

  @media (max-width: 480px) {
    .site-title {
      font-size: 1.8rem;
    }

    .titles-grid {
      grid-template-columns: 1fr;
    }

    .category-tab {
      min-width: 120px;
      padding: 10px 15px;
      font-size: 0.9rem;
    }

    .search-input {
      padding: 12px 40px 12px 15px;
    }
  }
</style>
</head>
<body>

<div class="container">
  <div class="header">
    <h1 class="site-title">ПРОСМОТРЕННЫЕ ТАЙТЛЫ</h1>
    <p class="subtitle">Моя коллекция аниме, сериалов, фильмов и книг</p>
  </div>

  <a href="/" class="home-link">
    ← Вернуться на главную
  </a>

  <!-- Кнопка администрации (скрыта по умолчанию) -->
  <div class="admin-button-container" id="adminButtonContainer">
    <a href="ADMINKA.html" class="admin-button">
      Вход в администрацию
    </a>
  </div>

  <!-- Поисковая строка -->
<div class="search-container">
  <div class="search-box">
    <input type="text" class="search-input" id="searchInput" placeholder="Поиск тайтлов..." autocomplete="off">
    <div class="search-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"></circle>
        <path d="m21 21-4.3-4.3"></path>
      </svg>
    </div>
    <div class="search-results" id="searchResults"></div>
  </div>
</div>

  <div class="category-tabs">
    <button class="category-tab active" data-category="anime">Аниме</button>
    <button class="category-tab" data-category="serials">Сериалы</button>
    <button class="category-tab" data-category="movies">Фильмы</button>
    <button class="category-tab" data-category="books">Книги</button>
  </div>

  <!-- Остальной контент без изменений -->
  <div id="anime" class="content-section active">
    <h2 class="section-header">Аниме</h2>
    <div class="titles-grid">
      <a href="page1.html" class="title-card">
        <div class="title-name">Бездомный бог</div>
      </a>
      <a href="page2.html" class="title-card">
        <div class="title-name">Твоё имя</div>
      </a>
      <a href="page3.html" class="title-card">
        <div class="title-name">Дитя погоды</div>
      </a>
      <a href="page4.html" class="title-card">
        <div class="title-name">Человек-бензопила</div>
      </a>
      <a href="page5.html" class="title-card">
        <div class="title-name">Фрирен</div>
      </a>
      <a href="page6.html" class="title-card">
        <div class="title-name">Хантер х Хантер</div>
      </a>
      <a href="page7.html" class="title-card">
        <div class="title-name">Форма голоса</div>
      </a>
      <a href="page8.html" class="title-card">
        <div class="title-name">Монолог Фармацевта</div>
      </a>
      <a href="page9.html" class="title-card">
        <div class="title-name">Первородный грех Такопи</div>
      </a>
      <a href="page10.html" class="title-card">
        <div class="title-name">Закрывающая двери Судзумэ</div>
      </a>
      <a href="page11.html" class="title-card">
        <div class="title-name">Клинок рассекающий демонов</div>
      </a>
      <a href="page12.html" class="title-card">
        <div class="title-name">Магическая битва</div>
      </a>
      <a href="page13.html" class="title-card">
        <div class="title-name">Одинокий рокер</div>
      </a>
      <a href="page14.html" class="title-card">
        <div class="title-name">Ковбой бибоп</div>
      </a>
      <a href="page15.html" class="title-card">
        <div class="title-name">Опасность в моём сердце</div>
      </a>
      <a href="page16.html" class="title-card">
        <div class="title-name">Благоухающий цветок</div>
      </a>
      <a href="page17.html" class="title-card">
        <div class="title-name">Необъятный океан</div>
      </a>
      <a href="page18.html" class="title-card">
        <div class="title-name">Ходячий замок</div>
      </a>
      <a href="page19.html" class="title-card">
        <div class="title-name">Соло левелинг</div>
      </a>
      <a href="page20.html" class="title-card">
        <div class="title-name">Тетрадь смерти</div>
      </a>
      <a href="page21.html" class="title-card">
        <div class="title-name">Проза бродячих псов</div>
      </a>
      <a href="page22.html" class="title-card">
        <div class="title-name">Звёздное дитя</div>
      </a>
      <a href="page23.html" class="title-card">
        <div class="title-name">Этот глупый свин не знает мечты девочки</div>
      </a>
      <a href="page24.html" class="title-card">
        <div class="title-name">ДжоДжо</div>
      </a>
      <a href="page25.html" class="title-card">
        <div class="title-name">Евангелион</div>
      </a>
      <a href="page26.html" class="title-card">
        <div class="title-name">Я хочу съесть твою поджелудочную</div>
      </a>
      <a href="page27.html" class="title-card">
        <div class="title-name">Дандадан</div>
      </a>
      <a href="page28.html" class="title-card">
        <div class="title-name">Летнее время</div>
      </a>
      <a href="page29.html" class="title-card">
        <div class="title-name">Обещанный Неверленд</div>
      </a>
      <a href="page30.html" class="title-card">
        <div class="title-name">Семья шпиона</div>
      </a>
      <a href="page31.html" class="title-card">
        <div class="title-name">Эта фарфоровая кукла влюбилась</div>
      </a>
      <a href="page32.html" class="title-card">
        <div class="title-name">Для тебя бессмертный</div>
      </a>
      <a href="page33.html" class="title-card">
        <div class="title-name">Город в котором меня нет</div>
      </a>
      <a href="page34.html" class="title-card">
        <div class="title-name">Кайдзю №8</div>
      </a>
      <a href="page35.html" class="title-card">
        <div class="title-name">Песнь ночных сов</div>
      </a>
      <a href="page36.html" class="title-card">
        <div class="title-name">Дороро</div>
      </a>
      <a href="page37.html" class="title-card">
        <div class="title-name">Дракон горничная Кобояши</div>
      </a>
      <a href="page38.html" class="title-card">
        <div class="title-name">Хоримия</div>
      </a>
      <a href="page39.html" class="title-card">
        <div class="title-name">Блюлок</div>
      </a>
      <a href="page40.html" class="title-card">
        <div class="title-name">Нет игры Нет жизни</div>
      </a>
      <a href="page41.html" class="title-card">
        <div class="title-name">Пираты чёрной лагуны</div>
      </a>
      <a href="page42.html" class="title-card">
        <div class="title-name">Чудачества любви не помеха!</div>
      </a>
      <a href="page43.html" class="title-card">
        <div class="title-name">За гранью</div>
      </a>
      <a href="page44.html" class="title-card">
        <div class="title-name">Слишком много проигравших героинь</div>
      </a>
      <a href="page45.html" class="title-card">
        <div class="title-name">Адский рай</div>
      </a>
      <a href="page46.html" class="title-card">
        <div class="title-name">Унесённые призраками</div>
      </a>
      <a href="page47.html" class="title-card">
        <div class="title-name">Буччигири!</div>
      </a>
      <a href="page48.html" class="title-card">
        <div class="title-name">Эксперименты Лэйн</div>
      </a>
      <a href="page49.html" class="title-card">
        <div class="title-name">Маленький гражданин</div>
      </a>
      <a href="page50.html" class="title-card">
        <div class="title-name">Гачиакута <span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="page51.html" class="title-card">
        <div class="title-name">Унеси меня на луну</div>
      </a>
      <a href="page52.html" class="title-card">
        <div class="title-name">У Коми проблемы с общением</div>
      </a>
      <a href="page53.html" class="title-card">
        <div class="title-name">Моя геройская академия</div>
      </a>
      <a href="page54.html" class="title-card">
        <div class="title-name">Рыбка Поньё на утёсе</div>
      </a>
      <a href="page55.html" class="title-card">
        <div class="title-name">Тоннель в лето, выход прощаний</div>
      </a>
      <a href="page56.html" class="title-card">
        <div class="title-name">Дни Сакамото</div>
      </a>
      <a href="page57.html" class="title-card">
        <div class="title-name">Восхождение героя щита</div>
      </a>
      <a href="page58.html" class="title-card">
        <div class="title-name">Ангел по соседству</div>
      </a>
      <a href="page59.html" class="title-card">
        <div class="title-name">Токийские мстители</div>
      </a>
      <a href="page60.html" class="title-card">
        <div class="title-name">Токийский гуль</div>
      </a>
      <a href="page61.html" class="title-card">
        <div class="title-name">Шарлотта</div>
      </a>
      <a href="page62.html" class="title-card">
        <div class="title-name">Труська, Чулка и пресвятой подвяз</div>
      </a>
      <a href="page63.html" class="title-card">
        <div class="title-name">Ветролом</div>
      </a>
      <a href="page64.html" class="title-card">
        <div class="title-name">Ая и ведьма</div>
      </a>
      <a href="page65.html" class="title-card">
        <div class="title-name">Паразит</div>
      </a>
      <a href="page66.html" class="title-card">
        <div class="title-name">Сквозь слёзы я притворяюсь кошкой</div>
      </a>
      <a href="page67.html" class="title-card">
        <div class="title-name">Дьявол может плакать</div>
      </a>
      <a href="page68.html" class="title-card">
        <div class="title-name">Я женился на однокласснице, которую ненавидел</div>
      </a>
      <a href="page69.html" class="title-card">
        <div class="title-name">Приоритет чудо яйца</div>
      </a>
      <a href="page70.html" class="title-card">
        <div class="title-name">Дневник будущего</div>
      </a>
      <a href="page71.html" class="title-card">
        <div class="title-name">Меланхолия Харухи Судзумии</div>
      </a>
      <a href="page72.html" class="title-card">
        <div class="title-name">Санда <span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="page73.html" class="title-card">
        <div class="title-name">Можно спросить ещё кое-что? <span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="page74.html" class="title-card">
        <div class="title-name">Безэмоциональная Кашивада и эмоциональный Ота <span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="page75.html" class="title-card">
        <div class="title-name">Монстр хочет съесть меня <span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="page76.html" class="title-card">
        <div class="title-name">Вечность Югурэ <span class="title-status status-soon">(скоро)</span></div>
      </a>
    </div>
  </div>

  <div id="serials" class="content-section">
    <h2 class="section-header">Сериалы</h2>
    <div class="titles-grid">
      <a href="serial1.html" class="title-card">
        <div class="title-name">Уэйн</div>
      </a>
      <a href="serial2.html" class="title-card">
        <div class="title-name">Слово пацана. Кровь на асфальте</div>
      </a>
      <a href="serial3.html" class="title-card">
        <div class="title-name">Пищеблок</div>
      </a>
      <a href="serial4.html" class="title-card">
        <div class="title-name">Пищеблок 2</div>
      </a>
      <a href="serial5.html" class="title-card">
        <div class="title-name">13 клиническая</div>
      </a>
      <a href="serial6.html" class="title-card">
        <div class="title-name">Предпоследняя инстанция</div>
      </a>
      <a href="serial7.html" class="title-card">
        <div class="title-name">Закрыть гештальт</div>
      </a>
      <a href="serial8.html" class="title-card">
        <div class="title-name">Фишер</div>
      </a>
      <a href="serial9.html" class="title-card">
        <div class="title-name">Кухня</div>
      </a>
      <a href="serial10.html" class="title-card">
        <div class="title-name">Два холма</div>
      </a>
      <a href="serial11.html" class="title-card">
        <div class="title-name">Последний богатырь. Наследие</div>
      </a>
      <a href="serial12.html" class="title-card">
        <div class="title-name">Смешарики</div>
      </a>
    </div>
  </div>

  <div id="movies" class="content-section">
    <h2 class="section-header">Фильмы</h2>
    <div class="titles-grid">
      <a href="movie1.html" class="title-card">
        <div class="title-name">Люди в чёрном</div>
      </a>
      <a href="movie2.html" class="title-card">
        <div class="title-name">Люди в чёрном 2</div>
      </a>
      <a href="movie3.html" class="title-card">
        <div class="title-name">Люди в чёрном 3</div>
      </a>
      <a href="movie4.html" class="title-card">
        <div class="title-name">Люди в чёрном: Интернешнл</div>
      </a>
      <a href="movie5.html" class="title-card">
        <div class="title-name">Железный человек</div>
      </a>
      <a href="movie6.html" class="title-card">
        <div class="title-name">Железный человек 2</div>
      </a>
      <a href="movie7.html" class="title-card">
        <div class="title-name">Железный человек 3</div>
      </a>
      <a href="movie8.html" class="title-card">
        <div class="title-name">Мстители</div>
      </a>
      <a href="movie9.html" class="title-card">
        <div class="title-name">Мстители: Эра Альтрона</div>
      </a>
      <a href="movie10.html" class="title-card">
        <div class="title-name">Доктор Стрэндж</div>
      </a>
      <a href="movie11.html" class="title-card">
        <div class="title-name">Человек-паук: Возвращение домой</div>
      </a>
      <a href="movie12.html" class="title-card">
        <div class="title-name">Чёрная Пантера</div>
      </a>
      <a href="movie13.html" class="title-card">
        <div class="title-name">Капитан Марвел</div>
      </a>
      <a href="movie14.html" class="title-card">
        <div class="title-name">Мстители: Финал</div>
      </a>
      <a href="movie15.html" class="title-card">
        <div class="title-name">Человек-паук: Вдали от дома</div>
      </a>
      <a href="movie16.html" class="title-card">
        <div class="title-name">Человек-паук: Нет пути домой</div>
      </a>
      <a href="movie17.html" class="title-card">
        <div class="title-name">Доктор Стрэндж: В мультивселенной безумия</div>
      </a>
      <a href="movie18.html" class="title-card">
        <div class="title-name">Стражи Галактики</div>
      </a>
      <a href="movie19.html" class="title-card">
        <div class="title-name">Стражи Галактики 2</div>
      </a>
      <a href="movie20.html" class="title-card">
        <div class="title-name">Стражи Галактики 3</div>
      </a>
      <a href="movie21.html" class="title-card">
        <div class="title-name">Дэдпул и Росомаха</div>
      </a>
      <a href="movie22.html" class="title-card">
        <div class="title-name">Громовержцы*</div>
      </a>
      <a href="movie23.html" class="title-card">
        <div class="title-name">Гарри Поттер и философский камень</div>
      </a>
      <a href="movie24.html" class="title-card">
        <div class="title-name">Гарри Поттер и Тайная комната</div>
      </a>
      <a href="movie25.html" class="title-card">
        <div class="title-name">Гарри Поттер и узник Азкабана</div>
      </a>
      <a href="movie26.html" class="title-card">
        <div class="title-name">Гарри Поттер и Кубок огня</div>
      </a>
      <a href="movie27.html" class="title-card">
        <div class="title-name">Гарри Поттер и Орден Феникса</div>
      </a>
      <a href="movie28.html" class="title-card">
        <div class="title-name">Гарри Поттер и Принц-полукровка</div>
      </a>
      <a href="movie29.html" class="title-card">
        <div class="title-name">Гарри Поттер и Дары смерти: Часть 1</div>
      </a>
      <a href="movie30.html" class="title-card">
        <div class="title-name">Гарри Поттер и Дары смерти: Часть 2</div>
      </a>
      <a href="movie31.html" class="title-card">
        <div class="title-name">Гарри Поттер 20 лет спустя: Возвращение в Хогвартс</div>
      </a>
      <a href="movie32.html" class="title-card">
        <div class="title-name">Человек-паук: Через вселенные</div>
      </a>
      <a href="movie33.html" class="title-card">
        <div class="title-name">Человек-паук: Паутина вселенных</div>
      </a>
      <a href="movie34.html" class="title-card">
        <div class="title-name">Трансформеры</div>
      </a>
      <a href="movie35.html" class="title-card">
        <div class="title-name">Трансформеры 2</div>
      </a>
      <a href="movie36.html" class="title-card">
        <div class="title-name">Трансформеры 3</div>
      </a>
      <a href="movie37.html" class="title-card">
        <div class="title-name">Трансформеры 4</div>
      </a>
      <a href="movie38.html" class="title-card">
        <div class="title-name">Трансформеры 5</div>
      </a>
      <a href="movie39.html" class="title-card">
        <div class="title-name">Трансформеры: Восхождение Звероботов</div>
      </a>
      <a href="movie40.html" class="title-card">
        <div class="title-name">Бамблби</div>
      </a>
      <a href="movie41.html" class="title-card">
        <div class="title-name">Ночь в музее</div>
      </a>
      <a href="movie42.html" class="title-card">
        <div class="title-name">Фантастические твари и где они обитают</div>
      </a>
      <a href="movie43.html" class="title-card">
        <div class="title-name">Пираты Карибского моря: Проклятие Чёрной жемчужины</div>
      </a>
      <a href="movie44.html" class="title-card">
        <div class="title-name">Пираты Карибского моря: Сундук мертвеца</div>
      </a>
      <a href="movie45.html" class="title-card">
        <div class="title-name">Пираты Карибского моря 3: На краю Света</div>
      </a>
      <a href="movie46.html" class="title-card">
        <div class="title-name">Пираты Карибского моря: На странных берегах</div>
      </a>
      <a href="movie47.html" class="title-card">
        <div class="title-name">Пираты Карибского моря: Мертвецы не рассказывают сказки</div>
      </a>
      <a href="movie48.html" class="title-card">
        <div class="title-name">Назад в будущее</div>
      </a>
      <a href="movie49.html" class="title-card">
        <div class="title-name">Назад в будущее 2</div>
      </a>
      <a href="movie50.html" class="title-card">
        <div class="title-name">Шрэк</div>
      </a>
      <a href="movie51.html" class="title-card">
        <div class="title-name">Шрэк 2</div>
      </a>
      <a href="movie52.html" class="title-card">
        <div class="title-name">Шрэк 3</div>
      </a>
      <a href="movie53.html" class="title-card">
        <div class="title-name">Шрэк 4</div>
      </a>
      <a href="movie54.html" class="title-card">
        <div class="title-name">Майнкрафт в кино</div>
      </a>
      <a href="movie55.html" class="title-card">
        <div class="title-name">Лысый нянька: Спецзадание</div>
      </a>
      <a href="movie56.html" class="title-card">
        <div class="title-name">Дети шпионов</div>
      </a>
      <a href="movie57.html" class="title-card">
        <div class="title-name">Соник в кино</div>
      </a>
      <a href="movie58.html" class="title-card">
        <div class="title-name">Соник в кино 2</div>
      </a>
      <a href="movie59.html" class="title-card">
        <div class="title-name">Соник в кино 3</div>
      </a>
      <a href="movie60.html" class="title-card">
        <div class="title-name">Перси Джексон и похититель молний</div>
      </a>
      <a href="movie61.html" class="title-card">
        <div class="title-name">Перси Джексон и Море чудовищ</div>
      </a>
      <a href="movie62.html" class="title-card">
        <div class="title-name">Малефисента</div>
      </a>
      <a href="movie63.html" class="title-card">
        <div class="title-name">Иллюзия обмана</div>
      </a>
      <a href="movie64.html" class="title-card">
        <div class="title-name">Иллюзия обмана 2</div>
      </a>
      <a href="movie65.html" class="title-card">
        <div class="title-name">1+1</div>
      </a>
      <a href="movie66.html" class="title-card">
        <div class="title-name">Третий лишний</div>
      </a>
      <a href="movie67.html" class="title-card">
        <div class="title-name">Зверополис</div>
      </a>
      <a href="movie68.html" class="title-card">
        <div class="title-name">Зверопой</div>
      </a>
      <a href="movie69.html" class="title-card">
        <div class="title-name">Алиса в Стране чудес (2025)</div>
      </a>
      <a href="movie70.html" class="title-card">
        <div class="title-name">Тачки</div>
      </a>
      <a href="movie71.html" class="title-card">
        <div class="title-name">Тачки 2</div>
      </a>
      <a href="movie72.html" class="title-card">
        <div class="title-name">Тачки 3</div>
      </a>
      <a href="movie73.html" class="title-card">
        <div class="title-name">Тайна Коко</div>
      </a>
      <a href="movie74.html" class="title-card">
        <div class="title-name">Как приручить дракона</div>
      </a>
      <a href="movie75.html" class="title-card">
        <div class="title-name">Как приручить дракона 2</div>
      </a>
      <a href="movie76.html" class="title-card">
        <div class="title-name">Как приручить дракона 3</div>
      </a>
      <a href="movie77.html" class="title-card">
        <div class="title-name">Монстры на каникулах</div>
      </a>
      <a href="movie78.html" class="title-card">
        <div class="title-name">Монстры на каникулах 2</div>
      </a>
      <a href="movie79.html" class="title-card">
        <div class="title-name">Монстры на каникулах 3</div>
      </a>
      <a href="movie80.html" class="title-card">
        <div class="title-name">Монстры на каникулах 4</div>
      </a>
      <a href="movie81.html" class="title-card">
        <div class="title-name">Холодное сердце</div>
      </a>
      <a href="movie82.html" class="title-card">
        <div class="title-name">Пять ночей с Фредди</div>
      </a>
      <a href="movie83.html" class="title-card">
        <div class="title-name">Пять ночей с Фредди 2</div>
      </a>
      <a href="movie84.html" class="title-card">
        <div class="title-name">Аватар</div>
      </a>
      <a href="movie85.html" class="title-card">
        <div class="title-name">Аватар: Путь воды</div>
      </a>
      <a href="movie86.html" class="title-card">
        <div class="title-name">Аватар: Пламя и пепел</div>
      </a>
      <a href="movie87.html" class="title-card">
        <div class="title-name">Аватар: Ещё не вышел</div>
      </a>
      <a href="movie88.html" class="title-card">
        <div class="title-name">Бойцовский клуб</div>
      </a>
      <a href="movie89.html" class="title-card">
        <div class="title-name">Субстанция</div>
      </a>
      <a href="movie90.html" class="title-card">
        <div class="title-name">Волк с Уолл-стрит</div>
      </a>
      <a href="movie91.html" class="title-card">
        <div class="title-name">Моана</div>
      </a>
      <a href="movie92.html" class="title-card">
        <div class="title-name">Титаник</div>
      </a>
      <a href="movie93.html" class="title-card">
        <div class="title-name">Холоп</div>
      </a>
      <a href="movie94.html" class="title-card">
        <div class="title-name">Холоп 2</div>
      </a>
      <a href="movie95.html" class="title-card">
        <div class="title-name">Батя</div>
      </a>
      <a href="movie96.html" class="title-card">
        <div class="title-name">Батя 2. Дед</div>
      </a>
      <a href="movie97.html" class="title-card">
        <div class="title-name">Иван Васильевич меняет профессию</div>
      </a>
      <a href="movie98.html" class="title-card">
        <div class="title-name">Бриллиантовая рука</div>
      </a>
      <a href="movie99.html" class="title-card">
        <div class="title-name">Кракен</div>
      </a>
      <a href="movie100.html" class="title-card">
        <div class="title-name">Сто лет тому вперёд</div>
      </a>
      <a href="movie101.html" class="title-card">
        <div class="title-name">Приключения Электроника</div>
      </a>
      <a href="movie102.html" class="title-card">
        <div class="title-name">Лулу и Бриггс</div>
      </a>
      <a href="movie103.html" class="title-card">
        <div class="title-name">Маска</div>
      </a>
      <a href="movie104.html" class="title-card">
        <div class="title-name">Приключения Падингтона</div>
      </a>
      <a href="movie105.html" class="title-card">
        <div class="title-name">Приключения Падингтона 2</div>
      </a>
      <a href="movie106.html" class="title-card">
        <div class="title-name">Каратэ-пацан</div>
      </a>
      <a href="movie107.html" class="title-card">
        <div class="title-name">Большой и добрый великан</div>
      </a>
      <a href="movie108.html" class="title-card">
        <div class="title-name">Тролли</div>
      </a>
      <a href="movie109.html" class="title-card">
        <div class="title-name">Тролли 2</div>
      </a>
      <a href="movie110.html" class="title-card">
        <div class="title-name">Тролли 3</div>
      </a>
      <a href="movie111.html" class="title-card">
        <div class="title-name">Чарли и шоколадная фабрика</div>
      </a>
      <a href="movie112.html" class="title-card">
        <div class="title-name">Джуманджи</div>
      </a>
      <a href="movie113.html" class="title-card">
        <div class="title-name">Кролик Питер</div>
      </a>
      <a href="movie114.html" class="title-card">
        <div class="title-name">Кролик Питер 2</div>
      </a>
      <a href="movie115.html" class="title-card">
        <div class="title-name">Покемон. Детектив Пикачу</div>
      </a>
      <a href="movie116.html" class="title-card">
        <div class="title-name">Живая сталь</div>
      </a>
      <a href="movie117.html" class="title-card">
        <div class="title-name">Рождественская история</div>
      </a>
      <a href="movie118.html" class="title-card">
        <div class="title-name">Годзилла</div>
      </a>
      <a href="movie119.html" class="title-card">
        <div class="title-name">Конг: Остров Черепа</div>
      </a>
      <a href="movie120.html" class="title-card">
        <div class="title-name">Годзилла 2: Король монстра</div>
      </a>
      <a href="movie121.html" class="title-card">
        <div class="title-name">Годзилла против Конга</div>
      </a>
      <a href="movie122.html" class="title-card">
        <div class="title-name">Годзилла и конг: Новая империя</div>
      </a>
      <a href="movie123.html" class="title-card">
        <div class="title-name">Оно</div>
      </a>
      <a href="movie124.html" class="title-card">
        <div class="title-name">Оно 2</div>
      </a>
      <a href="movie125.html" class="title-card">
        <div class="title-name">Первому игроку приготовиться</div>
      </a>
      <a href="movie126.html" class="title-card">
        <div class="title-name">Веном</div>
      </a>
      <a href="movie127.html" class="title-card">
        <div class="title-name">Веном 2</div>
      </a>
      <a href="movie128.html" class="title-card">
        <div class="title-name">Веном 3</div>
      </a>
      <a href="movie129.html" class="title-card">
        <div class="title-name">Дэдпул</div>
      </a>
      <a href="movie130.html" class="title-card">
        <div class="title-name">Дэдпул 2</div>
      </a>
      <a href="movie131.html" class="title-card">
        <div class="title-name">Война миров Z</div>
      </a>
      <a href="movie132.html" class="title-card">
        <div class="title-name">Гадки я</div>
      </a>
      <a href="movie133.html" class="title-card">
        <div class="title-name">Гадки я 2</div>
      </a>
      <a href="movie134.html" class="title-card">
        <div class="title-name">Гадки я 3</div>
      </a>
      <a href="movie135.html" class="title-card">
        <div class="title-name">Гадки я 4</div>
      </a>
      <a href="movie136.html" class="title-card">
        <div class="title-name">RRR: Рядом Ревёт Революция</div>
      </a>
      <a href="movie137.html" class="title-card">
        <div class="title-name">Шоу Трумана</div>
      </a>
      <a href="movie138.html" class="title-card">
        <div class="title-name">Американский огурчик</div>
      </a>
      <a href="movie139.html" class="title-card">
        <div class="title-name">Тихоокеанский рубеж</div>
      </a>
      <a href="movie140.html" class="title-card">
        <div class="title-name">Тихоокеанский рубеж 2</div>
      </a>
      <a href="movie141.html" class="title-card">
        <div class="title-name">Морбиус</div>
      </a>
    </div>
  </div>

  <div id="books" class="content-section">
    <h2 class="section-header">Книги</h2>
    <div class="titles-grid">
      <a href="book1.html" class="title-card">
        <div class="title-name">Горе от ума</div>
      </a>
      <a href="book2.html" class="title-card">
        <div class="title-name">Капитанская дочка<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book3.html" class="title-card">
        <div class="title-name">Сказка о царе Султане<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book4.html" class="title-card">
        <div class="title-name">Дубровский<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book5.html" class="title-card">
        <div class="title-name">Евгений Онегин<span class="title-status status-soon">(В процессе)</span></div>
      </a>
      <a href="book6.html" class="title-card">
        <div class="title-name">Сказка о рыбаке и рыбке<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book7.html" class="title-card">
        <div class="title-name">Война и мир<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book8.html" class="title-card">
        <div class="title-name">Преступление и наказание<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book9.html" class="title-card">
        <div class="title-name">Тарас Бульба<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book10.html" class="title-card">
        <div class="title-name">Вий<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book11.html" class="title-card">
        <div class="title-name">Кладбище домашних животных<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book12.html" class="title-card">
        <div class="title-name">Краткая история времени<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book13.html" class="title-card">
        <div class="title-name">Взлом креатива<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book14.html" class="title-card">
        <div class="title-name">Нравственные письма к Луцилию<span class="title-status status-soon">(скоро)</span></div>
      </a>
      <a href="book15.html" class="title-card">
        <div class="title-name">Философский экспресс<span class="title-status status-soon">(скоро)</span></div>
      </a>
      </div>
    </div>
  </div>

<script>
  document.addEventListener('DOMContentLoaded', function() {
    const categoryTabs = document.querySelectorAll('.category-tab');
    const contentSections = document.querySelectorAll('.content-section');
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    const adminButtonContainer = document.getElementById('adminButtonContainer');

    let currentSearchTerm = ''; // Храним текущий поисковый запрос

    // Функция для получения всех видимых карточек в активной категории
    function getActiveCategoryCards() {
      const activeSection = document.querySelector('.content-section.active');
      return activeSection.querySelectorAll('.title-card');
    }

    // Функция поиска
    function performSearch(searchTerm) {
      const activeCards = getActiveCategoryCards();

      if (searchTerm.length < 2) {
        // Показываем все карточки, если поисковый запрос короткий
        activeCards.forEach(card => {
          card.classList.remove('hidden');
          card.classList.add('visible');
        });
        searchResults.classList.remove('show');
        return;
      }

      const lowerSearchTerm = searchTerm.toLowerCase();
      let foundCount = 0;

      activeCards.forEach(card => {
        const titleText = card.querySelector('.title-name').textContent.toLowerCase();

        if (titleText.includes(lowerSearchTerm)) {
          card.classList.remove('hidden');
          card.classList.add('visible');
          foundCount++;
        } else {
          card.classList.add('hidden');
          card.classList.remove('visible');
        }
      });

      // Показываем результаты поиска
      if (foundCount > 0) {
        searchResults.textContent = `Найдено тайтлов: ${foundCount}`;
        searchResults.classList.add('show');
      } else {
        searchResults.textContent = 'По вашему запросу ничего не найдено';
        searchResults.classList.add('show');
      }
    }

    // Обработчик ввода в поисковую строку
    searchInput.addEventListener('input', function() {
      currentSearchTerm = this.value;

      // Проверка на секретную команду
      if (currentSearchTerm.toLowerCase() === 'showadmin0') {
        adminButtonContainer.classList.add('show');
        this.value = '';
        currentSearchTerm = '';
        searchResults.textContent = '';
        searchResults.classList.remove('show');

        // Показываем все карточки в активной категории
        const activeCards = getActiveCategoryCards();
        activeCards.forEach(card => {
          card.classList.remove('hidden');
          card.classList.add('visible');
        });
      } else {
        adminButtonContainer.classList.remove('show');
        performSearch(currentSearchTerm);
      }
    });

    categoryTabs.forEach(tab => {
      tab.addEventListener('click', function() {
        const category = this.dataset.category;

        // Убираем активный класс у всех табов
        categoryTabs.forEach(t => t.classList.remove('active'));
        // Добавляем активный класс текущему табу
        this.classList.add('active');

        // Скрываем все секции
        contentSections.forEach(section => {
          section.classList.remove('active');
        });

        // Показываем нужную секцию
        document.getElementById(category).classList.add('active');

        // Не сбрасываем поисковую строку, сохраняем текст
        // Выполняем поиск снова, если есть активный запрос
        if (currentSearchTerm && currentSearchTerm !== 'showadmin0') {
          performSearch(currentSearchTerm);
        } else {
          // Если поискового запроса нет, показываем все карточки
          const activeCards = getActiveCategoryCards();
          activeCards.forEach(card => {
            card.classList.remove('hidden');
            card.classList.add('visible');
          });
          searchResults.classList.remove('show');
        }
      });
    });

    // Инициализация
    // Начинаем с пустого поиска и показываем все карточки в активной категории
    const initialActiveCards = getActiveCategoryCards();
    initialActiveCards.forEach(card => {
      card.classList.add('visible');
    });
  });
</script>

</body>
</html>""",
    "aboutme": """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Обо мне</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet" />
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        background-image: url('https://sun9-70.userapi.com/s/v1/ig2/uuN1CGadOQmwCY2or7OdtYP2bEBsc7iuammrWJAS-lyaC3yYusKwbRS2Ou1CSp90FMHWEhKY6CnFUKpyc-AqQtZI.jpg?quality=95&as=32x18,48x27,72x40,108x61,160x90,240x135,360x202,480x270,540x304,640x360,720x405,1080x607,1280x720,1440x810,2560x1440&from=bu&u=QcW86cnjL8xQ4y1TVxYAM6WCJEl5K2vPAG_3JKYyUJw&cs=640x0');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 15px;
        min-height: 100vh;
        opacity: 0;
        animation: fadeInBody 1.5s ease-out forwards;
    }

    /* Анимации */
    @keyframes fadeInBody {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes fadeInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes scaleIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    .container {
        max-width: 900px;
        margin: 30px auto;
        background-color: rgba(20, 20, 30, 0.85);
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        text-align: center;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        opacity: 0;
        animation: fadeInUp 1s ease-out 0.3s forwards;
        position: relative;
    }

    .container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(to right, #8b0000, #c62828, #8b0000);
        border-radius: 12px 12px 0 0;
    }

    h1 {
        font-family: 'Playfair Display', serif;
        color: #fff;
        font-size: clamp(2rem, 6vw, 2.8rem);
        margin-bottom: 10px;
        line-height: 1.3;
        font-weight: 700;
        opacity: 0;
        animation: fadeInDown 0.8s ease-out 0.5s forwards;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }

    .subtitle {
        font-family: 'Inter', sans-serif;
        color: #b0b0b0;
        font-size: clamp(1rem, 3vw, 1.2rem);
        margin-bottom: 30px;
        font-weight: 400;
        opacity: 0;
        animation: fadeInDown 0.8s ease-out 0.7s forwards;
    }

    h2 {
        font-family: 'Playfair Display', serif;
        color: #fff;
        font-size: clamp(1.5rem, 5vw, 1.8rem);
        margin-top: 35px;
        margin-bottom: 18px;
        font-weight: 600;
        opacity: 0;
        animation: fadeInLeft 0.8s ease-out 0.9s forwards;
        position: relative;
        display: inline-block;
    }

    h2::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 50px;
        height: 2px;
        background: #c62828;
    }

    p.rt {
        font-family: 'Inter', sans-serif;
        font-size: clamp(1rem, 3.5vw, 1.1rem);
        line-height: 1.7;
        margin: 18px 0;
        color: #e0e0e0;
        text-align: left;
        padding: 0 5px;
        opacity: 0;
        animation: fadeInRight 0.8s ease-out 1.1s forwards;
    }

    .profile-photo {
        width: min(250px, 65vw);
        max-width: 100%;
        height: auto;
        border-radius: 50%;
        margin: 25px auto;
        border: 3px solid #c62828;
        display: block;
        opacity: 1;
        animation: scaleIn 1s ease-out 0.4s forwards;
        cursor: pointer;
        transition: all 0.4s ease;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }

    .profile-photo:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 25px rgba(198, 40, 40, 0.3);
        border-color: #ff5252;
    }

    .social-buttons {
        margin: 30px 0;
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 15px;
    }

    .social-buttons a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 55px;
        height: 55px;
        font-size: 1.5em;
        color: #fff;
        transition: all 0.3s ease;
        background: rgba(198, 40, 40, 0.8);
        border-radius: 50%;
        text-decoration: none;
        min-width: 55px;
        min-height: 55px;
        opacity: 1;
        animation: scaleIn 0.6s ease-out forwards;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(5px);
    }

    .social-buttons a:nth-child(1) { animation-delay: 1.3s; }
    .social-buttons a:nth-child(2) { animation-delay: 1.4s; }
    .social-buttons a:nth-child(3) { animation-delay: 1.5s; }
    .social-buttons a:nth-child(4) { animation-delay: 1.6s; }

    .social-buttons a:hover {
        color: #fff;
        transform: translateY(-5px);
        background: rgba(255, 82, 82, 0.9);
        box-shadow: 0 8px 15px rgba(198, 40, 40, 0.4);
    }

    .back-link {
        display: inline-block;
        margin-top: 25px;
        padding: 14px 30px;
        background: rgba(198, 40, 40, 0.8);
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s ease;
        font-size: clamp(0.9rem, 3.5vw, 1rem);
        min-height: 50px;
        line-height: 1.2;
        opacity: 1;
        animation: scaleIn 0.6s ease-out 1.7s forwards;
        position: relative;
        overflow: hidden;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(5px);
    }

    .back-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }

    .back-link:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(198, 40, 40, 0.4);
        background: rgba(255, 82, 82, 0.9);
    }

    .back-link:hover::before {
        left: 100%;
    }

    section {
        margin-bottom: 30px;
        padding: 0 5px;
        opacity: 0;
        animation: fadeInUp 0.8s ease-out forwards;
    }

    section:nth-child(1) { animation-delay: 0.8s; }
    section:nth-child(2) { animation-delay: 1.0s; }
    section:nth-child(3) { animation-delay: 1.2s; }

    a {
        -webkit-tap-highlight-color: transparent;
    }

    /* Эффект для email */
    a[href^="mailto"] {
        transition: all 0.3s ease;
        position: relative;
        color: #ff8a80;
        font-weight: 500;
        text-decoration: none;
    }

    a[href^="mailto"]:hover {
        color: #ff5252;
        text-decoration: underline;
    }

    .highlight {
        background: rgba(198, 40, 40, 0.15);
        padding: 15px;
        border-radius: 8px;
        border-left: 3px solid #c62828;
        margin: 15px 0;
    }

    .highlight p.rt {
        color: #fff;
    }

    /* Улучшение читаемости списков */
    p.rt b {
        color: #fff;
        font-weight: 600;
    }

    /* Затемнение фона для лучшей читаемости */
    body::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(10, 10, 20, 0.7);
        z-index: -1;
    }

    @media (max-width: 768px) {
        body {
            padding: 10px;
        }

        .container {
            padding: 30px 20px;
            margin: 20px auto;
            backdrop-filter: blur(10px);
        }

        h1 {
            margin-bottom: 15px;
        }

        h2 {
            margin-top: 30px;
            margin-bottom: 15px;
        }

        .profile-photo {
            width: min(220px, 60vw);
            margin: 20px auto;
        }

        .social-buttons {
            margin: 25px 0;
            gap: 12px;
        }

        .social-buttons a {
            width: 50px;
            height: 50px;
            min-width: 50px;
            min-height: 50px;
            font-size: 1.4em;
        }

        section {
            margin-bottom: 25px;
            padding: 0;
        }

        p.rt {
            line-height: 1.6;
            margin: 15px 0;
            text-align: justify;
        }
    }

    @media (max-width: 480px) {
        .container {
            padding: 25px 15px;
            margin: 15px auto;
            backdrop-filter: blur(8px);
        }

        p.rt {
            font-size: 0.95rem;
            text-align: left;
        }

        .social-buttons a {
            width: 48px;
            height: 48px;
            min-width: 48px;
            min-height: 48px;
            font-size: 1.3em;
        }

        .back-link {
            padding: 12px 25px;
        }
    }

    @media (max-width: 360px) {
        body {
            padding: 8px;
        }

        .container {
            padding: 20px 15px;
        }

        .social-buttons {
            gap: 10px;
        }

        .social-buttons a {
            width: 45px;
            height: 45px;
            min-width: 45px;
            min-height: 45px;
        }
    }
</style>
</head>
<body>
<div class="container">
    <h1>Рогожкин Сергей</h1>
    <p class="subtitle">Ученик 9 класса | Будущий сценарист-режиссёр</p>

    <img src="https://avatars.mds.yandex.net/i?id=f2f1538b9b9bf9fe2097cf7b41a0bc279dabb2b0-15383683-images-thumbs&n=13" class="profile-photo" alt="Мое фото" />

    <section>
        <h2>Обо мне</h2>
        <p class="rt">Мне 14 лет, мой день рождения 5 января. Я учусь в 9-м классе. Мои любимые предметы — алгебра и литература.</p>
        <div class="highlight">
            <p class="rt"><b>Хочу стать сценаристом-режиссёром.</b></p>
        </div>
        <p class="rt">Играю в CS2, REPO, SCP:SL, Minecraft, а также в разные новеллы и другие игры. Люблю фильмы, сериалы, аниме, мангу, книги — в общем, все жанры.</p>

        <p class="rt"><b>Из любимых могу выделить:</b></p>
        <p class="rt">• <b>Аниме:</b> Бездомный бог, Дитя погоды, Гачиакута, За гранью, Человек-бензопила</p>
        <p class="rt">• <b>Фильмы:</b> Особенности национальной рыбалки, Время [2011], Люди в чёрном</p>
        <p class="rt">• <b>Сериалы:</b> Уэйн, Пищеблок, 13 клиническая, Предпоследняя инстанция</p>
        <p class="rt">• <b>Манга:</b> Евангелион, Крутой учитель Онидзука, Хеллсинг</p>
        <p class="rt">Также играю в волейбол.</p>
    </section>

    <section>
        <h2>Мои хобби</h2>
        <div class="highlight">
            <p class="rt"><b>Писательство.</b> Я пишу своё произведение, которое в будущем планирую перевести в мангу.</p>
        </div>
    </section>

    <section>
        <h2>Контакты</h2>
        <p class="rt"><b>Мой email:</b> <a href="mailto:dzhondayviharris994@gmail.com">dzhondayviharris994@gmail.com</a></p>
    </section>

    <div class="social-buttons">
        <a href="https://t.me/Forverunu" target="_blank" title="Telegram">
            <i class="fab fa-telegram"></i>
        </a>
        <a href="https://vk.com/black___raison___detre" target="_blank" title="ВКонтакте">
            <i class="fab fa-vk"></i>
        </a>
        <a href="https://tiktok.com/@forverunu" target="_blank" title="TikTok">
            <i class="fab fa-tiktok"></i>
        </a>
        <a href="https://shikimori.one/Forverunu13" target="_blank" title="Shikimori">
            <i class="fas fa-moon"></i>
        </a>
    </div>

    <a href="/" class="back-link">Вернуться на главную</a>
</div>

<script>
    // Анимация при скролле
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
            }
        });
    }, observerOptions);

    // Наблюдаем за всеми секциями
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
</script>
</body>
</html>""",
    "myuniverse": """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Моя Вселенная</title>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      margin: 0;
      font-family: 'Exo 2', sans-serif;
      background:
        radial-gradient(circle at 20% 80%, rgba(10, 10, 30, 0.9) 0%, transparent 70%),
        radial-gradient(circle at 80% 20%, rgba(5, 5, 15, 0.9) 0%, transparent 70%),
        linear-gradient(135deg, #000000 0%, #0a0a0a 25%, #111111 50%, #0a0a0a 75%, #000000 100%);
      color: #ccc;
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
    }

    /* Минималистичная текстура */
    .texture {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image:
        repeating-linear-gradient(0deg,
          transparent,
          transparent 1px,
          rgba(20, 20, 20, 0.1) 1px,
          rgba(20, 20, 20, 0.1) 2px
        );
      pointer-events: none;
      z-index: -1;
      opacity: 0.3;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      padding: 40px 20px;
      position: relative;
      z-index: 1;
    }

    .title-container {
      text-align: center;
      margin-bottom: 60px;
      position: relative;
    }

    .main-title {
      font-family: 'Orbitron', monospace;
      font-size: clamp(2.5rem, 8vw, 4.5rem);
      font-weight: 900;
      color: #fff;
      text-shadow:
        0 0 10px rgba(255, 255, 255, 0.1),
        0 0 20px rgba(255, 255, 255, 0.05);
      animation: titleGlow 4s ease-in-out infinite alternate;
      margin-bottom: 20px;
      letter-spacing: 3px;
      text-transform: uppercase;
    }

    @keyframes titleGlow {
      0% {
        text-shadow:
          0 0 10px rgba(255, 255, 255, 0.1),
          0 0 20px rgba(255, 255, 255, 0.05);
      }
      100% {
        text-shadow:
          0 0 15px rgba(255, 255, 255, 0.15),
          0 0 30px rgba(255, 255, 255, 0.08),
          0 0 40px rgba(255, 255, 255, 0.03);
      }
    }

    .subtitle {
      font-size: clamp(0.9rem, 3vw, 1.1rem);
      color: #888;
      font-weight: 300;
      letter-spacing: 2px;
      text-transform: uppercase;
      opacity: 0;
      animation: fadeIn 1s ease 0.5s forwards;
    }

    @keyframes fadeIn {
      to {
        opacity: 0.7;
      }
    }

    .galaxy-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 25px;
      max-width: 900px;
      width: 100%;
      margin-bottom: 50px;
    }

    .portal {
      background: rgba(15, 15, 15, 0.9);
      backdrop-filter: blur(10px);
      border: 1px solid #222;
      border-radius: 12px;
      padding: 30px 20px;
      text-decoration: none;
      color: #ccc;
      text-align: center;
      transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
      position: relative;
      overflow: hidden;
      opacity: 0;
      transform: translateY(30px);
      animation: portalAppear 0.8s ease forwards;
      box-shadow:
        0 5px 15px rgba(0, 0, 0, 0.5),
        inset 0 0 0 1px rgba(255, 255, 255, 0.03);
    }

    .portal::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.03), transparent);
      transition: left 0.6s ease;
    }

    .portal:hover::before {
      left: 100%;
    }

    .portal:nth-child(1) { animation-delay: 0.3s; }
    .portal:nth-child(2) { animation-delay: 0.5s; }
    .portal:nth-child(3) { animation-delay: 0.7s; }
    .portal:nth-child(4) { animation-delay: 0.9s; }

    @keyframes portalAppear {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .portal:hover {
      transform: translateY(-5px);
      border-color: #333;
      background: rgba(20, 20, 20, 0.95);
      box-shadow:
        0 10px 25px rgba(0, 0, 0, 0.7),
        0 0 0 1px rgba(255, 255, 255, 0.05),
        inset 0 0 20px rgba(255, 255, 255, 0.02);
    }

    .portal-icon {
      font-size: 2.5rem;
      margin-bottom: 15px;
      display: block;
      transition: transform 0.4s ease;
      color: #666;
      filter: drop-shadow(0 0 3px rgba(255, 255, 255, 0.1));
    }

    .portal:hover .portal-icon {
      transform: scale(1.1);
      color: #888;
    }

    .portal-title {
      font-family: 'Orbitron', monospace;
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 8px;
      color: #fff;
      text-transform: uppercase;
      letter-spacing: 1px;
      position: relative;
    }

    .portal-title::after {
      content: '';
      position: absolute;
      bottom: -4px;
      left: 50%;
      transform: translateX(-50%);
      width: 30px;
      height: 1px;
      background: #333;
      transition: width 0.3s ease;
    }

    .portal:hover .portal-title::after {
      width: 50px;
      background: #444;
    }

    .portal-desc {
      font-size: 0.9rem;
      color: #666;
      font-weight: 300;
      line-height: 1.4;
    }

    .portal:hover .portal-desc {
      color: #777;
    }

    .wormhole {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 16px 32px;
      background: rgba(15, 15, 15, 0.9);
      backdrop-filter: blur(10px);
      border: 1px solid #222;
      border-radius: 8px;
      color: #888;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      transition: all 0.4s ease;
      position: relative;
      overflow: hidden;
      opacity: 0;
      animation: fadeInUp 1s ease 1.1s forwards;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .wormhole::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.03), transparent);
      transition: left 0.6s ease;
    }

    .wormhole:hover::before {
      left: 100%;
    }

    .wormhole:hover {
      transform: translateY(-3px);
      border-color: #333;
      color: #aaa;
      box-shadow:
        0 5px 20px rgba(0, 0, 0, 0.6),
        0 0 0 1px rgba(255, 255, 255, 0.03);
    }

    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Темные геометрические фигуры на фоне */
    .shape {
      position: fixed;
      z-index: 0;
      opacity: 0.05;
      pointer-events: none;
    }

    .shape-1 {
      width: 200px;
      height: 200px;
      top: 10%;
      left: 5%;
      border: 1px solid #222;
      border-radius: 50%;
      animation: float 20s infinite ease-in-out;
    }

    .shape-2 {
      width: 150px;
      height: 150px;
      bottom: 15%;
      right: 8%;
      border: 1px solid #222;
      animation: float 25s infinite ease-in-out reverse;
    }

    @keyframes float {
      0%, 100% {
        transform: translateY(0) rotate(0deg);
      }
      50% {
        transform: translateY(-20px) rotate(180deg);
      }
    }

    /* Адаптивность */
    @media (max-width: 768px) {
      .galaxy-container {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
      }

      .portal {
        padding: 25px 15px;
      }

      .main-title {
        letter-spacing: 2px;
      }

      .shape-1, .shape-2 {
        display: none;
      }
    }

    @media (max-width: 480px) {
      .galaxy-container {
        grid-template-columns: 1fr;
        gap: 15px;
      }

      .container {
        padding: 30px 15px;
      }

      .main-title {
        font-size: 2.2rem;
        letter-spacing: 1px;
      }
    }

    /* Тонкая линия при наведении */
    .portal::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 1px;
      background: linear-gradient(90deg, transparent, #222, transparent);
      transform: scaleX(0);
      transform-origin: center;
      transition: transform 0.3s ease;
    }

    .portal:hover::after {
      transform: scaleX(1);
    }
  </style>
</head>
<body>
  <div class="texture"></div>
  <div class="shape shape-1"></div>
  <div class="shape shape-2"></div>

  <div class="container">
    <div class="title-container">
      <h1 class="main-title">МОЯ ВСЕЛЕННАЯ</h1>
      <p class="subtitle">Исследуйте глубины творения</p>
    </div>

    <div class="galaxy-container">
      <a href="Character.html" class="portal">
        <span class="portal-icon">👤</span>
        <div class="portal-title">Персонажи</div>
        <div class="portal-desc">Обитатели вселенной</div>
      </a>

      <a href="Plot.html" class="portal">
        <span class="portal-icon">📖</span>
        <div class="portal-title">Сюжет</div>
        <div class="portal-desc">Истории и события</div>
      </a>

      <a href="Manga.html" class="portal">
        <span class="portal-icon">🎨</span>
        <div class="portal-title">Манга</div>
        <div class="portal-desc">Визуальное воплощение</div>
      </a>

      <a href="Rating.html" class="portal">
        <span class="portal-icon">📊</span>
        <div class="portal-title">Рейтинг</div>
        <div class="portal-desc">Характеристики и сила</div>
      </a>
    </div>

    <a href="/" class="wormhole">
      <span>←</span>
      На главную
    </a>
  </div>
</body>
</html>"""
}

# Маршруты для страниц
@app.get("/", response_class=HTMLResponse)
async def get_index():
    return HTMLResponse(content=pages["index"])

@app.get("/games", response_class=HTMLResponse)
async def get_games():
    return HTMLResponse(content=pages["games"])

@app.get("/viewed", response_class=HTMLResponse)
async def get_viewed():
    return HTMLResponse(content=pages["viewed"])

@app.get("/aboutme", response_class=HTMLResponse)
async def get_aboutme():
    return HTMLResponse(content=pages["aboutme"])

@app.get("/myuniverse", response_class=HTMLResponse)
async def get_myuniverse():
    return HTMLResponse(content=pages["myuniverse"])

# Главная страница тоже доступна по /index
@app.get("/index", response_class=HTMLResponse)
async def get_index_page():
    return HTMLResponse(content=pages["index"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)