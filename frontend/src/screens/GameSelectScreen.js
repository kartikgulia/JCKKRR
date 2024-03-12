import React from "react";
import { Link } from "react-router-dom";
import "../styles/GameSelectScreen.css";

const GameSelectScreen = () => {
  return (
    <div className="container">
      <h1 className="title">Select Difficulty</h1>

      <Link to="/playGame/Easy" className="button-link">
        <button className="button-style">Easy</button>
      </Link>

      <Link to="/playGame/Medium" className="button-link">
        <button className="button-style">Medium</button>
      </Link>

      <Link to="/playGame/Hard" className="button-link">
        <button className="button-style">Hard</button>
      </Link>

      <Link to="/leaderboard" className="button-link">
        <button className="button-style">Leaderboard</button>
      </Link>
    </div>
  );
};

export default GameSelectScreen;
