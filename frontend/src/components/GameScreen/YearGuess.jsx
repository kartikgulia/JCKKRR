import React from "react";
import YearSlider from "./YearSlider";

const YearGuess = ({
  year,
  onYearChange,
  onSubmitYearGuess,
  minYear,
  maxYear,
}) => {
  return (
    <div style={container}>
      <YearSlider
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
