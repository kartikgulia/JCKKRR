import React from "react";

import BackgroundImage from "./BackgroundImage";
import YearSlider from "./YearSlider";
import SubmitButton from "./SubmitButton";

const YearGuess = ({
  year,
  onYearChange,
  onSubmitYearGuess,
  minYear,
  maxYear,
  backgroundImageSRC,
}) => {
  return (
    <div style={container}>
      <h1>Guess what year this image is from?</h1>
      <BackgroundImage src={backgroundImageSRC} />
      <YearSlider
        min={minYear}
        max={maxYear}
        value={year}
        onChange={onYearChange}
      />
      <SubmitButton
        onClick={onSubmitYearGuess}
        text={"Submit Year Guess"}
        color={"dodgerblue"}
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
