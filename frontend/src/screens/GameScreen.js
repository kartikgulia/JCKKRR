import React, { useState, useEffect } from "react";
import Round from "../components/GameScreen/Round";
import "../styles/GameScreen.css";

function Game() {
  const [currentRound, setCurrentRound] = useState(0);
  const [mockRounds, setMockRounds] = useState([]);
  const [roundsTotal, setRoundsTotal] = useState(0);
  const [roundsLoaded, setRoundsLoaded] = useState(false);

  const minYear = 1900;
  const maxYear = 2024;

  useEffect(() => {
    const fetchRounds = async () => {
      const mockRoundsData = [
        {
          backgroundImagePath: "https://picsum.photos/1000/500",
          targetImageCoordinates: { x: 100, y: 200 },
          yearTaken: 2000,
        },
        {
          backgroundImagePath: "https://picsum.photos/500/500",
          targetImageCoordinates: { x: 150, y: 250 },
          yearTaken: 2010,
        },
        {
          backgroundImagePath: "https://picsum.photos/600/500",
          targetImageCoordinates: { x: 150, y: 250 },
          yearTaken: 2010,
        },
        {
          backgroundImagePath: "https://picsum.photos/700/500",
          targetImageCoordinates: { x: 150, y: 250 },
          yearTaken: 2010,
        },
        {
          backgroundImagePath: "https://picsum.photos/800/500",
          targetImageCoordinates: { x: 150, y: 250 },
          yearTaken: 2010,
        },
      ];

      setMockRounds(mockRoundsData);
      setRoundsTotal(mockRoundsData.length);

      // Assuming images are loaded in Round component
      setRoundsLoaded(true);
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

  return (
    <div className="container">
      <Round
        roundData={mockRounds[currentRound]}
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
