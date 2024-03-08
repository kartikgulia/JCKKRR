import React, { useState } from "react";
import PropTypes from "prop-types";
import "../../styles/submitButton.css";

const SubmitButton = ({ color, text, onClick }) => {
  const [isPressed, setIsPressed] = useState(false);
  const handleMouseDown = () => {
    setIsPressed(true);
  };

  const handleMouseUp = () => {
    setIsPressed(false);
  };

  // Enhance the onClick to also reset the isPressed state
  const enhancedOnClick = (e) => {
    setIsPressed(false);
    onClick(e);
  };

  return (
    <button
      onMouseDown={handleMouseDown}
      onMouseUp={handleMouseUp}
      onMouseLeave={handleMouseUp}
      onClick={enhancedOnClick}
      className="btn"
    >
      {text}
    </button>
  );
};

SubmitButton.propTypes = {
  text: PropTypes.string.isRequired,
  color: PropTypes.string,
  onClick: PropTypes.func.isRequired,
};

export default SubmitButton;
