import React from "react";
import "../../styles/Scoreboard.css"; 
import { Link } from 'react-router-dom';

const Scoreboard = ({ scores, onPlayAgain }) => {

  return (
    <div className="container">
      <h2 className="title">Scores</h2>
      <div className="scoreboard-score">
        {scores.map((score, index) => (
          <li key={index}>Round {index + 1}: {score} points</li>
        ))}
      </div>
      <Link to="/gameSelect" className="button">Play Again?</Link>
    </div>
  );
};

export default Scoreboard;
