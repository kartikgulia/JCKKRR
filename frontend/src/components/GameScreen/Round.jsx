import React, { useState, useEffect } from "react";
import BackgroundImage from "./BackgroundImage";
import SubmitButton from "./SubmitButton";
import YearGuess from "./YearGuess";
import Scoreboard from "./Scoreboard";
import "../../styles/Round.css";
import SERVER_URL from "../../config";

const Round = ({
  roundData,
  currentRound,
  roundsTotal,
  onSubmit,
  minYear,
  maxYear,
}) => {
  const [year, setYear] = useState(0);
  const [clickPosition, setClickPosition] = useState({ x: null, y: null });
  const [imageLoaded, setImageLoaded] = useState(false);
  const [roundsFinished, setRoundsFinished] = useState(false);
  const [roundScores, setRoundScores] = useState([]);

  useEffect(() => {
    if (roundData != null) {
      setImageLoaded(true);
    }
  }, [roundData]);

  const handleBackgroundImageClick = (event) => {
    console.log("bg image clicked");
    if (imageLoaded) {
      console.log("image loaded true after bg image clicked");
      const rect = event.target.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      setClickPosition({ x, y });
    }
  };

  const handleImageLoad = () => {
    setImageLoaded(true);
  };

  const handleRoundSubmit = async () => {
    if (imageLoaded && clickPosition.x !== null && clickPosition.y !== null) {
      onSubmit(year, clickPosition);
      // submitYearGuess(); dont need this

      await storeRoundGuess();

      setClickPosition({ x: null, y: null });
      setYear(0);

      if (currentRound === roundsTotal) {
        setRoundsFinished(true);
      }
    } else {
      console.log("Image not loaded or coordinates not chosen yet.");
    }
  };

  const storeRoundGuess = async () => {
    console.log("Storing round guesses in the backend");

    const yearGuess = year;
    const targetGuess = clickPosition;
    const userID = localStorage.getItem("userToken");
    try {
      const response = await fetch(`${SERVER_URL}/storeRoundGuesses`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ yearGuess, targetGuess, userID }),
      });
      const data = await response.json();
      console.log(data); // Process the response data
    } catch {}
  };
  // const submitYearGuess = () => {
  //   console.log("Selected Year:", year);
  //   let actualYear = 2000;
  //   let score = calculateScoreForYearGuess(year, actualYear);
  //   console.log(score);
  //   setRoundScores([...roundScores, score]);
  // };

  const handlePlayAgain = () => {
    setRoundScores([]);
    setRoundsFinished(false);
  };

  const handleYearChange = (value) => {
    setYear(value);
  };

  // const calculateScoreForYearGuess = (yearGuessed, yearActual) => {
  //   let yearRange = maxYear - minYear;
  //   let offBy = Math.abs(yearGuessed - yearActual);
  //   let score = yearRange - offBy;
  //   return score;
  // };

  if (imageLoaded) {
    return (
      <div className="round-container">
        {roundsFinished ? (
          <Scoreboard scores={roundScores} onPlayAgain={handlePlayAgain} />
        ) : (
          <>
            <div className="target-image-container">
              <h2 className="find-image-heading">
                Find this image and guess the year this was taken from! Click on
                the picture and drag the slider.
              </h2>
            </div>
            <div
              className="background-image-container"
              onClick={handleBackgroundImageClick}
            >
              <BackgroundImage
                src={roundData.backgroundImagePath}
                onLoad={handleImageLoad}
              />
              {clickPosition.x !== null && clickPosition.y !== null && (
                <div>
                  <div
                    className="red-circle"
                    style={{
                      left: `${clickPosition.x}px`,
                      top: `${clickPosition.y}px`,
                    }}
                  ></div>
                  <div className="text">
                    Clicked Coordinates: {clickPosition.x}, {clickPosition.y}
                  </div>
                </div>
              )}
            </div>

            <YearGuess
              currentRound={currentRound}
              year={year}
              onYearChange={handleYearChange}
              minYear={minYear}
              maxYear={maxYear}
            />

            <SubmitButton
              onClick={handleRoundSubmit}
              text={"Submit Your Guess"}
            />

            <div className="text">
              Round {currentRound} of {roundsTotal}
            </div>
          </>
        )}
      </div>
    );
  } else {
    return <div>Loading...</div>;
  }
};

export default Round;
