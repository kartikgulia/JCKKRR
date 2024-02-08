import React from "react";
import { Link } from "react-router-dom";

const GameSelectScreen = () => {
  return (
    <div style={container}>
      <h1>Select Difficulty</h1>

      <Link to="/playGame" style={buttonLink}>
        <button style={buttonStyle}>Easy</button>
      </Link>

      <Link to="/playGame" style={buttonLink}>
        <button style={buttonStyle}>Normal</button>
      </Link>

      <Link to="/playGame" style={buttonLink}>
        <button style={buttonStyle}>Hard</button>
      </Link>

      <Link to="/leaderboard" style={buttonLink}>
        <button style={buttonStyle}>Leaderboard</button>
      </Link>
    </div>
  );
};

const container = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
};

const buttonLink = {
  textDecoration: "none",
  margin: "10px",
};

const buttonStyle = {
  padding: "10px 20px",
  fontSize: "16px",
  cursor: "pointer",
  backgroundColor: "#3498db", 
  color: "#fff", 
  border: "none",
  borderRadius: "5px",
  width: "200px", 
  textAlign: "center",
};

export default GameSelectScreen;
