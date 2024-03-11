import React, { useState, useEffect } from "react";
import Round from "../components/GameScreen/Round";
import "../styles/GameScreen.css";
import SERVER_URL from "../config";

function Game() {
  const mockRoundsData = [
    {
      backgroundImagePath: "https://picsum.photos/1000/500",
      targetImageCoordinates: [
        [100, 200],
        [100, 100],
        [200, 100],
        [200, 200],
      ],
      yearTaken: 2000,
    },
    {
      backgroundImagePath: "https://picsum.photos/500/500",
      targetImageCoordinates: [
        [150, 250],
        [150, 150],
        [250, 150],
        [250, 250],
      ],
      yearTaken: 2010,
    },
    {
      backgroundImagePath: "https://picsum.photos/600/500",
      targetImageCoordinates: [
        [150, 250],
        [150, 150],
        [250, 150],
        [250, 250],
      ],
      yearTaken: 2010,
    },
    {
      backgroundImagePath: "https://picsum.photos/700/500",
      targetImageCoordinates: [
        [150, 250],
        [150, 150],
        [250, 150],
        [250, 250],
      ],
      yearTaken: 2010,
    },
    {
      backgroundImagePath: "https://picsum.photos/800/500",
      targetImageCoordinates: [
        [150, 250],
        [150, 150],
        [250, 150],
        [250, 250],
      ],
      yearTaken: 2010,
    },
  ];

  const [currentRound, setCurrentRound] = useState(0);
  const [rounds, setRounds] = useState([]);
  const [roundsTotal, setRoundsTotal] = useState(0);
  const [roundsLoaded, setRoundsLoaded] = useState(false);

  const [errorMessage, setErrorMessage] = useState(null);
  const minYear = 1900;
  const maxYear = 2024;

  useEffect(() => {
    const route = window.location.pathname;
    const parts = route.split("/"); // Split the pathname by '/'
    const gameDifficultyLevel = parts[parts.length - 1];
    // console.log(difficulty);

    const fetchRounds = async () => {
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
      // console.log(data); // Process the response data

      if (data.message === "Success") {
        console.log(data.description);
        console.log(data.roundsArray);
        setRounds(data.roundsArray);
        setRoundsTotal(data.roundsArray.length);
        setRoundsLoaded(true);
      } else {
        setErrorMessage(data.message);
      }
    };

    fetchRounds();
  }, []);

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

  if (!roundsLoaded) {
    return <div>Loading...</div>;
  }

  if (errorMessage) {
    return <div>{errorMessage}</div>;
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
