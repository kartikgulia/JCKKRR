import React, { useState, useEffect } from "react";
import YearGuess from "../components/GameScreen/YearGuess";
import Round from "../components/GameScreen/Round";
import SERVER_URL from "../config";

function Game() {
  const [year, setYear] = useState(0); // Initial slider value
  const [onYearGuessPage, setOnYearGuessPage] = useState(true);
  const [backgroundImageSRC, setBackgroundImageSRC] = useState("");
  const [targetImageSRC, setTargetImageSRC] = useState("");
  const [targetImageCoordinates, setTargetImageCoordinates] = useState({});
  const [imagesLoaded, setImagesLoaded] = useState(false);
  const [difficulty, setDifficulty] = useState(null);

  const minYear = 0;
  const maxYear = 2024;

  useEffect(() => {
    const route = window.location.pathname;
    const parts = route.split("/"); // Split the pathname by '/'
    const difficulty = parts[parts.length - 1];
    console.log(difficulty); // Output the difficulty level
    setDifficulty(difficulty);
    console.log("Difficulty updated:", difficulty);
    initializeGame(); // Ensure initializeGame is called after difficulty is set
  }, []);

  const loadImage = (src) =>
    new Promise((resolve, reject) => {
      const img = new Image();
      img.src = src;
      img.onload = () => resolve(img);
      img.onerror = reject;
    });

  const initializeGame = async () => {
    console.log("Game component has been mounted.");
    console.log("Use difficulty to retrieve a game from Firestore");
    console.log(difficulty);

    try {
      const backgroundImageSrc = "https://picsum.photos/1000/500";
      const targetImageSrc = "https://picsum.photos/500/500";

      // Load both images asynchronously
      const [backgroundImage, targetImage] = await Promise.all([
        loadImage(backgroundImageSrc),
        loadImage(targetImageSrc),
      ]);

      setBackgroundImageSRC(backgroundImage.src);
      setTargetImageSRC(targetImage.src);
      setTargetImageCoordinates({ x: 100, y: 200 });
      setImagesLoaded(true);
    } catch (error) {
      console.error("Error during image processing", error);
      setBackgroundImageSRC("Error during Image Processing");
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
          year={year}
          onYearChange={handleYearChange}
          onSubmitYearGuess={submitYearGuess}
          minYear={minYear}
          maxYear={maxYear}
          backgroundImageSRC={backgroundImageSRC}
        />
      ) : (
        <Round
          backgroundImageSRC={backgroundImageSRC}
          targetImage={targetImageSRC}
          targetImageCoordinates={targetImageCoordinates}
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
