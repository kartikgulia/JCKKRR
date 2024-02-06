import React from "react";
import PropTypes from "prop-types";

const BackgroundImage = ({ src }) => {
  const style = {
    maxWidth: "100%",
    maxHeight: "100vh",
    position: "relative",
  };

  return <img src={src} style={style} alt="" />;
};

BackgroundImage.propTypes = {
  src: PropTypes.string.isRequired, // Ensure src is a required string prop
};

export default BackgroundImage;
