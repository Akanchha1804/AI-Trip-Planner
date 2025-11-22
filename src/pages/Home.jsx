import React, { useState, useEffect } from "react";
import "./Home.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

export default function Home() {
    const [navOpen, setNavOpen] = useState(false);
    const [currentImage, setCurrentImage] = useState(0);

    // Slideshow images
    const heroImages = [
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e", // beach
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb", // mountain
        "https://images.unsplash.com/photo-1505761671935-60b3a7427bad", // city
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee", // desert
    ];

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentImage((prev) => (prev + 1) % heroImages.length);
        }, 5000);
        return () => clearInterval(interval);
    }, [heroImages.length]);

    return (
        <div className="home-lux">
            {/* Sidebar */}
            <aside className={`sidebar ${navOpen ? "open" : ""}`}>
                <button className="close-btn" onClick={() => setNavOpen(false)}>
                    &times;
                </button>
                <nav>
                    <a href="/">Home</a>
                    <a href="/planner">Plan Trip</a>
                    <a href="/bookings">Bookings</a>
                    <a href="/dashboard">Dashboard</a>
                    <a href="/about">About</a>
                    <a href="/contact">Contact</a>
                </nav>
            </aside>

            {/* Hamburger */}
            <div className="hamburger" onClick={() => setNavOpen(true)}>
                <i className="fa-solid fa-bars"></i>
            </div>

            {/* Hero Section */}
            <section className="hero">
                {heroImages.map((img, index) => (
                    <div
                        key={index}
                        className={`hero-bg ${index === currentImage ? "active" : ""}`}
                        style={{ backgroundImage: `url(${img})` }}
                    ></div>
                ))}
                <div className="hero-overlay"></div>
                <div className="hero-content">
                    <h1>Luxury. Motion. Memory.</h1>
                    <p>
                        Experience AI-crafted journeys that redefine how luxury and
                        technology blend.
                    </p>
                    <div className="search-bar">
                        <input
                            type="text"
                            placeholder="Search destinations, moods, or inspirations..."
                        />
                        <button>
                            <i className="fa-solid fa-magnifying-glass"></i> Discover
                        </button>
                    </div>
                </div>
            </section>

            {/* Features Section */}
            <section className="features">
                <h2>Signature Experiences</h2>
                <div className="feature-grid">
                    <Feature icon="fa-robot" title="AI Itineraries" desc="Tailored travel crafted by intelligent design." />
                    <Feature icon="fa-bolt" title="Instant Booking" desc="Seamless reservations wrapped in luxury." />
                    <Feature icon="fa-map-marked-alt" title="Trip Suggestions" desc="Explore hidden gems curated by intuition." />
                    <Feature icon="fa-image" title="Mood Boards" desc="Visualize your journey in living color." />
                    <Feature icon="fa-users" title="Group Chatrooms" desc="Plan together, elegantly and effortlessly." />
                    <Feature icon="fa-chart-line" title="Dashboards" desc="Your travel universe, beautifully organized." />
                </div>
            </section>

            {/* Footer */}
            <footer>
                <p>© 2025 TripMind — Crafted in code and curiosity.</p>
                <div className="footer-links">
                    <a href="/">Privacy</a> | <a href="/">Terms</a> | <a href="/">Support</a>
                </div>
            </footer>
        </div>
    );
}

function Feature({ icon, title, desc }) {
    return (
        <div className="feature-card">
            <div className="icon-glow">
                <i className={`fa-solid ${icon}`}></i>
            </div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
    );
}
