import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Planner.css";

const Planner = () => {
    const [destination, setDestination] = useState("");
    const [startDate, setStartDate] = useState("");
    const [endDate, setEndDate] = useState("");
    const [budget, setBudget] = useState("");
    const [interests, setInterests] = useState([]);
    const navigate = useNavigate();

    const handleInterestChange = (interest) => {
        setInterests(prev =>
            prev.includes(interest)
                ? prev.filter(i => i !== interest)
                : [...prev, interest]
        );
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Navigate to results with state
        navigate("/results", {
            state: { destination, startDate, endDate, budget, interests }
        });
    };

    return (
        <div className="planner-container">
            <h1>Plan Your Trip</h1>
            <form onSubmit={handleSubmit} className="planner-form">
                <div className="form-group">
                    <label htmlFor="destination">Destination</label>
                    <input
                        type="text"
                        id="destination"
                        value={destination}
                        onChange={(e) => setDestination(e.target.value)}
                        placeholder="Enter your destination"
                        required
                    />
                </div>

                <div className="form-row">
                    <div className="form-group">
                        <label htmlFor="startDate">Start Date</label>
                        <input
                            type="date"
                            id="startDate"
                            value={startDate}
                            onChange={(e) => setStartDate(e.target.value)}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="endDate">End Date</label>
                        <input
                            type="date"
                            id="endDate"
                            value={endDate}
                            onChange={(e) => setEndDate(e.target.value)}
                            required
                        />
                    </div>
                </div>

                <div className="form-group">
                    <label htmlFor="budget">Budget (USD)</label>
                    <input
                        type="number"
                        id="budget"
                        value={budget}
                        onChange={(e) => setBudget(e.target.value)}
                        placeholder="Enter your budget"
                        min="0"
                        required
                    />
                </div>

                <div className="form-group">
                    <label>Interests</label>
                    <div className="interests-grid">
                        {["Adventure", "Culture", "Food", "Nature", "Relaxation", "Shopping"].map(interest => (
                            <label key={interest} className="interest-checkbox">
                                <input
                                    type="checkbox"
                                    checked={interests.includes(interest)}
                                    onChange={() => handleInterestChange(interest)}
                                />
                                {interest}
                            </label>
                        ))}
                    </div>
                </div>

                <button type="submit" className="submit-btn">Generate Itinerary</button>
            </form>
        </div>
    );
};

export default Planner;
