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
}) => {
  return (
    <div style={container}>
      <h1>Guess what year this image is from?</h1>
      <BackgroundImage src={"https://picsum.photos/500/500"} />
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
  height: "100vh",
};

export default YearGuess;
