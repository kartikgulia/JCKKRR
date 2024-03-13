import React, { useState, useEffect } from "react";
import { useLocation, Link } from "react-router-dom";
import Round from "../components/GameScreen/Round";
import "../styles/GameScreen.css";
import SERVER_URL from "../config";

function Game() {
  const location = useLocation(); // Access location to get state passed from navigate
  const { roundsArray, currentRoundNumber } = location.state || {}; // Destructure state, with fallbacks

  const [currentRound, setCurrentRound] = useState(
    currentRoundNumber ? currentRoundNumber - 1 : 0
  );
  const [rounds, setRounds] = useState(roundsArray || []);
  const [roundsTotal, setRoundsTotal] = useState(
    (roundsArray && roundsArray.length) || 0
  );
  const [roundsLoaded, setRoundsLoaded] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);

  const minYear = 1800;
  const maxYear = 2024;

  // const mockRoundsData = [
  //   {
  //     backgroundImagePath: "https://picsum.photos/1000/500",
  //     targetImageCoordinates: [
  //       [100, 200],
  //       [100, 100],
  //       [200, 100],
  //       [200, 200],
  //     ],
  //     yearTaken: 2000,
  //   },
  //   {
  //     backgroundImagePath: "https://picsum.photos/500/500",
  //     targetImageCoordinates: [
  //       [150, 250],
  //       [150, 150],
  //       [250, 150],
  //       [250, 250],
  //     ],
  //     yearTaken: 2010,
  //   },
  //   {
  //     backgroundImagePath: "https://picsum.photos/600/500",
  //     targetImageCoordinates: [
  //       [150, 250],
  //       [150, 150],
  //       [250, 150],
  //       [250, 250],
  //     ],
  //     yearTaken: 2010,
  //   },
  //   {
  //     backgroundImagePath: "https://picsum.photos/700/500",
  //     targetImageCoordinates: [
  //       [150, 250],
  //       [150, 150],
  //       [250, 150],
  //       [250, 250],
  //     ],
  //     yearTaken: 2010,
  //   },
  //   {
  //     backgroundImagePath: "https://picsum.photos/800/500",
  //     targetImageCoordinates: [
  //       [150, 250],
  //       [150, 150],
  //       [250, 150],
  //       [250, 250],
  //     ],
  //     yearTaken: 2010,
  //   },
  // ];

  useEffect(() => {
    // If roundsArray is not provided through navigation state, fetch the rounds
    if (!roundsArray) {
      console.log("New game");
      const fetchRounds = async () => {
        const route = window.location.pathname;
        const parts = route.split("/"); // Split the pathname by '/'
        const gameDifficultyLevel = parts[parts.length - 1];

        const userID = localStorage.getItem("userToken");
        const response = await fetch(
          `${SERVER_URL}/getGameInfo?gameDifficultyLevel=${gameDifficultyLevel}&userID=${userID}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        const data = await response.json();

        if (data.message === "Success") {
          setRounds(data.roundsArray);
          setRoundsTotal(data.roundsArray.length);
          setRoundsLoaded(true);
        } else {
          setErrorMessage(data.message);
        }
      };

      fetchRounds();
    } else {
      // If roundsArray is provided, use it directly

      setRoundsLoaded(true);
    }
  }, [roundsArray]);

  const handleRoundSubmit = (yearGuess, coordinates) => {
    console.log(
      `Round ${
        currentRound + 1
      } Submission: Year Guess - ${yearGuess}, Coordinates - ${JSON.stringify(
        coordinates
      )}`
    );

    if (currentRound + 1 < roundsTotal) {
      setCurrentRound(currentRound + 1);
    } else {
      console.log("Game completed!");
    }
  };

  if (errorMessage) {
    return (
      <div>
        <h1>{errorMessage}</h1>
        <Link to="/gameSelect" className="button">
          Go back to Game Select
        </Link>
      </div>
    );
  }

  if (!roundsLoaded) {
    return <div>Loading...</div>;
  }

  return (
    <div className="container">
      <Round
        roundData={rounds[currentRound]}
        currentRound={currentRound + 1}
        roundsTotal={roundsTotal}
        onSubmit={handleRoundSubmit}
        minYear={minYear}
        maxYear={maxYear}
      />
    </div>
  );
}

export default Game;
