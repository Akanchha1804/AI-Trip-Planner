import React from "react";
import { useLocation } from "react-router-dom";
import "./Results.css";

const Results = () => {
    const location = useLocation();
    const { destination, startDate, endDate, budget, interests } = location.state || {};

    // Mock itinerary data
    const itinerary = [
        {
            day: 1,
            title: "Arrival and City Exploration",
            activities: [
                "Arrive at airport and check into hotel",
                "Visit central market for local street food",
                "Evening walk in the historic district"
            ]
        },
        {
            day: 2,
            title: "Cultural Immersion",
            activities: [
                "Morning visit to local museum",
                "Afternoon cooking class",
                "Traditional dance performance in the evening"
            ]
        },
        {
            day: 3,
            title: "Adventure Day",
            activities: [
                "Hiking in nearby nature reserve",
                "Visit to local waterfall",
                "Relax at beach or spa"
            ]
        }
    ];

    const estimatedCost = budget ? parseInt(budget) * 0.8 : 0;

    return (
        <div className="results-container">
            <h1>Your Trip Itinerary</h1>

            <div className="trip-summary">
                <h2>Trip Summary</h2>
                <div className="summary-grid">
                    <div className="summary-item">
                        <strong>Destination:</strong> {destination || "Not specified"}
                    </div>
                    <div className="summary-item">
                        <strong>Dates:</strong> {startDate || "N/A"} to {endDate || "N/A"}
                    </div>
                    <div className="summary-item">
                        <strong>Budget:</strong> ${budget || "N/A"}
                    </div>
                    <div className="summary-item">
                        <strong>Interests:</strong> {interests?.join(", ") || "None specified"}
                    </div>
                    <div className="summary-item">
                        <strong>Estimated Cost:</strong> ${estimatedCost}
                    </div>
                </div>
            </div>

            <div className="itinerary">
                <h2>Day-by-Day Itinerary</h2>
                {itinerary.map((day, index) => (
                    <div key={index} className="day-card">
                        <h3>Day {day.day}: {day.title}</h3>
                        <ul>
                            {day.activities.map((activity, i) => (
                                <li key={i}>{activity}</li>
                            ))}
                        </ul>
                    </div>
                ))}
            </div>

            <div className="actions">
                <button className="btn-primary">Download Itinerary</button>
                <button className="btn-secondary">Modify Trip</button>
            </div>
        </div>
    );
};

export default Results;
