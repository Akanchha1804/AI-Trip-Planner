import React, { useEffect, useRef } from "react";
import "./HomePage.css";

const Home = () => {
    const carouselRef = useRef(null);

    useEffect(() => {
        const carousel = carouselRef.current;
        let scrollAmount = 0;

        const interval = setInterval(() => {
            if (carousel) {
                scrollAmount += 250;
                if (scrollAmount >= carousel.scrollWidth - carousel.clientWidth) {
                    scrollAmount = 0;
                }
                carousel.scrollTo({
                    left: scrollAmount,
                    behavior: "smooth",
                });
            }
        }, 3000);

        return () => clearInterval(interval);
    }, []);

    return (
        <div className="home-page">
            {/* Hero Section */}
            <section className="hero">
                <div className="overlay"></div>
                <div className="hero-content">
                    <h1>Plan Your Perfect Journey</h1>
                    <p>Find destinations, hotels, and adventures tailored for you.</p>
                    <div className="search-bar">
                        <input type="text" placeholder="Where do you want to go?" />
                        <button>
                            <i className="fa-solid fa-magnifying-glass"></i> Search
                        </button>
                    </div>
                </div>
            </section>

            {/* Popular Destinations */}
            <section className="destinations">
                <h2>Popular Destinations</h2>
                <div className="destination-carousel" ref={carouselRef}>
                    {[
                        { name: "Paris", img: "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg?auto=compress&cs=tinysrgb&w=600" },
                        { name: "New York", img: "https://images.pexels.com/photos/466685/pexels-photo-466685.jpeg?auto=compress&cs=tinysrgb&w=600" },
                        { name: "Tokyo", img: "https://images.pexels.com/photos/2341830/pexels-photo-2341830.jpeg?auto=compress&cs=tinysrgb&w=600" },
                        { name: "Bali", img: "https://images.pexels.com/photos/2233416/pexels-photo-2233416.jpeg?auto=compress&cs=tinysrgb&w=600" },
                        { name: "Rome", img: "https://images.pexels.com/photos/1796715/pexels-photo-1796715.jpeg?auto=compress&cs=tinysrgb&w=600" },
                    ].map((d, i) => (
                        <div key={i} className="destination-card">
                            <img src={d.img} alt={d.name} />
                            <h3>{d.name}</h3>
                        </div>
                    ))}
                </div>
            </section>

            {/* Mood Board */}
            <section className="mood-board">
                <h2>Travel Mood Board</h2>
                <div className="mood-grid">
                    {[
                        "https://images.pexels.com/photos/457882/pexels-photo-457882.jpeg?auto=compress&cs=tinysrgb&w=600",
                        "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&w=600",
                        "https://images.pexels.com/photos/3586966/pexels-photo-3586966.jpeg?auto=compress&cs=tinysrgb&w=600",
                        "https://images.pexels.com/photos/1154619/pexels-photo-1154619.jpeg?auto=compress&cs=tinysrgb&w=600",
                        "https://images.pexels.com/photos/1005417/pexels-photo-1005417.jpeg?auto=compress&cs=tinysrgb&w=600",
                        "https://images.pexels.com/photos/210205/pexels-photo-210205.jpeg?auto=compress&cs=tinysrgb&w=600",
                    ].map((img, i) => (
                        <div key={i} className="mood-item">
                            <img src={img} alt={`Mood ${i}`} />
                        </div>
                    ))}
                </div>
            </section>
        </div>
    );
};

export default Home;
