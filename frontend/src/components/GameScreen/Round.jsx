import React, { useState } from "react";
import BackgroundImage from "./BackgroundImage";
import SubmitButton from "./SubmitButton";
import YearGuess from "./YearGuess";
import "../../styles/Round.css"

const Round = ({ roundData, currentRound, roundsTotal, onSubmit, minYear, maxYear }) => {
  const [year, setYear] = useState(0);
  const [clickPosition, setClickPosition] = useState({ x: null, y: null });

  const handleBackgroundImageClick = (event) => {
    const rect = event.target.getBoundingClientRect();
    const circleDiameter = 20;
    const offsetX = circleDiameter / 2;
    const offsetY = circleDiameter / 2;
    const x = event.clientX - rect.left - offsetX;
    const y = event.clientY - rect.top - offsetY;

    setClickPosition({ x, y });
  };

  const handleRoundSubmit = () => {
    onSubmit(year, clickPosition);
    setClickPosition({ x: null, y: null });
    setYear(0);
  };

  const submitYearGuess = () => {
    console.log("Selected Year:", year);
    let actualYear = 2000;
    let score = calculateScoreForYearGuess(year, actualYear);
    console.log(score);
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

  return (
    <div className="round-container">
      <div className="target-image-container">
        <h2 className="find-image-heading">Find this image</h2>
      </div>
      <div className="background-image-container" onClick={handleBackgroundImageClick}>
        <BackgroundImage src={roundData.backgroundImagePath} />
        {clickPosition.x !== null && clickPosition.y !== null && (
        <div>
          <div className="red-circle" style={{ left: `${clickPosition.x}px`, top: `${clickPosition.y}px` }}></div>
          <div className="text">
            Clicked Coordinates: {clickPosition.x}, {clickPosition.y}
          </div>
        </div>
      )}
      </div>

      <YearGuess
          year={year}
          onYearChange={handleYearChange}
          onSubmitYearGuess={submitYearGuess}
          minYear={minYear}
          maxYear={maxYear}
      />

      <SubmitButton onClick={handleRoundSubmit} text={"Submit Your Guess"}/>

      <div className="text">Round {currentRound} of {roundsTotal}</div>
    </div>
  );
};

export default Round;
