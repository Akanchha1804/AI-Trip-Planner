import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Planner from "./pages/Planner";
import Results from "./pages/Results";

function App() {
    return ( <
        Router >
        <
        Navbar / >
        <
        Routes >
        <
        Route path = "/"
        element = { < Home / > }
        /> <
        Route path = "/planner"
        element = { < Planner / > }
        /> <
        Route path = "/results"
        element = { < Results / > }
        /> < /
        Routes > <
        /Router>
    );
}

export default App;