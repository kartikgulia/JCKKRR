import React, { useState, useEffect } from "react";
import Round from "../components/GameScreen/Round";
import "../styles/GameScreen.css";

function Game() {
  const [currentRound, setCurrentRound] = useState(0);
  const [mockRounds, setMockRounds] = useState([]);
  const [roundsTotal, setRoundsTotal] = useState(0);
  const [backgroundImageSRC, setBackgroundImageSRC] = useState("");
  const [targetImageSRC, setTargetImageSRC] = useState("");
  const [targetImageCoordinates, setTargetImageCoordinates] = useState({});
  const [imagesLoaded, setImagesLoaded] = useState(false);
  const [difficulty, setDifficulty] = useState(null);

  const minYear = 0;
  const maxYear = 2024;

  useEffect(() => {
    const mockRoundsData = [
      { backgroundImagePath: "https://picsum.photos/1000/500", targetImageCoordinates: { x: 100, y: 200 }, yearTaken: 2000 },
      { backgroundImagePath: "https://picsum.photos/500/500", targetImageCoordinates: { x: 150, y: 250 }, yearTaken: 2010 },
      { backgroundImagePath: "https://picsum.photos/600/500", targetImageCoordinates: { x: 150, y: 250 }, yearTaken: 2010 },
      { backgroundImagePath: "https://picsum.photos/700/500", targetImageCoordinates: { x: 150, y: 250 }, yearTaken: 2010 },
      { backgroundImagePath: "https://picsum.photos/800/500", targetImageCoordinates: { x: 150, y: 250 }, yearTaken: 2010 },
    ];

    const route = window.location.pathname;
    const parts = route.split("/");
    const difficulty = parts[parts.length - 1];
    setDifficulty(difficulty);

    setMockRounds(mockRoundsData);
    setRoundsTotal(mockRoundsData.length);
    initializeGame();
  }, []);

  const initializeGame = async () => {
    try {
      const backgroundImageSrc = "https://picsum.photos/1000/500";
      const targetImageSrc = "https://picsum.photos/500/500";

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

  const loadImage = (src) =>
    new Promise((resolve, reject) => {
      const img = new Image();
      img.src = src;
      img.onload = () => resolve(img);
      img.onerror = reject;
    });

  const handleRoundSubmit = (yearGuess, coordinates) => {
    console.log(`Round ${currentRound + 1} Submission: Year Guess - ${yearGuess}, Coordinates - ${JSON.stringify(coordinates)}`);

    if (currentRound + 1 < roundsTotal) {
      setCurrentRound(currentRound + 1);
    } else {
      console.log("Game completed!");
    }
  };

  if (!imagesLoaded) {
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
