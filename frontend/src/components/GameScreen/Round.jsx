import React from "react";
import BackgroundImage from "./BackgroundImage";

const Round = ({ backgroundImageSRC, targetImage }) => {
  return (
    <div>
      <h1>Round</h1>
      <BackgroundImage src={backgroundImageSRC} />

      <img
        src={targetImage}
        alt="Target"
        style={{ maxWidth: "100%", height: "auto" }}
      />
    </div>
  );
};

export default Round;
