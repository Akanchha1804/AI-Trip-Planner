import React, { useState } from "react";
import "./booking.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

export default function Booking() {
    const [activeTab, setActiveTab] = useState("flights");

    const tabs = [
        { id: "flights", label: "Flights", icon: "fa-plane" },
        { id: "trains", label: "Trains", icon: "fa-train" },
        { id: "hotels", label: "Hotels", icon: "fa-hotel" },
        { id: "buses", label: "Buses", icon: "fa-bus" },
    ];

    return (
        <div className="booking-page">
            <div className="bg-overlay"></div>

            <div className="booking-container">
                <h1 className="title text-gradient">Book Your Next Journey</h1>

                <div className="tabs">
                    {tabs.map((tab) => (
                        <button
                            key={tab.id}
                            className={`tab-btn ${activeTab === tab.id ? "active" : ""}`}
                            onClick={() => setActiveTab(tab.id)}
                        >
                            <i className={`fa-solid ${tab.icon}`}></i> {tab.label}
                        </button>
                    ))}
                </div>

                <div className="booking-card fade-in-up">
                    {activeTab === "flights" && <FlightForm />}
                    {activeTab === "trains" && <TrainForm />}
                    {activeTab === "hotels" && <HotelForm />}
                    {activeTab === "buses" && <BusForm />}
                </div>

                <div className="results-section">
                    <h2 className="results-title">Available Options</h2>
                    <div className="results-grid">
                        {[1, 2, 3].map((i) => (
                            <div className="result-card" key={i}>
                                <div className="result-content">
                                    <h3>Sample Option {i}</h3>
                                    <p>From AI-curated travel listings</p>
                                    <button className="book-btn">Book Now</button>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}

/* ==== Sub Components ==== */

function FlightForm() {
    return (
        <div className="form-grid">
            <input type="text" placeholder="From" />
            <input type="text" placeholder="To" />
            <input type="date" />
            <button className="search-btn">Search Flights</button>
        </div>
    );
}

function TrainForm() {
    return (
        <div className="form-grid">
            <input type="text" placeholder="Departure Station" />
            <input type="text" placeholder="Arrival Station" />
            <input type="date" />
            <button className="search-btn">Search Trains</button>
        </div>
    );
}

function HotelForm() {
    return (
        <div className="form-grid">
            <input type="text" placeholder="City" />
            <input type="date" placeholder="Check-in" />
            <input type="date" placeholder="Check-out" />
            <button className="search-btn">Search Hotels</button>
        </div>
    );
}

function BusForm() {
    return (
        <div className="form-grid">
            <input type="text" placeholder="From" />
            <input type="text" placeholder="To" />
            <input type="date" />
            <button className="search-btn">Search Buses</button>
        </div>
    );
}
