import React, { useState, useEffect } from "react";
import YearGuess from "../components/GameScreen/YearGuess";
import Round from "../components/GameScreen/Round";
import SERVER_URL from "../config";

function Game() {
  const [year, setYear] = useState(0);
  const [rounds, setRounds] = useState([]);
  const [currentRound, setCurrentRound] = useState(0);
  const [totalRounds, setTotalRounds] = useState(0);
  const [onYearGuessPage, setOnYearGuessPage] = useState(true);
  const [imagesLoaded, setImagesLoaded] = useState(false);
  const [difficulty, setDifficulty] = useState(null);

  const minYear = 0;
  const maxYear = 2024;

  useEffect(() => {
    const route = window.location.pathname;
    const parts = route.split("/");
    const difficulty = parts[parts.length - 1];
    setDifficulty(difficulty);
    initializeGame(difficulty);
  }, []);

  const initializeGame = async (difficulty) => {
    try {
      const response = await fetch(`${SERVER_URL}/bg_target?difficulty=${difficulty}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      setRounds(data.rounds);
      setTotalRounds(data.rounds.length);
      setCurrentRound(1); // Start from the first round
      setImagesLoaded(true);
    } catch (error) {
      console.error("Error during game initialization", error);
    }
  };

  const handleYearChange = (value) => {
    setYear(value);
  };

  const calculateScoreForYearGuess = (yearGuessed, yearActual) => {
    let yearRange = maxYear - minYear;
    let offBy = Math.abs(yearGuessed - yearActual);
    let score = yearRange - offBy;
    return score;
  };

  const submitYearGuess = () => {
    console.log("Selected Year:", year);
    let actualYear = 2000;
    let score = calculateScoreForYearGuess(year, actualYear);
    console.log(score);
    setOnYearGuessPage(false);
  };

  if (!imagesLoaded) {
    return <div>Loading...</div>;
  }

  return (
    <div style={container}>
      {onYearGuessPage ? (
        <YearGuess
          year={0}  // Set initial year value
          onYearChange={handleYearChange}
          onSubmitYearGuess={submitYearGuess}
          minYear={minYear}
          maxYear={maxYear}
          backgroundImageSRC={rounds[currentRound - 1].backgroundImagePath}
        />
      ) : (
        <Round
          backgroundImageSRC={rounds[currentRound - 1].backgroundImagePath}
          targetImage={rounds[currentRound - 1].targetImageCoordinates}
          targetImageCoordinates={rounds[currentRound - 1].targetImageCoordinates}
        />
      )}
    </div>
  );
}

const container = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
  height: "100vh",
};

export default Game;
