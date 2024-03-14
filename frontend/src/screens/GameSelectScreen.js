import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom"; // useNavigate instead of useHistory
import "../styles/GameSelectScreen.css";
import SERVER_URL from "../config";

const GameSelectScreen = () => {
  const [errorMessage, setErrorMessage] = useState(null);
  const navigate = useNavigate(); // useNavigate hook

  useEffect(() => {
    const fetchExistingGame = async () => {
      const userID = localStorage.getItem("userToken");
      const response = await fetch(
        `${SERVER_URL}/getExistingGameInfo?userID=${userID}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const data = await response.json();

      if (data.message === "Success" && data.description === "Game exists") {
        // Navigate with useNavigate and pass state
        console.log(data.currentRoundNumber);
        navigate(`/playGame/${data.difficulty}`, {
          state: {
            roundsArray: data.roundsArray,
            currentRoundNumber: data.currentRoundNumber,
          },
        });
      } else if (data.message !== "Success") {
        setErrorMessage(data.message);
      }
    };

    fetchExistingGame();
  }, [navigate]); // Add navigate to the dependencies array

  return (
    <div className="container">
      {errorMessage && <p className="error-message">{errorMessage}</p>}

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

      <Link to="/profile" className="button-link">
        <button className="button-style">Profile</button>
      </Link>
    </div>
  );
};

export default GameSelectScreen;
