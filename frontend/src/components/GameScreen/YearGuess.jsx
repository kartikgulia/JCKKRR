import React, { useState, useEffect } from "react";
import YearSlider from "./YearSlider";

const YearGuess = ({ year, onYearChange, onSubmitYearGuess, minYear, maxYear, currentRound }) => {
  const [resetKey, setResetKey] = useState(0);

  useEffect(() => {
    // Reset the slider whenever the current round changes
    setResetKey((prevKey) => prevKey + 1);
  }, [currentRound]);

  return (
    <div style={container}>
      <YearSlider
        key={resetKey} 
        min={minYear}
        max={maxYear}
        value={year}
        onChange={onYearChange}
      />
    </div>
  );
};

const container = {
  display: "flex",
  flexDirection: "column",
  justifyContent: "center",
  alignItems: "center",
};

export default YearGuess;
