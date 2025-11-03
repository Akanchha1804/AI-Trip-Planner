import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav style={{ padding: "1rem", background: "#1e40af", color: "white" }}>
            <h1 style={{ display: "inline", marginRight: "2rem" }}>AI Trip Planner</h1>
            <Link to="/" style={{ marginRight: "1rem", color: "white" }}>Home</Link>
            <Link to="/planner" style={{ marginRight: "1rem", color: "white" }}>Plan Trip</Link>
            <Link to="/results" style={{ color: "white" }}>Results</Link>
        </nav>
    );
}
